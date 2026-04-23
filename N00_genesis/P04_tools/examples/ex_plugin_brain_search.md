---
id: p04_plug_brain_search
kind: plugin
name: brain_search_plugin
version: 1.0.0
entrypoint: organization_brain.vector_search
capabilities: [keyword_search, vector_search, hybrid_fusion, index_rebuild]
repository: internal
license: proprietary
keywords: [bm25, faiss, ollama, nomic, hybrid-search]
pillar: P04
created: 2026-03-24
author: builder_agent
quality: 9.1
tags: [plugin, search, bm25, faiss, vector, semantic]
updated: "2026-04-07"
domain: "tool integration"
title: "Plugin Brain Search"
density_score: 0.92
tldr: "Defines plugin for plugin brain search, with validation gates and integration points."
related:
  - p10_bi_organization_brain
  - bld_knowledge_card_knowledge_index
  - knowledge-index-builder
  - p01_rs_brain_faiss_index
  - p04_mcp_organization_brain
  - p01_kc_knowledge_index
  - bld_examples_component_map
  - bld_examples_knowledge_index
  - bld_examples_instruction
  - p01_rc_hybrid_rag
---

# Plugin: brain_search

## Purpose
1. Extends: organization-brain MCP server
2. Adds: Hybrid retrieval (BM25 keyword + FAISS semantic fusion)
3. Does not own: Index storage format, embedding model selection

## Integration
| Field | Value |
|-------|-------|
| Entrypoint | `organization_brain.vector_search` |
| Inputs | query string, scope filter, k results |
| Outputs | ranked chunks with scores and source paths |
| Dependencies | ollama (nomic-embed-text), faiss-cpu |

## Lifecycle
1. Load: Import BM25 pre-built index (~50ms) + FAISS index (~2s) on server boot
2. Execute: Parallel BM25 + FAISS search, score fusion via weighted sum (0.4 keyword + 0.6 vector)
3. Unload: Indexes stay in memory until server shutdown (LRU cache for queries)

## Failure Handling
1. Retry: None (stateless queries, instant response)
2. Fallback: Ollama unavailable = BM25-only mode (~50% accuracy vs ~88% hybrid)
3. Audit: Query count + cache hit rate via brain_status tool

## Specs
| Component | Detail |
|-----------|--------|
| BM25 index | Pre-built, ~5ms/query, keyword matching |
| FAISS index | nomic-embed-text 768d, ~150ms/query, ~140MB on disk |
| Fusion | Weighted: 0.4 BM25 + 0.6 FAISS, top-k merge |
| Rebuild | `python build_indexes_ollama.py --scope all` (~20 min) |
| Cache | LRU 100 entries, tracks hit rate |

## Metadata

```yaml
id: p04_plug_brain_search
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p04-plug-brain-search.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_bi_organization_brain]] | downstream | 0.55 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.50 |
| [[knowledge-index-builder]] | downstream | 0.47 |
| [[p01_rs_brain_faiss_index]] | related | 0.46 |
| [[p04_mcp_organization_brain]] | related | 0.43 |
| [[p01_kc_knowledge_index]] | downstream | 0.43 |
| [[bld_examples_component_map]] | related | 0.43 |
| [[bld_examples_knowledge_index]] | downstream | 0.40 |
| [[bld_examples_instruction]] | downstream | 0.39 |
| [[p01_rc_hybrid_rag]] | upstream | 0.37 |
