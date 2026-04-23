---
kind: collaboration
id: bld_collaboration_retriever
pillar: P13
llm_function: COLLABORATE
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [collaboration, retriever, P13, RAG, crew, handoff]
density_score: 1.0
title: Collaboration ISO - retriever
related:
  - bld_collaboration_retriever_config
  - bld_architecture_kind
  - bld_collaboration_builder
  - bld_collaboration_vector_store
  - kind-builder
  - bld_collaboration_search_tool
  - bld_collaboration_embedder_provider
  - bld_collaboration_knowledge_card
  - bld_collaboration_agent
  - bld_collaboration_document_loader
---
# Collaboration: retriever-builder

## My Role in Crews
SPECIALIST — I handle VECTOR/HYBRID SEARCH DEFINITION.
I own: store_type, embedding_model, similarity_metric, search_type, top_k, reranker,
metadata_filters, namespace.
I do NOT own: web search (search-tool-builder), file ingestion (document-loader-builder),
SQL queries (db-connector-builder), REST calls (api-client-builder).

## Crew Compositions

### RAG Pipeline (most common)
```
document-loader-builder -> retriever-builder -> [agent-builder | instruction-builder]
```
- document-loader-builder: defines chunking strategy, embedding storage
- retriever-builder: defines how to query what was stored
- agent-builder: orchestrates retrieval + generation
- Dependency: retriever MUST know store_type and embedding_model from document-loader output

### Knowledge System
```
knowledge-card-builder + retriever-builder -> agent-builder
```
- knowledge-card-builder: structures domain knowledge
- retriever-builder: provides search interface over knowledge store

### Hybrid Augmented RAG
```
document-loader-builder -> retriever-builder + search-tool-builder -> fusion-builder -> agent-builder
```
- retriever-builder: local knowledge (private docs)
- search-tool-builder: live web search (public information)
- fusion-builder: merges local + web results

### Evaluation Crew
```
retriever-builder -> benchmark-builder -> e2e-eval-builder
```
- benchmark-builder: defines BEIR-style eval dataset
- e2e-eval-builder: runs recall@k, MRR, NDCG metrics

## Handoff Protocol

### I Receive From document-loader-builder:
```yaml
store_type: chroma          # which backend was used for ingestion
embedding_model: text-embedding-3-small  # MUST match retriever exactly
collection_name: my_docs    # namespace to query
chunk_size: 512             # for context window planning
metadata_schema: [source, date, category]  # available filter fields
```

### I Produce For agent-builder / instruction-builder:
```yaml
retriever_id: p04_retr_{store_slug}
search_type: hybrid
top_k: 10
reranker: null | model_name
metadata_filters: [field1, field2]
sdk_reference: langchain.QdrantRetriever | llama_index.VectorStoreIndex
```

## Builders I Depend On

| Builder | What I Need | Dependency Type |
|---------|-------------|-----------------|
| document-loader-builder | store_type, embedding_model, collection schema | HARD — must match exactly |
| embedding-config-builder | embedding model name, dimensions, provider | SOFT — can specify independently |

## Builders That Depend On Me

| Builder | What They Take | Usage |
|---------|---------------|-------|
| agent-builder | retriever_id, SDK reference | Agent wires retriever into tool belt |
| instruction-builder | retrieval step spec | Instructions reference retriever by id |
| chain-builder | retriever artifact | Chain wires retriever -> generator |
| dag-builder | retriever node | DAG includes retrieval as pipeline step |
| e2e-eval-builder | retriever config | Eval harness tests retrieval quality |

## Conflict Resolution
If embedding_model in retriever does not match document-loader artifact: BLOCK — raise
conflict before producing artifact. Dimension mismatch is a silent failure that corrupts
retrieval quality at runtime. Always align with document-loader-builder output first.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_retriever_config]] | sibling | 0.43 |
| [[bld_architecture_kind]] | upstream | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_collaboration_vector_store]] | sibling | 0.36 |
| [[kind-builder]] | upstream | 0.36 |
| [[bld_collaboration_search_tool]] | sibling | 0.35 |
| [[bld_collaboration_embedder_provider]] | sibling | 0.34 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.34 |
| [[bld_collaboration_agent]] | sibling | 0.34 |
| [[bld_collaboration_document_loader]] | sibling | 0.32 |
