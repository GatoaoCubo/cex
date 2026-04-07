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
