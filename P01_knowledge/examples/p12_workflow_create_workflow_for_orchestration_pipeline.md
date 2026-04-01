---
id: p12_wf_orchestration_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "workflow-builder"
title: "Orchestration Pipeline Workflow"
steps_count: 4
execution: mixed
agent_nodes: [orchestrator, n01, n02, n03, n04, n05, n06]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [mission_planned, nuclei_dispatched, execution_complete, pipeline_complete, error]
spawn_configs: [p12_spawn_orchestrator_mission, p12_spawn_nucleus_solo]
domain: "orchestration"
quality: 8.8
tags: [workflow, orchestration, pipeline, multi-nucleus]
tldr: "4-step mixed workflow: plan mission, dispatch to nuclei, parallel execution, consolidate results with error recovery"
density_score: 0.91
---
## Purpose
Orchestrates complex multi-nucleus missions through planning, parallel dispatch, autonomous execution, and consolidation. This workflow enables the orchestrator to decompose missions into domain-specific tasks, route them to appropriate nuclei (N01-N06), monitor parallel execution, and consolidate results into final deliverables.

## Steps

### Step 1: Mission Planning [orchestrator]
- **Agent**: orchestrator (N07)
- **Action**: Analyze mission goal and decompose into domain-specific tasks with nucleus routing
- **Input**: Mission specification from handoff file
- **Output**: Task decomposition with nucleus assignments in .cex/runtime/handoffs/
- **Signal**: mission_planned with task count and nucleus assignments
- **Depends on**: none

### Step 2: Nucleus Dispatch [orchestrator]
- **Agent**: orchestrator (N07)
- **Action**: Create handoff files and launch assigned nuclei via spawn configurations
- **Input**: Task decomposition from Step 1
- **Output**: Active nucleus processes with handoff files
- **Signal**: nuclei_dispatched with process IDs and handoff paths
- **Depends on**: Step 1

### Step 3: Parallel Execution [multiple nuclei]
- **Agent**: n01, n02, n03, n04, n05, n06 (domain-specific)
- **Action**: Execute assigned tasks autonomously via 8F pipeline
- **Input**: Domain-specific handoff files from Step 2
- **Output**: Domain artifacts committed to respective pillars
- **Signal**: execution_complete with quality scores per nucleus
- **Depends on**: Step 2

### Step 4: Results Consolidation [orchestrator]
- **Agent**: orchestrator (N07)
- **Action**: Collect nucleus outputs, validate quality, archive handoffs, push to remote
- **Input**: Completed artifacts and signals from Step 3
- **Output**: Consolidated mission deliverable with quality report
- **Signal**: pipeline_complete with aggregate quality score
- **Depends on**: Step 3

## Dependencies
- Mission handoff file must exist with clear goal and requirements
- Spawn configurations for orchestrator and target nuclei must be valid
- Target nuclei must have appropriate builder capabilities for assigned tasks
- Git repository must be clean with no conflicting processes

## Signals
- **On mission planned**: mission_planned signal with task breakdown and nucleus routing map
- **On nuclei dispatched**: nuclei_dispatched signal with active process tracking
- **On parallel execution complete**: execution_complete signal with per-nucleus quality scores
- **On workflow complete**: pipeline_complete signal with consolidated deliverable path
- **On error**: error signal with failure point, retry per step (max 1), escalate to manual intervention

## References
- Signal contracts defined by signal-builder for orchestration events
- Spawn configurations from spawn-config-builder for nucleus launch parameters
- 8F pipeline enforcement for autonomous nucleus execution
- Quality gate validation for artifact acceptance criteria