---
kind: architecture
id: bld_architecture_supervisor
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of supervisor — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_supervisor
  - p03_sp_director_builder
  - supervisor-builder
  - p01_kc_supervisor
  - bld_instruction_supervisor
  - p11_qg_director
  - bld_tools_supervisor
  - bld_knowledge_card_supervisor
  - bld_examples_supervisor
  - bld_schema_supervisor
---

# Architecture: supervisor in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Identity header (topic, builders, dispatch_mode, signal_check, etc.) | supervisor-builder | required |
| topic | Domain scope of the orchestration mission | author | required |
| builders | Named list of builders this supervisor dispatches | author | required |
| dispatch_mode | Execution strategy: sequential, parallel, or conditional | author | required |
| signal_check | Whether to wait for builder completion signals | author | required |
| wave_topology | Ordered wave sequence with dependencies and signal gates | supervisor-builder | required |
| fallback_per_builder | Recovery behavior when a builder fails or times out | supervisor-builder | required |
| handoff_file | Mission context written to `.cex/runtime/handoffs/` for each builder | dispatch system | required |
| signal_file | Completion signal emitted by each builder upon finish | builder | required |
## Dependency Graph
```
mission_plan      --feeds-->    supervisor   --dispatches-->  builders (N01-N06)
decision_manifest --constrains-> supervisor   --writes-->     handoff_files
agent_card        --identifies-> supervisor   --monitors-->   signal_files
workflow          --sequences--> supervisor   --produces-->   consolidated_output
```
| From | To | Type | Data |
|------|----|------|------|
| mission_plan (P08) | supervisor | data_flow | goal, tasks, artifact list, wave structure |
| decision_manifest (P09) | supervisor | constraint | subjective decisions from GDP |
| agent_card (P02) | supervisor | identity | builder persona and capability references |
| workflow (P12) | supervisor | sequence | overall orchestration graph position |
| supervisor | handoff_files | produces | per-builder mission context in `.cex/runtime/handoffs/` |
| supervisor | signal_files | monitors | `.cex/runtime/signals/` for completion/failure |
| supervisor | spawn_config | data_flow | dispatch target with mode and fallback |
| supervisor | consolidated_output | produces | merged results from all builders |
## Boundary Table
| supervisor IS | supervisor IS NOT |
|-------------|-----------------|
| A coordination plan — dispatches builders without executing tasks | A builder (which executes tasks and produces artifacts) |
| The definition of WHO runs, WHEN, and WHAT happens on failure | A workflow (generic execution sequence without dispatch semantics) |
| Scoped to a mission with named builders and wave topology | A law (which constrains behavior, not orchestrates it) |
| Signal-aware — waits for completion before advancing waves | A spawn_config (initialization params, not orchestration logic) |
| A dispatch plan consumable by cex_mission_runner.py | A handoff file (the message TO a builder, not the plan) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Inputs | mission_plan, decision_manifest, agent_cards | Supply goal, decisions, and builder identities |
| Orchestration | wave_topology, dispatch_mode, signal_check | Define coordination strategy and execution order |
| Resilience | fallback_per_builder, timeout, retry policy | Handle builder failure without mission abort |
| Output | handoff_files, signal monitoring, consolidated_output | Dispatch builders and collect results |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_supervisor]] | downstream | 0.68 |
| [[p03_sp_director_builder]] | upstream | 0.63 |
| [[supervisor-builder]] | upstream | 0.62 |
| [[p01_kc_supervisor]] | related | 0.59 |
| [[bld_instruction_supervisor]] | upstream | 0.57 |
| [[p11_qg_director]] | downstream | 0.56 |
| [[bld_tools_supervisor]] | upstream | 0.53 |
| [[bld_knowledge_card_supervisor]] | upstream | 0.49 |
| [[bld_examples_supervisor]] | upstream | 0.49 |
| [[bld_schema_supervisor]] | upstream | 0.43 |
