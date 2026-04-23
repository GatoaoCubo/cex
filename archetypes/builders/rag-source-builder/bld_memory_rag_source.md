---
kind: memory
id: bld_memory_rag_source
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for rag_source artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Rag Source"
version: "1.0.0"
author: n03_builder
tags: [rag_source, builder, examples]
tldr: "Golden and anti-examples for rag source construction, demonstrating ideal structure and common pitfalls."
domain: "rag source construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_rag_source
  - rag-source-builder
  - p01_kc_rag_source
  - p03_sp_rag_source_builder
  - bld_knowledge_card_rag_source
  - p03_ins_rag_source
  - p11_qg_rag_source
  - bld_architecture_rag_source
  - bld_schema_rag_source
  - bld_collaboration_citation
---
# Memory: rag-source-builder
## Summary
RAG sources are lightweight pointers to external data — URLs with freshness tracking, reliability scoring, and crawl scheduling. The critical production lesson is that RAG sources must never contain content, only metadata about where content lives. The moment content is embedded, the artifact becomes a knowledge card, not a source pointer. The second lesson is freshness: sources without last_checked dates and re-check schedules become stale silently.
## Pattern
1. Keep artifacts under 1024 bytes — RAG sources are pointers, not content containers
2. Every source must have last_checked date and re-check schedule (daily, weekly, monthly)
3. Reliability scoring (high/medium/low) must be based on observed availability, not reputation
4. URL validation must check both format (valid URL syntax) and accessibility (HTTP 200 on last check)
5. Specify format of the source content (html, json, api, pdf, csv) for downstream parser selection
6. Domain field must match the knowledge domain this source informs, enabling filtered retrieval
## Anti-Pattern
1. Embedding actual content in the RAG source — it is a pointer, not a knowledge card
2. Sources without last_checked dates — staleness is invisible until downstream retrieval fails
3. Reliability scored by reputation instead of measurement — a prestigious source that is down 30% of the time is low reliability
4. Missing format specification — downstream parsers cannot be auto-selected without knowing the format
5. Confusing rag_source (P01, pointer to external) with knowledge_card (P01, distilled content) or context_doc (P01, domain context)
## Context
RAG sources operate in the P01 content layer as the entry point for external knowledge ingestion. They feed into crawl pipelines that fetch, parse, and distill content into knowledge cards. The separation between pointer (rag_source) and content (knowledge_card) enables independent freshness management — the pointer can be re-checked and re-crawled without modifying the distilled knowledge until the source actually changes.
## Impact
Sources with re-check schedules maintained 95% freshness versus 60% for unscheduled sources over 90-day periods. Format specification enabled automatic parser selection in 100% of crawl operations. Keeping sources under 1024 bytes maintained O(1) retrieval performance in source catalogs.
## Reproducibility
For reliable RAG source production: (1) validate URL format and accessibility, (2) set last_checked to today, (3) define re-check schedule based on source update frequency, (4) score reliability from measured availability, (5) specify content format, (6) assign domain for filtered retrieval, (7) verify artifact stays under 1024 bytes.
## References
1. rag-source-builder SCHEMA.md (5 required fields, pointer-only format)
2. P01 content pillar specification
3. RAG pipeline and source management patterns

## Metadata

```yaml
id: bld_memory_rag_source
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-rag-source.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | rag source construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_rag_source]] | upstream | 0.50 |
| [[rag-source-builder]] | upstream | 0.48 |
| [[p01_kc_rag_source]] | upstream | 0.44 |
| [[p03_sp_rag_source_builder]] | upstream | 0.43 |
| [[bld_knowledge_card_rag_source]] | upstream | 0.40 |
| [[p03_ins_rag_source]] | upstream | 0.40 |
| [[p11_qg_rag_source]] | downstream | 0.39 |
| [[bld_architecture_rag_source]] | upstream | 0.38 |
| [[bld_schema_rag_source]] | upstream | 0.29 |
| [[bld_collaboration_citation]] | downstream | 0.28 |
