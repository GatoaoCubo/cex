---
kind: collaboration
id: bld_collaboration_rag_source
pillar: P01
llm_function: COLLABORATE
purpose: How rag-source-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Rag Source"
version: "1.0.0"
author: n03_builder
tags: [rag_source, builder, examples]
tldr: "Golden and anti-examples for rag source construction, demonstrating ideal structure and common pitfalls."
domain: "rag source construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_knowledge_card
  - bld_collaboration_knowledge_index
  - bld_collaboration_citation
  - bld_collaboration_embedding_config
  - bld_memory_rag_source
  - bld_collaboration_builder
  - bld_collaboration_context_doc
  - rag-source-builder
  - bld_collaboration_retriever_config
  - bld_collaboration_knowledge_graph
---

# Collaboration: rag-source-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "where can we find authoritative external data for this domain?"
I catalog external URLs with freshness policies and reliability scores — pointer only, no content body. I do not distill content, write domain context, or configure embeddings.
## Crew Compositions
### Crew: "Knowledge Ingestion Pipeline"
```
  1. rag-source-builder       -> "pointer to external URL with freshness policy and reliability score"
  2. knowledge-card-builder   -> "distilled content extracted from the indexed source"
  3. knowledge-index-builder      -> "search index built over the knowledge cards"
```
### Crew: "RAG-Augmented Agent Stack"
```
  1. rag-source-builder       -> "catalog of authoritative sources to query at runtime"
  2. embedding-config-builder -> "embedding model and chunking config for the sources"
  3. context-doc-builder      -> "domain context document assembled from retrieved chunks"
  4. prompt-template-builder  -> "template with {{context}} slot filled by retrieval"
```
### Crew: "Research Domain Setup"
```
  1. rag-source-builder       -> "5-10 authoritative sources for the domain"
  2. scraper-builder          -> "scraper config targeting the cataloged URLs"
  3. knowledge-card-builder   -> "distilled cards from scraped content"
```
## Handoff Protocol
### I Receive
- seeds: domain name, target URL(s), required freshness (daily/weekly/monthly), reliability expectation
- optional: existing source catalog to extend, format hints (html/json/api/pdf/csv), auth notes
### I Produce
- rag_source artifact (YAML frontmatter only, pointer with no content body, max 1024 bytes)
- committed to: `cex/P01/examples/p01_rs_{domain}_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- None required. I am a primary producer — I only need a URL and domain name from the task request.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| knowledge-card-builder | Uses my source pointers to know where to retrieve and distill content |
| embedding-config-builder | Configures embeddings scoped to the sources I catalog |
| scraper-builder | Targets the URLs I register for scheduled crawling |
| knowledge-index-builder | Indexes content retrieved from my registered sources |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_card]] | sibling | 0.48 |
| [[bld_collaboration_knowledge_index]] | sibling | 0.43 |
| [[bld_collaboration_citation]] | sibling | 0.42 |
| [[bld_collaboration_embedding_config]] | sibling | 0.41 |
| [[bld_memory_rag_source]] | downstream | 0.40 |
| [[bld_collaboration_builder]] | sibling | 0.38 |
| [[bld_collaboration_context_doc]] | sibling | 0.37 |
| [[rag-source-builder]] | related | 0.37 |
| [[bld_collaboration_retriever_config]] | sibling | 0.36 |
| [[bld_collaboration_knowledge_graph]] | sibling | 0.35 |
