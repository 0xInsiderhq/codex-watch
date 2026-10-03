# Changelog

Newest first. Every entry is a change in the public `openai/codex` source.

## 2026-09-29 · baseline at [`openai/codex@c248f6d48b97`](https://github.com/openai/codex/commit/c248f6d48b97eb4a2aa56147a0b11b7d763278b9)

Tracking starts here, on DevDay morning. The snapshot holds 10 catalog models, 154 feature flags, 29 model IDs and 57 chatgpt.com / openai.com URLs.

Already in the code at this point:

- Plan labels `Pro 100`, `Pro 200`, `Pro 500` for `prolite`, `pro`, `promax` ([#49079](https://github.com/openai/codex/pull/49079)), plus `Business Premium` for `SelfServeBusinessProLite`.
- Hidden catalog entries `gpt-daybreak-blue-latest`, `gpt-daybreak-red-latest` (the Daybreak cyber programs) and `codex-auto-review`.
- `gpt-6-astra-wm`, treated the same as `gpt-6-astra` in `codex-rs/tui/src/daybreak.rs`, and nowhere in the catalog.
