---
id: p12_wf_create_orchestration_agent
kind: workflow
8f: F8_collaborate
pillar: P12
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "workflow-builder"
title: "Create Agent for Orchestration Nucleus"
steps_count: 3
execution: mixed
agent_groups: [n03, n05]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_n03_solo_build, p12_spawn_n05_solo_validate]
domain: "orchestration"
quality: 9.0
tags: [workflow, orchestration, agent-creation]
tldr: "3-step mixed workflow: n03 builds orchestration agent artifact, n05 deploys to N07 runtime, n05 validates end-to-end dispatch capabilities"
density_score: 0.88
related:
  - p12_wf_orchestration_pipeline
  - p12_wf_admin_orchestration
  - p12_wf_builder_8f_pipeline
  - p12_wf_creation_pipeline
  - bld_collaboration_agent
  - p12_wf_engineering_pipeline
  - bld_examples_workflow
  - p12_dr_orchestration
  - workflow-builder
  - p02_agent_creation_nucleus
---
## Purpose
Establishes a new agent artifact scoped to the N07 orchestration nucleus. Step 1 builds the agent YAML with nucleus routing, dispatch protocol, and signal contracts via N03. Step 2 deploys the artifact and registers it in the N07 runtime environment. Step 3 validates the agent can dispatch tasks, receive signals, and consolidate nucleus outputs correctly.

## Steps

### Step 1: Build Orchestration Agent [n03]
- **Agent**: n03 (opus builder)
- **Action**: Build agent artifact with N07 routing table, dispatch capabilities, and signal contracts
- **Input**: Orchestration intent, nucleus routing definitions from `.claude/rules/n07-orchestrator.md`
- **Output**: `p02_agent_orchestration_nucleus.yaml` committed to `P02_agents/`
- **Signal**: `n03_complete` with artifact quality score
- **Depends on**: none (wave 1)

### Step 2: Deploy and Configure [n05]
- **Agent**: n05 (codex operations)
- **Action**: Register agent in N07 runtime, bind to spawn_configs, update dispatch routing table
- **Input**: Agent artifact from Step 1, `.cex/runtime/` configuration state
- **Output**: Updated dispatch routing; agent registered in `.cex/runtime/decisions/`
- **Signal**: `n05_deploy_complete` with deployment status
- **Depends on**: Step 1 (wave 2)

### Step 3: Validate Orchestration Capabilities [n05]
- **Agent**: n05 (codex operations)
- **Action**: Run system tests — dispatch smoke test, signal round-trip, consolidate check
- **Input**: Deployed agent artifact; test harness from `cex_system_test.py`
- **Output**: Validation report with pass/fail per capability
- **Signal**: `n05_validate_complete` with test results summary
- **Depends on**: Step 2 (wave 2, sequential after deploy)

## Dependencies
- N03 builder healthy: `python _tools/cex_doctor.py`
- `spawn_configs` for n03 and n05 must exist before workflow starts
- `.cex/runtime/` directory initialized and writable

## Signals
- **On step complete**: `{nucleus}_complete` emitted by assigned agent (see signal-builder conventions)
- **On workflow complete**: `workflow_complete` with aggregate quality score from all steps
- **On error**: `{nucleus}_error` emitted; retry per step (max 2), then escalate to N07 orchestrator

## References
- signal-builder: P12 signal emission conventions
- spawn-config-builder: `p12_spawn_n03_solo_build`, `p12_spawn_n05_solo_validate`
- N07 routing rules: `.claude/rules/n07-orchestrator.md`

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `workflow`
- **Artifact ID**: `p12_wf_create_orchestration_agent`
- **Tags**: [workflow, orchestration, agent-creation]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `workflow` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_orchestration_pipeline]] | sibling | 0.48 |
| [[p12_wf_admin_orchestration]] | sibling | 0.44 |
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.40 |
| [[p12_wf_creation_pipeline]] | sibling | 0.39 |
| [[bld_collaboration_agent]] | related | 0.38 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.37 |
| [[bld_examples_workflow]] | upstream | 0.36 |
| [[p12_dr_orchestration]] | related | 0.35 |
| [[workflow-builder]] | related | 0.35 |
| [[p02_agent_creation_nucleus]] | upstream | 0.35 |
