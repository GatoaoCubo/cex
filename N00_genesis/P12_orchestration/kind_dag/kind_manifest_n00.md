---
id: n00_dag_manifest
kind: knowledge_card
8f: F3_inject
pillar: P12
nucleus: n00
title: "DAG -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, dag, p12, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_dag
  - bld_architecture_dag
  - p01_kc_dag
  - bld_collaboration_dag
  - p12_dag_builder_8f
  - dag-builder
  - p11_qg_dag
  - bld_knowledge_card_dag
  - p03_sp_dag_builder
  - bld_schema_reranker_config
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A dag (Directed Acyclic Graph) defines an acyclic dependency graph for workflow tasks, specifying nodes (tasks) and edges (dependencies) that determine execution order and parallelism. It is the formal dependency model that workflow orchestrators use to schedule maximum-parallelism execution while respecting data dependencies between tasks.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `dag` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nodes | array | yes | List of task nodes with ID, kind, nucleus, and description |
| edges | array | yes | Dependency edges as {from: node_id, to: node_id} pairs |
| entry_nodes | array | yes | Node IDs with no incoming edges (start nodes) |
| exit_nodes | array | yes | Node IDs with no outgoing edges (final outputs) |
| max_parallelism | integer | no | Maximum concurrent nodes (default: unlimited) |
| timeout_minutes | integer | no | Maximum total execution time |

## When to use
- When planning a multi-task mission with complex dependency relationships
- When N07 needs to compute the critical path for wave scheduling
- When visualizing workflow dependencies for review before dispatch

## Builder
`archetypes/builders/dag-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind dag --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: dag_fractal_fill_w3
kind: dag
pillar: P12
nucleus: n07
title: "Example DAG"
version: 1.0
quality: null
---
# DAG: FRACTAL_FILL Wave 3
nodes:
  - id: kc_build, nucleus: n04
  - id: agent_build, nucleus: n03
  - id: qa_review, nucleus: n05
edges: [{from: kc_build, to: qa_review}, {from: agent_build, to: qa_review}]
entry_nodes: [kc_build, agent_build]
exit_nodes: [qa_review]
```

## Related kinds
- `workflow` (P12) -- workflow that this DAG represents the execution graph of
- `dispatch_rule` (P12) -- rules that govern how DAG nodes are dispatched to nuclei
- `visual_workflow` (P12) -- visual representation of this DAG

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dag]] | upstream | 0.54 |
| [[bld_architecture_dag]] | upstream | 0.53 |
| [[p01_kc_dag]] | sibling | 0.48 |
| [[bld_collaboration_dag]] | related | 0.46 |
| [[p12_dag_builder_8f]] | related | 0.45 |
| [[dag-builder]] | related | 0.43 |
| [[p11_qg_dag]] | upstream | 0.39 |
| [[bld_knowledge_card_dag]] | sibling | 0.39 |
| [[p03_sp_dag_builder]] | upstream | 0.38 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
