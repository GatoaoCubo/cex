---
kind: knowledge_card
id: bld_knowledge_card_dag
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for dag production — dependency graph specification
sources: graph theory (Kahn 1962), Apache Airflow, Makefile dependencies, topological sort
quality: 9.1
title: "Knowledge Card Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_dag
  - p11_qg_dag
  - p10_lr_dag_builder
  - bld_instruction_dag
  - bld_schema_dag
  - p03_sp_dag_builder
  - bld_architecture_dag
  - bld_collaboration_dag
  - dag-builder
  - p12_dag_builder_8f
---

# Domain Knowledge: dag
## Executive Summary
DAGs (Directed Acyclic Graphs) are static dependency specifications defining task order and parallelism. They answer "what depends on what?" and "what can run in parallel?" DAGs are blueprints consumed by orchestrators — they do not execute tasks themselves. They differ from workflows (runtime execution), component maps (structural inventory), and chains (prompt pipelines).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| llm_function | PRODUCE |
| Max size | 3072 bytes |
| Core elements | nodes (tasks), edges (dependencies) |
| Key constraint | MUST be acyclic — cycles are validation failure |
| Naming | p12_dag_{pipeline}.yaml |
| Execution order | Derived via topological sort into waves |
## Patterns
- **Graph properties**: every valid DAG must satisfy these constraints
| Property | Requirement |
|----------|-------------|
| Acyclicity | No cycles — A→B→C→A is invalid |
| Direction | Edges point from dependency to dependent |
| Entry points | Nodes with zero incoming edges start first |
| Terminal points | Nodes with zero outgoing edges are endpoints |
| Parallelism | Independent nodes in same wave run concurrently |
- **Topological sort into waves**: derive execution order automatically
  - Wave 1: nodes with no incoming edges (entry points)
  - Wave 2: nodes whose dependencies are all in Wave 1
  - Wave N: nodes whose dependencies are all in Waves 1..N-1
- **Node specification**: each node carries id, label, and optional assignee
- **Edge specification**: each edge carries source, target, and optional type (data, trigger, approval)
- **Static blueprint**: DAGs define structure only — no actions, no error handling, no runtime state
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Cycles (A→B→C→A) | Topological sort fails; infinite loop |
| Runtime logic in DAG | DAGs are static; use workflow for conditionals |
| Missing entry point | No node to start execution |
| Disconnected subgraphs | Orphan nodes never execute |
| Over-serialized (A→B→C→D→E all linear) | Misses parallelism opportunities |
| Unlabeled edges | Ambiguous dependency type; cannot reason about data flow |
## Application
1. List all tasks as nodes: id, label, optional assignee
2. Define edges: source → target for each dependency
3. Verify acyclicity: no cycles in the graph
4. Derive waves: topological sort groups parallel-eligible nodes
5. Identify entry and terminal points
6. Validate: <= 3072 bytes, no cycles, no orphans, all nodes reachable
## References
- Kahn 1962: topological sorting algorithm for DAGs
- Apache Airflow: DAG-based workflow orchestration
- Make: dependency-based build system (Makefile rules)
- Dagger.io: CI/CD pipelines as directed acyclic graphs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_dag]] | sibling | 0.52 |
| [[p11_qg_dag]] | downstream | 0.48 |
| [[p10_lr_dag_builder]] | downstream | 0.48 |
| [[bld_instruction_dag]] | downstream | 0.47 |
| [[bld_schema_dag]] | downstream | 0.43 |
| [[p03_sp_dag_builder]] | downstream | 0.43 |
| [[bld_architecture_dag]] | downstream | 0.42 |
| [[bld_collaboration_dag]] | downstream | 0.41 |
| [[dag-builder]] | downstream | 0.36 |
| [[p12_dag_builder_8f]] | downstream | 0.32 |
