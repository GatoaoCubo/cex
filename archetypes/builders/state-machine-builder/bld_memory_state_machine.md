---
id: p10_lr_state_machine_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "State machines missing final states cause infinite lifecycle loops -- entities never terminate. Missing guard definitions leave transitions unimplementable. Non-deterministic transitions (same state+event without guards) cause random behavior in runtime FSM libraries."
pattern: "Always declare final states. Define every guard as implementable boolean expression. Verify determinism before committing."
evidence: "7 entity lifecycle reviews: 3 missing final states; 2 non-deterministic transitions in production caused random order states; 4 guard conditions undefined causing spec-vs-implementation drift."
confidence: 0.89
outcome: SUCCESS
domain: state_machine
tags: [state-machine, FSM, determinism, final-states, guards, xstate]
tldr: "Final states + defined guards + determinism check = implementable FSM. Missing any of these causes production runtime errors."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [state machine, FSM, finite state machine, states, transitions, guards, actions, XState, determinism]
memory_scope: project
observation_types: [feedback, project]
quality: null
title: "Memory State Machine"
density_score: 0.90
llm_function: INJECT
---

## Summary

FSM artifacts fail at runtime when they omit three things: final states, guard definitions,
and determinism verification. These are the three most common causes of production state
machine bugs in XState and Spring State Machine implementations.

## Pattern

**Final states + implementable guards + deterministic transitions.**

Final state discipline:
1. Every entity lifecycle must have at least one final state (TERMINATED, DELETED, COMPLETED)
2. Final states have no outgoing transitions -- enforce this in the artifact
3. Mark final states explicitly in the States table with type: final

Guard discipline:
1. Every guard must be an implementable boolean expression
2. Format: `methodName()` with return type boolean
3. Define the expression in the ## Guards section
4. Guards with same (state, event) must be mutually exclusive

Determinism discipline:
1. Check: no (from_state, event) pair appears twice without guards
2. If two transitions needed: add guards that are mutually exclusive
3. Document: "DETERMINISM CHECK: PASS -- no ambiguous transitions"

## Anti-Pattern

1. Missing final states -- entity lifecycle loops forever
2. Guards as strings ("if valid") without boolean definition -- unimplementable
3. Non-deterministic transitions -- random behavior in runtime
4. Using state_machine for sequential steps -- that is workflow (DAG)
5. More than 20 states -- refactor into sub-machines or hierarchical states

## Evidence Table

| Issue | Impact | Fix |
|-------|--------|-----|
| 3/7 missing final states | Infinite lifecycle loops | Always define TERMINATED/COMPLETED |
| 2/7 non-deterministic | Random order states in production | Add mutually exclusive guards |
| 4/7 undefined guards | Spec-vs-implementation drift | Define each guard as boolean expression |

## Determinism Check Table

| Situation | Outcome | Fix |
|-----------|---------|-----|
| One (state, event) -> one target | DETERMINISTIC -- OK | None needed |
| One (state, event) -> two targets, mutually exclusive guards | DETERMINISTIC -- OK | Document guard exclusivity |
| One (state, event) -> two targets, no guards | NON-DETERMINISTIC -- FAIL | Add guards |
| No transitions from state | DEAD STATE -- WARN | Add transitions or mark as final |

## Application Checklist

| Check | Question | Pass Condition |
|-------|----------|----------------|
| Final states | At least one final state? | Yes, TERMINATED or COMPLETED |
| Initial state | initial_state in states list? | Yes |
| Guard definitions | All guards defined as boolean? | Yes, methodName() or expr |
| Determinism | No ambiguous (state, event)? | Yes, verified |
| counts | states_count + transitions_count match body? | Yes |
| sub-machines count | Correct if > 20 states? | Yes, refactored into sub-machines |
| entry_actions | Entry actions documented? | Yes, for each state |
| exit_actions | Exit actions documented? | Yes, for each state |
| guard_exclusivity | Guarded branches mutually exclusive? | Yes, verified |
