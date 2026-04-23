---
id: p12_spawn_grid_continuous
kind: spawn_config
pillar: P12
title: "Spawn Config: Grid Continuous Mode"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.1
tags: [spawn, config, grid, continuous, orchestration]
tldr: "Continuous grid spawn: auto-fill slots on completion, 3 max concurrent, 5s delay, handoffs named batch_{N}_{sat}.md"
max_bytes: 1024
density_score: 0.89
source: organization-core/records/agent_groups/stella/mental_model.yaml + records/skills/continuous_batching/SKILL.md
linked_artifacts:
  pattern: p08_pat_continuous_batching
  workflow: p12_wf_stella_dispatch
domain: "orchestration"
related:
  - p08_pat_continuous_batching
  - p12_crew_agent_group_grid
  - p01_kc_lp12_orchestration
  - p08_diag_agent_group_grid
  - p01_kc_spawn_config
  - bld_output_template_spawn_config
  - spawn-config-builder
  - p09_rr_agent_group_spawn
  - p12_sig_agent_group_complete
  - bld_tools_spawn_config
---

# Spawn Config: Grid Continuous Mode

## Configuration

```yaml
spawn_config:
  mode: continuous
  script: spawn_grid.ps1
  trigger: "handoffs_count > available_slots (auto-detected)"

  slots:
    max_concurrent: 3    # hard limit — BSOD at 4
    spawn_delay: 5s      # between terminal opens (RAM stability)

  flags:
    interactive: true    # keeps terminal open (-k flag in TSP)
    skip_permissions: true  # --dangerously-skip-permissions
    no_chrome: true         # --no-chrome

  handoff_pattern: "{MISSION}_batch_{N}_{SAT}.md"
  signal_pattern: ".claude/signals/{sat}_complete_{timestamp}.json"
```

## Invocation

```powershell
# Standard continuous grid:
powershell -NoProfile -ExecutionPolicy Bypass `
  -File records/framework/powershell/spawn_grid.ps1 `
  -mission CEX7 `
  -mode continuous `
  -interactive

# Auto-detect (preferred — grid decides static vs continuous):
powershell -NoProfile -ExecutionPolicy Bypass `
  -File records/framework/powershell/spawn_grid.ps1 `
  -mission CEX7 `
  -interactive
```

## Slot Lifecycle

```
[IDLE] → spawn handoff → [RUNNING] → signal complete → [IDLE] → spawn next handoff
                                                              ↑
                                            monitor detects signal file → assigns next
```

## Monitor Commands

```powershell
# Check how many signals received:
find .claude/signals -name "*_complete_*.json" | wc -l

# Watch live (spawn_monitor.ps1):
powershell -File records/framework/powershell/spawn_monitor.ps1

# Stop all:
powershell -File records/framework/powershell/spawn_stop.ps1
```

## Handoff Queue Example (CEX7, 10 knowledge_agent tasks)

```
.claude/handoffs/
  CEX7_batch_1_pytha.md   # spawned immediately (slot 1)
  CEX7_batch_2_pytha.md   # spawned when slot 1 completes
  CEX7_batch_3_pytha.md   # spawned when slot 1 completes again
  ...
  CEX7_batch_10_pytha.md  # final batch
```

## Measured Results

1. ISOFIX mission: 7 batches, 1 slot → 1.6x speedup vs static waves
2. CBTEST: 3 mixed agent_groups (research_agent+builder_agent+knowledge_agent) → zero git lock contention

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `spawn_config` |
| Pillar | P12 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_continuous_batching]] | upstream | 0.38 |
| [[p12_crew_agent_group_grid]] | related | 0.38 |
| [[p01_kc_lp12_orchestration]] | upstream | 0.31 |
| [[p08_diag_agent_group_grid]] | upstream | 0.31 |
| [[p01_kc_spawn_config]] | related | 0.31 |
| [[bld_output_template_spawn_config]] | upstream | 0.30 |
| [[spawn-config-builder]] | related | 0.29 |
| [[p09_rr_agent_group_spawn]] | upstream | 0.28 |
| [[p12_sig_agent_group_complete]] | related | 0.28 |
| [[bld_tools_spawn_config]] | upstream | 0.27 |
