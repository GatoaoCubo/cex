---
id: kc_state_machine
kind: knowledge_card
pillar: P01
title: "Knowledge Card -- State Machine"
version: 1.0.0
quality: null
tags: [knowledge, state_machine, fsm, xstate, uml-statechart, entity-lifecycle]
---

# State Machine

## Definition

A `state_machine` is a formal finite state machine (FSM) definition that governs entity lifecycle. It specifies all valid states an entity can be in, the events that trigger transitions between states, guard conditions gating transitions, and actions executed on transitions or state entry/exit. Based on UML 2.5 Statecharts (OMG standard) and XState 5.0 (JavaScript FSM library by David Khourshid).

Not workflow (ordered DAG of steps). Not process_manager (event coordinator across multiple processes).

## When to Use

| Scenario | Use state_machine? |
|----------|-------------------|
| Entity has multiple lifecycle states (Order: DRAFT->SUBMITTED->ACTIVE) | YES |
| State changes triggered by events with conditions | YES |
| Need deterministic lifecycle governance | YES |
| Complex sequence of workflow steps | NO -- use workflow |
| Coordinating events across multiple processes | NO -- use process_manager |

## Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| entity | string | YES | Entity whose lifecycle is modeled |
| initial_state | string | YES | Starting state (exactly one) |
| final_states | list | YES | Terminal states (no outgoing transitions) |
| states_count | integer | YES | Total number of states |
| transitions_count | integer | YES | Total number of transitions |
| transitions | table | YES | (from, event, to, guard, action) tuples |

## State Types

| Type | Description | Example |
|------|-------------|---------|
| Initial | Starting state; only one allowed | DRAFT, PENDING |
| Intermediate | Can transition in and out | ACTIVE, SUBMITTED |
| Final | No outgoing transitions | TERMINATED, DELETED |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Non-deterministic transitions | Same (state, event) -> two states | Add mutually exclusive guards |
| Missing final states | Entity lifecycle never terminates | Define TERMINATED/COMPLETED |
| Guards undefined | Unimplementable spec | Define guards as boolean expressions |
| More than 20 states | Unmaintainable FSM | Split into sub-machines |

## Cross-Framework Map

| Library | Language | Notes |
|---------|----------|-------|
| XState 5.0 | JavaScript/TypeScript | Identical semantics: states, events, guards, actions |
| Spring State Machine | Java | JVM implementation |
| Polly StateMachine | .NET | .NET implementation |
| UML Statechart | Visual notation | Graphical representation of this kind |

## Decision Tree

```
Governing an entity's lifecycle?
  YES -> state_machine
    Entity changes states in response to events?
      YES -> state_machine (correct)
      No:
        Sequence of steps with order?
          YES -> workflow (DAG)
          Coordinating events across processes?
            YES -> process_manager
```

## Integration

- Governs: agent (P02) session lifecycle
- Triggers: action_prompt (P03) via entry/exit actions
- Observed by: monitor (P11) -- state transitions are events
- Emits: event_schema (P06) -- domain events on transitions
- Referenced by: workflow (P12) -- workflow instances have state
- Pillar: P12 (Orchestration) -- entity lifecycle governance
