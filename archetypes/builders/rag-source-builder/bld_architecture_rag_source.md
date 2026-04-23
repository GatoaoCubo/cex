---
kind: architecture
id: bld_architecture_rag_source
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of rag_source — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Rag Source"
version: "1.0.0"
author: n03_builder
tags: [rag_source, builder, examples]
tldr: "Golden and anti-examples for rag source construction, demonstrating ideal structure and common pitfalls."
domain: "rag source construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - rag-source-builder
  - p01_kc_rag_source
  - p03_sp_rag_source_builder
  - p03_ins_rag_source
  - bld_knowledge_card_rag_source
  - bld_memory_rag_source
  - bld_schema_rag_source
  - bld_architecture_knowledge_index
  - bld_collaboration_rag_source
  - bld_examples_rag_source
---

# Architecture: rag_source in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 5-field required metadata header (id, kind, url, domain, last_checked) | rag-source-builder | active |
| url_reference | Validated URL pointing to the external data source | author | active |
| freshness_policy | Re-check schedule and staleness conditions | author | active |
| reliability_score | Confidence rating of the source (high/medium/low) | author | active |
| format_type | Data format of the source (html, json, api, pdf, csv) | author | active |
| domain_tags | Searchable tags linking source to knowledge domains | author | active |
## Dependency Graph
```
external_source  --tracked_by-->  rag_source  --consumed_by-->  ingestion_pipeline
rag_source       --produces-->    knowledge_card  --indexed_by--> knowledge_index
rag_source       --signals-->     freshness_alert
```
| From | To | Type | Data |
|------|----|------|------|
| external_source (web) | rag_source | data_flow | URL and metadata of the authoritative source |
| rag_source | ingestion_pipeline | consumes | pipeline reads URL to fetch and process content |
| rag_source | knowledge_card (P01) | produces | distilled content extracted from the source |
| rag_source | knowledge_index (P01) | data_flow | source metadata indexed for retrieval |
| rag_source | freshness_alert (P12) | signals | emitted when source exceeds staleness threshold |
| embedding_config (P01) | rag_source | dependency | embedding settings for indexing source content |
## Boundary Table
| rag_source IS | rag_source IS NOT |
|---------------|-------------------|
| A pointer to an external indexable source with URL and freshness | Distilled content from the source (knowledge_card P01) |
| Lightweight (max 1024 bytes) — metadata only, no body content | A domain context document (context_doc P01) |
| Tracked for freshness with re-check schedule | An embedding configuration (embedding_config P01) |
| Rated by reliability (high/medium/low) | A scraper with CSS selectors (scraper P04) |
| Scoped to one URL per artifact | A search index or vector store |
| Consumed by ingestion pipelines for content extraction | A static snapshot of content at a point in time |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | external_source, url_reference | Identify the authoritative external data |
| Metadata | frontmatter, format_type, domain_tags, reliability_score | Classify and rate the source |
| Freshness | freshness_policy, freshness_alert | Monitor staleness and trigger re-checks |
| Ingestion | ingestion_pipeline, embedding_config | Fetch, process, and embed source content |
| Output | knowledge_card, knowledge_index | Distilled content and search index entries |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[rag-source-builder]] | upstream | 0.51 |
| [[p01_kc_rag_source]] | upstream | 0.50 |
| [[p03_sp_rag_source_builder]] | upstream | 0.49 |
| [[p03_ins_rag_source]] | upstream | 0.48 |
| [[bld_knowledge_card_rag_source]] | upstream | 0.43 |
| [[bld_memory_rag_source]] | downstream | 0.41 |
| [[bld_schema_rag_source]] | upstream | 0.37 |
| [[bld_architecture_knowledge_index]] | sibling | 0.37 |
| [[bld_collaboration_rag_source]] | upstream | 0.36 |
| [[bld_examples_rag_source]] | upstream | 0.34 |
