---
id: p12_dag_builder_8f
kind: dag
pillar: P12
title: DAG -- 8F Pipeline
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [dag, builder, N03, pipeline]
tldr: The 8F pipeline as DAG -- 9 nodes, strict order, retry loop at F6-F7.
density_score: 0.88
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
