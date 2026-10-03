#!/usr/bin/env python3
"""codex-watch: log the changes in openai/codex that hint at unreleased
models, plans and features.

Reads a local checkout of openai/codex, extracts a small set of signals,
compares them with snapshot.json and, when something changed, writes a
CHANGELOG entry, refreshes the README and optionally pings Telegram.

Standard library only. Python 3.10+.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
import urllib.request

REPO = "openai/codex"
HERE = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT = os.path.join(HERE, "snapshot.json")
CHANGELOG = os.path.join(HERE, "CHANGELOG.md")
CHANGES_JSONL = os.path.join(HERE, "changes.jsonl")
README = os.path.join(HERE, "README.md")

PATHS = {
    "models": "codex-rs/models-manager/models.json",
    "features": "codex-rs/features/src/lib.rs",
    "plans": "codex-rs/tui/src/subscription.rs",
    "plan_types": "codex-rs/protocol/src/account.rs",
}

MODEL_FIELDS = (
    "display_name", "description", "visibility", "priority",
    "context_window", "max_context_window", "default_reasoning_level",
    "model_specialty", "multi_agent_version",
)

SKIP_DIRS = {".git", "node_modules", "target", "third_party", "dist", "build"}
SKIP_PATH = re.compile(
    r"(/tests?/|_tests?\.rs$|/tests\.rs$|/snapshots/|\.snap$|/fixtures?/|"
    r"/mocks?/|/test_|\.test\.|\.spec\.|/benches/|/examples/)"
)
SOURCE_EXT = (".rs", ".ts", ".tsx", ".js", ".json", ".toml", ".py")
MODEL_ID = re.compile(
    r'"((?:gpt|o[1-9])-[a-z0-9](?:[a-z0-9.\-]*[a-z0-9])?|o[1-9]|codex-auto-[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|codex-mini(?:-[a-z0-9.\-]*[a-z0-9])?)"'
)
URL = re.compile(r"https://(?:[a-z0-9\-]+\.)*(?:chatgpt\.com|openai\.com)[^\s\"'`)\]}>\\]*")


# ---------------------------------------------------------------- extraction

def read(root: str, rel: str) -> str | None:
    try:
        with open(os.path.join(root, rel), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def extract_models(root: str) -> dict:
    text = read(root, PATHS["models"])
    if text is None:
        return {}
    data = json.loads(text)
    items = data.get("models", data) if isinstance(data, dict) else data
    out = {}
    for m in items:
        slug = m.get("slug")
        if not slug:
            continue
        rec = {k: m.get(k) for k in MODEL_FIELDS if m.get(k) is not None}
        levels = [lv.get("effort") for lv in m.get("supported_reasoning_levels") or [] if lv.get("effort")]
        if levels:
            rec["reasoning_levels"] = levels
        out[slug] = rec
    return out


def _blocks(text: str, opener: str) -> list[str]:
    """Return the bodies of every `opener {...}` block, brace-matched."""
    bodies, i = [], 0
    while True:
        i = text.find(opener, i)
        if i == -1:
            return bodies
        j = text.find("{", i)
        depth, k = 0, j
        while k < len(text):
            if text[k] == "{":
                depth += 1
            elif text[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        bodies.append(text[j + 1:k])
        i = k


def extract_features(root: str) -> dict:
    text = read(root, PATHS["features"])
    if text is None:
        return {}
    start = text.find("pub const FEATURES")
    if start == -1:
        return {}
    out = {}
    for body in _blocks(text[start:], "FeatureSpec {"):
        key = re.search(r'key:\s*"([^"]+)"', body)
        if not key:
            continue
        stage = re.search(r"stage:\s*Stage::(\w+)", body)
        if re.search(r"stage:\s*if\s", body):
            stage_name = "Conditional:" + "/".join(dict.fromkeys(re.findall(r"Stage::(\w+)", body)))
        else:
            stage_name = stage.group(1) if stage else "?"
        default = re.search(r"default_enabled:\s*(true|false)", body)
        rec = {
            "stage": stage_name,
            "default_enabled": (default.group(1) == "true") if default else None,
        }
        name = re.search(r'\bname:\s*"((?:[^"\\]|\\.)*)"', body)
        desc = re.search(r'menu_description:\s*"((?:[^"\\]|\\.)*)"', body)
        if name:
            rec["name"] = name.group(1)
        if desc:
            rec["description"] = desc.group(1)
        out[key.group(1)] = rec
    return out


def extract_plans(root: str) -> dict:
    text = read(root, PATHS["plans"])
    if text is None:
        return {}
    out = {}
    for pattern, label in re.findall(r'\(([^()]*PlanType::[^()]*)\)\s*=>\s*\{?\s*"([^"]+)"', text):
        key = re.sub(r"\s+", " ", pattern.replace("PlanType::", "").replace("Self::", "")).strip()
        out[key] = label
    return out


def extract_plan_types(root: str) -> list[str]:
    text = read(root, PATHS["plan_types"])
    if text is None:
        return []
    bodies = _blocks(text, "pub enum PlanType")
    if not bodies:
        return []
    names = []
    for line in bodies[0].splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "//")):
            continue
        m = re.match(r"([A-Z]\w*)\s*[,({]?", line)
        if m:
            names.append(m.group(1))
    return names


def extract_strings(root: str) -> tuple[dict, list[str]]:
    """Model-looking IDs and chatgpt.com/openai.com URLs in non-test source."""
    ids: dict[str, str] = {}
    urls: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if not fn.endswith(SOURCE_EXT):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            if SKIP_PATH.search("/" + rel):
                continue
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            cut = text.find("#[cfg(test)]")
            if cut != -1:
                text = text[:cut]
            for mid in MODEL_ID.findall(text):
                ids.setdefault(mid, rel)
            for u in URL.findall(text):
                u = u.rstrip(".,;:")
                if "{" not in u:
                    urls.add(u)
    return dict(sorted(ids.items())), sorted(urls)


def build_snapshot(root: str, sha: str, commit_date: str) -> dict:
    ids, urls = extract_strings(root)
    return {
        "schema": 1,
        "source": {"repo": REPO, "sha": sha, "commit_date": commit_date},
        "models": extract_models(root),
        "features": extract_features(root),
        "plans": extract_plans(root),
        "plan_types": extract_plan_types(root),
        "model_ids": ids,
        "urls": urls,
    }


# ---------------------------------------------------------------------- diff

def fmt(v) -> str:
    if isinstance(v, list):
        return "[" + ", ".join(map(str, v)) + "]"
    return json.dumps(v, ensure_ascii=False) if isinstance(v, str) else str(v)


def diff_dicts(old: dict, new: dict, describe) -> list[str]:
    lines = []
    for k in sorted(new.keys() - old.keys()):
        lines.append(f"added `{k}` {describe(new[k])}".rstrip())
    for k in sorted(old.keys() - new.keys()):
        lines.append(f"removed `{k}`")
    for k in sorted(old.keys() & new.keys()):
        a, b = old[k], new[k]
        if a == b:
            continue
        if isinstance(a, dict) and isinstance(b, dict):
            parts = [f"{f}: {fmt(a.get(f))} → {fmt(b.get(f))}"
                     for f in sorted(a.keys() | b.keys()) if a.get(f) != b.get(f)]
            lines.append(f"changed `{k}` " + "; ".join(parts))
        else:
            lines.append(f"changed `{k}`: {fmt(a)} → {fmt(b)}")
    return lines


def describe_model(m: dict) -> str:
    bits = [fmt(m.get("display_name", ""))]
    for f in ("visibility", "context_window", "model_specialty"):
        if m.get(f) is not None:
            bits.append(f"{f} {m[f]}")
    return "(" + ", ".join(b for b in bits if b) + ")"


def describe_feature(f: dict) -> str:
    bits = [f.get("stage", "?"), "on by default" if f.get("default_enabled") else "off by default"]
    if f.get("name"):
        bits.append(fmt(f["name"]))
    return "(" + ", ".join(bits) + ")"


def compute_diff(old: dict, new: dict) -> dict[str, list[str]]:
    sections = {
        "Models in the bundled catalog": diff_dicts(old.get("models", {}), new["models"], describe_model),
        "Plan labels": diff_dicts(old.get("plans", {}), new["plans"], lambda v: f"→ {fmt(v)}"),
        "Plan types": diff_dicts(
            {p: True for p in old.get("plan_types", [])}, {p: True for p in new["plan_types"]}, lambda v: ""),
        "Feature flags": diff_dicts(old.get("features", {}), new["features"], describe_feature),
        "Model IDs anywhere in source": diff_dicts(
            {k: v for k, v in old.get("model_ids", {}).items() if k not in old.get("models", {})},
            {k: v for k, v in new["model_ids"].items() if k not in new["models"]},
            lambda p: f"(first seen in `{p}`)"),
        "chatgpt.com / openai.com URLs": diff_dicts(
            {u: True for u in old.get("urls", [])}, {u: True for u in new["urls"]}, lambda v: ""),
    }
    return {k: v for k, v in sections.items() if v}


# ------------------------------------------------------------------ commits

def related_commits(old: dict, new: dict, sections: dict) -> list[dict]:
    """Commits in openai/codex that touched the changed files since the last change."""
    token = os.environ.get("GITHUB_TOKEN")
    since = old.get("source", {}).get("commit_date")
    if not token or not since:
        return []
    paths = set()
    names = {
        "Models in the bundled catalog": [PATHS["models"]],
        "Plan labels": [PATHS["plans"]],
        "Plan types": [PATHS["plan_types"]],
        "Feature flags": [PATHS["features"]],
    }
    for sec in sections:
        paths.update(names.get(sec, []))
    for mid in new["model_ids"].keys() - old.get("model_ids", {}).keys():
        paths.add(new["model_ids"][mid])
    seen, out = set(), []
    for p in sorted(paths)[:8]:
        q = urllib.parse.urlencode({"path": p, "since": since, "per_page": 10})
        req = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}/commits?{q}",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                commits = json.load(r)
        except Exception as e:  # network trouble must not break the log
            print(f"commit lookup failed for {p}: {e}", file=sys.stderr)
            continue
        for c in commits:
            if c["sha"] in seen or c["commit"]["committer"]["date"] <= since:
                continue
            seen.add(c["sha"])
            title = c["commit"]["message"].splitlines()[0]
            pr = re.search(r"\(#(\d+)\)\s*$", title)
            out.append({
                "sha": c["sha"],
                "date": c["commit"]["committer"]["date"],
                "title": title,
                "pr": int(pr.group(1)) if pr else None,
            })
    return sorted(out, key=lambda c: c["date"])[:15]


# ------------------------------------------------------------------- output

def render_entry(old: dict, new: dict, sections: dict, commits: list[dict], now: str) -> str:
    sha = new["source"]["sha"]
    short = sha[:12] if sha else "unknown"
    head = f"## {now} · [`{REPO}@{short}`](https://github.com/{REPO}/commit/{sha})" if sha else f"## {now}"
    lines = [head, ""]
    for title, items in sections.items():
        lines.append(f"**{title}**")
        lines += [f"- {i}" for i in items]
        lines.append("")
    if commits:
        lines.append("**Commits that touched these files**")
        for c in commits:
            link = (f"[#{c['pr']}](https://github.com/{REPO}/pull/{c['pr']})" if c["pr"]
                    else f"[{c['sha'][:7]}](https://github.com/{REPO}/commit/{c['sha']})")
            lines.append(f"- {link} {c['title']} ({c['date'][:16].replace('T', ' ')} UTC)")
        lines.append("")
    old_sha = old.get("source", {}).get("sha")
    if old_sha and sha and old_sha != sha:
        lines.append(f"[Full diff since the last change](https://github.com/{REPO}/compare/{old_sha[:12]}...{sha[:12]})")
        lines.append("")
    return "\n".join(lines)


def prepend_changelog(entry: str) -> None:
    header = "# Changelog\n\nNewest first. Every entry is a change in the public `openai/codex` source.\n\n"
    body = ""
    if os.path.exists(CHANGELOG):
        with open(CHANGELOG, encoding="utf-8") as f:
            text = f.read()
        body = text.split("\n## ", 1)[1] if "\n## " in text else ""
        body = ("## " + body) if body else ""
    with open(CHANGELOG, "w", encoding="utf-8") as f:
        f.write(header + entry + ("\n" + body if body else ""))


def replace_block(text: str, name: str, content: str) -> str:
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    if start not in text or end not in text:
        return text
    a, b = text.index(start) + len(start), text.index(end)
    return text[:a] + "\n" + content.rstrip() + "\n" + text[b:]


def catalog_table(snap: dict) -> str:
    rows = ["| slug | name | visibility | context | reasoning |", "|---|---|---|---|---|"]
    models = sorted(snap["models"].items(), key=lambda kv: (kv[1].get("priority") or 999, kv[0]))
    for slug, m in models:
        ctx = m.get("context_window", "")
        if m.get("max_context_window") and m.get("max_context_window") != ctx:
            ctx = f"{ctx} (max {m['max_context_window']})"
        rows.append(f"| `{slug}` | {m.get('display_name', '')} | {m.get('visibility', '')} | {ctx} | "
                    f"{', '.join(m.get('reasoning_levels', []))} |")
    src = snap["source"]
    rows.append("")
    rows.append(f"From [`{REPO}@{(src.get('sha') or '')[:12]}`](https://github.com/{REPO}/commit/{src.get('sha')}), "
                f"committed {src.get('commit_date', '?')}. Hidden models are in the catalog but not in the picker.")
    return "\n".join(rows)


def update_readme(snap: dict, entry: str | None) -> None:
    if not os.path.exists(README):
        return
    with open(README, encoding="utf-8") as f:
        text = f.read()
    text = replace_block(text, "catalog", catalog_table(snap))
    if entry:
        text = replace_block(text, "latest", entry.replace("## ", "### ", 1))
    with open(README, "w", encoding="utf-8") as f:
        f.write(text)


def notify_telegram(sections: dict, new: dict, commits: list[dict]) -> None:
    token, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        return
    sha = new["source"]["sha"]
    msg = [f"codex-watch: change in {REPO}@{sha[:7]}"]
    for title, items in sections.items():
        msg.append(f"\n{title}")
        msg += items[:10]
    for c in commits[:5]:
        msg.append(f"#{c['pr']} {c['title']}" if c["pr"] else c["title"])
    text = "\n".join(msg)[:3900]
    data = urllib.parse.urlencode({"chat_id": chat, "text": text, "disable_web_page_preview": "true"}).encode()
    try:
        urllib.request.urlopen(f"https://api.telegram.org/bot{token}/sendMessage", data=data, timeout=20)
    except Exception as e:
        print(f"telegram failed: {e}", file=sys.stderr)


def set_output(**kv) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        for k, v in kv.items():
            f.write(f"{k}={v}\n")


def summary_line(sections: dict, sha: str) -> str:
    counts = ", ".join(f"{len(v)} × {k.lower()}" for k, v in sections.items())
    return f"{REPO}@{sha[:7]}: {counts}"


# --------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--codex", required=True, help="path to a checkout of openai/codex")
    ap.add_argument("--sha", default="", help="commit SHA of that checkout")
    ap.add_argument("--commit-date", default="", help="ISO date of that commit")
    ap.add_argument("--baseline", action="store_true", help="write snapshot.json without logging a change")
    ap.add_argument("--dry-run", action="store_true", help="print the entry, write nothing")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(args.codex, "codex-rs")):
        print(f"{args.codex} does not look like an openai/codex checkout", file=sys.stderr)
        return 2

    new = build_snapshot(args.codex, args.sha, args.commit_date)
    if not new["models"] or not new["features"]:
        print("warning: models or features came back empty, the source layout may have moved", file=sys.stderr)

    if args.baseline or not os.path.exists(SNAPSHOT):
        if not args.dry_run:
            with open(SNAPSHOT, "w", encoding="utf-8") as f:
                json.dump(new, f, indent=1, ensure_ascii=False)
                f.write("\n")
            update_readme(new, None)
        print(f"baseline written: {len(new['models'])} models, {len(new['features'])} flags, "
              f"{len(new['model_ids'])} model IDs, {len(new['urls'])} URLs")
        set_output(changed="false")
        return 0

    with open(SNAPSHOT, encoding="utf-8") as f:
        old = json.load(f)
    sections = compute_diff(old, new)
    if not sections:
        print("no change")
        set_output(changed="false")
        return 0

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    commits = related_commits(old, new, sections)
    entry = render_entry(old, new, sections, commits, now)
    print(entry)
    if args.dry_run:
        return 0

    prepend_changelog(entry)
    with open(CHANGES_JSONL, "a", encoding="utf-8") as f:
        f.write(json.dumps({"logged_at": now, "source": new["source"], "changes": sections,
                            "commits": commits}, ensure_ascii=False) + "\n")
    with open(SNAPSHOT, "w", encoding="utf-8") as f:
        json.dump(new, f, indent=1, ensure_ascii=False)
        f.write("\n")
    update_readme(new, entry)
    notify_telegram(sections, new, commits)
    msg_path = os.environ.get("RUNNER_TEMP", "/tmp") + "/codex-watch-msg.txt"
    with open(msg_path, "w", encoding="utf-8") as f:
        f.write(summary_line(sections, new["source"]["sha"] or "unknown") + "\n")
    set_output(changed="true", message_file=msg_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
