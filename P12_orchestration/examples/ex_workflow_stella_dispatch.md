---
id: p12_wf_stella_dispatch
kind: workflow
pillar: P12
title: "Workflow: orchestrator 5-Phase Dispatch"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: EDISON
quality: 9.5
tags: [stella, dispatch, workflow, orchestration]
tldr: "orchestrator's mandatory 5-phase dispatch: CLARIFY > ENRICH > COMPOSE > EXECUTE > MONITOR — orchestrates without executing"
density_score: 0.93
timeout: 60 min
source: organization-core/.claude/rules/orchestrator_RULES.md
---

# Workflow: orchestrator 5-Phase Dispatch

## Overview

| Property | Value |
|----------|-------|
| Trigger | User requests any task in orchestrator terminal |
| Input | User task description (natural language) |
| Output | Completed agent_node work (commits + signals) |
| Timeout | 60 min (varies by agent_node count) |

## Steps

```
[CLARIFY] --> [ENRICH] --> [COMPOSE] --> [EXECUTE] --> [MONITOR]
                 |                           |
            [brain_query]              [spawn_solo/grid]
```

### Step 1: CLARIFY
- **Input**: User request (natural language)
- **Action**: Decompose into agent_node tasks. Present table: agent_node, task, model. Ask "Confirma? (sim/ajustar)"
- **Output**: Approved task decomposition (1 agent_node = 1 deliverable, max 3 tasks per sat)
- **Duration**: 1-2 min

### Step 2: ENRICH
- **Input**: Approved task list
- **Action**: `brain_query("[domain] [keywords]")` per agent_node. Generate 5-10 seed words per handoff. Identify scope fence (SOMENTE/NAO TOQUE)
- **Output**: Context map with agents, artifacts, seeds per agent_node
- **Duration**: 1-3 min

### Step 3: COMPOSE
- **Input**: Enriched context per agent_node
- **Action**: Write `.claude/handoffs/{MISSION}_{sat}.md` with CONTEXTO, SEEDS, TAREFAS, SCOPE FENCE, COMMIT template, SIGNAL command
- **Output**: Handoff files on disk (1 per agent_node, or `batch_{N}` for >6 tasks)
- **Duration**: 2-5 min

### Step 4: EXECUTE
- **Input**: Handoff files
- **Action**: `spawn_solo.ps1` (1 sat) or `spawn_grid.ps1` (multi-sat, auto-detects static vs continuous)
- **Output**: Running agent_node terminals
- **Duration**: 5-30 min (agent_node work time)

### Step 5: MONITOR
- **Input**: Running agent_nodes
- **Action**: Check `.claude/signals/*_complete_*.json`, `git log --oneline -10`, `spawn_stop.ps1` when done
- **Output**: Consolidated report, archived handoffs, git push
- **Duration**: 2-5 min

## Parallel Groups

| Group | Steps | Max Concurrent |
|-------|-------|----------------|
| Satellite execution | Step 4 | 3 (BSOD limit at 4) |

## Rollback

| Step | Rollback Action |
|------|-----------------|
| COMPOSE | Delete handoff files from `.claude/handoffs/` |
| EXECUTE | `spawn_stop.ps1` to kill agent_node terminals |

## Success Criteria

- All agent_node signals received with score >= 8.0
- All commits present in `git log`
- Zero orphaned terminals after MONITOR

---
*Migrated from: organization-core/.claude/rules/orchestrator_RULES.md (DISPATCH FLOW section)*
