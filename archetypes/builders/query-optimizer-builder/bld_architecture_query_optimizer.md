---
kind: architecture
id: bld_architecture_query_optimizer
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of query_optimizer
quality: null
title: "Query Optimizer Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, architecture]
tldr: "Architecture context for query optimizer: components and boundary."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_query_optimizer
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| techniques | Optimization techniques in pipeline order | query-optimizer-builder | required |
| rewriter | LLM-based query reformulation | query-optimizer-builder | optional |
| expander | Term expansion module | query-optimizer-builder | optional |
| decomposer | Complex query splitter | query-optimizer-builder | optional |
| reranker | Cross-encoder re-ranking | query-optimizer-builder | optional |
| latency_budget | Time allocation per step | query-optimizer-builder | required |

## Dependency Graph

```
user_query --input--> query_optimizer --output--> optimized_query
optimized_query --consumed_by--> retriever_config (P02)
embedding_config (P01) --informs--> query_optimizer (embedding-aware rewriting)
query_optimizer --evaluated_by--> retrieval_evaluator (P07)
```

## Boundary Table

| query_optimizer IS | query_optimizer IS NOT |
|-------------------|----------------------|
| Query transformation pipeline | A retriever -- retriever executes the search |
| Defines rewriting, expansion, re-ranking | An embedding_config -- embedding configures vectors |
| Pre-retrieval optimization | A knowledge_index -- index configures search structure |
| Latency-budgeted pipeline | A search_strategy -- strategy defines overall search approach |
