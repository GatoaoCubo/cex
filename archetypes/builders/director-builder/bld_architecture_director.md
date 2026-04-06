---
kind: architecture
id: bld_architecture_director
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of director — inventory, dependencies, and architectural position
---

# Architecture: director in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Identity header (topic, builders, dispatch_mode, signal_check, etc.) | director-builder | required |
| topic | Domain scope of the orchestration mission | author | required |
| builders | Named list of builders this director dispatches | author | required |
| dispatch_mode | Execution strategy: sequential, parallel, or conditional | author | required |
| signal_check | Whether to wait for builder completion signals | author | required |
| wave_topology | Ordered wave sequence with dependencies and signal gates | director-builder | required |
| fallback_per_builder | Recovery behavior when a builder fails or times out | director-builder | required |
| handoff_file | Mission context written to `.cex/runtime/handoffs/` for each builder | dispatch system | required |
| signal_file | Completion signal emitted by each builder upon finish | builder | required |
## Dependency Graph
```
mission_plan      --feeds-->    director   --dispatches-->  builders (N01-N06)
decision_manifest --constrains-> director   --writes-->     handoff_files
agent_card        --identifies-> director   --monitors-->   signal_files
workflow          --sequences--> director   --produces-->   consolidated_output
```
| From | To | Type | Data |
|------|----|------|------|
| mission_plan (P08) | director | data_flow | goal, tasks, artifact list, wave structure |
| decision_manifest (P09) | director | constraint | subjective decisions from GDP |
| agent_card (P02) | director | identity | builder persona and capability references |
| workflow (P12) | director | sequence | overall orchestration graph position |
| director | handoff_files | produces | per-builder mission context in `.cex/runtime/handoffs/` |
| director | signal_files | monitors | `.cex/runtime/signals/` for completion/failure |
| director | spawn_config | data_flow | dispatch target with mode and fallback |
| director | consolidated_output | produces | merged results from all builders |
## Boundary Table
| director IS | director IS NOT |
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
