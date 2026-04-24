---
id: p01_kc_knowledge_index
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P10
title: "Brain Index — Deep Knowledge for knowledge_index"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: knowledge_index
quality: 9.1
tags: [knowledge_index, P10, INJECT, kind-kc]
tldr: "knowledge_index is the configuration spec for a semantic search index — backend (BM25/FAISS/hybrid), dimensions, hybrid alpha weight, and stale rebuild threshold — scoped to a named domain."
when_to_use: "Building, reviewing, or reasoning about knowledge_index artifacts"
keywords: [vector_index, FAISS, hybrid_search]
feeds_kinds: [knowledge_index]
density_score: null
related:
  - knowledge-index-builder
  - bld_collaboration_knowledge_index
  - bld_knowledge_card_knowledge_index
  - p03_sp_knowledge_index_builder
  - bld_collaboration_embedding_config
  - bld_examples_knowledge_index
  - bld_architecture_knowledge_index
  - p10_bi_organization_brain
  - p10_lr_knowledge-index-builder
  - p04_plug_brain_search
---

# Brain Index

## Spec
```yaml
kind: knowledge_index
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_bi_{{index}}.yaml
core: true
```

## What It Is
A knowledge_index is the configuration spec for a named semantic search index — defining its backend algorithm (BM25, FAISS, or hybrid), embedding dimensions, hybrid alpha weighting, and stale rebuild threshold. It is NOT an embedding_config (P01, which configures the embedding model itself), NOT a rag_source (P01, which is a pointer to an external data source).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `VectorStore` (FAISS, Chroma) | Index backed by embedding store with similarity search |
| LlamaIndex | `VectorStoreIndex` + `StorageContext` | Manages index lifecycle + FAISS/Pinecone backend |
| CrewAI | `embedder` config in `Crew` | Embedding config for knowledge base indexing |
| DSPy | `ColBERTv2` retriever | ColBERT dense index for few-shot and context retrieval |
| Haystack | `DocumentStore` (InMemory, Chroma) | Abstract store with BM25 + embedding query modes |
| OpenAI | `vector_store` resource | Assistants API file_search vector store |
| Anthropic | N/A | No native index; retrieval via MCP brain tool |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| backend | enum | faiss | faiss/bm25/hybrid — hybrid best recall+precision |
| dimensions | int | 768 | Must match embedding_config — mismatch = silent failure |
| hybrid_alpha | float | 0.7 | 0=pure keyword, 1=pure semantic; 0.7 balances both |
| rebuild_on_stale_h | int | 24 | Lower = fresher index; higher = less rebuild overhead |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Hybrid search | Balance recall (BM25) with precision (FAISS) | `hybrid_alpha: 0.7` — default for most domains |
| Stale detection | Auto-rebuild when index diverges from source | `rebuild_on_stale_h: 24` — daily rebuild trigger |
| Scope isolation | Separate indexes per knowledge domain | `brain_main`, `brain_pool`, `brain_agents` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Single global index | All content mixed = precision collapse on large corpora | Scope indexes by domain (agents, pool, knowledge) |
| No stale detection | Index silently diverges from source files | Always set `rebuild_on_stale_h` |
| Dimension mismatch | Wrong dimensions between embedding_config and index | Pin dimensions explicitly; validate on build |

## Integration Graph
```
embedding_config, rag_source --> [knowledge_index] --> retriever_config, agent_card
                                       |
                                  chunk_strategy, env_config, path_config
```

## Decision Tree
- IF recall is priority THEN `hybrid_alpha: 0.5` (balance BM25 + FAISS)
- IF precision is priority THEN `hybrid_alpha: 0.9` (lean semantic)
- IF no GPU or Ollama unavailable THEN `backend: bm25` (fallback, no embeddings)
- DEFAULT: hybrid backend, `alpha: 0.7`, dimensions from embedding_config

## Quality Criteria
- GOOD: backend, dimensions, hybrid_alpha, rebuild_on_stale_h all present
- GREAT: scope isolation documented, fallback backend named, build command included
- FAIL: global index mixing all content, no stale detection, dimension not pinned

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-index-builder]] | related | 0.58 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.49 |
| [[bld_knowledge_card_knowledge_index]] | sibling | 0.48 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.45 |
| [[bld_collaboration_embedding_config]] | downstream | 0.45 |
| [[bld_examples_knowledge_index]] | upstream | 0.43 |
| [[bld_architecture_knowledge_index]] | upstream | 0.41 |
| [[p10_bi_organization_brain]] | related | 0.39 |
| [[p10_lr_knowledge-index-builder]] | related | 0.38 |
| [[p04_plug_brain_search]] | upstream | 0.37 |
