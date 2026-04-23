---
kind: collaboration
id: bld_collaboration_embedding_config
pillar: P12
llm_function: COLLABORATE
purpose: How embedding-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_knowledge_index
  - bld_collaboration_embedder_provider
  - bld_collaboration_retriever_config
  - bld_collaboration_knowledge_card
  - bld_collaboration_vector_store
  - knowledge-index-builder
  - embedding-config-builder
  - bld_architecture_embedding_config
  - bld_collaboration_rag_source
  - bld_collaboration_memory_scope
---

# Collaboration: embedding-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which embedding model, with what parameters, for this RAG pipeline?"
I do not build search indexes. I do not create knowledge content.
I configure embedding models so vector search systems produce accurate representations.
## Crew Compositions
### Crew: "RAG Pipeline Setup"
```
  1. embedding-config-builder -> "embedding model parameters (dimensions, chunk, distance)"
  2. knowledge-index-builder -> "search index configuration"
  3. knowledge-card-builder -> "content to embed and index"
```
### Crew: "Vector Infrastructure"
```
  1. embedding-config-builder -> "model config (provider, dimensions, tokenizer)"
  2. knowledge-index-builder -> "FAISS/BM25 index using embedding config"
  3. benchmark-builder -> "retrieval quality measurement"
```
## Handoff Protocol
### I Receive
- seeds: use case (search, similarity, clustering), content domain
- optional: provider preference, dimension constraints, cost budget, batch size
### I Produce
- embedding_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P01/examples/p01_embedding_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Embedding configs are defined from requirements.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| knowledge-index-builder | Needs embedding dimensions and distance metric for index config |
| benchmark-builder | Measures retrieval quality using configured embeddings |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_index]] | sibling | 0.65 |
| [[bld_collaboration_embedder_provider]] | sibling | 0.53 |
| [[bld_collaboration_retriever_config]] | sibling | 0.52 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.48 |
| [[bld_collaboration_vector_store]] | sibling | 0.47 |
| [[knowledge-index-builder]] | upstream | 0.46 |
| [[embedding-config-builder]] | upstream | 0.46 |
| [[bld_architecture_embedding_config]] | upstream | 0.43 |
| [[bld_collaboration_rag_source]] | sibling | 0.41 |
| [[bld_collaboration_memory_scope]] | sibling | 0.40 |
