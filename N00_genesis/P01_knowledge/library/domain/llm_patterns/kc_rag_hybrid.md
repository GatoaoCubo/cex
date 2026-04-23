---
id: p01_kc_rag_hybrid
kind: knowledge_card
type: domain
pillar: P01
title: "RAG Hybrid — Retrieval-Augmented Generation Patterns"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [rag, retrieval, hybrid, embedding, knowledge-base]
tldr: "Combine retrieval (search knowledge base) with generation (LLM). Hybrid RAG: TF-IDF for structure + embeddings for semantics. Chunking strategies matter."
when_to_use: "Building knowledge-aware LLM systems with external data sources"
keywords: [rag, retrieval, embedding, vector-db, hybrid-search, chunking]
density_score: 0.92
updated: "2026-04-07"
related:
  - n04_rag_pipeline_memory
  - n04_kc_knowledge_management
  - p01_gl_rag
  - graph-rag-config-builder
  - p06_arch_rag_pipeline
  - n04_rc_knowledge
  - bld_collaboration_vector_store
  - atom_21_rag_taxonomy
  - p06_schema_embedding
  - kc_graph_rag_config
---

# RAG Hybrid Patterns

## Core RAG Loop
```
QUERY → RETRIEVE (search KB) → AUGMENT (inject context) → GENERATE (LLM)
```

## Search Strategies

| Strategy | How | Strength |
|----------|-----|----------|
| TF-IDF / BM25 | Keyword frequency matching | Exact terms, structured data |
| Vector/Semantic | Embedding similarity | Meaning, synonyms, concepts |
| Hybrid | BM25 + Vector, combine scores | Best of both worlds |
| Knowledge Graph | Entity + relationship traversal | Structured relationships |

## Chunking Strategies

| Strategy | Chunk Size | Overlap | Use Case |
|----------|-----------|---------|----------|
| Fixed | 500-1000 tokens | 50-100 | General purpose |
| Semantic | By paragraph/section | Headers | Structured docs |
| Sentence window | 1 sentence + N context | Full window | QA systems |
| Parent-child | Section → sub-sections | Hierarchy | Long documents |

## CEX RAG Implementation
1. TF-IDF via `cex_query.py` (covers ~90% of cases)
2. File-based knowledge: `P01_knowledge/library/` (194+ KCs)
3. `cex_memory_select.py` = memory retrieval
4. `compose_prompt()` = the augmentation step
5. No vector DB needed yet — file-based TF-IDF is sufficient at current scale

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_rag_pipeline_memory]] | downstream | 0.37 |
| [[n04_kc_knowledge_management]] | sibling | 0.34 |
| [[p01_gl_rag]] | related | 0.32 |
| [[graph-rag-config-builder]] | related | 0.30 |
| [[p06_arch_rag_pipeline]] | downstream | 0.30 |
| [[n04_rc_knowledge]] | related | 0.28 |
| [[bld_collaboration_vector_store]] | downstream | 0.28 |
| [[atom_21_rag_taxonomy]] | sibling | 0.27 |
| [[p06_schema_embedding]] | downstream | 0.27 |
| [[kc_graph_rag_config]] | sibling | 0.27 |
