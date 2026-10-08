# codex-watch

A running log of what changes in OpenAI's public [Codex](https://github.com/openai/codex) source that points at unreleased models, plans and features.

OpenAI ships Codex in the open. Model catalogs, plan names and feature flags land in `main` before anyone announces them. This repo reads `main` every 15 minutes and writes down what moved, with the commit and PR that moved it.

## Latest change

<!-- latest:start -->
### 2026-10-08 16:21 UTC · [`openai/codex@cd85a26cae00`](https://github.com/openai/codex/commit/cd85a26cae00385a0dd9247381ef5d1d7ffe9ef3)

**Feature flags**
- changed `shell_zsh_fork` stage: "UnderDevelopment" → "Removed"
- changed `unified_exec_zsh_fork` default_enabled: True → False

**Commits that touched these files**
- [#52160](https://github.com/openai/codex/pull/52160) Remove the patched zsh shell execution backend (#52160) (2026-10-08 16:19 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/72c959528ee4...cd85a26cae00)
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

From [`openai/codex@cd85a26cae00`](https://github.com/openai/codex/commit/cd85a26cae00385a0dd9247381ef5d1d7ffe9ef3), committed 2026-10-08T16:19:09Z. Hidden models are in the catalog but not in the picker.
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
