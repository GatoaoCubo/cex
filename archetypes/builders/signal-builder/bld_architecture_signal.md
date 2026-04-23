---
kind: architecture
id: bld_architecture_signal
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of signal — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - signal-builder
  - bld_collaboration_signal
  - p03_sp_signal_builder
  - bld_knowledge_card_signal
  - bld_memory_signal
  - p03_ins_signal_builder
  - p01_kc_signal
  - bld_tools_signal
  - bld_examples_signal
  - p11_qg_signal
---

# Architecture: signal in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Minimal metadata (id, kind, pillar, emitter, status, timestamp) | signal-builder | active |
| status_field | Signal type: complete, error, or progress | emitter | active |
| payload | Minimal JSON body with score, message, and optional extensions | emitter | active |
| emitter_id | Identifier of the agent_group or agent that produced the signal | emitter | active |
| timestamp | ISO 8601 timestamp of emission | system | active |
| extensions | Optional additional fields without breaking consumer contracts | emitter | active |
## Dependency Graph
```
agent_group/agent  --emits-->     signal  --consumed_by-->  orchestrator
signal           --consumed_by-->  monitor  --triggers-->  workflow_step
signal           --signals-->      downstream_action
```
| From | To | Type | Data |
|------|----|------|------|
| agent_group/agent (P02) | signal | produces | emitter creates signal on task completion or error |
| signal | orchestrator | consumes | orchestrator reads signals to track agent_group status |
| signal | monitor | consumes | monitoring system aggregates signals for dashboards |
| signal | workflow_step (P12) | data_flow | signal triggers next step in multi-step workflow |
| signal | downstream_action | signals | cascading action triggered by signal reception |
| spawn_config (P12) | signal | dependency | spawn config defines expected signal patterns |
## Boundary Table
| signal IS | signal IS NOT |
|-----------|---------------|
| An atomic status event between agents (complete, error, progress) | A full instruction set for a task (handoff P12) |
| Minimal JSON payload with low overhead | A routing policy or dispatch rule (dispatch_rule P12) |
| Emitted once per event — fire and forget | A persistent state that evolves over time |
| Consumed by orchestrators and monitors | A multi-step execution flow (workflow P12) |
| Extensible via optional fields without breaking consumers | A schema-heavy artifact requiring full validation |
| Timestamped and attributed to a specific emitter | An anonymous or unattributed event |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Emission | agent_group/agent, emitter_id, timestamp | Identify who emitted the signal and when |
| Payload | status_field, payload, extensions | Carry the signal data with optional extensions |
| Consumption | orchestrator, monitor | Read and react to signals |
| Cascading | workflow_step, downstream_action | Trigger subsequent actions based on signal content |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[signal-builder]] | downstream | 0.61 |
| [[bld_collaboration_signal]] | downstream | 0.57 |
| [[p03_sp_signal_builder]] | upstream | 0.48 |
| [[bld_knowledge_card_signal]] | downstream | 0.46 |
| [[bld_memory_signal]] | downstream | 0.46 |
| [[p03_ins_signal_builder]] | upstream | 0.45 |
| [[p01_kc_signal]] | downstream | 0.40 |
| [[bld_tools_signal]] | upstream | 0.39 |
| [[bld_examples_signal]] | upstream | 0.38 |
| [[p11_qg_signal]] | downstream | 0.38 |
