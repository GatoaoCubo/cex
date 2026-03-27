---
id: p12_spawn_grid_continuous
kind: spawn_config
pillar: P12
title: "Spawn Config: Grid Continuous Mode"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: PYTHA
quality: 9.0
tags: [spawn, config, grid, continuous, orchestration]
tldr: "Continuous grid spawn: auto-fill slots on completion, 3 max concurrent, 5s delay, handoffs named batch_{N}_{sat}.md"
max_bytes: 1024
density_score: 0.89
source: codexa-core/records/satellites/stella/mental_model.yaml + records/skills/continuous_batching/SKILL.md
linked_artifacts:
  pattern: p08_pat_continuous_batching
  workflow: p12_wf_stella_dispatch
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

## Handoff Queue Example (CEX7, 10 PYTHA tasks)

```
.claude/handoffs/
  CEX7_batch_1_pytha.md   # spawned immediately (slot 1)
  CEX7_batch_2_pytha.md   # spawned when slot 1 completes
  CEX7_batch_3_pytha.md   # spawned when slot 1 completes again
  ...
  CEX7_batch_10_pytha.md  # final batch
```

## Measured Results

- ISOFIX mission: 7 batches, 1 slot → 1.6x speedup vs static waves
- CBTEST: 3 mixed satellites (SHAKA+EDISON+PYTHA) → zero git lock contention
