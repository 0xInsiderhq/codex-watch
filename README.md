# codex-watch

A running log of what changes in OpenAI's public [Codex](https://github.com/openai/codex) source that points at unreleased models, plans and features.

OpenAI ships Codex in the open. Model catalogs, plan names and feature flags land in `main` before anyone announces them. This repo reads `main` every 15 minutes and writes down what moved, with the commit and PR that moved it.

## Latest change

<!-- latest:start -->
### 2026-10-26 21:55 UTC · [`openai/codex@716b4ec6dffc`](https://github.com/openai/codex/commit/716b4ec6dffc7b23b1c598400bccb622551bf787)

**Feature flags**
- added `critical_path_timing` (UnderDevelopment, off by default)
- added `mcp_connection_sharing` (UnderDevelopment, off by default)
- added `plugin_discovery_prefetch` (Stable, on by default)
- added `skill_catalog_deltas` (UnderDevelopment, off by default)
- added `untrusted_as_tool_output` (UnderDevelopment, off by default)

**chatgpt.com / openai.com URLs**
- added `https://gov.chatgpt.com/backend-api/`
- added `https://gov.chatgpt.com/backend-api/codex`

**Commits that touched these files**
- [#57201](https://github.com/openai/codex/pull/57201) Capture direct-tool critical paths behind a feature flag (#57201) (2026-10-26 19:19 UTC)
- [#57204](https://github.com/openai/codex/pull/57204) Register the `untrusted_as_tool_output` feature flag (#57204) (2026-10-26 19:27 UTC)
- [#57210](https://github.com/openai/codex/pull/57210) Add opt-in protocol discovery for local stdio MCP servers (#57210) (2026-10-26 19:37 UTC)
- [#57211](https://github.com/openai/codex/pull/57211) Share eligible local stdio MCP connections across chats (#57211) (2026-10-26 19:37 UTC)
- [#57249](https://github.com/openai/codex/pull/57249) Allow disabling plugin discovery prefetch at app-server startup (#57249) (2026-10-26 20:54 UTC)
- [#57262](https://github.com/openai/codex/pull/57262) Add incremental skill catalogs behind `skill_catalog_deltas` (#57262) (2026-10-26 21:20 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/2839ed763bd3...716b4ec6dffc)
<!-- latest:end -->

Full history in [CHANGELOG.md](CHANGELOG.md). Machine-readable in [changes.jsonl](changes.jsonl).

## What it tracks

| signal | where it lives in openai/codex |
|---|---|
| Bundled model catalog: slug, name, visibility, context window, reasoning levels | `codex-rs/models-manager/models.json` |
| Plan labels shown in the CLI (`Pro 200`, `Business Premium`…) | `codex-rs/tui/src/subscription.rs` |
| Plan types the client knows about | `codex-rs/protocol/src/account.rs` |
| Feature flags: key, stage, default | `codex-rs/features/src/lib.rs` |
| Any model-looking ID anywhere in non-test source | whole repo |
| Any chatgpt.com / openai.com URL in non-test source | whole repo |

Test files and `#[cfg(test)]` blocks are skipped, so `gpt-test` and friends don't show up.

## Model catalog right now

<!-- catalog:start -->
| slug | name | visibility | context | reasoning |
|---|---|---|---|---|
| `gpt-6.1-sol` | GPT-6.1-Sol | list | 272000 (max 872000) | low, medium, high, xhigh, max, ultra |
| `gpt-6-astra` | GPT-6-Astra | list | 272000 (max 872000) | low, medium, high, xhigh, max, ultra |
| `gpt-6-sol` | GPT-6-Sol | list | 272000 (max 872000) | low, medium, high, xhigh, max, ultra |
| `gpt-6-luna` | GPT-6-Luna | list | 272000 (max 872000) | low, medium, high, xhigh, max |
| `gpt-5.6-sol` | GPT-5.6-Sol | list | 272000 (max 872000) | low, medium, high, xhigh, max, ultra |
| `gpt-5.6-terra` | GPT-5.6-Terra | list | 272000 (max 872000) | low, medium, high, xhigh, max, ultra |
| `gpt-5.6-luna` | GPT-5.6-Luna | list | 272000 (max 872000) | low, medium, high, xhigh, max |
| `gpt-daybreak-blue-latest` | Daybreak Blue | hide | 272000 (max 872000) | low, medium, high, xhigh, max, ultra |
| `gpt-daybreak-red-latest` | Daybreak Red | hide | 372000 | low, medium, high, xhigh, max, ultra |
| `gpt-5.5` | GPT-5.5 | list | 272000 | low, medium, high, xhigh |
| `codex-auto-review` | Codex Auto Review | hide | 272000 (max 872000) | low, medium, high, xhigh, max |

From [`openai/codex@716b4ec6dffc`](https://github.com/openai/codex/commit/716b4ec6dffc7b23b1c598400bccb622551bf787), committed 2026-10-26T21:48:19Z. Hidden models are in the catalog but not in the picker.
<!-- catalog:end -->

## Found before this repo existed

The ChatGPT Pro tiers were renamed three times in Codex in a few days:

| PR | `prolite` | `pro` | `promax` |
|---|---|---|---|
| [#47971](https://github.com/openai/codex/pull/47971) | Pro | Pro (More) | Pro (Max) |
| [#49043](https://github.com/openai/codex/pull/49043), 28 Sep 17:58 UTC | Pro Standard | Pro Extra | Pro Max |
| [#49079](https://github.com/openai/codex/pull/49079), 28 Sep 20:59 UTC | **Pro 100** | **Pro 200** | **Pro 500** |

The last rename landed the night before DevDay. The public Pro plans are $100 and $200, so the third label reads like a price. That part is our reading, not something the code says.

## How it works

1. GitHub Actions clones `openai/codex` at depth 1 every 15 minutes ([workflow](.github/workflows/watch.yml)).
2. [`watch.py`](watch.py) extracts the signals above and compares them with [`snapshot.json`](snapshot.json).
3. If anything changed, it prepends an entry to the changelog, looks up the commits that touched those files, refreshes this README and commits.

No dependencies beyond the Python standard library.

```bash
git clone --depth 1 https://github.com/openai/codex /tmp/codex
python3 watch.py --codex /tmp/codex --dry-run
```

### Alerts

Add two repository secrets, `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`, and every logged change is also sent to that chat.

## Read it with care

- A string in the code is not a launch. Slugs, flags and labels get added, renamed and deleted all the time.
- Hidden catalog entries exist for internal and access-gated models. Hidden does not mean coming soon.
- This reads public code only. Not affiliated with OpenAI.

Made by [@0xInsiderf5](https://x.com/0xInsiderf5). Found something in the log worth a post? Tag me.
