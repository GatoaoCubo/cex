---
kind: collaboration
id: bld_collaboration_vector_store
pillar: P02
llm_function: COLLABORATE
purpose: How vector-store-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Vector Store"
version: "1.0.0"
author: n03_builder
tags: [vector_store, builder, examples]
tldr: "Golden and anti-examples for vector store construction, demonstrating ideal structure and common pitfalls."
domain: "vector store construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_embedder_provider
  - bld_collaboration_embedding_config
  - bld_collaboration_retriever_config
  - bld_collaboration_retriever
  - bld_collaboration_model_provider
  - vector-store-builder
  - bld_collaboration_knowledge_graph
  - bld_collaboration_builder
  - bld_collaboration_knowledge_index
  - bld_collaboration_model_card
---

# Collaboration: vector-store-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should we store and index vectors for this RAG pipeline?"
I produce storage and indexing configurations for vector databases with backend connection details, dimension contracts, HNSW parameters, namespace strategies, and lifecycle operations. I do NOT handle embedding models (embedder-provider-builder), LLM routing (model-provider-builder), retrieval pipelines (retriever-builder), or chunking strategies (chunker-config-builder).
## Crew Compositions
### Crew: "Build RAG Pipeline from Scratch"
```
  1. embedder-provider-builder  -> "embedding model config: provider, dimensions, normalization"
  2. vector-store-builder   -> "vector storage config: backend, index, distance metric"
  3. chunker-config-builder     -> "chunking strategy: size, overlap, splitter type"
  4. retriever-builder          -> "retrieval pipeline: query, rerank, hybrid search"
  5. rag-source-builder         -> "document source: URLs, formats, refresh schedule"
```
### Crew: "Upgrade TF-IDF to Vector Search"
```
  1. embedder-provider-builder  -> "embedding model replacing TF-IDF similarity"
  2. vector-store-builder   -> "vector index replacing inverted index"
  3. retriever-builder          -> "new retrieval pipeline with vector similarity"
```
### Crew: "Scale Vector Storage"
```
  1. vector-store-builder   -> "migration config from local (FAISS) to cloud (Pinecone)"
  2. lens-builder               -> "cost/performance perspective for backend selection"
  3. scoring-rubric-builder     -> "scores backends against latency, cost, scale criteria"
```
### Crew: "Multi-Domain Knowledge Base"
```
  1. vector-store-builder   -> "namespace strategy for domain isolation"
  2. embedder-provider-builder  -> "shared embedding model across domains"
  3. rag-source-builder         -> "per-domain document sources"
  4. retriever-builder          -> "cross-domain or scoped retrieval"
```
## Handoff Protocol
### I Receive
- seeds: backend name, dimensions from embedder_provider (minimum required)
- optional: expected scale (vector count), deployment target (local/cloud), latency requirements
### I Produce
- vector_store artifact (YAML, 22+ frontmatter fields, index config, namespace strategy)
- committed to: `cex/P01_knowledge/examples/p01_vdb_{backend}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| Builder | Why |
|---------|-----|
| embedder-provider-builder | MUST receive dimensions and normalization flag to set dimension contract and distance metric |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| retriever-builder        | needs collection name, connection, and query interface |
| rag-source-builder       | needs collection target for document ingestion |
| agent-package-builder    | includes vector_store as a deploy dependency |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_embedder_provider]] | sibling | 0.72 |
| [[bld_collaboration_embedding_config]] | sibling | 0.47 |
| [[bld_collaboration_retriever_config]] | sibling | 0.46 |
| [[bld_collaboration_retriever]] | sibling | 0.44 |
| [[bld_collaboration_model_provider]] | sibling | 0.43 |
| [[vector-store-builder]] | related | 0.42 |
| [[bld_collaboration_knowledge_graph]] | sibling | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_collaboration_knowledge_index]] | sibling | 0.38 |
| [[bld_collaboration_model_card]] | sibling | 0.36 |
