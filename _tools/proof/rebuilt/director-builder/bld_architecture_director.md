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
| frontmatter block | 24-field metadata header (id, kind, pillar, mission, entry_point, exit_point, builders, dag_edges, etc.) | director-builder | active |
| crew_composition | Table of participating builders with roles, inputs, outputs, and sequence positions | author | active |
| dag_structure | Directed acyclic graph of builder dependencies and data flow edges | author | active |
| handoff_contracts | Data type contracts between each connected builder pair | author | active |
| parallelism_rules | Concurrent groups and forced sequencing constraints across the crew | author | active |
| failure_handling | Per-builder fallback strategy and crew-level recovery protocol | author | active |
| entry_exit_anchors | Entry point (first builder) and exit point (final output builder) with acceptance criteria | author | active |
## Dependency Graph
```
orchestrator    --dispatches_to-->  director        --coordinates-->  builder[]
director        --sequences-->      dag_edges        --resolves-->    handoff_contracts
director        --signals-->        crew_complete
```
| From | To | Type | Data |
|------|----|------|------|
| orchestrator (P02) | director | data_flow | mission dispatched to crew via director routing rules |
| spawn_config (P12) | director | dependency | crew launch parameters reference director definition |
| director | builder (P03) | produces | director instantiates and sequences individual builders |
| director | handoff_contracts | dependency | each dag_edge requires a matching handoff contract |
| director | crew_complete (P12) | signals | emits completion signal when exit_point builder finishes |
| builder (P03) | director | dependency | builder collaboration files declare which directors they participate in |
## Boundary Table
| director IS | director IS NOT |
|-------------|-----------------|
| A coordination spec for a multi-builder crew | An individual builder identity card (builder P03) |
| Defines DAG topology, handoff contracts, and parallelism | A satellite architecture specification (satellite_spec P08) |
| Scoped to one mission with named entry and exit anchors | A reusable coordination solution (pattern P08) |
| Includes failure handling and recovery per builder | An inviolable operational rule (law P08) |
| Configures crew-level observability via completion signals | A visual architecture representation (diagram P08) |
| Documents the full crew as an orchestratable unit | An inventory of generic system components (component_map P08) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | frontmatter, mission | Director name, domain, and crew outcome |
| Composition | crew_composition, dag_structure | Which builders participate and how they connect |
| Coordination | handoff_contracts, parallelism_rules | Data contracts and execution ordering |
| Resilience | failure_handling | Per-builder fallback and crew recovery |
| Integration | entry_exit_anchors, orchestrator, spawn_config | How the crew is started and terminates |
