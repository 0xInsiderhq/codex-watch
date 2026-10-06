# Changelog

Newest first. Every entry is a change in the public `openai/codex` source.

## 2026-10-06 00:56 UTC · [`openai/codex@4d1579433666`](https://github.com/openai/codex/commit/4d15794336668d6098c0e36eb8e96cbbbfdb1d2d)

**Feature flags**
- added `code_mode_tool_search` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#51209](https://github.com/openai/codex/pull/51209) Add ranked tool discovery to JavaScript code mode (#51209) (2026-10-06 00:36 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/5ad689169645...4d1579433666)

## 2026-10-06 00:29 UTC · [`openai/codex@5ad689169645`](https://github.com/openai/codex/commit/5ad689169645a953ec7380762c4ae596712057ee)

**Feature flags**
- added `cli_daybreak` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#51207](https://github.com/openai/codex/pull/51207) Gate CLI Daybreak controls and selection behind an opt-in feature (#51207) (2026-10-06 00:16 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/685270a56a96...5ad689169645)

## 2026-10-05 23:56 UTC · [`openai/codex@685270a56a96`](https://github.com/openai/codex/commit/685270a56a96c76ae5b0853373a19d6ed5bc6fd4)

**Feature flags**
- changed `apply_patch_preserve_line_endings` stage: "UnderDevelopment" → "Removed"

**Commits that touched these files**
- [#51203](https://github.com/openai/codex/pull/51203) Make apply_patch preserve line endings unconditionally (#51203) (2026-10-05 23:52 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/335c7f8ecab2...685270a56a96)

## 2026-10-04 21:11 UTC · [`openai/codex@335c7f8ecab2`](https://github.com/openai/codex/commit/335c7f8ecab29c4462a553bbf174276d2c67a766)

**Feature flags**
- added `stable_environment_tools` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#50962](https://github.com/openai/codex/pull/50962) Gate stable environment tool exposure behind a feature flag (#50962) (2026-10-04 21:08 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/58ae3ba61186...335c7f8ecab2)

## 2026-10-03 18:42 UTC · [`openai/codex@58ae3ba61186`](https://github.com/openai/codex/commit/58ae3ba61186c39b849a6ebe60e60f4b11690373)

**Feature flags**
- added `code_mode_only_strict_3p_tools` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#50687](https://github.com/openai/codex/pull/50687) Keep third-party tools deferred in strict Code Mode Only (#50687) (2026-10-03 18:15 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/19e554bb7010...58ae3ba61186)

## 2026-10-03 07:16 UTC · [`openai/codex@19e554bb7010`](https://github.com/openai/codex/commit/19e554bb70103b17aa7dca6bbd0dbf1c8b2eddb6)

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

## 2026-09-29 · baseline at [`openai/codex@c248f6d48b97`](https://github.com/openai/codex/commit/c248f6d48b97eb4a2aa56147a0b11b7d763278b9)

Tracking starts here, on DevDay morning. The snapshot holds 10 catalog models, 154 feature flags, 29 model IDs and 57 chatgpt.com / openai.com URLs.

Already in the code at this point:

- Plan labels `Pro 100`, `Pro 200`, `Pro 500` for `prolite`, `pro`, `promax` ([#49079](https://github.com/openai/codex/pull/49079)), plus `Business Premium` for `SelfServeBusinessProLite`.
- Hidden catalog entries `gpt-daybreak-blue-latest`, `gpt-daybreak-red-latest` (the Daybreak cyber programs) and `codex-auto-review`.
- `gpt-6-astra-wm`, treated the same as `gpt-6-astra` in `codex-rs/tui/src/daybreak.rs`, and nowhere in the catalog.
