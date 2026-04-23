---
id: batch
kind: instruction
pillar: P12
description: "Run many tasks in parallel worktrees. Usage: /batch <intents-file> [--workers N]"
quality: 9.1
title: "Batch"
version: "1.0.0"
author: n03_builder
tags: [instruction, command, parallel, worktree, boris_merge]
tldr: "Fan out N independent tasks across isolated worktrees via dispatch.sh swarm."
domain: "CEX system"
created: "2026-04-15"
updated: "2026-04-15"
density_score: 0.88
related:
  - p01_kc_git_worktree_isolation
  - dispatch
  - p01_kc_orchestration
  - p02_agent_admin_orchestrator
  - p01_kc_orchestration_best_practices
  - p08_ac_admin_orchestrator
  - p03_sp_admin_orchestrator
  - agent_card_engineering_nucleus
  - self_audit_n03_builder_20260408
  - p03_sp_orchestration_nucleus
---

# /batch — Parallel Worktree Execution

> Replaces the old `--tmux` stub with real `dispatch.sh swarm` + worktree isolation.

## Usage

| Form | Action |
|------|--------|
| `/batch intents.txt` | One line per task, default 3 workers |
| `/batch intents.txt --workers 6` | 6 concurrent worktrees |
| `/batch --swarm n03 5 "scaffold a landing page"` | 5 parallel n03 instances, same task |
| `/batch --kind landing_page 4` | 4 n03 instances building landing_page variants |

## Input Format

`intents.txt` -- one intent per line, blank lines ignored, `#` comment:

```
build a pricing page for SaaS
scaffold an onboarding flow for edtech
write 3 ad variants for black-friday
# skip: old intent, already shipped
research competitor pricing in legal-tech
```

## Execution Model

Each intent gets its own **git worktree** (isolation: worktree):

```
.cex/worktrees/batch_<timestamp>/
  cell_01/  (branch: batch/20260415-160000/cell_01)
  cell_02/
  cell_03/
  ...
```

One nucleus per cell, fully isolated. Merge strategy determined after wave.

## Invocation

Delegates to `dispatch.sh`:

```bash
bash _spawn/dispatch.sh swarm <kind> <N>         # N of same kind
bash _spawn/dispatch.sh grid BATCH_<id> -w       # heterogenous from intents
```

For heterogenous batches, /batch writes handoffs to
`.cex/runtime/handoffs/BATCH_<id>_cell_NN.md` then dispatches grid mode.

## Concurrency Guardrails

1. `--workers` clamps to `[1, 6]` (Claude Code) or `[1, 20]` (Ollama local)
2. Rate-limit-aware: reads `.cex/P09_config/rate_limits.yaml` before spawn
3. Auto-degrades: Sonnet -> Haiku if pool near cap (N01-N04 eligible)
4. Worktree count never exceeds `git worktree list` max (default 100)

## Merge Modes

| Mode | Semantics |
|------|-----------|
| `--merge-best` | Consolidator scores all cells, keeps highest quality |
| `--merge-all` | Every successful cell merged to main (check conflicts) |
| `--merge-none` | Leave worktrees for manual review |

Default: `--merge-best` for `--kind` batches, `--merge-all` for heterogenous.

## Cross-runtime

| Runtime | Swarm primitive |
|---------|-----------------|
| Claude Code | Task tool (subagent) + git worktree |
| Codex | `boot/n0X_codex.ps1 -Worktree` |
| Gemini | `boot/n0X_gemini.ps1 -Worktree` |
| Ollama | `python _tools/cex_8f_runner.py --worktree` (no CLI needed) |

## Example

```
/batch intents.txt --workers 4 --merge-best
-> 12 intents, 4 worktrees, rolling pool
-> cell_01 done (quality=9.2, kept)
-> cell_02 done (quality=8.7, discarded)
-> ...
-> final: 5 artifacts merged, 7 discarded, 0 conflicts
```

## When NOT to use

- Single task -- use `/dispatch` directly.
- Tasks with dependencies -- use `/mission` (respects wave order).
- Shared-file edits -- use `.proposal` pattern, not parallel worktrees.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_git_worktree_isolation]] | upstream | 0.41 |
| [[dispatch]] | sibling | 0.26 |
| [[p01_kc_orchestration]] | upstream | 0.25 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.23 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.23 |
| [[p08_ac_admin_orchestrator]] | upstream | 0.23 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.22 |
| [[agent_card_engineering_nucleus]] | upstream | 0.22 |
| [[self_audit_n03_builder_20260408]] | upstream | 0.22 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.21 |
