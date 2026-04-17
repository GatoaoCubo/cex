---
kind: examples
id: bld_examples_reranker_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of reranker_config artifacts
quality: 8.8
title: "Examples Reranker Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [reranker_config, builder, examples]
tldr: "Golden and anti-examples of reranker_config artifacts"
domain: "reranker_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
---
model: "rerank-english-v2.0"
provider: "Cohere"
strategy: "cross-encoder"
parameters:
  top_k: 10
  temperature: 0.7
---
Reranker config for Cohere's English reranking model. Uses cross-encoder strategy to re-score top 10 candidates from initial retrieval. Temperature controls softmax sharpness during scoring.
```

## Anti-Example 1: Confusing retriever and reranker models
```yaml
---
model: "BM25"
provider: "Elasticsearch"
strategy: "vector-similarity"
parameters:
  top_k: 100
---
```
## Why it fails
BM25 is a first-stage retrieval model, not a reranker. Reranker configs must use models trained for re-scoring, not initial document retrieval. Strategy "vector-similarity" is also inappropriate for reranking.

## Anti-Example 2: Missing essential strategy definition
```yaml
---
model: "cross-encoder/ms-marco-MiniLM-2-4"
provider: "HuggingFace"
parameters:
  top_k: 5
---
```
## Why it fails
The config lacks a "strategy" field which is required for reranking. Without specifying how the model will re-score documents (e.g., "cross-encoder", "dot-product"), the system cannot execute reranking logic properly.
