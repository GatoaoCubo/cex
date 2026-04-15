---
description: 4-runtime grid showoff -- validate claude+codex+gemini+ollama in 5 waves
argument-hint: "[--wave N] [--dry-run]"
---

# /showoff -- Multi-Runtime Grid Validation

Runs 5 smoke waves to prove all 4 CEX runtimes work in grid dispatch.
Each wave uses the cheapest model for its runtime; each nucleus produces
one signature artifact under `_showoff/wN/{nucleus}_{runtime}.md`.

## Waves

| # | Runtime | Model | Cost | Notes |
|---|---------|-------|------|-------|
| 1 | ollama  | qwen3:8b                   | $0    | Local, free, slowest |
| 2 | gemini  | gemini-2.5-flash           | cheap | Higher RPM than pro |
| 3 | codex   | gpt-5-codex                | cheap | OpenAI CLI |
| 4 | claude  | claude-haiku-4-5-20251001  | cheap | Cheapest Claude tier |
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
- gemini: quota exhausted on `gemini-2.5-flash` -- retry later.
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
