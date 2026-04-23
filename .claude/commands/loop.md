---
id: loop
kind: instruction
pillar: P12
description: "Run a prompt or command on a recurring interval. Usage: /loop [interval] <command>"
quality: 9.1
title: "Loop"
version: "1.0.0"
author: n03_builder
tags: [instruction, command, scheduling, boris_merge]
tldr: "Recurring execution of a prompt or slash-command; self-paced if interval omitted."
domain: "CEX system"
created: "2026-04-15"
updated: "2026-04-15"
density_score: 0.88
related:
  - bld_knowledge_card_dual_loop_architecture
  - dual-loop-architecture-builder
  - bld_collaboration_dual_loop_architecture
  - kc_dual_loop_architecture
  - schedule
  - p03_sp_self_improvement_loop_builder
  - p03_sp_dual_loop_architecture_builder
  - bld_instruction_dual_loop_architecture
  - p08_qg_dual_loop_architecture
  - p10_lr_dual_loop_architecture_builder
---

# /loop — Recurring Execution

> Harness-native in Claude Code. Runtime bridges for codex/gemini/ollama.

## Usage

| Form | Semantics |
|------|-----------|
| `/loop 5m /mission evolve` | Every 5 min, run `/mission evolve` |
| `/loop 1h /consolidate` | Hourly consolidation |
| `/loop /grid BORIS_MERGE` | Self-paced (LLM picks interval via ScheduleWakeup) |
| `/loop stop` | End the current loop |

## Intent Mapping

Natural-language triggers N07 should map to `/loop`:

| User says | Maps to |
|-----------|---------|
| "keep evolving artifacts overnight" | `/loop 1h /mission evolve` |
| "babysit the PRs" | `/loop 10m /review-pr` |
| "monitor the deploy every 5 min" | `/loop 5m /status` |
| "run until stable" | self-paced `/loop <prompt>` |

## Interval Grammar

1. `<n>s` seconds (min 60s enforced by harness)
2. `<n>m` minutes
3. `<n>h` hours (max 1h = 3600s per wake)
4. omitted -- dynamic, LLM uses `ScheduleWakeup` per iteration

## Cache-Aware Pacing (when self-paced)

- **60-270s**: cache warm, use for active polling
- **300s**: WORST -- cache miss without amortization, avoid
- **1200-3600s**: cache miss OK, long idle between iterations

Default when idle: 1200-1800s.

## Cross-runtime Bridge

| Runtime | Mechanism |
|---------|-----------|
| Claude Code | native `Skill(skill="loop")` |
| Codex/Gemini | external cron + `bash _spawn/dispatch.sh solo <nucleus> "<task>"` |
| Ollama | `python _tools/cex_8f_runner.py --schedule` + cron |

The CEX bridge lives in `_tools/cex_loop_bridge.py` (optional -- harness-native
path is preferred when present).

## When NOT to use

- One-off tasks -- just run it once.
- Work that blocks on user input -- loops must be autonomous.
- Long-running builds -- use `/mission` with blocking signal_watch instead.

## Stop Conditions

1. User types `/loop stop`
2. Max iterations reached (set via `--max <n>`)
3. Success signal written (e.g. `cex_quality_monitor.py` reports >=9.0)
4. Error triples in a row

## Example

```
/loop 30m /mission evolve
-> iteration 1: evolved 42 artifacts, 3 promoted
-> iteration 2: evolved 31 artifacts, 1 promoted
-> iteration 3: 0 candidates below 9.0 -> stop
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_dual_loop_architecture]] | upstream | 0.35 |
| [[dual-loop-architecture-builder]] | upstream | 0.35 |
| [[bld_collaboration_dual_loop_architecture]] | related | 0.33 |
| [[kc_dual_loop_architecture]] | upstream | 0.32 |
| [[schedule]] | sibling | 0.32 |
| [[p03_sp_self_improvement_loop_builder]] | upstream | 0.31 |
| [[p03_sp_dual_loop_architecture_builder]] | upstream | 0.29 |
| [[bld_instruction_dual_loop_architecture]] | sibling | 0.27 |
| [[p08_qg_dual_loop_architecture]] | upstream | 0.27 |
| [[p10_lr_dual_loop_architecture_builder]] | upstream | 0.24 |
