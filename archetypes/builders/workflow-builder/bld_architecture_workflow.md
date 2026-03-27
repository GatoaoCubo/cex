---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of workflow — inventory, dependencies, and architectural position
---

# Architecture: workflow in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 20-field metadata header (id, kind, pillar, domain, steps_count, mode, etc.) | workflow-builder | active |
| step_definitions | Ordered list of steps with agent, task, and dependency declarations | author | active |
| wave_ordering | Grouping of steps into parallel waves with dependency constraints | author | active |
| signal_contracts | Expected completion/error signals per step from signal-builder | author | active |
| spawn_references | Spawn configurations per satellite from spawn-config-builder | author | active |
| error_recovery | Retry, skip, and rollback strategies for failed steps | author | active |
| completion_criteria | Conditions that define the workflow as successfully finished | author | active |

## Dependency Graph

```
orchestrator    --executes-->   workflow  --dispatches_to-->  satellite/agent
signal          --consumed_by-->  workflow  --produces-->     mission_result
workflow        --depends-->    spawn_config
```

| From | To | Type | Data |
|------|----|------|------|
| orchestrator | workflow | consumes | orchestrator executes workflow steps in order |
| workflow | satellite/agent (P02) | produces | steps dispatched to satellites for execution |
| signal (P12) | workflow | data_flow | completion signals advance workflow to next step |
| spawn_config (P12) | workflow | dependency | satellite launch parameters per step |
| workflow | mission_result | produces | aggregated output from all workflow steps |
| workflow | workflow_event (P12) | signals | emitted on step completion, failure, or workflow end |

## Boundary Table

| workflow IS | workflow IS NOT |
|-------------|-----------------|
| A multi-step orchestration with agents, waves, and signals | A prompt chaining sequence (chain P03) |
| Steps execute sequentially, in parallel, or mixed via waves | A dependency graph without execution semantics (dag P12) |
| References signal-builder for completion contracts | A simple keyword-to-destination mapping (dispatch_rule P12) |
| References spawn-config-builder for satellite launches | A routing table with confidence thresholds (router P02) |
| Includes error recovery with retry, skip, and rollback | A one-shot task prompt (action_prompt P03) |
| Scoped to a mission with defined completion criteria | An open-ended process without end condition |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Planning | frontmatter, step_definitions, wave_ordering | Define steps, agents, and parallel grouping |
| Launch | spawn_references, spawn_config | Configure how satellites are started per step |
| Execution | orchestrator, satellite/agent | Run steps and dispatch work to agents |
| Coordination | signal_contracts, signal | Track progress via completion signals |
| Completion | error_recovery, completion_criteria, mission_result | Handle failures and determine success |
