---
kind: collaboration
id: bld_collaboration_state_machine
pillar: P12
llm_function: COLLABORATE
purpose: How state-machine-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: null
title: "Collaboration State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, collaboration]
tldr: "Entity lifecycle specialist. Upstream of workflow and process_manager. Downstream of domain model design."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Collaboration: state-machine-builder
## My Role in Crews
| Responsibility | What I Answer | What I DON'T Do |
|----------------|---------------|-----------------|
| ENTITY LIFECYCLE SPECIALIST | "What states can this entity be in?" | Sequence workflow steps |
| Formal FSM definition | States, transitions, guards, actions | Coordinate cross-process events |
| Lifecycle governance | Deterministic entity state changes | Schedule recurring tasks |
## Crew Compositions
### Crew: "Domain Model Package"
```
  1. bounded-context-builder  -> "define BC and ubiquitous language"
  2. state-machine-builder    -> "entity lifecycle FSMs"
  3. aggregate-root-builder   -> "aggregate root enforcing invariants"
  4. event-schema-builder     -> "domain events emitted on state transitions"
```
### Crew: "Workflow + Lifecycle"
```
  1. state-machine-builder    -> "entity state lifecycle"
  2. workflow-builder         -> "orchestration DAG for fulfillment"
  3. process-manager-builder  -> "event coordinator across state machines"
```
### Crew: "Agent Lifecycle"
```
  1. state-machine-builder    -> "agent session lifecycle (IDLE/ACTIVE/PAUSED/TERMINATED)"
  2. agent-builder            -> "agent using this lifecycle definition"
  3. monitor-builder          -> "observability for state transitions"
```
## Handoff Protocol
### I Receive
| Input | Type | Notes |
|-------|------|-------|
| Entity name and domain | string | Entity whose lifecycle is governed |
| Business events | list | Events that change entity state |
| Business rules | list | Guard conditions constraining state changes |
| Side-effects required | list | Notifications, billing, etc. on transitions |
### I Produce
| Output | Format | Destination |
|--------|--------|-------------|
| state_machine artifact | .md with YAML frontmatter + tables | N0X_{domain}/P12_orchestration/ |
| Compilation signal | complete with quality score | .cex/runtime/signals/ |
## Builders I Depend On
| Builder | Why | Dependency Type |
|---------|-----|----------------|
| None | Independent builder (layer 0) | -- |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder | Workflow instances have state machine transitions |
| process-manager-builder | Coordinates events across multiple state machines |
| agent-builder | Agents with session lifecycle reference state machine |
| monitor-builder | Monitors track state transition events |
| event-schema-builder | Domain events emitted by state machine transitions |
## Quality Checklist Before Signal
| Check | Pass Condition |
|-------|---------------|
| id pattern | ^p12_sm_[a-z][a-z0-9_]+$ |
| initial_state | in states list |
| final_states | all in states list |
| states_count | matches body row count |
| transitions_count | matches body row count |
| determinism | no (state, event) appears twice without guards |
| guards | all defined as boolean expressions |
| actions | all defined with trigger and effect |
