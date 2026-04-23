---
kind: collaboration
id: bld_collaboration_knowledge_index
pillar: P12
llm_function: COLLABORATE
purpose: How knowledge-index-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_embedding_config
  - knowledge-index-builder
  - bld_collaboration_knowledge_card
  - bld_collaboration_memory_scope
  - bld_collaboration_retriever_config
  - bld_collaboration_rag_source
  - bld_collaboration_context_doc
  - bld_collaboration_vector_store
  - bld_collaboration_knowledge_graph
  - bld_collaboration_embedder_provider
---

# Collaboration: knowledge-index-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how is content indexed and searched for retrieval?"
I do not configure embedding models. I do not create content.
I define search index configuration so retrieval systems can find content efficiently.
## Crew Compositions
### Crew: "RAG Pipeline Setup"
```
  1. embedding-config-builder -> "embedding model parameters"
  2. knowledge-index-builder -> "search index configuration (BM25/FAISS/hybrid)"
  3. knowledge-card-builder -> "content to be indexed"
```
### Crew: "Knowledge Infrastructure"
```
  1. knowledge-index-builder -> "index configuration and ranking strategies"
  2. glossary-entry-builder -> "term definitions for query expansion"
  3. context-doc-builder -> "domain context for scope boundaries"
```
## Handoff Protocol
### I Receive
- seeds: content scope, search algorithm preference (BM25, FAISS, hybrid)
- optional: rebuild schedule, ranking weights, filter rules
### I Produce
- knowledge_index artifact (.md + .yaml frontmatter)
- committed to: `cex/P10/examples/p10_knowledge_index_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- embedding-config-builder: provides embedding model parameters for vector search
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| knowledge-card-builder | Content must conform to index scope for discoverability |
| context-doc-builder | Domain docs are indexed via knowledge_index configuration |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_embedding_config]] | sibling | 0.64 |
| [[knowledge-index-builder]] | upstream | 0.55 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.53 |
| [[bld_collaboration_memory_scope]] | sibling | 0.43 |
| [[bld_collaboration_retriever_config]] | sibling | 0.43 |
| [[bld_collaboration_rag_source]] | sibling | 0.43 |
| [[bld_collaboration_context_doc]] | sibling | 0.38 |
| [[bld_collaboration_vector_store]] | sibling | 0.38 |
| [[bld_collaboration_knowledge_graph]] | sibling | 0.38 |
| [[bld_collaboration_embedder_provider]] | sibling | 0.38 |
