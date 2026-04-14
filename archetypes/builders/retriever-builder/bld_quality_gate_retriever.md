---
id: p11_qg_retriever
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [quality_gate, retriever, P11, validation, RAG, vector-search]
tldr: "10 HARD gates block delivery. 12 SOFT dimensions score 0-10. Threshold 7.0."
density_score: 1.0
title: Quality Gate ISO - retriever
---
# Gate: retriever

## Definition
- Metric: composite score 0-10
- Threshold: >= 7.0 to deliver
- HARD gates: block delivery regardless of score
- SOFT gates: contribute to composite score

## HARD Gates (all must pass — any failure blocks delivery)

| ID | Check | Fail Action |
|----|-------|-------------|
| H01 | YAML frontmatter parses without errors | Fix syntax |
| H02 | id matches `^p04_retr_[a-z][a-z0-9_]+$` AND equals filename stem | Fix id or rename file |
| H03 | kind == "retriever" (exact string) | Fix kind field |
| H04 | quality == null (not a number, not absent) | Remove numeric score |
| H05 | All required fields present: id, name, store_type, embedding_model, similarity_metric, top_k | Add missing fields |
| H06 | store_type is valid enum: chroma, pinecone, faiss, qdrant, weaviate, milvus, elasticsearch, costm | Fix to valid value |
| H07 | embedding_model is a non-empty string | Specify model name |
| H08 | similarity_metric is valid enum: cosine, dot_product, euclidean, manhattan | Fix to valid value |
| H09 | top_k >= 1 (integer) | Fix to positive integer |
| H10 | Body byte count <= 2048 (sections only, excludes frontmatter) | Trim content |

## SOFT Scoring (12 dimensions, each 0-1, sum * 10/12)

| ID | Dimension | Weight | Criteria |
|----|-----------|--------|----------|
| S01 | store_coverage | 1.0 | store_type matches real backend; version/tier noted if relevant |
| S02 | embedding_model_docs | 1.0 | model name, provider, dimension size documented |
| S03 | similarity_justification | 1.0 | metric choice explained relative to embedding model |
| S04 | hybrid_strategy | 0.8 | if hybrid: fusion method (RRF/weighted) and alpha specified |
| S05 | reranking_config | 0.8 | reranker null OR model named with trigger condition |
| S06 | metadata_filter_docs | 0.8 | filters listed with field names and types |
| S07 | namespace_scoping | 0.7 | namespace/collection specified or explicitly "default" |
| S08 | integration_docs | 1.0 | SDK/library named, auth pattern, connection string format |
| S09 | boundary_clarity | 1.0 | explicitly states what this is NOT (web search, ingestion, SQL) |
| S10 | domain_specificity | 0.9 | use case context clear; not generic "search documents" |
| S11 | testsbility | 0.8 | enough info to write a retrieval test (store + model + k) |
| S12 | error_handling | 0.5 | notes fallback behavior if store unavailable or score below threshold |

## Scoring Tiers

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Pool as golden artifact |
| >= 8.0 | Skilled | Pool + remember pattern |
| >= 7.0 | Learning | Deliver with notes |
| < 7.0 | Rejected | Revise before delivery |

## Bypass
No bypass for HARD gates. SOFT gate threshold may be reduced to 6.0 only when:
- Prototype/draft explicitly requested by user
- store_type is "costm" with acknowledged unknowns
Document bypass reason in artifact description field.
