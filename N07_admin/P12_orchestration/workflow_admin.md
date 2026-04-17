---
id: p12_wf_admin_orchestration
kind: workflow
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
title: "Orchestration Workflows — Solo, Grid Static, Grid Continuous"
steps_count: 5
execution: mixed
agent_groups: [orchestrator, n01, n02, n03, n04, n05, n06]
timeout: 3600
retry_policy: per_step
depends_on: [dispatch_rule_admin]
signals: [complete, error, progress]
spawn_configs: [spawn_config_admin]
domain: orchestration
quality: 9.1
tags: [workflow, orchestration, N07, dispatch, solo, grid]
tldr: "3 orchestration workflows — solo dispatch, grid static, grid continuous — with concrete spawn commands."
density_score: 1.0
---

# Orchestration Workflows

## Purpose

Three concrete workflows that N07 uses to dispatch tasks. Solo for single-nucleus
tasks, Grid Static for fixed parallel missions, Grid Continuous for ongoing
multi-wave missions. Each workflow has explicit steps with commands.

## Workflow A: Solo Dispatch

Single builder, single task, new terminal window.

### Step 1: Write Handoff [orchestrator]
- **Agent**: N07 orchestrator
- **Action**: Write handoff file with task, context, scope fence, commit convention
- **Input**: Human intent + routing classification
- **Output**: `.cex/runtime/handoffs/{mission}_{nucleus}.md`
- **Signal**: none (internal step)
- **Depends on**: none

### Step 2: Dispatch Builder [orchestrator]
- **Agent**: N07 orchestrator
- **Action**: Launch builder in new terminal
- **Input**: Handoff file path
- **Output**: Builder process running in new window
- **Command**: `bash _spawn/dispatch.sh solo {nucleus} "Leia .cex/runtime/handoffs/{file} e execute."`
- **Signal**: none (builder emits signal on completion)
- **Depends on**: Step 1

### Step 3: Monitor Signal [orchestrator]
- **Agent**: N07 orchestrator
- **Action**: Poll `.cex/runtime/signals/` for builder completion signal
- **Input**: Expected signal from target nucleus
- **Output**: Signal JSON with status and quality score
- **Command**: `bash _spawn/dispatch.sh status`
- **Signal**: reads builder signal
- **Depends on**: Step 2

### Step 4: Validate Quality [orchestrator]
- **Agent**: N07 orchestrator
- **Action**: Check quality score >= 8.0, run doctor if needed
- **Input**: Builder signal + artifact path
- **Output**: Accept or reject decision
- **Command**: `python _tools/cex_doctor.py`
- **Signal**: none
- **Depends on**: Step 3

### Step 5: Accept or Feedback [orchestrator]
- **Agent**: N07 orchestrator
- **Action**: If quality >= 8.0: move handoff to `_done/`. If < 8.0: re-dispatch with feedback.
- **Input**: Validation result
- **Output**: Moved handoff or new dispatch
- **Signal**: `write_signal('n07', 'complete', score, 'mission')`
- **Depends on**: Step 4

## Workflow B: Grid Static

Up to 6 parallel builders, one handoff per nucleus, all launch simultaneously.

### Preparation
1. Write N handoff files to `.cex/runtime/handoffs/{mission}_{nucleus}_{seq}.md`
2. Launch grid: `bash _spawn/dispatch.sh grid {MISSION_NAME}`
3. Grid reads handoffs, spawns one builder per nucleus in parallel windows
4. Each builder runs independently, commits, and signals on completion

### Monitoring
- `bash _spawn/dispatch.sh status` — shows active builders and signal state
- Grid completes when ALL builders have signaled complete or error
- If any builder errors: N07 reviews, may re-dispatch solo

### Quality Gate
- Validate each builder output independently
- Mission completes only when ALL artifacts pass quality >= 8.0

## Workflow C: Grid Continuous

Multi-wave mission with dependency ordering between waves.

### Wave Execution
1. **Wave 0**: Independent tasks (no dependencies) dispatch in parallel
2. **Wait**: Monitor signals until all Wave 0 builders complete
3. **Wave 1**: Dependent tasks dispatch (using Wave 0 outputs as context)
4. **Repeat**: Continue until all waves complete
5. **Finalize**: Validate all outputs, move handoffs to `_done/`, emit mission complete signal

### Commands
```bash
# Launch continuous grid
bash _spawn/dispatch.sh grid {MISSION_NAME}

# Monitor (repeat until all complete)
bash _spawn/dispatch.sh status

# Final validation
python _tools/cex_doctor.py
```

## Dependencies

- Dispatch rules: N07_admin/orchestration/dispatch_rule_admin.md
- Spawn config: N07_admin/orchestration/spawn_config_admin.md
- DAG: N07_admin/orchestration/dag_admin.md

## Signals

- **On step complete**: nucleus emits signal to `.cex/runtime/signals/{nucleus}_complete.json`
- **On workflow complete**: N07 emits `write_signal('n07', 'complete', score, 'mission')`
- **On error**: nucleus emits error signal, N07 reads and decides (retry/escalate)

## References

- DAG definition: N07_admin/orchestration/dag_admin.md
- Spawn config: N07_admin/orchestration/spawn_config_admin.md
- Grid ops (positions, recovery, crashes): N07_admin/memory/grid_orchestration_mastery.md
