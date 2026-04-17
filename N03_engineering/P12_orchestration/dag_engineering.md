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
quality: 9.1
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


## DAG Execution Semantics

The directed acyclic graph defines strict execution ordering with these constraints:

- **No cycles allowed**: validator rejects graphs containing backward edges at parse time
- **Parallel branches**: independent nodes execute concurrently up to nucleus pool limit
- **Failure propagation**: node failure blocks all downstream dependents immediately
- **Partial results**: completed branches produce artifacts even if sibling branches fail

### DAG Definition Example

```yaml
# Engineering pipeline DAG
dag:
  name: build_and_validate
  nodes:
    - id: scaffold
      nucleus: N03
      depends: []
    - id: test
      nucleus: N05
      depends: [scaffold]
    - id: document
      nucleus: N04
      depends: [scaffold]
    - id: review
      nucleus: N05
      depends: [test, document]
```

| Property | Constraint | Default |
|----------|-----------|---------|
| max_depth | 8 levels | 5 |
| max_width | 6 parallel | 4 |
| timeout_per_node | 300s | 120s |
| retry_on_failure | 0-3 | 1 |

