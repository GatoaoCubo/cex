---
kind: examples
id: bld_examples_retriever_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of retriever_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Retriever Config"
version: "1.0.0"
author: n03_builder
tags: [retriever_config, builder, examples]
tldr: "Golden and anti-examples for retriever config construction, demonstrating ideal structure and common pitfalls."
domain: "retriever config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: retriever-config-builder
## Golden Example
INPUT: "Create retriever config for hybrid search over knowledge base"
OUTPUT:
```yaml
id: p01_retr_hybrid_knowledge
kind: retriever_config
pillar: P01
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Hybrid Knowledge Base Retriever"
quality: null
tags: [retriever_config, P01, retriever]
tldr: "Hybrid Knowledge Base Retriever — production-ready retriever_config configuration"
```
## Overview
Hybrid retriever combining FAISS dense search with BM25 sparse search for knowledge base queries.
Balances semantic understanding with keyword precision.

## Search Strategy
Algorithm: hybrid (reciprocal rank fusion)
Dense: FAISS cosine similarity on nomic-embed-text vectors.
Sparse: BM25 keyword matching on raw chunk text.
Fusion: RRF with k=60, dense_weight=0.7, sparse_weight=0.3.
Reranker: cross-encoder/ms-marco-MiniLM-L-6-v2 on top 15 candidates.

## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| store_type | faiss | Local, fast, no external dependency |
| top_k | 5 | Balances context window budget with recall |
| search_type | hybrid | Best F1 for mixed query types |
| hybrid_ratio | 0.7 | Dense-weighted; semantic queries dominate |
| fetch_k | 15 | 3x top_k for reranker input |
| reranker | ms-marco-MiniLM-L-6-v2 | Fast cross-encoder, <50ms latency |
| score_threshold | 0.3 | Drops irrelevant results on weak queries |

## Integration
- Input: query string + optional metadata filters
- Output: list of (Document, score) tuples, ranked by relevance
- Upstream: p01_chunk_tech_docs (chunks), p01_emb_nomic (embeddings)
- Downstream: LLM context assembly, RAG prompt injection
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_retr_ pattern (H02 pass)
- kind: retriever_config (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Search Strategy, Parameters, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "retriever_config" (S02 pass)
## Anti-Example
INPUT: "Create retriever for product search"
BAD OUTPUT:
```yaml
id: product-search
kind: retriever
quality: 9.0
tags: [retriever]
```
FAILURES:
1. id has hyphens and no p01_retr_ prefix -> H02 FAIL
2. kind: 'retriever' not 'retriever_config' -> H04 FAIL
3. Missing fields: store_type, top_k, search_type -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. No ## Search Strategy section -> H07 FAIL
6. No parameters table -> S03 FAIL
