---
id: p01_rs_SOURCE_SLUG
kind: rag_source
8f: F3_inject
pillar: P01
version: 1.0.0
title: "Template — RAG Source"
tags: [template, rag, source, indexing, retrieval]
tldr: "Registers an external source for RAG retrieval. Defines URL, trust level, refresh schedule, chunking hints, and embedding configuration."
url: "[https://source.example/page]"
domain: "[source_domain]"
last_checked: "[YYYY-MM-DD]"
quality: 9.0
updated: "2026-04-07"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.97
related:
  - bld_memory_rag_source
  - bld_collaboration_rag_source
  - atom_21_rag_taxonomy
  - bld_architecture_rag_source
  - rag-source-builder
  - p03_ins_rag_source
  - n01_emb_text_embedding_4
  - embedding-config-builder
  - p06_schema_embedding
  - ex_knowledge_card_rag_fundamentals
---

# RAG Source: [SOURCE_SLUG]

## Source Identity
- **URL**: [https://source.example/page]
- **Domain**: [source_domain]
- **Type**: [docs | api_reference | paper | blog | dataset]
- **Language**: [en | pt-BR | multi]
- **License**: [MIT | CC-BY | proprietary | unknown]

## Trust Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Authority | [high\|med\|low] | [Who publishes this?] |
| Freshness | [high\|med\|low] | [How often updated?] |
| Accuracy | [high\|med\|low] | [Peer reviewed? Production tested?] |
| Relevance | [high\|med\|low] | [How specific to our domain?] |

## Refresh Schedule
- **Checked at**: [YYYY-MM-DD]
- **Refresh rule**: [daily | weekly | monthly | on_change]
- **Staleness threshold**: [30d | 90d | 365d] — re-check after this period

## Indexing Configuration
- **Chunk strategy**: [heading_based | fixed_tokens | semantic]
- **Max tokens per chunk**: [256 | 512 | 1024]
- **Overlap**: [0 | 64 | 128] tokens
- **Embedding model**: [text-embedding-3-small | nomic-embed-text]
- **Embedding dimensions**: [256 | 384 | 768 | 1536]

## Retrieval Hints
- **Search mode**: [keyword | semantic | hybrid]
- **Boost factor**: [1.0 | 1.5 | 2.0] — relative importance vs other sources
- **Filter tags**: [tag1, tag2] — only retrieve chunks matching these tags

## Quality Gate
- [ ] URL is accessible and returns 200
- [ ] Trust rating ≥ medium on at least 3/4 dimensions
- [ ] Chunk strategy matches document structure
- [ ] Refresh schedule defined

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `rag source`
- **Artifact ID**: `p01_rs_SOURCE_SLUG`
- **Tags**: [template, rag, source, indexing, retrieval]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `rag source` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_rag_source]] | downstream | 0.30 |
| [[bld_collaboration_rag_source]] | related | 0.26 |
| [[atom_21_rag_taxonomy]] | related | 0.26 |
| [[bld_architecture_rag_source]] | downstream | 0.25 |
| [[rag-source-builder]] | related | 0.25 |
| [[p03_ins_rag_source]] | related | 0.25 |
| [[n01_emb_text_embedding_4]] | related | 0.24 |
| [[embedding-config-builder]] | related | 0.24 |
| [[p06_schema_embedding]] | downstream | 0.24 |
| [[ex_knowledge_card_rag_fundamentals]] | related | 0.23 |
