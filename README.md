# codex-watch

A running log of what changes in OpenAI's public [Codex](https://github.com/openai/codex) source that points at unreleased models, plans and features.

OpenAI ships Codex in the open. Model catalogs, plan names and feature flags land in `main` before anyone announces them. This repo reads `main` every 15 minutes and writes down what moved, with the commit and PR that moved it.

## Latest change

<!-- latest:start -->
### 2026-10-03 07:16 UTC · [`openai/codex@19e554bb7010`](https://github.com/openai/codex/commit/19e554bb70103b17aa7dca6bbd0dbf1c8b2eddb6)

**Models in the bundled catalog**
- added `gpt-6.1-sol` ("GPT-6.1-Sol", visibility list, context_window 272000)
- changed `gpt-5.5` priority: 12 → 13
- changed `gpt-5.6-luna` priority: 8 → 9
- changed `gpt-5.6-sol` description: "Older coding model for complex work." → "Older generation workhorse model."; priority: 4 → 5
- changed `gpt-5.6-terra` priority: 7 → 8
- changed `gpt-6-astra` priority: 1 → 2
- changed `gpt-6-luna` priority: 3 → 4
- changed `gpt-6-sol` description: "Workhorse model for coding and everyday work." → "Previous generation workhorse model."; priority: 2 → 3
- changed `gpt-daybreak-blue-latest` priority: 10 → 11
- changed `gpt-daybreak-red-latest` priority: 11 → 12

**Feature flags**
- added `api_key_cyber_access_programs` (Stable, off by default)
- added `browser_annotation_api` (Stable, on by default)
- added `guardianv2_decisions_comparison` (UnderDevelopment, off by default)
- added `in_app_voice` (Stable, on by default)
- added `incremental_tools` (UnderDevelopment, off by default)
- added `login_shell_package_path` (Experimental, off by default, "Bundled tools in login shells")
- added `model_catalog_in_context` (UnderDevelopment, off by default)
- added `multi_agent_v2_dynamic_tools` (UnderDevelopment, off by default)
- changed `api_key_model_discovery` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**chatgpt.com / openai.com URLs**
- added `https://api.openai.com/v1/decisions`
- added `https://chatgpt.com/settings/usage`
- added `https://learn.chatgpt.com/docs/enterprise/govcloud-configuration`
- removed `https://chatgpt.com/codex/settings/usage`

**Commits that touched these files**
- [#49267](https://github.com/openai/codex/pull/49267) Support remote agent message boards in multi-agent sessions (#49267) (2026-09-29 13:52 UTC)
- [#49318](https://github.com/openai/codex/pull/49318) Add GPT-6.1 Sol as the default catalog model (#49318) (2026-09-29 17:22 UTC)
- [#49339](https://github.com/openai/codex/pull/49339) Add GPT-6.1 Sol to Bedrock catalogs and make it the default (#49339) (2026-09-29 18:50 UTC)
- [#49345](https://github.com/openai/codex/pull/49345) Enable multi-agent V2 and Ultra reasoning on Amazon Bedrock (#49345) (2026-09-29 19:03 UTC)
- [#49403](https://github.com/openai/codex/pull/49403) Add an experimental flag for bundled tools in login shells (#49403) (2026-09-29 23:33 UTC)
- [#49406](https://github.com/openai/codex/pull/49406) Support explicit cyber access programs with OpenAI API keys (#49406) (2026-09-30 00:08 UTC)
- [#49560](https://github.com/openai/codex/pull/49560) Add an opt-in model catalog to multi-agent context (#49560) (2026-09-30 10:03 UTC)
- [#49683](https://github.com/openai/codex/pull/49683) Add a managed feature gate for in-app voice (#49683) (2026-09-30 17:20 UTC)
- [#49784](https://github.com/openai/codex/pull/49784) Add a requirements feature gate for the browser annotation API (#49784) (2026-10-01 00:56 UTC)
- [#49807](https://github.com/openai/codex/pull/49807) Enable API-key model discovery by default (#49807) (2026-10-01 01:38 UTC)
- [#50082](https://github.com/openai/codex/pull/50082) Enable dynamic tool inheritance for fresh V2 subagents (#50082) (2026-10-01 19:45 UTC)
- [#50099](https://github.com/openai/codex/pull/50099) Add opt-in Decisions comparison for Guardian V2 (#50099) (2026-10-01 21:05 UTC)
- [#50464](https://github.com/openai/codex/pull/50464) Add the `incremental_tools` feature flag (#50464) (2026-10-02 23:49 UTC)
- [#50472](https://github.com/openai/codex/pull/50472) Enable Ultrafast service tiers for Amazon Bedrock Astra models (#50472) (2026-10-03 00:31 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/c248f6d48b97...19e554bb7010)
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

From [`openai/codex@19e554bb7010`](https://github.com/openai/codex/commit/19e554bb70103b17aa7dca6bbd0dbf1c8b2eddb6), committed 2026-10-03T07:14:12Z. Hidden models are in the catalog but not in the picker.
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
