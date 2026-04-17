---
id: p12_wf_creation_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "workflow-builder"
title: "Creation Pipeline Workflow"
steps_count: 4
execution: mixed
agent_groups: [research_agent, builder_agent, validator_agent, orchestrator]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_research_agent_solo, p12_spawn_builder_agent_solo, p12_spawn_validator_agent_solo]
domain: "orchestration"
quality: 9.0
tags: [workflow, creation, pipeline, orchestration, mixed]
tldr: "4-step mixed workflow: research domain → build artifact via 8F → validate quality gates → consolidate and deploy"
density_score: 0.91
---
## Purpose
Orchestrates the complete artifact creation pipeline from domain research through final deployment. Wave 1: research_agent collects knowledge cards and examples. Wave 2: builder_agent produces the artifact following the 8F pipeline using research findings. Wave 3: validator_agent enforces HARD gates H01-H10 and SOFT scoring. Wave 4: orchestrator consolidates, compiles YAML, and signals completion.

## Steps

### Step 1: Domain Research [research_agent]
- **Agent**: research_agent (gemini-pro)
- **Wave**: 1
- **Action**: Research target domain; collect knowledge cards, examples, and anti-patterns
- **Input**: Creation intent and domain specification from handoff file
- **Output**: Research brief and knowledge cards committed to `records/pool/`
- **Signal**: `research_complete` with knowledge card count
- **Depends on**: none
- **on_failure**: retry (max 2), then abort
- **timeout_ms**: 1800000

### Step 2: Artifact Build [builder_agent]
- **Agent**: builder_agent (opus)
- **Wave**: 2
- **Action**: Build target artifact following 8F pipeline using research findings from Step 1
- **Input**: Research brief and knowledge cards from `research_complete` signal
- **Output**: Draft artifact `.md` committed to correct pillar directory
- **Signal**: `build_complete` with artifact path and byte count
- **Depends on**: Step 1
- **on_failure**: retry (max 1), then abort
- **timeout_ms**: 2400000

### Step 3: Quality Validation [validator_agent]
- **Agent**: validator_agent (opus)
- **Wave**: 3
- **Action**: Run HARD gates H01-H10 and SOFT scoring; reject artifacts scoring below 7.0
- **Input**: Artifact path from `build_complete` signal
- **Output**: Validation report; scored artifact with gate results
- **Signal**: `validation_complete` with score and gate pass/fail counts
- **Depends on**: Step 2
- **on_failure**: skip (log rejection), escalate to orchestrator
- **timeout_ms**: 600000

### Step 4: Consolidation [orchestrator]
- **Agent**: orchestrator (opus)
- **Wave**: 4
- **Action**: Compile YAML, archive handoffs, push final commit, emit workflow completion signal
- **Input**: Signals from Steps 1-3; git log; artifact path from Step 3
- **Output**: Compiled `.yaml`, archived handoffs, signed commit
- **Signal**: `workflow_complete` with aggregate quality score
- **Depends on**: Steps 1, 2, 3
- **on_failure**: abort
- **timeout_ms**: 300000

## Dependencies
- Handoff files must exist for research_agent, builder_agent, and validator_agent before dispatch
- All `spawn_configs` referenced must be registered and valid
- GDP decisions (domain, tone, audience) must be resolved in `decision_manifest.yaml` before workflow starts

## Signals
- **On step complete**: `{agent}_complete` emitted per step (see signal-builder conventions)
- **On workflow complete**: `workflow_complete` with aggregate quality score across all steps
- **On validation fail**: `validation_error` triggers orchestrator escalation; artifact flagged for rework
- **On error**: `{agent}_error`; `per_step` retry up to `max_retries`, then abort workflow

## References
- signal-builder: completion signal contract and naming conventions per step
- spawn-config-builder: agent_group launch parameters per agent_group
- bld_quality_gate_workflow: H01-H10 HARD gates and SOFT scoring rubric