---
id: p12_wf_orchestration_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "workflow-builder"
title: "CEX Orchestration Pipeline"
steps_count: 4
execution: mixed
agent_nodes: [stella, shaka, edison, stella]
timeout: 3600
retry_policy: per_step
depends_on: []
signals: [complete, error, pipeline_complete]
spawn_configs: [p12_spawn_stella_orchestrator, p12_spawn_shaka_researcher, p12_spawn_edison_builder]
domain: "orchestration"
quality: 8.8
tags: [workflow, orchestration, pipeline, multi-agent]
tldr: "4-step orchestration pipeline: decompose mission, research context, build artifacts, consolidate results with wave-based parallel execution"
density_score: 0.92
---
## Purpose
Defines the complete CEX orchestration pipeline from mission intake to consolidated delivery. Demonstrates wave-based execution where planning is sequential, research and building run in parallel, then consolidation finalizes the pipeline. Each step emits completion signals to coordinate handoffs between orchestrator and specialist agents.

## Steps
### Step 1: Mission Decomposition [stella]
- **Agent**: stella (orchestrator)
- **Action**: Parse mission goal, identify required artifacts, create handoff files for specialist agents
- **Input**: mission goal from user request
- **Output**: handoff files in .cex/runtime/handoffs/ and task decomposition
- **Signal**: decomposition_complete with task count
- **Depends on**: none

### Step 2: Context Research [shaka]
- **Agent**: shaka (research specialist)
- **Action**: Gather domain knowledge, analyze similar artifacts, build context foundation
- **Input**: research handoff file from Step 1
- **Output**: knowledge cards and context brief committed to records/
- **Signal**: research_complete with knowledge score
- **Depends on**: Step 1

### Step 3: Artifact Construction [edison]
- **Agent**: edison (build specialist)
- **Action**: Execute 8F pipeline to produce target artifacts with quality validation
- **Input**: build handoff file from Step 1
- **Output**: completed artifacts with quality >= 8.0
- **Signal**: build_complete with quality score
- **Depends on**: Step 1

### Step 4: Pipeline Consolidation [stella]
- **Agent**: stella (orchestrator)
- **Action**: Verify outputs, archive handoffs, commit results, emit pipeline completion
- **Input**: signals from Steps 2-3, git log, artifact quality scores
- **Output**: consolidated commit and pipeline completion report
- **Signal**: pipeline_complete with aggregate quality
- **Depends on**: Steps 2, 3

## Dependencies
- Mission goal must be defined in initial user request
- .cex/runtime/handoffs/ directory must exist for handoff file storage
- spawn_configs for stella, shaka, and edison must be valid and accessible
- Git repository must be initialized for commit operations

## Signals
- **On step complete**: {agent}_complete signal emitted with quality/progress data
- **On pipeline complete**: pipeline_complete signal with aggregate metrics and success status
- **On error**: {agent}_error signal with failure reason, per_step retry up to 1 attempt, then escalate to orchestrator
- **Wave coordination**: Steps 2-3 run in parallel after Step 1 completion, Step 4 waits for both

## References
- signal-builder conventions for completion/error signal structure
- spawn-config-builder for agent launch parameters
- handoff protocol for inter-agent task delegation