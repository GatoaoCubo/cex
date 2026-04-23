---
kind: knowledge_card
id: bld_knowledge_card_rag_source
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for rag_source production — atomic searchable facts
sources: rag-source-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Rag Source"
version: "1.0.0"
author: n03_builder
tags: [rag_source, builder, examples]
tldr: "Golden and anti-examples for rag source construction, demonstrating ideal structure and common pitfalls."
domain: "rag source construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_rag_source
  - bld_schema_rag_source
  - p03_sp_rag_source_builder
  - p11_qg_rag_source
  - rag-source-builder
  - bld_architecture_rag_source
  - bld_memory_rag_source
  - bld_examples_rag_source
  - p01_kc_rag_source
  - bld_collaboration_rag_source
---

# Domain Knowledge: rag_source
## Executive Summary
A rag_source is a pointer-only artifact that catalogs an external indexable URL for RAG pipelines — it records WHERE content lives, not the content itself. Body max is 1024 bytes. If the body contains extracted text paragraphs, the artifact is a knowledge_card, not a rag_source. Two files are always required: `.md` (human-readable) and `.yaml` (machine twin), both sharing the same `id`.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| ID pattern | `^p01_rs_[a-z][a-z0-9_]+$` |
| Required frontmatter fields | 13 (includes `url` and `last_checked`) |
| Recommended fields | 4 (keywords, reliability, format, extraction_method) |
| Max body | 1024 bytes |
| Body sections | 3 (Source Description, Freshness Policy, Extraction Notes) |
| Dual-file artifact | `.md` + `.yaml` twin; IDs must match |
| `quality` field | ALWAYS null |
## Patterns
| Pattern | Rule |
|---------|------|
| Pointer discipline | Body describes metadata about the source; never contains extracted content |
| Dual-file requirement | Both `.md` and `.yaml` required; id must be identical in both |
| Freshness policy | Specify re-check cadence + staleness threshold (e.g., stale after 30 days) |
| `last_checked` update | Must be updated on each URL validation; not synonymous with `created` |
| Reliability levels | `high` = official docs/APIs; `medium` = curated third-party; `low` = informal/social |
| Format field | `html` / `json` / `api` / `pdf` / `csv` — drives extraction_method choice |
| URL preference | `https://` preferred; HTTP must be documented as deliberate exception |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Body contains extracted paragraphs | Wrong kind — this is a knowledge_card, not a rag_source |
| Missing `url` field | Core identifier; HARD gate H06 blocks on absent required fields |
| `last_checked` equals `created` and never updated | Freshness policy is meaningless; indexer cannot determine staleness |
| No `## Freshness Policy` section | Body section is mandatory; artifact fails structural gate |
| Body > 1024 bytes | Violates hard size constraint; artifact is rejected |
| `.md` and `.yaml` twins with mismatched `id` | Schema integrity failure; lookup by ID breaks |
| `reliability` omitted | Downstream retrieval cannot weight source trustworthiness |
## Application
1. Identify the external URL; validate format (`https://`) and reachability
2. Write frontmatter: 13 required fields including `url`, `domain`, `last_checked`; `quality: null`
3. Add recommended fields: `reliability` (high/medium/low), `format`, `extraction_method`, `keywords` (3–8 terms)
4. Write `## Source Description` — what the source is, who maintains it, why it is authoritative
5. Write `## Freshness Policy` — re-check cadence + staleness threshold
6. Write `## Extraction Notes` — method, auth requirements, pagetion quirks
7. Verify body <= 1024 bytes; create `.yaml` machine twin with identical `id`
## References
- rag-source-builder MANIFEST.md v1.0.0
- rag_source SCHEMA.md v1.0.0
- Boundary: rag_source (pointer) vs knowledge_card (distilled content) vs context_doc (domain framing) vs embedding_config (index configuration)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_rag_source]] | related | 0.47 |
| [[bld_schema_rag_source]] | downstream | 0.46 |
| [[p03_sp_rag_source_builder]] | downstream | 0.46 |
| [[p11_qg_rag_source]] | downstream | 0.43 |
| [[rag-source-builder]] | related | 0.42 |
| [[bld_architecture_rag_source]] | downstream | 0.41 |
| [[bld_memory_rag_source]] | downstream | 0.40 |
| [[bld_examples_rag_source]] | downstream | 0.39 |
| [[p01_kc_rag_source]] | sibling | 0.39 |
| [[bld_collaboration_rag_source]] | related | 0.32 |
