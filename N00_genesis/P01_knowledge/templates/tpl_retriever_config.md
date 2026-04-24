---
id: p01_retriever_config
kind: retriever_config
8f: F3_inject
pillar: P01
version: 1.0.0
title: "Template — Retriever Config"
tags: [template, retriever, rag, search, vector]
tldr: "Configures how the retrieval engine searches and ranks chunks. Defines search mode, top-k, reranking, filters, and fallback chains for RAG pipelines."
quality: 9.0
related:
  - p04_retriever_NAME
  - n04_rc_knowledge
  - bld_knowledge_card_retriever_config
  - p01_kc_retriever
  - retriever-builder
  - bld_architecture_retriever
  - bld_instruction_retriever
  - bld_memory_retriever
  - bld_examples_retriever_config
  - p10_lr_retriever_config_builder
---

# Retriever Configuration

## Purpose
Controls how queries are matched against indexed chunks. A retriever config sits between the user query and the vector store, defining search strategy, ranking, and filtering.

## Configuration
```yaml
id: p01_rc_[RETRIEVER_NAME]
kind: retriever_config
search_mode: [semantic | keyword | hybrid]
top_k: [5 | 10 | 20]
similarity_threshold: [0.7 | 0.75 | 0.8]
rerank: [none | cross_encoder | llm]
max_tokens_context: [2048 | 4096 | 8192]
```

## Search Modes

| Mode | How It Works | Best For |
|------|-------------|----------|
| semantic | Cosine similarity on embeddings | Conceptual queries |
| keyword | BM25 / TF-IDF text matching | Exact term lookup |
| hybrid | Weighted sum of semantic + keyword | General purpose (default) |

## Ranking Pipeline
```
Query → Embed → Vector Search (top_k * 3) → Filter → Rerank (top_k) → Context Window
```
1. **Embed**: Convert query to vector using same model as indexing
2. **Vector Search**: Retrieve 3x `top_k` candidates (over-fetch for reranking)
3. **Filter**: Apply metadata filters (tags, source, date)
4. **Rerank**: Score candidates with cross-encoder or LLM, keep `top_k`
5. **Context Window**: Concatenate top chunks, truncate to `max_tokens_context`

## Filter Configuration
```yaml
filters:
  - field: source_type
    operator: in
    values: [docs, api_reference]
  - field: last_updated
    operator: gte
    value: "2025-01-01"
  - field: trust_level
    operator: in
    values: [high, medium]
```

## Fallback Chain
When primary retrieval returns no results above threshold:
1. Relax `similarity_threshold` by 0.1
2. Switch from `semantic` to `hybrid`
3. Remove metadata filters
4. Return "no relevant context found" disclaimer

## Quality Gate
- [ ] `top_k` ≤ 20 (context window budget)
- [ ] `similarity_threshold` ≥ 0.6 (avoid noise)
- [ ] Reranking model matches embedding model family
- [ ] Fallback chain defined (at least 2 levels)
- [ ] `max_tokens_context` ≤ LLM context window / 3

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_retriever_NAME]] | downstream | 0.53 |
| [[n04_rc_knowledge]] | sibling | 0.40 |
| [[bld_knowledge_card_retriever_config]] | related | 0.39 |
| [[p01_kc_retriever]] | related | 0.38 |
| [[retriever-builder]] | downstream | 0.36 |
| [[bld_architecture_retriever]] | downstream | 0.35 |
| [[bld_instruction_retriever]] | downstream | 0.35 |
| [[bld_memory_retriever]] | downstream | 0.34 |
| [[bld_examples_retriever_config]] | downstream | 0.33 |
| [[p10_lr_retriever_config_builder]] | downstream | 0.32 |
