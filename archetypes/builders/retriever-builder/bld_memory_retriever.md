---
kind: learning_record
id: bld_memory_retriever
pillar: P12
llm_function: INJECT
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [memory, retriever, P12, RAG, anti-patterns, lessons]
memory_scope: project
observation_types: [user, feedback, project, reference]
density_score: 1.0
title: Memory ISO - retriever
---
# Memory: retriever-builder

## Summary
Embedding model choice and similarity metric alignment are the most critical retriever
decisions — a metric mismatch produces silently degraded results with no error at runtime.
Retriever is downstream of document_loader and upstream of LLM generation: it reads only,
never ingests.

## Patterns (What Works)

| Pattern | Rationale |
|---------|-----------|
| Match metric to model: OpenAI -> cosine, Cohere embed-v3 -> dot_product | Prevents ranking degradation from unnormalized math |
| Hybrid search as default for production RAG | Captures both semantic intent and exact term matching |
| top_k=50 for first-pass when reranking | Cheap retrieval + expensive precision reranking = best quality/cost tradeoff |
| Metadata pre-filter before ANN search | Reduces search space; improves both latency and precision |
| RRF (k=60) as default fusion for hybrid | Stable, parameter-free, works across score scales |
| Separate namespace per document corpus | Prevents cross-corpus contamination in multi-tenant systems |
| Chunk size assumption documented | Downstream LLM context window planning depends on average chunk size |

## Anti-Patterns (What Fails)

| Anti-Pattern | Consequence | Fix |
|-------------|-------------|-----|
| No embedding_model specified | Dimension mismatch at query time breaks silently | Always name model + provider |
| Cosine on unnormalized embeddings | Incorrect ranking; cosine != dot_product for unnormalized vectors | Check model normalization; use dot_product if natively normalized |
| top_k too high without reranking (k > 20) | Noise drowns signal; LLM gets irrelevant context | Add reranker or reduce top_k |
| No metadata filters on large corpus (>100K chunks) | Full collection scan; latency degrades at scale | Define at least 1-2 filterable fields |
| Confusing retriever with search_tool | Wrong builder called; web search artifacts incompatible with local RAG | Retriever = local; search_tool = web |
| Confusing retriever with document_loader | Loader ingests; retriever queries — different P04 kinds | Check kind field; loaders produce chunks, retrievers consume them |
| top_k=1 for generation | Too brittle; single missed retrieval breaks generation | Use k >= 3 for robustness |
| quality != null | Violates HARD gate H04; self-scoring is invalid | Always set quality: null |
| id not matching filename stem | HARD gate H02 failure; breaks pool indexing | id == filename stem, always |
| Body exceeding 2048 bytes | HARD gate H10 failure; retriever artifacts are specs, not docs | Trim to spec essentials only |

## Context
- 2048 byte budget forces spec-only discipline — no implementation code
- Retriever is stateless at query time: reads embeddings, returns chunks
- document_loader -> [embedding store] -> retriever -> LLM (pipeline order)
- Retriever quality directly determines generation quality in RAG systems
- BEIR benchmark: hybrid consistently outperforms pure vector on heterogeneous corpora
- ColBERT late-interaction is more accurate than cross-encoder but slower than Cohere rerank API

## Session Observations
- Users often conflate "retriever" with "web search" — boundary enforcement is critical
- Users often omit embedding_model assuming it is obvious — always ask or specify explicitly
- Hybrid search is underspecified by users — always ask for fusion method preference
