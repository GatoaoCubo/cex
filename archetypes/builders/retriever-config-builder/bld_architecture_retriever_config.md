---
kind: architecture
id: bld_architecture_retriever_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of retriever_config — inventory, dependencies, and architectural position
quality: 9.2
title: "Architecture Retriever Config"
version: "1.0.0"
author: n03_builder
tags: [retriever_config, builder, examples]
tldr: "Golden and anti-examples for retriever config construction, demonstrating ideal structure and common pitfalls."
domain: "retriever config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_chunk_strategy
  - p03_sp_retriever_config_builder
  - bld_examples_retriever_config
  - retriever-config-builder
  - bld_output_template_retriever_config
  - p10_lr_retriever_config_builder
  - bld_instruction_retriever_config
  - bld_knowledge_card_retriever_config
  - p11_qg_retriever_config
  - retriever-builder
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| store_type | Vector store backend (faiss, chroma, pinecone, weaviate) | retriever_config | required |
| top_k | Number of results to return | retriever_config | required |
| search_type | Search algorithm (dense, sparse, hybrid) | retriever_config | required |
| hybrid_ratio | Weight between dense and sparse (0.0-1.0) | retriever_config | optional |
| reranker | Cross-encoder model for result reranking | external | optional |
| filters | Metadata filters applied before search | retriever_config | optional |
| chunk_strategy | Chunking config that produced the indexed documents | P01 | upstream |
| embedding_config | Vector model used to encode queries | P01 | upstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| store_type | retriever_config | produces | Vector store backend (faiss, chroma, pinecone, weaviate) |
| top_k | retriever_config | produces | Number of results to return |
| search_type | retriever_config | produces | Search algorithm (dense, sparse, hybrid) |
| hybrid_ratio | retriever_config | produces | Weight between dense and sparse (0.0-1.0) |
| reranker | external | produces | Cross-encoder model for result reranking |
| filters | retriever_config | produces | Metadata filters applied before search |
| chunk_strategy | P01 | depends | Chunking config that produced the indexed documents |
| embedding_config | P01 | depends | Vector model used to encode queries |
## Boundary Table
| retriever_config IS | retriever_config IS NOT |
|-------------|----------------|
| Retrieval parameters — how to search and rank chunks from a vector/hybrid store | embedding_config (vector model) |
| Not embedding_config | embedding_config (vector model) |
| Not chunk_strategy | chunk_strategy (splitting) |
| Not knowledge_card | knowledge_card (content) |
| Not knowledge_index | knowledge_index (index infra) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | store_type, top_k, search_type | Define the artifact's core parameters |
| optional | hybrid_ratio, reranker, filters | Extend with recommended fields |
| external | chunk_strategy, embedding_config | Upstream/downstream connections |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_retriever_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-retriever-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_chunk_strategy]] | sibling | 0.51 |
| [[p03_sp_retriever_config_builder]] | upstream | 0.51 |
| [[bld_examples_retriever_config]] | upstream | 0.44 |
| [[retriever-config-builder]] | upstream | 0.44 |
| [[bld_output_template_retriever_config]] | upstream | 0.37 |
| [[p10_lr_retriever_config_builder]] | downstream | 0.37 |
| [[bld_instruction_retriever_config]] | upstream | 0.37 |
| [[bld_knowledge_card_retriever_config]] | upstream | 0.35 |
| [[p11_qg_retriever_config]] | downstream | 0.34 |
| [[retriever-builder]] | upstream | 0.32 |
