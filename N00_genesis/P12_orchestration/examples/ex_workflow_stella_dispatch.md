---
id: p12_wf_stella_dispatch
kind: workflow
pillar: P12
title: "Workflow: orchestrator 5-Phase Dispatch"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
quality: 9.0
tags: [stella, dispatch, workflow, orchestration]
tldr: "orchestrator's mandatory 5-phase dispatch: CLARIFY > ENRICH > COMPOSE > EXECUTE > MONITOR — orchestrates without executing"
density_score: 0.93
timeout: 60 min
source: organization-core/.claude/rules/orchestrator_RULES.md
related:
  - bld_knowledge_card_handoff
  - p01_kc_handoff
  - bld_collaboration_agent_card
  - p11_bl_agent_group_execution
  - p06_iface_agent_group_handoff
  - p03_ins_agent_card_builder
  - bld_collaboration_spawn_config
  - p03_sp_dispatch_rule_builder
  - p12_crew_agent_group_grid
  - bld_knowledge_card_agent_card
---

# Workflow: orchestrator 5-Phase Dispatch

## Overview

| Property | Value |
|----------|-------|
| Trigger | User requests any task in orchestrator terminal |
| Input | User task description (natural language) |
| Output | Completed agent_group work (commits + signals) |
| Timeout | 60 min (varies by agent_group count) |

## Steps

```
[CLARIFY] --> [ENRICH] --> [COMPOSE] --> [EXECUTE] --> [MONITOR]
                 |                           |
            [brain_query]              [spawn_solo/grid]
```

### Step 1: CLARIFY
- **Input**: User request (natural language)
- **Action**: Decompose into agent_group tasks. Present table: agent_group, task, model. Ask "Confirma? (sim/ajustar)"
- **Output**: Approved task decomposition (1 agent_group = 1 deliverable, max 3 tasks per sat)
- **Duration**: 1-2 min

### Step 2: ENRICH
- **Input**: Approved task list
- **Action**: `brain_query("[domain] [keywords]")` per agent_group. Generate 5-10 seed words per handoff. Identify scope fence (SOMENTE/NAO TOQUE)
- **Output**: Context map with agents, artifacts, seeds per agent_group
- **Duration**: 1-3 min

### Step 3: COMPOSE
- **Input**: Enriched context per agent_group
- **Action**: Write `.claude/handoffs/{MISSION}_{sat}.md` with CONTEXTO, SEEDS, TAREFAS, SCOPE FENCE, COMMIT template, SIGNAL command
- **Output**: Handoff files on disk (1 per agent_group, or `batch_{N}` for >6 tasks)
- **Duration**: 2-5 min

### Step 4: EXECUTE
- **Input**: Handoff files
- **Action**: `spawn_solo.ps1` (1 sat) or `spawn_grid.ps1` (multi-sat, auto-detects static vs continuous)
- **Output**: Running agent_group terminals
- **Duration**: 5-30 min (agent_group work time)

### Step 5: MONITOR
- **Input**: Running agent_groups
- **Action**: Check `.claude/signals/*_complete_*.json`, `git log --oneline -10`, `spawn_stop.ps1` when done
- **Output**: Consolidated report, archived handoffs, git push
- **Duration**: 2-5 min

## Parallel Groups

| Group | Steps | Max Concurrent |
|-------|-------|----------------|
| Agent_group execution | Step 4 | 3 (BSOD limit at 4) |

## Rollback

| Step | Rollback Action |
|------|-----------------|
| COMPOSE | Delete handoff files from `.claude/handoffs/` |
| EXECUTE | `spawn_stop.ps1` to kill agent_group terminals |

## Success Criteria

- All agent_group signals received with score >= 8.0
- All commits present in `git log`
- Zero orphaned terminals after MONITOR

---
*Migrated from: organization-core/.claude/rules/orchestrator_RULES.md (DISPATCH FLOW section)*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_handoff]] | upstream | 0.38 |
| [[p01_kc_handoff]] | related | 0.36 |
| [[bld_collaboration_agent_card]] | upstream | 0.34 |
| [[p11_bl_agent_group_execution]] | upstream | 0.34 |
| [[p06_iface_agent_group_handoff]] | upstream | 0.34 |
| [[p03_ins_agent_card_builder]] | upstream | 0.32 |
| [[bld_collaboration_spawn_config]] | related | 0.31 |
| [[p03_sp_dispatch_rule_builder]] | upstream | 0.30 |
| [[p12_crew_agent_group_grid]] | related | 0.29 |
| [[bld_knowledge_card_agent_card]] | upstream | 0.29 |
