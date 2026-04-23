---
kind: architecture
id: bld_architecture_retrieval_evaluator
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of retrieval_evaluator -- inventory, dependencies, and architectural position
quality: null
title: "Retrieval Evaluator Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, architecture]
tldr: "Architecture context for retrieval evaluator: components, dependencies, and boundary with retrieval logic."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_retrieval_evaluator
  - bld_schema_retrieval_evaluator
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| primary_metric | Main ranking metric (NDCG, MRR, MAP) | retrieval-evaluator-builder | required |
| k_values | Cutoff values for position-aware metrics | retrieval-evaluator-builder | required |
| judgment_scale | Relevance annotation scheme | retrieval-evaluator-builder | required |
| query_set | Evaluation queries with gold relevance | retrieval-evaluator-builder | required |
| baseline | Reference system for comparison | retrieval-evaluator-builder | required |
| thresholds | Pass/fail/regression numeric criteria | retrieval-evaluator-builder | required |
| statistical_tests | Significance testing methodology | retrieval-evaluator-builder | optional |

## Dependency Graph

```
embedding_config (P01) --upstream--> retrieval system --evaluated_by--> retrieval_evaluator
retriever_config (P02) --upstream--> retrieval system --evaluated_by--> retrieval_evaluator
retrieval_evaluator --consumed_by--> benchmark_suite (P07)
retrieval_evaluator --consumed_by--> regression_check (P11)
retrieval_evaluator --independent-- knowledge_index (P10)
```

## Boundary Table

| retrieval_evaluator IS | retrieval_evaluator IS NOT |
|----------------------|---------------------------|
| Evaluation methodology: what metrics, what thresholds | A retriever -- retriever executes queries |
| Defines quality criteria for retrieval output | An embedding_config -- embedding configures the model |
| Specifies judgment protocol for relevance | A benchmark_suite -- suite bundles multiple evaluators |
| Consumed by regression checks and CI pipelines | A knowledge_index -- index configures search structure |
