---
id: bld_knowledge_card_state_machine
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 8.5
title: "State Machine Builder -- Knowledge Card"
llm_function: INJECT
tags: [state_machine, fsm, xstate, P12, entity-lifecycle]
tldr: "state_machine: formal FSM with states, transitions, guards, and actions for entity lifecycle. NOT workflow (DAG) nor process_manager (event coordinator)."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
related:
  - bld_schema_lifecycle_rule
  - p03_ins_lifecycle_rule
  - bld_schema_runtime_state
  - bld_memory_runtime_state
  - bld_schema_quickstart_guide
  - bld_memory_lifecycle_rule
  - bld_architecture_lifecycle_rule
  - p11_qg_lifecycle_rule
  - bld_schema_usage_report
  - p03_sp_lifecycle_rule_builder
---

# Knowledge Card: state_machine

## Definition

A `state_machine` is a formal finite state machine (FSM) definition that governs entity lifecycle.
It specifies all possible states an entity can be in, the events that trigger transitions between
states, guard conditions that gate transitions, and actions executed on transitions or state entry/exit.
Based on UML 2.5 Statecharts (OMG standard) and XState 5.0 (JavaScript FSM by David Khourshid).

## Origin

- **Moore/Mealy machines** (1950s): foundational FSM theory
- **Harel Statecharts** (1987): hierarchical states, concurrent regions, history states
- **UML 2.5** (OMG 2015): standardized statechart diagrams
- **XState 5.0** (David Khourshid, 2019): JavaScript/TypeScript FSM library
- **CEX pillar**: P12 (Orchestration) -- governs entity lifecycle in workflows

## Key Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| entity | string | YES | Entity whose lifecycle is modeled |
| initial_state | string | YES | Starting state (pseudo-state) |
| final_states | list | YES | Terminal states (no outgoing transitions) |
| states | list | YES | All valid states with type and description |
| transitions | list | YES | (from, event, to, guard, action) tuples |
| guard | expression | OPT | Boolean condition gating transition |
| entry_action | string | OPT | Action on state entry |
| exit_action | string | OPT | Action on state exit |

## When to Use

| Scenario | Use state_machine? |
|----------|-------------------|
| Entity has multiple lifecycle states (Order: DRAFT -> SUBMITTED -> ACTIVE) | YES |
| State changes are triggered by events with guard conditions | YES |
| Need deterministic lifecycle governance (no ambiguous transitions) | YES |
| Complex sequence of steps in a workflow | NO -- use workflow (DAG) |
| Coordinating events across multiple processes | NO -- use process_manager |
| Simple CRUD operation | NO -- no state machine needed |

## Transition Table Format

| from_state | event | to_state | guard | action |
|------------|-------|----------|-------|--------|
| DRAFT | submit | SUBMITTED | valid(form) | sendConfirmation() |
| SUBMITTED | approve | APPROVED | hasApprover() | notifyUser() |
| SUBMITTED | reject | DRAFT | - | notifyRejection() |
| APPROVED | activate | ACTIVE | - | createAccount() |
| ACTIVE | suspend | SUSPENDED | - | pauseBilling() |
| SUSPENDED | resume | ACTIVE | - | resumeBilling() |
| ACTIVE | terminate | TERMINATED | - | closeBilling() |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Non-deterministic transitions | Same (state, event) -> two possible states | Add guard conditions to disambiguate |
| Missing final states | Entity lifecycle never completes | Define TERMINATED/DELETED/COMPLETED |
| Guards as strings without definition | Unimplementable spec | Define guards in ## Guards section |
| Using for workflow steps | FSM is for state, not sequence | Use workflow (DAG) for sequential steps |
| Missing initial_state | No entry point | Always declare initial_state |

## Decision Tree

```
Governing an entity's lifecycle?
  YES -> state_machine
    Does the entity change states in response to events?
      YES -> state_machine (correct)
      NO:
        Is it a sequence of steps with order?
          YES -> workflow (DAG)
          Is it coordinating events across processes?
            YES -> process_manager
```

## Cross-Framework Map

| Framework/Library | Equivalent | Notes |
|------------------|-----------|-------|
| XState (JavaScript) | state_machine | Identical semantics: states, events, transitions, guards, actions |
| Redux Toolkit stateMachine | state_machine | Similar but tied to Redux store |
| Spring State Machine | state_machine | JVM implementation |
| AWS Step Functions (Choice state) | state_machine | Partial -- Step Functions is more workflow |
| UML Statechart Diagram | state_machine | Visual representation of this kind |

## Integration Graph

```
state_machine (P12)
  |
  |-- governs --> agent (P02) -- agent state lifecycle
  |-- governs --> workflow (P12) -- workflow instances have state
  |-- triggers --> action_prompt (P03) -- entry/exit actions are prompts
  |-- observed by --> monitor (P11) -- state transitions are observable events
  |-- referenced by --> bugloop (P11) -- error states trigger recovery
```

## XState 5 Example

```javascript
import { createMachine } from 'xstate';
const orderMachine = createMachine({
  id: 'order',
  initial: 'draft',
  states: {
    draft: { on: { SUBMIT: { target: 'submitted', guard: 'isValid' } } },
    submitted: {
      on: {
        APPROVE: { target: 'approved', actions: 'notifyUser' },
        REJECT: 'draft'
      }
    },
    approved: { on: { ACTIVATE: 'active' } },
    active: {
      on: {
        SUSPEND: 'suspended',
        TERMINATE: 'terminated'
      }
    },
    suspended: { on: { RESUME: 'active' } },
    terminated: { type: 'final' }
  }
});
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lifecycle_rule]] | downstream | 0.41 |
| [[p03_ins_lifecycle_rule]] | downstream | 0.34 |
| [[bld_schema_runtime_state]] | downstream | 0.33 |
| [[bld_memory_runtime_state]] | downstream | 0.32 |
| [[bld_schema_quickstart_guide]] | downstream | 0.31 |
| [[bld_memory_lifecycle_rule]] | downstream | 0.31 |
| [[bld_architecture_lifecycle_rule]] | downstream | 0.31 |
| [[p11_qg_lifecycle_rule]] | downstream | 0.31 |
| [[bld_schema_usage_report]] | downstream | 0.29 |
| [[p03_sp_lifecycle_rule_builder]] | downstream | 0.29 |
