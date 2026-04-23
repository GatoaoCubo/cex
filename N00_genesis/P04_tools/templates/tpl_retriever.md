---
id: p04_retriever_NAME
kind: retriever
pillar: P04
version: 1.0.0
title: "Template — Retriever"
tags: [template, retriever, rag, search, tool]
tldr: "A retriever tool that fetches relevant documents from a vector store or search index. Configures search strategy, ranking, filtering, and context assembly."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.98
related:
  - p01_retriever_config
  - p01_kc_retriever
  - bld_instruction_retriever
  - retriever-builder
  - bld_architecture_retriever
  - n04_rc_knowledge
  - p08_dir_rag_pipeline
  - p03_sp_retriever_builder
  - bld_memory_retriever
  - bld_knowledge_card_retriever_config
---

# Retriever: [NAME]

## Purpose
[WHAT knowledge this retriever accesses — domain docs, code, conversations]

## Configuration
```yaml
store: [supabase_vectors | pinecone | chromadb | qdrant]
embedding_model: [text-embedding-3-small | nomic-embed-text]
dimensions: [256 | 384 | 768 | 1536]
search_mode: [semantic | keyword | hybrid]
top_k: [5 | 10 | 20]
similarity_threshold: [0.7 | 0.75 | 0.8]
```

## Search Pipeline
```
Query → Embed(query) → Search(store, top_k*3) → Filter → Rerank(top_k) → Format
```

| Stage | Tool | Config |
|-------|------|--------|
| Embed | [MODEL] | dimensions=[N] |
| Search | [STORE] | top_k=[N], threshold=[F] |
| Filter | metadata | [FILTER_RULES] |
| Rerank | [cross_encoder \| none] | model=[MODEL] |
| Format | context_builder | max_tokens=[N] |

## Filter Rules
```yaml
filters:
  - field: kind
    op: in
    values: [knowledge_card, example]
  - field: updated
    op: gte
    value: "2025-01-01"
```

## Context Assembly
Format retrieved chunks for LLM consumption:
```
## Retrieved Context ({N} sources)
### Source 1: {title} (score: {similarity})
{chunk_text}
### Source 2: {title} (score: {similarity})
{chunk_text}
```
**Max context tokens**: [4096] — truncate lowest-scored chunks first

## Error Handling
- **Store unavailable**: Return empty context + warning flag
- **No results above threshold**: Relax threshold by 0.1, retry once
- **Embedding API error**: Cache recent queries, serve from cache

## Quality Gate
- [ ] Store and embedding model specified
- [ ] top_k and threshold configured
- [ ] Filter rules defined (not searching everything)
- [ ] Context assembly format documented

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_retriever_config]] | upstream | 0.46 |
| [[p01_kc_retriever]] | upstream | 0.34 |
| [[bld_instruction_retriever]] | upstream | 0.33 |
| [[retriever-builder]] | related | 0.32 |
| [[bld_architecture_retriever]] | downstream | 0.31 |
| [[n04_rc_knowledge]] | related | 0.30 |
| [[p08_dir_rag_pipeline]] | downstream | 0.29 |
| [[p03_sp_retriever_builder]] | related | 0.27 |
| [[bld_memory_retriever]] | downstream | 0.26 |
| [[bld_knowledge_card_retriever_config]] | upstream | 0.26 |
