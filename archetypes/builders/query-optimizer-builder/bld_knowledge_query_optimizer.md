---
kind: knowledge_card
id: bld_knowledge_query_optimizer
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for query_optimizer production -- search query rewriting and optimization
sources: query expansion literature, HyDE, query decomposition, re-ranking, LlamaIndex query engines
quality: null
title: "Query Optimizer Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, knowledge]
tldr: "Domain knowledge for query optimizers: rewriting, expansion, decomposition, HyDE, and re-ranking strategies."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_query_optimizer
  - bld_schema_query_optimizer
---

# Domain Knowledge: query_optimizer

## Executive Summary

Query optimizers transform raw user queries into optimized retrieval queries that improve search precision and recall. They apply techniques like query rewriting, expansion, decomposition, hypothetical document embedding (HyDE), and re-ranking. A query_optimizer is a P01 artifact -- it defines the OPTIMIZATION STRATEGY, not the retrieval engine or index.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Techniques | rewriting, expansion, decomposition, HyDE, step-back, re-ranking |
| Placement | Between user query and retrieval engine |
| Key trade-off | Precision vs latency (more optimization = better results but slower) |

## Patterns

- **Query rewriting** -- LLM reformulates ambiguous queries into precise retrieval queries
- **Query expansion** -- adds synonyms, related terms, or alternate phrasings to increase recall
- **Query decomposition** -- splits complex multi-part queries into atomic sub-queries
- **HyDE** -- generates a hypothetical answer, then uses it as the retrieval query; improves semantic matching
- **Step-back prompting** -- generates a broader question first, retrieves general context, then answers specific
- **Re-ranking** -- retrieves top-N results with fast retriever, re-ranks with cross-encoder for precision

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| No optimization | Raw user queries miss relevant documents due to vocabulary mismatch |
| Over-expansion | Too many terms dilute query intent; precision drops |
| No latency budget | Each optimization step adds latency; unbounded pipeline is unusable |
| Single strategy | Different query types need different optimization paths |
| No fallback | Optimization failure should fall back to raw query, not error |
