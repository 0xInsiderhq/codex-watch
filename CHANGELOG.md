# Changelog

Newest first. Every entry is a change in the public `openai/codex` source.

## 2026-10-29 06:19 UTC · [`openai/codex@23934d31b15b`](https://github.com/openai/codex/commit/23934d31b15b1127c83535f84854e5009f7cd51d)

**Feature flags**
- added `tui_extensions_statusline` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#57970](https://github.com/openai/codex/pull/57970) Add an experimental UI tree renderer for the status line (#57970) (2026-10-29 03:07 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/f276b82185f0...23934d31b15b)

## 2026-10-29 00:16 UTC · [`openai/codex@f276b82185f0`](https://github.com/openai/codex/commit/f276b82185f021e7b8d532a3851413bc79a67594)

**Feature flags**
- added `gcp_setup_wizard` (Stable, off by default)
- added `interrupt_on_cancel` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#57857](https://github.com/openai/codex/pull/57857) Add Google Cloud Vertex AI setup to TUI onboarding (#57857) (2026-10-28 23:06 UTC)
- [#57864](https://github.com/openai/codex/pull/57864) Allow upstream interruption when canceling Responses Lite turns (#57864) (2026-10-29 00:03 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/4d3ed3f3b47d...f276b82185f0)

## 2026-10-27 18:37 UTC · [`openai/codex@4d3ed3f3b47d`](https://github.com/openai/codex/commit/4d3ed3f3b47d39f8fe0b60df74a20f528b6fc618)

**Feature flags**
- added `omit_skill_descriptions` (UnderDevelopment, off by default)
- changed `code_mode_tool_description_first` stage: "UnderDevelopment" → "Removed"

**Commits that touched these files**
- [#57451](https://github.com/openai/codex/pull/57451) Route state-changing multi-agent calls through Guardian review (#57451) (2026-10-27 13:21 UTC)
- [#57462](https://github.com/openai/codex/pull/57462) Always put Code Mode tool descriptions before namespace descriptions (#57462) (2026-10-27 14:14 UTC)
- [#57500](https://github.com/openai/codex/pull/57500) Add an option to omit descriptions from skill catalogs (#57500) (2026-10-27 16:16 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/a5ef02e56147...4d3ed3f3b47d)

## 2026-10-27 12:46 UTC · [`openai/codex@a5ef02e56147`](https://github.com/openai/codex/commit/a5ef02e56147c4c3da493655fd5e2c64db13210f)

**Feature flags**
- added `guardian_native_multi_agent_history` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#57441](https://github.com/openai/codex/pull/57441) Add Guardian native multi-agent history feature flag (#57441) (2026-10-27 12:28 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/ce7adb6a31f2...a5ef02e56147)

## 2026-10-27 01:21 UTC · [`openai/codex@ce7adb6a31f2`](https://github.com/openai/codex/commit/ce7adb6a31f2909a48afa538c2cdb7a6254a0e4b)

**Models in the bundled catalog**
- added `gpt-6.1-terra` ("GPT-6.1 Terra", visibility list, context_window 500000)

**Feature flags**
- added `prediction_preserve_parent_tools` (Stable, on by default)
- added `simplified_selection_hints` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#57287](https://github.com/openai/codex/pull/57287) Preserve parent tool declarations in prediction forks (#57287) (2026-10-26 22:05 UTC)
- [#57293](https://github.com/openai/codex/pull/57293) Add GPT-6.1 Terra to model catalogs (#57293) (2026-10-26 22:13 UTC)
- [#57317](https://github.com/openai/codex/pull/57317) Add opt-in concise hints for explicitly selected plugins (#57317) (2026-10-27 00:52 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/716b4ec6dffc...ce7adb6a31f2)

## 2026-10-26 21:55 UTC · [`openai/codex@716b4ec6dffc`](https://github.com/openai/codex/commit/716b4ec6dffc7b23b1c598400bccb622551bf787)

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

## 2026-10-23 15:24 UTC · [`openai/codex@2839ed763bd3`](https://github.com/openai/codex/commit/2839ed763bd3f404398e1f0c95bf4e2d172213c0)

**Feature flags**
- added `guardianv3` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#56459](https://github.com/openai/codex/pull/56459) Add Guardian V3 feature configuration (#56459) (2026-10-23 12:16 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/2f3fb111be71...2839ed763bd3)

## 2026-10-22 13:20 UTC · [`openai/codex@2f3fb111be71`](https://github.com/openai/codex/commit/2f3fb111be71d277c80bd5b96d9019748b921f5a)

**Feature flags**
- changed `reasoning_effort_override` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**Commits that touched these files**
- [#56163](https://github.com/openai/codex/pull/56163) Enable reasoning effort overrides by default (#56163) (2026-10-22 12:46 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/b337fe06b7d8...2f3fb111be71)

## 2026-10-22 10:08 UTC · [`openai/codex@b337fe06b7d8`](https://github.com/openai/codex/commit/b337fe06b7d8d6e5b42295e04c5e92c2b9c46567)

**Feature flags**
- added `guardian_recorded_items` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#56124](https://github.com/openai/codex/pull/56124) Forward Guardian reviewer events to parent raw-event subscribers (#56124) (2026-10-22 09:20 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/86e17e98c7f9...b337fe06b7d8)

## 2026-10-22 07:04 UTC · [`openai/codex@86e17e98c7f9`](https://github.com/openai/codex/commit/86e17e98c7f901277aeeb4649cf1b01462b082f2)

**Feature flags**
- added `tui_multi_backend` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#56097](https://github.com/openai/codex/pull/56097) Prepare TUI startup to accept multiple backend sessions (#56097) (2026-10-22 06:32 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/45179176e52a...86e17e98c7f9)

## 2026-10-22 01:19 UTC · [`openai/codex@45179176e52a`](https://github.com/openai/codex/commit/45179176e52ab890a3cf5ce47e8ab585e7295f7e)

**Feature flags**
- changed `bedrock_setup_wizard` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**Commits that touched these files**
- [#56033](https://github.com/openai/codex/pull/56033) Enable the Bedrock setup wizard by default (#56033) (2026-10-22 00:50 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/35757adb728b...45179176e52a)

## 2026-10-20 23:55 UTC · [`openai/codex@35757adb728b`](https://github.com/openai/codex/commit/35757adb728b268a1e75eabeb3e4cf9a6def5c18)

**Feature flags**
- changed `mcp_oauth_refresh_coordination` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**Commits that touched these files**
- [#55701](https://github.com/openai/codex/pull/55701) Enable MCP OAuth refresh coordination by default (#55701) (2026-10-20 23:42 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/cb00a6756945...35757adb728b)

## 2026-10-20 17:39 UTC · [`openai/codex@cb00a6756945`](https://github.com/openai/codex/commit/cb00a67569450aea2fdb1b1f31fc042fc0b5416f)

**Feature flags**
- added `runtime_agent_instances` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#55636](https://github.com/openai/codex/pull/55636) Add runtime assertion authentication modes and an auth provider (#55636) (2026-10-20 17:29 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/79a19cbb3008...cb00a6756945)

## 2026-10-19 23:13 UTC · [`openai/codex@79a19cbb3008`](https://github.com/openai/codex/commit/79a19cbb3008afe2882ccc2c5d93f02cde9a0823)

**chatgpt.com / openai.com URLs**
- added `https://auth.openai.com/agent/register`

[Full diff since the last change](https://github.com/openai/codex/compare/e64530972398...79a19cbb3008)

## 2026-10-19 22:02 UTC · [`openai/codex@e64530972398`](https://github.com/openai/codex/commit/e64530972398604464a6aa0d1ace7b9399e9e942)

**Plan types**
- added `Sci`
- added `SciPlus`

**Feature flags**
- changed `transcript_v2` stage: "Deprecated" → "Removed"

**Commits that touched these files**
- [#55387](https://github.com/openai/codex/pull/55387) Add support for Academic Researchers plans (#55387) (2026-10-19 21:43 UTC)
- [#55388](https://github.com/openai/codex/pull/55388) Mark `transcript_v2` as removed (#55388) (2026-10-19 21:44 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/e389b2444c75...e64530972398)

## 2026-10-19 20:48 UTC · [`openai/codex@e389b2444c75`](https://github.com/openai/codex/commit/e389b2444c75cbc92d40b2135ca5db300d076979)

**Feature flags**
- added `subagent_thread_environments` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#55375](https://github.com/openai/codex/pull/55375) Add configured thread environment inheritance for subagents (#55375) (2026-10-19 20:30 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/c953dacb42d2...e389b2444c75)

## 2026-10-19 20:04 UTC · [`openai/codex@c953dacb42d2`](https://github.com/openai/codex/commit/c953dacb42d2773d0ca9cc25a01129bba2ca36a8)

**Feature flags**
- changed `incremental_tools` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**Commits that touched these files**
- [#55327](https://github.com/openai/codex/pull/55327) Add configured thread environment inheritance for subagents (#55327) (2026-10-19 17:16 UTC)
- [#55331](https://github.com/openai/codex/pull/55331) Use step environment snapshots for subagent inheritance (#55331) (2026-10-19 17:43 UTC)
- [#55368](https://github.com/openai/codex/pull/55368) Enable incremental tools by default for Responses Lite (#55368) (2026-10-19 20:01 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/8c076942cb70...c953dacb42d2)

## 2026-10-18 02:00 UTC · [`openai/codex@8c076942cb70`](https://github.com/openai/codex/commit/8c076942cb70fba8e5c4732c23f1faabc4aed484)

**Feature flags**
- added `wake_on_agent_messages` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#54961](https://github.com/openai/codex/pull/54961) Allow agent messages to wake idle root sessions behind a feature flag (#54961) (2026-10-18 01:58 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/7b44ac166143...8c076942cb70)

## 2026-10-17 23:50 UTC · [`openai/codex@7b44ac166143`](https://github.com/openai/codex/commit/7b44ac1661433ae3a6f375fde873fa7123c935fe)

**Feature flags**
- added `app_server_websocket_compression` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#54949](https://github.com/openai/codex/pull/54949) Gate app-server WebSocket compression behind a feature flag (#54949) (2026-10-17 23:34 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/5009a99dfc07...7b44ac166143)

## 2026-10-17 00:35 UTC · [`openai/codex@5009a99dfc07`](https://github.com/openai/codex/commit/5009a99dfc07830ddf7464c26f310a2b8532b55d)

**Feature flags**
- added `multi_env_copy_file` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#54741](https://github.com/openai/codex/pull/54741) Gate the file-copy extension behind `multi_env_copy_file` (#54741) (2026-10-17 00:02 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/0df4aa67781a...5009a99dfc07)

## 2026-10-16 17:04 UTC · [`openai/codex@0df4aa67781a`](https://github.com/openai/codex/commit/0df4aa67781ae45a3c97befa4db48b734afe46d9)

**Feature flags**
- added `mcp_tool_list_changed` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#54656](https://github.com/openai/codex/pull/54656) Honor MCP tool-list changes within a turn (#54656) (2026-10-16 16:40 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/bb64b894fd67...0df4aa67781a)

## 2026-10-15 04:05 UTC · [`openai/codex@bb64b894fd67`](https://github.com/openai/codex/commit/bb64b894fd67158be0f874872e6d7bfe717e7368)

**Feature flags**
- changed `realtime_conversation` stage: "Stable" → "Removed"
- changed `worktrees` stage: "Stable" → "Removed"

**Commits that touched these files**
- [#54175](https://github.com/openai/codex/pull/54175) Retire worktree and voice feature flags (#54175) (2026-10-15 03:48 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/160b2b1ef621...bb64b894fd67)

## 2026-10-15 03:28 UTC · [`openai/codex@160b2b1ef621`](https://github.com/openai/codex/commit/160b2b1ef62114eeb41e41e5e3be0000d944b713)

**chatgpt.com / openai.com URLs**
- added `https://gov.chatgpt.com`

[Full diff since the last change](https://github.com/openai/codex/compare/1ffa95ee8a02...160b2b1ef621)

## 2026-10-14 21:27 UTC · [`openai/codex@1ffa95ee8a02`](https://github.com/openai/codex/commit/1ffa95ee8a02ec68f6ccd758998bcb7d4b32bcdb)

**Feature flags**
- changed `stable_environment_tools` stage: "UnderDevelopment" → "Removed"

**Commits that touched these files**
- [#54098](https://github.com/openai/codex/pull/54098) Keep environment tools stable across readiness changes (#54098) (2026-10-14 21:06 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/cf0ed4c60016...1ffa95ee8a02)

## 2026-10-13 18:43 UTC · [`openai/codex@cf0ed4c60016`](https://github.com/openai/codex/commit/cf0ed4c600161fcaa18eeac02b5fc715e1076955)

**Feature flags**
- added `executor_capability_discovery_v2` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#53736](https://github.com/openai/codex/pull/53736) Acquire and cache opt-in executor capability inventories via V2 (#53736) (2026-10-13 18:15 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/6cc7d9cc5c70...cf0ed4c60016)

## 2026-10-13 17:02 UTC · [`openai/codex@6cc7d9cc5c70`](https://github.com/openai/codex/commit/6cc7d9cc5c702c0ca133f7ea48432166e0b880be)

**Feature flags**
- changed `api_key_cyber_access_programs` default_enabled: False → True

**Commits that touched these files**
- [#53717](https://github.com/openai/codex/pull/53717) Enable Cyber access programs for API-key sessions by default (#53717) (2026-10-13 16:57 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/6fbfc352cafb...6cc7d9cc5c70)

## 2026-10-13 15:38 UTC · [`openai/codex@6fbfc352cafb`](https://github.com/openai/codex/commit/6fbfc352cafb50332d62dbdc8720cb5d7fe3b7c7)

**Feature flags**
- changed `cli_daybreak` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**Commits that touched these files**
- [#53701](https://github.com/openai/codex/pull/53701) Enable CLI Daybreak by default and enforce background-turn eligibility (#53701) (2026-10-13 15:33 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/669449b02c4b...6fbfc352cafb)

## 2026-10-13 07:51 UTC · [`openai/codex@669449b02c4b`](https://github.com/openai/codex/commit/669449b02c4b58de4bcd22485eb60c98a6e38a54)

**Feature flags**
- added `async_compaction` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#53595](https://github.com/openai/codex/pull/53595) Add async compaction feature configuration (#53595) (2026-10-13 07:32 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/6c0c6759d061...669449b02c4b)

## 2026-10-10 17:34 UTC · [`openai/codex@6c0c6759d061`](https://github.com/openai/codex/commit/6c0c6759d0617d7670826b61aca0a931bbb6db1f)

**Feature flags**
- added `retain_client_tool_outputs` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#52937](https://github.com/openai/codex/pull/52937) Retain client-marked tool outputs across compaction (#52937) (2026-10-10 17:30 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/5ef96ab2785f...6c0c6759d061)

## 2026-10-10 01:47 UTC · [`openai/codex@5ef96ab2785f`](https://github.com/openai/codex/commit/5ef96ab2785f3ecddf279639eff7b1b42c906fa4)

**Feature flags**
- added `output_token_replay` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#52742](https://github.com/openai/codex/pull/52742) Add opt-in output token replay for OpenAI requests (#52742) (2026-10-10 01:25 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/4bad6d78e9b5...5ef96ab2785f)

## 2026-10-09 23:45 UTC · [`openai/codex@4bad6d78e9b5`](https://github.com/openai/codex/commit/4bad6d78e9b50f9fa8bd941f1db012ed491ad2da)

**Feature flags**
- added `code_mode_host_grpc` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#52723](https://github.com/openai/codex/pull/52723) Add opt-in gRPC over stdio for the code-mode host (#52723) (2026-10-09 23:26 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/65b82cdf96f9...4bad6d78e9b5)

## 2026-10-09 18:19 UTC · [`openai/codex@65b82cdf96f9`](https://github.com/openai/codex/commit/65b82cdf96f9d305494bc8c6c8d2404d37709030)

**Feature flags**
- added `subagent_default_context_limits` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#52659](https://github.com/openai/codex/pull/52659) Add an opt-in feature for subagent model context defaults (#52659) (2026-10-09 17:48 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/99aa05341d15...65b82cdf96f9)

## 2026-10-08 22:47 UTC · [`openai/codex@99aa05341d15`](https://github.com/openai/codex/commit/99aa05341d1564cf4ca2b463c83b607ea5d1bb3e)

**Feature flags**
- added `credential_masking` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#52302](https://github.com/openai/codex/pull/52302) Add opt-in credential masking for proxied sandboxed sessions (#52302) (2026-10-08 22:27 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/3b6ab3471a2d...99aa05341d15)

## 2026-10-08 20:19 UTC · [`openai/codex@3b6ab3471a2d`](https://github.com/openai/codex/commit/3b6ab3471a2d4d994c9fad322fca749564bc05e0)

**Feature flags**
- added `guardian_trust_orchestrator_connectors` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#52250](https://github.com/openai/codex/pull/52250) Add opt-in Guardian trust for orchestrator connector identities (#52250) (2026-10-08 20:04 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/cd85a26cae00...3b6ab3471a2d)

## 2026-10-08 16:21 UTC · [`openai/codex@cd85a26cae00`](https://github.com/openai/codex/commit/cd85a26cae00385a0dd9247381ef5d1d7ffe9ef3)

**Feature flags**
- changed `shell_zsh_fork` stage: "UnderDevelopment" → "Removed"
- changed `unified_exec_zsh_fork` default_enabled: True → False

**Commits that touched these files**
- [#52160](https://github.com/openai/codex/pull/52160) Remove the patched zsh shell execution backend (#52160) (2026-10-08 16:19 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/72c959528ee4...cd85a26cae00)

## 2026-10-07 21:47 UTC · [`openai/codex@72c959528ee4`](https://github.com/openai/codex/commit/72c959528ee4ca74abdb8575fbbc4e36960a8c47)

**Feature flags**
- changed `code_mode_interrupt` default_enabled: False → True; stage: "UnderDevelopment" → "Stable"

**Commits that touched these files**
- [#51835](https://github.com/openai/codex/pull/51835) Enable code mode interruption by default (#51835) (2026-10-07 21:28 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/406b0c44460c...72c959528ee4)

## 2026-10-07 19:45 UTC · [`openai/codex@406b0c44460c`](https://github.com/openai/codex/commit/406b0c44460cf71e90c21c7abe6e581add3a6421)

**Feature flags**
- changed `instant_interrupt` default_enabled: False → True

**Commits that touched these files**
- [#51812](https://github.com/openai/codex/pull/51812) Enable instant interrupts by default (#51812) (2026-10-07 19:42 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/95ec46861938...406b0c44460c)

## 2026-10-07 13:48 UTC · [`openai/codex@95ec46861938`](https://github.com/openai/codex/commit/95ec468619386ebb93506ac2091a48e5a558d25c)

**Feature flags**
- added `code_mode_tool_description_first` (UnderDevelopment, off by default)

**Commits that touched these files**
- [#51690](https://github.com/openai/codex/pull/51690) Add a feature flag for Code Mode tool description ordering (#51690) (2026-10-07 13:25 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/162fcb3976e2...95ec46861938)

## 2026-10-06 03:48 UTC · [`openai/codex@162fcb3976e2`](https://github.com/openai/codex/commit/162fcb3976e292fb7492924f7d493fdfce328551)

**Feature flags**
- added `ultrafast_mode` (Stable, on by default)

**Commits that touched these files**
- [#51253](https://github.com/openai/codex/pull/51253) Enforce Fast and Ultra Fast policies independently (#51253) (2026-10-06 03:35 UTC)

[Full diff since the last change](https://github.com/openai/codex/compare/4d1579433666...162fcb3976e2)

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
