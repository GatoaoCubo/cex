---
kind: architecture
id: bld_architecture_workflow
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of workflow — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Workflow"
version: "1.0.0"
author: n03_builder
tags: [workflow, builder, examples]
tldr: "Golden and anti-examples for workflow construction, demonstrating ideal structure and common pitfalls."
domain: "workflow construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - workflow-builder
  - bld_collaboration_workflow
  - bld_memory_workflow
  - bld_knowledge_card_workflow
  - p01_kc_workflow
  - p11_qg_workflow
  - p03_sp_workflow-builder
  - bld_examples_workflow
  - p03_ins_workflow
  - bld_collaboration_spawn_config
---

# Architecture: workflow in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 20-field metadata header (id, kind, pillar, domain, steps_count, mode, etc.) | workflow-builder | active |
| step_definitions | Ordered list of steps with agent, task, and dependency declarations | author | active |
| wave_ordering | Grouping of steps into parallel waves with dependency constraints | author | active |
| signal_contracts | Expected completion/error signals per step from signal-builder | author | active |
| spawn_references | Spawn configurations per agent_group from spawn-config-builder | author | active |
| error_recovery | Retry, skip, and rollback strategies for failed steps | author | active |
| completion_criteria | Conditions that define the workflow as successfully finished | author | active |
## Dependency Graph
```
orchestrator    --executes-->   workflow  --dispatches_to-->  agent_group/agent
signal          --consumed_by-->  workflow  --produces-->     mission_result
workflow        --depends-->    spawn_config
```
| From | To | Type | Data |
|------|----|------|------|
| orchestrator | workflow | consumes | orchestrator executes workflow steps in order |
| workflow | agent_group/agent (P02) | produces | steps dispatched to agent_groups for execution |
| signal (P12) | workflow | data_flow | completion signals advance workflow to next step |
| spawn_config (P12) | workflow | dependency | agent_group launch parameters per step |
| workflow | mission_result | produces | aggregated output from all workflow steps |
| workflow | workflow_event (P12) | signals | emitted on step completion, failure, or workflow end |
## Boundary Table
| workflow IS | workflow IS NOT |
|-------------|-----------------|
| A multi-step orchestration with agents, waves, and signals | A prompt chaining sequence (chain P03) |
| Steps execute sequentially, in parallel, or mixed via waves | A dependency graph without execution semantics (dag P12) |
| References signal-builder for completion contracts | A simple keyword-to-destination mapping (dispatch_rule P12) |
| References spawn-config-builder for agent_group launches | A routing table with confidence thresholds (router P02) |
| Includes error recovery with retry, skip, and rollback | A one-shot task prompt (action_prompt P03) |
| Scoped to a mission with defined completion criteria | An open-ended process without end condition |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Planning | frontmatter, step_definitions, wave_ordering | Define steps, agents, and parallel grouping |
| Launch | spawn_references, spawn_config | Configure how agent_groups are started per step |
| Execution | orchestrator, agent_group/agent | Run steps and dispatch work to agents |
| Coordination | signal_contracts, signal | Track progress via completion signals |
| Completion | error_recovery, completion_criteria, mission_result | Handle failures and determine success |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-builder]] | downstream | 0.63 |
| [[bld_collaboration_workflow]] | downstream | 0.59 |
| [[bld_memory_workflow]] | downstream | 0.55 |
| [[bld_knowledge_card_workflow]] | upstream | 0.53 |
| [[p01_kc_workflow]] | downstream | 0.48 |
| [[p11_qg_workflow]] | downstream | 0.48 |
| [[p03_sp_workflow-builder]] | upstream | 0.47 |
| [[bld_examples_workflow]] | upstream | 0.40 |
| [[p03_ins_workflow]] | upstream | 0.38 |
| [[bld_collaboration_spawn_config]] | downstream | 0.37 |
