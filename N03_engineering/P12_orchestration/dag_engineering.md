---
id: p12_dag_builder_8f
kind: dag
8f: F8_collaborate
pillar: P12
title: DAG -- 8F Pipeline
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [dag, builder, N03, pipeline]
tldr: "8F pipeline as directed acyclic graph: 8 nodes (F1-F8), 1 retry cycle (F6<->F7, max 2), 5 deterministic nodes (F1/F2/F3/F5/F7) + 2 LLM nodes (F4/F6) + 1 I/O node (F8). Cross-artifact parallelism via cex_forge.py."
density_score: 0.88
related:
  - p01_kc_dag
  - bld_schema_dag
  - bld_architecture_dag
  - p11_qg_dag
  - bld_collaboration_dag
  - dag-builder
  - p03_sp_dag_builder
  - bld_schema_kind
  - bld_knowledge_card_dag
  - p10_lr_dag_builder
---

# DAG: 8F Construction Pipeline

## Graph

    F1_CONSTRAIN -> F2_BECOME -> F3_INJECT -> F4_REASON
                                                  |
                                                  v
                                              F5_CALL
                                                  |
                                                  v
                                           F6_PRODUCE <--+
                                                  |      |
                                                  v      | retry (max 2)
                                             F7_GOVERN --+
                                                  |
                                                  v
                                           F8_COLLABORATE
                                          (save+compile+index)

## Nodes

| Node | Input | Output | Deterministic |
|------|-------|--------|---------------|
| F1 | kind name | constraints | Yes |
| F2 | kind name | builder identity | Yes |
| F3 | kind name | knowledge context | Yes |
| F4 | F1+F2+F3 | construction plan | No (LLM) |
| F5 | kind name | tools + existing | Yes |
| F6 | F4+F5 | artifact text | No (LLM) |
| F7 | F6 output | pass/fail + score | Yes |
| F8 | F7 pass | saved path | Yes |

## Edges

All sequential. F6->F7->F6 is the only cycle (retry).
Max cycle: 2. After 2 retries, F7 emits HARD FAIL.

## Parallelism

- Within single artifact: none (strict sequential)
- Across artifacts: full parallel via cex_forge.py
- Across nuclei: full parallel via spawn grid


## Cycle Exception: F6-F7 Retry Loop

The graph is acyclic except for the controlled F6->F7->F6 retry edge. This is not
a general cycle -- it is a bounded retry with hard termination:

| Attempt | Trigger | Action |
|---------|---------|--------|
| 1st | F7 returns SOFT FAIL | F6 re-generates with issues list injected |
| 2nd | F7 returns SOFT FAIL again | F6 re-generates with both prior issues |
| 3rd | F7 returns anything < 8.0 | HARD FAIL -- no more retries, error signal |

## Cross-Artifact Parallelism

| Scope | Tool | Max Concurrent | Coordination |
|-------|------|---------------|--------------|
| Single artifact | cex_8f_runner.py | 1 (sequential F1-F8) | None needed |
| Batch same-kind | cex_forge.py | 6 (configurable) | Independent -- no shared state |
| Multi-nucleus grid | spawn_grid.ps1 | 6 nuclei | Signal-based via .cex/runtime/signals/ |

## Multi-Nucleus DAG Example

```
N01 research ──┐
               ├──> N03 build ──> N05 test ──> N07 consolidate
N04 knowledge ─┘
```

Each node is a full 8F pipeline run. Inter-node edges are handoff files.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_dag]] | related | 0.33 |
| [[bld_schema_dag]] | upstream | 0.33 |
| [[bld_architecture_dag]] | upstream | 0.32 |
| [[p11_qg_dag]] | upstream | 0.31 |
| [[bld_collaboration_dag]] | related | 0.30 |
| [[dag-builder]] | related | 0.28 |
| [[p03_sp_dag_builder]] | upstream | 0.25 |
| [[bld_schema_kind]] | upstream | 0.25 |
| [[bld_knowledge_card_dag]] | upstream | 0.25 |
| [[p10_lr_dag_builder]] | upstream | 0.24 |
