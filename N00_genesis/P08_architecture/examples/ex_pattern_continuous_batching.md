---
id: p08_pat_continuous_batching
kind: pattern
8f: F4_reason
pillar: P08
title: "Pattern: Continuous Batching (Agent_group Grid)"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [pattern, continuous-batching, grid, dispatch, orchestration]
tldr: "When queue > slots: fill slots immediately as they complete instead of waiting for entire wave — 1.6x speedup on 7+ task missions"
max_bytes: 2048
density_score: 0.92
source: organization-core/records/skills/continuous_batching/SKILL.md
linked_artifacts:
  workflow: p12_wf_stella_dispatch
  spawn: p12_spawn_grid_continuous
related:
  - bld_examples_pattern
  - p12_spawn_grid_continuous
  - p10_lr_continuous_batching
  - bld_examples_learning_record
  - continuous_batching_report
  - p01_kc_spawn_config
  - p12_wf_admin_orchestration
  - p08_diag_agent_group_grid
  - p01_kc_lp12_orchestration
  - kc_workflow_run_crate
---

# Pattern: Continuous Batching (Agent_group Grid)

## Problem

Static batching (launch N tasks → wait ALL done → launch next wave) causes idle slots when tasks finish at different speeds. In a 3-slot grid with tasks taking 5/10/20 min, slots 1+2 idle for 10+ min waiting for slot 3.

## Solution

Continuous batching: when any slot completes, immediately assign next task from queue. No idle time between tasks per slot.

## Diagram

```
STATIC (wave):          CONTINUOUS:
[A][B][C] → wait all   [A][B][C]
[D][E][F] → wait all    [D]  when A done
                        [E]      when B done
                        [F]          when C done
Total: 2x slowest       Total: ~1.6x speedup (measured)
```

## Auto-Detection Logic

```
IF handoffs_count > available_slots:
    mode = continuous
ELSE:
    mode = static (wave)
```

Trigger: `spawn_grid.ps1` auto-detects — orchestrator does not choose manually.

## Measured Performance

| Mission | Tasks | Slots | Mode | Result |
|---------|-------|-------|------|--------|
| ISOFIX | 7 batches | 3 | continuous | 1.6x speedup vs static |
| CBTEST | 8 mixed | 3 | continuous | research_agent+builder_agent+knowledge_agent confirmed |

## When to Use

| Condition | Use Continuous |
|-----------|---------------|
| Tasks > slots | YES (auto) |
| Tasks independent | YES |
| Tasks have dependencies (B needs A output) | NO — use wave order |
| < 4 tasks total | NO — overhead > gain |
| Sequential pipeline | NO — use ordered static |

## Handoff Naming Convention

```
{MISSION}_batch_{N}_{SAT}.md
Example: CEX7_batch_1_pytha.md, CEX7_batch_2_pytha.md
```

## Signal Protocol

Each batch signals independently:
```python
write_signal('pytha', 'complete', 9.0, task='cex7_batch_2')
# Spawn monitor detects → assigns next batch automatically
```

## Constraints

- Max 3 concurrent agent_groups (BSOD at 4 on current hardware)
- 5s delay between terminal spawns (RAM stability)
- Git lock: zero contention confirmed at 3 concurrent agent_groups

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_pattern]] | upstream | 0.51 |
| [[p12_spawn_grid_continuous]] | downstream | 0.40 |
| [[p10_lr_continuous_batching]] | downstream | 0.39 |
| [[bld_examples_learning_record]] | upstream | 0.39 |
| [[continuous_batching_report]] | upstream | 0.36 |
| [[p01_kc_spawn_config]] | downstream | 0.32 |
| [[p12_wf_admin_orchestration]] | downstream | 0.27 |
| [[p08_diag_agent_group_grid]] | related | 0.25 |
| [[p01_kc_lp12_orchestration]] | upstream | 0.24 |
| [[kc_workflow_run_crate]] | related | 0.23 |
