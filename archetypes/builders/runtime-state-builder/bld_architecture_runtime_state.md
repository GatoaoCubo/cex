---
kind: architecture
id: bld_architecture_runtime_state
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of runtime_state — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Runtime State"
version: "1.0.0"
author: n03_builder
tags: [runtime_state, builder, examples]
tldr: "Golden and anti-examples for runtime state construction, demonstrating ideal structure and common pitfalls."
domain: "runtime state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - runtime-state-builder
  - p03_ins_runtime_state
  - p03_sp_runtime_state_builder
  - bld_collaboration_runtime_state
  - bld_architecture_session_state
  - bld_memory_runtime_state
  - p01_kc_runtime_state
  - bld_knowledge_card_runtime_state
  - bld_architecture_mental_model
  - p03_ins_mental_model
---

# Architecture: runtime_state in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_agent, persistence_scope, etc.) | runtime-state-builder | active |
| routing_rules | Active routing decisions accumulated during runtime | agent | active |
| decision_history | Log of decisions made with context and outcomes | agent | active |
| priorities | Current priority ordering that may shift during execution | agent | active |
| heuristics | Runtime-adapted rules of thumb based on recent experience | agent | active |
| tool_preferences | Learned tool selection biases from recent success/failure | agent | active |
| state_transitions | Conditions that trigger state updates during execution | author | active |
## Dependency Graph
```
mental_model    --initializes-->  runtime_state  --consumed_by-->  agent
session_state   --feeds-->        runtime_state  --produces-->     updated_decisions
runtime_state   --signals-->      state_update
```
| From | To | Type | Data |
|------|----|------|------|
| mental_model (P02) | runtime_state | data_flow | design-time model provides initial state values |
| session_state (P10) | runtime_state | data_flow | ephemeral session data feeds runtime updates |
| runtime_state | agent (P02) | consumes | agent uses current runtime state for decisions |
| runtime_state | updated_decisions | produces | refined routing and priority decisions |
| runtime_state | state_update (P12) | signals | emitted when state transitions occur |
| learning_record (P10) | runtime_state | dependency | past learnings inform initial heuristics |
## Boundary Table
| runtime_state IS | runtime_state IS NOT |
|------------------|----------------------|
| A variable mental state accumulated during agent runtime | A design-time cognitive map (mental_model P02) |
| Contains routing rules, priorities, and heuristics that evolve | An ephemeral snapshot discarded after session (session_state P10) |
| Persists within or across sessions based on scope | A permanent record of past experience (learning_record P10) |
| Updated by state transitions triggered at runtime | A static configuration loaded once at boot |
| Scoped to one agent with specific update conditions | A search index or vector store (knowledge_index P01) |
| Reflects current operational intelligence | A historical changelog |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Initialization | mental_model, learning_record | Supply design-time defaults and past learnings |
| State | frontmatter, routing_rules, priorities, heuristics, tool_preferences | Current runtime values the agent operates with |
| Transitions | state_transitions, session_state | Define when and how state values update |
| Decisions | decision_history, updated_decisions | Record and produce routing decisions |
| Events | state_update | Signal state changes to observers |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[runtime-state-builder]] | downstream | 0.59 |
| [[p03_ins_runtime_state]] | downstream | 0.53 |
| [[p03_sp_runtime_state_builder]] | upstream | 0.50 |
| [[bld_collaboration_runtime_state]] | downstream | 0.49 |
| [[bld_architecture_session_state]] | sibling | 0.49 |
| [[bld_memory_runtime_state]] | downstream | 0.48 |
| [[p01_kc_runtime_state]] | downstream | 0.47 |
| [[bld_knowledge_card_runtime_state]] | upstream | 0.45 |
| [[bld_architecture_mental_model]] | sibling | 0.42 |
| [[p03_ins_mental_model]] | upstream | 0.37 |
