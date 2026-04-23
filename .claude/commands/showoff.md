---
description: 4-runtime grid showoff -- validate claude+codex+gemini+ollama in 5 waves
argument-hint: "[--wave N] [--dry-run]"
related:
  - showoff_w2_n05_gemini
  - showoff_w5_n06_gemini
  - showoff_w5_n02_gemini
  - smoke_test_gemini_20260415
  - p12_wf_admin_orchestration
  - p01_kc_orchestration_best_practices
  - showoff_w4_n01_claude
  - showoff_w4_n03_claude
  - showoff_w4_n05_claude
  - showoff_w4_n06_claude
---

# /showoff -- Multi-Runtime Grid Validation

Runs 5 smoke waves to prove all 4 CEX runtimes work in grid dispatch.
Each wave uses the cheapest model for its runtime; each nucleus produces
one signature artifact under `_showoff/wN/{nucleus}_{runtime}.md`.

## Waves

| # | Runtime | Model | Cost | Notes |
|---|---------|-------|------|-------|
| 1 | ollama  | llama3.1:8b                | $0    | Local, free, slowest |
| 2 | gemini  | gemini-2.5-flash-lite      | cheap | Only model that responds on oauth-personal (pro hangs, 2.0-flash 404s) |
| 3 | codex   | (auth default, no --model) | cheap | ChatGPT-plus auth rejects explicit models |
| 4 | claude  | claude-haiku-4-5-20251001  | cheap | Cheapest Claude tier (skip with `--skip claude`) |
| 5 | MIXED   | 2 ollama + 2 gemini + 1 codex + 1 claude | mix | Real multi-runtime grid |

Each nucleus receives a trivial task (create 1 file + commit + signal),
so even the smallest local models can finish. Total wall time: ~25-40 min.

## Usage

```bash
# Full 5-wave run
python _tools/cex_showoff.py

# Single wave (e.g. validate gemini fix)
python _tools/cex_showoff.py --wave 2

# See the plan without dispatching
python _tools/cex_showoff.py --dry-run
```

## What it validates

- `boot/n0X_{runtime}.ps1` for all 4 runtimes.
- `_spawn/dispatch.sh grid-{runtime}` subcommands (grid-ollama, grid-gemini, grid-codex, grid-haiku).
- `signal_writer.write_signal(...)` from each runtime.
- Pre-commit hook accepts minimal smoke_eval artifacts.
- Mixed-runtime wave proves the grid can mix CLIs when you need to.

## After it runs

- `_showoff/w1/` .. `_showoff/w5/` -- 6 artifacts per wave (up to 30 total).
- `git log --grep SHOWOFF` -- up to 30 commits (one per nucleus per wave).
- Final report: per-wave signal count + artifact count + PASS/PARTIAL.

## When a wave PARTIAL-passes

- ollama: model not pulled (`ollama pull qwen3:8b`) or service down.
- gemini: quota exhausted on `gemini-2.5-flash-lite` -- retry later (oauth-personal only supports flash-lite; pro hangs, 2.0-flash 404s).
- codex: auth expired -- `codex login` first.
- claude: quota exhausted on haiku tier -- switch to sonnet in `nucleus_models.yaml`.

Partial = at least 3/6 nuclei completed; full fail = 0-2/6.

## Properties

| Property | Value |
|----------|-------|
| Kind | `slash_command` |
| Pillar | P12 |
| Nucleus | N07 |
| Cost | mostly free ($0 ollama + cheap tiers elsewhere) |
| Wall time | ~25-40 min full, ~5-8 min per wave |
| Pipeline | grid dispatch + signal polling + consolidation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[showoff_w2_n05_gemini]] | related | 0.36 |
| [[showoff_w5_n06_gemini]] | related | 0.36 |
| [[showoff_w5_n02_gemini]] | related | 0.35 |
| [[smoke_test_gemini_20260415]] | related | 0.34 |
| [[p12_wf_admin_orchestration]] | related | 0.33 |
| [[p01_kc_orchestration_best_practices]] | related | 0.31 |
| [[showoff_w4_n01_claude]] | related | 0.31 |
| [[showoff_w4_n03_claude]] | related | 0.31 |
| [[showoff_w4_n05_claude]] | related | 0.31 |
| [[showoff_w4_n06_claude]] | related | 0.31 |
