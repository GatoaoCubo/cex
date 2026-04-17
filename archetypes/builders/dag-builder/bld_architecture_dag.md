---
kind: architecture
id: bld_architecture_dag
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of dag — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| nodes | List of tasks with id, label, and description | dag-builder | required |
| edges | Directed dependencies between nodes: from → to | dag-builder | required |
| topological_order | Pre-computed valid execution sequence | dag-builder | required |
| parallel_groups | Sets of nodes with no mutual dependency (can run concurrently) | dag-builder | required |
| entry_points | Nodes with no incoming edges (start of execution) | dag-builder | required |
| exit_points | Nodes with no outgoing edges (end of execution) | dag-builder | required |
| cycle_check | Validation assertion: no cycles exist in the graph | dag-builder | required |
| metadata | dag id, version, mission context, author | dag-builder | required |
| node_annotations | Per-node: estimated duration, owner, criticality | dag-builder | optional |
## Dependency Graph
```
requirements --provides--> dag (mission brief defines nodes and constraints)
dag --produces_for--> workflow (P12) (execution implements the DAG structure)
dag --produces_for--> handoff (P12) (one handoff per DAG node)
dag --produces_for--> spawn_config (P12) (parallel_groups inform spawn slot count)
workflow (P12) --consumes--> dag (runtime walks topological order)
signal (P12) --independent-- dag (dag does not emit or consume runtime signals)
dispatch_rule (P12) --independent-- dag (routing policy is orthogonal to structure)
```
| From | To | Type | Data |
|------|----|------|------|
| requirements | dag | data_flow | task list, constraints, mission scope |
| dag | workflow | produces | topological order, parallel groups |
| dag | handoff | produces | per-node task context |
| dag | spawn_config | produces | parallelism count for slot allocation |
| workflow | dag | consumes | walks edges to determine execution order |
## Boundary Table
| dag IS | dag IS NOT |
|--------|------------|
| A static dependency graph: nodes, edges, topological order | A workflow — workflow executes steps with runtime state and error handling |
| Planning artifact: defines what must happen before what | A component_map — component_map inventories parts with ownership and health |
| Immutable structure: computed once before execution starts | A signal — signal reports atomic runtime events |
| Expresses parallelism as sets of independent nodes | A handoff — handoff provides full task instructions and scope fence |
| Validates acyclicity as a hard correctness constraint | A dispatch_rule — dispatch_rule routes tasks to execution targets |
| Consumed by orchestrators to determine execution order | A spawn_config — spawn_config defines how processes are launched |
| Has explicit entry and exit points | A crew — crew defines multi-agent coordination protocols |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | requirements, mission brief | Define the tasks and constraints the DAG must model |
| Structure | nodes, edges, metadata | Represent the dependency graph as a directed acyclic graph |
| Analysis | topological_order, parallel_groups, entry_points, exit_points | Derive execution sequence and concurrency opportunities |
| Validation | cycle_check | Enforce the acyclicity invariant (no cycles = valid DAG) |
| Annotation | node_annotations | Enrich nodes with duration estimates, ownership, criticality |
| Output | workflow, handoff, spawn_config | Downstream artifacts that implement or instantiate the DAG |
