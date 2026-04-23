---
quality: 8.8
quality: 8.2
kind: architecture
id: bld_architecture_state_machine
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of state_machine -- inventory, dependencies, and architectural position
title: "Architecture State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, architecture]
tldr: "Component map: states (initial/final/intermediate), transitions (from/event/to/guard/action), entry/exit actions. External: workflow, process_manager."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p03_sp_lifecycle_rule_builder
  - bld_memory_runtime_state
  - bld_collaboration_lifecycle_rule
  - p03_ins_lifecycle_rule
  - bld_memory_lifecycle_rule
  - p11_qg_runtime_state
  - bld_memory_action_paradigm
  - p11_qg_lifecycle_rule
  - runtime-state-builder
  - bld_knowledge_card_runtime_state
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| entity | Entity whose lifecycle is being modeled | state_machine | required |
| initial_state | Starting state (pseudo-state) | state_machine | required |
| states | Set of all named states | state_machine | required |
| final_states | Terminal states (entity lifecycle ends) | state_machine | required |
| transitions | List of (from, event, to, guard, action) tuples | state_machine | required |
| transition.from_state | State this transition originates from | transition | required |
| transition.event | Event that triggers transition | transition | required |
| transition.to_state | Destination state | transition | required |
| transition.guard | Boolean condition gating the transition | transition | optional |
| transition.action | Side-effect executed on transition | transition | optional |
| state.entry_action | Action executed when entering state | state | optional |
| state.exit_action | Action executed when leaving state | state | optional |
| workflow | DAG of sequential/parallel steps (separate kind) | P12 (separate kind) | external |
| process_manager | Event coordinator for long-running processes | P12 (separate kind) | external |

## FSM Structure Diagram

```
                  [event: submit]
DRAFT  -----------guard: valid----------->  SUBMITTED
  |                                              |
  | [event: delete]                    [event: approve]
  v                                              v
DELETED                               APPROVED
                                          |
                               [event: activate]
                                          v
                                       ACTIVE
                                          |
                               [event: suspend]
                                     <------->
                                      SUSPENDED
                                          |
                               [event: terminate]
                                          v
                                      TERMINATED (final)
```

## State Types

| Type | Description | Example |
|------|-------------|---------|
| Initial | Starting state; only one allowed | DRAFT, PENDING |
| Intermediate | Can transition in and out | ACTIVE, SUBMITTED |
| Final | No outgoing transitions | TERMINATED, DELETED |
| Composite | Contains sub-states (UML hierarchical) | PROCESSING (has sub-states) |

## Boundary Table

| state_machine IS | state_machine IS NOT |
|------------------|----------------------|
| Formal FSM with deterministic transitions | Ordered sequence of steps (that is workflow) |
| Entity lifecycle governance | Event orchestration across multiple processes (that is process_manager) |
| Guard-conditioned state changes | Task scheduling (that is schedule) |
| UML statechart / XState definition | BPMN process diagram (that is workflow) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| identity | entity, initial_state, final_states | Define what entity and lifecycle scope |
| state set | states | All possible states the entity can be in |
| transitions | from, event, to, guard | Define all valid state changes |
| actions | entry_action, exit_action, transition.action | Side-effects on state changes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_lifecycle_rule_builder]] | upstream | 0.37 |
| [[bld_memory_runtime_state]] | downstream | 0.36 |
| [[bld_collaboration_lifecycle_rule]] | downstream | 0.33 |
| [[p03_ins_lifecycle_rule]] | upstream | 0.31 |
| [[bld_memory_lifecycle_rule]] | downstream | 0.31 |
| [[p11_qg_runtime_state]] | downstream | 0.31 |
| [[bld_memory_action_paradigm]] | downstream | 0.29 |
| [[p11_qg_lifecycle_rule]] | downstream | 0.27 |
| [[runtime-state-builder]] | downstream | 0.25 |
| [[bld_knowledge_card_runtime_state]] | upstream | 0.25 |
