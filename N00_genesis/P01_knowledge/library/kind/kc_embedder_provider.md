---
id: p01_kc_embedder_provider
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "Embedder Provider -- Deep Knowledge for embedder_provider"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: embedder_provider
quality: 9.1
tags: [embedder_provider, p01, INJECT, kind-kc, knowledge, rag]
tldr: "Configuration for text-to-vector embedding services -- maps text chunks to dense vectors for semantic retrieval"
when_to_use: "Configuring RAG pipelines, vector stores, or semantic search for CEX knowledge retrieval"
keywords: [embedding, vector, rag, semantic, retrieval, openai, cohere, voyage]
feeds_kinds: [embedder_provider]
density_score: null
related:
  - p01_emb_openai_text_embedding_3_small
  - p03_sp_embedder_provider_builder
  - bld_examples_embedder_provider
  - embedder-provider-builder
  - p01_kc_vector_embedding_model_selection
  - p03_ins_embedder_provider
  - bld_knowledge_card_embedder_provider
  - p01_kc_embedding_config
  - bld_memory_embedder_provider
  - bld_collaboration_embedding_config
---

# Embedder Provider

## Spec
```yaml
kind: embedder_provider
pillar: P01
llm_function: INJECT
max_bytes: 3072
naming: p01_emb_{{provider}}.yaml
core: false
```

## Purpose

An embedder provider config connects CEX's knowledge retrieval system to a specific embedding API. It defines model, dimensions, batch size, and normalization so that `cex_retriever.py` can convert text to vectors consistently.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| provider | Service name | `openai`, `cohere`, `voyage`, `local` |
| model | Embedding model ID | `text-embedding-3-small`, `embed-english-v3.0` |
| dimensions | Vector dimensionality | `1536`, `1024`, `256` |
| max_tokens | Max input tokens per chunk | `8191` |
| batch_size | Chunks per API call | `100` |
| normalize | L2-normalize output vectors | `true` |
| api_key_env | Env var holding the API key | `OPENAI_API_KEY` |

## Key Patterns

1. **Dimension reduction**: Use `dimensions` param (OpenAI v3) to reduce from 1536 to 256 for smaller indexes
2. **Matryoshka**: Models like text-embedding-3 support truncated dimensions natively
3. **Hybrid**: Combine dense (semantic) + sparse (BM25/TF-IDF) for best recall
4. **Local fallback**: sentence-transformers for air-gapped/offline environments

## Anti-Patterns

- Mixing embeddings from different models in one vector store (cosine breaks)
- Not normalizing vectors before cosine similarity (magnitude skews results)
- Embedding entire documents instead of chunks (dilutes semantic signal)
- Using outdated models (ada-002 vs text-embedding-3-small: 5x cheaper, better quality)

## CEX Integration

- `cex_retriever.py` uses TF-IDF currently (2184 docs, 12K vocab)
- `cex_sdk/knowledge/embedders.py` wraps embedding providers
- Future: embedder_provider config feeds cex_retriever for dense retrieval path

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.56 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.48 |
| [[bld_examples_embedder_provider]] | downstream | 0.47 |
| [[embedder-provider-builder]] | downstream | 0.45 |
| [[p01_kc_vector_embedding_model_selection]] | sibling | 0.45 |
| [[p03_ins_embedder_provider]] | downstream | 0.43 |
| [[bld_knowledge_card_embedder_provider]] | sibling | 0.43 |
| [[p01_kc_embedding_config]] | sibling | 0.43 |
| [[bld_memory_embedder_provider]] | downstream | 0.41 |
| [[bld_collaboration_embedding_config]] | downstream | 0.41 |
