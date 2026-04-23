---
kind: schema
id: bld_schema_dag
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for dag - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_handoff
  - bld_schema_input_schema
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
---

# Schema: dag
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `dag` |
| Machine format | `yaml` |
| Naming | `p12_dag_{pipeline}.yaml` |
| Max bytes | 3072 |
## Required Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (`p12_dag_{slug}`) | YES | - | Unique DAG identifier |
| kind | literal "dag" | YES | - | Type integrity |
| lp | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| pipeline | string | YES | - | Pipeline or mission name |
| nodes | list[object{id, label, agent_group}] | YES | - | Tasks in the graph |
| edges | list[object{from, to}] | YES | - | Dependency arrows |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Searchability |
| tldr | string <= 160ch | YES | - | Dense summary |
## Optional Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| execution_order | list[list[string]] | NO | omitted | Topologically sorted waves |
| parallel_groups | list[list[string]] | NO | omitted | Nodes that run simultaneously |
| critical_path | list[string] | NO | omitted | Longest dependency chain |
| estimated_duration | string | NO | omitted | Estimated total time |
| node_count | integer >= 1 | NO | omitted | Total nodes |
| edge_count | integer >= 0 | NO | omitted | Total edges |
| max_parallelism | integer >= 1 | NO | omitted | Maximum concurrent nodes |
| keywords | list[string] | NO | omitted | Brain search terms |
| linked_artifacts | object {primary, related} | NO | omitted | Cross-references |
## Node Object
Fields: `id` (unique slug), `label` (human description), `agent_group` (executor, optional).
## Edge Object
Fields: `from` (node id that complete first), `to` (node id that depends on from).
## Semantic Rules
1. One DAG describes one pipeline or mission's dependency structure
2. Edges are directed: `from` must complete before `to` can start
3. The graph MUST be acyclic — cycles are a HARD validation failure
4. Nodes with no incoming edges are entry points (can start immediately)
5. Nodes with no outgoing edges are terminal (pipeline endpoints)
6. `execution_order` groups nodes into sequential waves of parallel tasks
## Boundary Rules
`dag` IS: static dependency structure, execution order spec, orchestration input.
`dag` IS NOT: `workflow` (runtime), `component_map` (inventory), `chain` (prompts),
`spawn_config` (boot), `signal` (events), `handoff` (instructions),
`dispatch_rule` (routing), `crew` (coordination). See ARCHITECTURE.md.
## ID Pattern
Regex: `^p12_dag_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Nodes` — task definitions with id, label, agent_group
2. `## Edges` — dependency relationships between nodes
3. `## Execution Order` — topologically sorted waves
## Constraints
- max_bytes: 3072
- naming: `p12_dag_{pipeline}.yaml`
- id == filename stem
- Graph MUST be acyclic
- Every edge must reference existing node ids
- No runtime state: DAG is a static spec

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_handoff]] | sibling | 0.58 |
| [[bld_schema_input_schema]] | sibling | 0.52 |
| [[bld_schema_reranker_config]] | sibling | 0.50 |
| [[bld_schema_usage_report]] | sibling | 0.50 |
| [[bld_schema_quickstart_guide]] | sibling | 0.49 |
| [[bld_schema_dataset_card]] | sibling | 0.49 |
| [[bld_schema_search_strategy]] | sibling | 0.49 |
| [[bld_schema_benchmark_suite]] | sibling | 0.48 |
| [[bld_schema_integration_guide]] | sibling | 0.48 |
| [[bld_schema_sandbox_config]] | sibling | 0.48 |
