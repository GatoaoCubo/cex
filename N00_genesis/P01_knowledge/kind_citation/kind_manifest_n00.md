---
id: n00_citation_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Citation -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, citation, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_citation
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_app_directory_entry
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_voice_pipeline
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Citation provides structured source attribution with full provenance: URL, access date, author, reliability score, and license. It ensures every knowledge claim in the CEX system can be traced to a verifiable source, supporting auditability and grounding of LLM outputs. Citations are injected into knowledge cards and intelligence reports.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `citation` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Short reference label |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| url | string | yes | Canonical URL of the source |
| accessed_date | date | yes | ISO 8601 date when source was accessed |
| author | string | no | Author(s) of the source |
| publication | string | no | Journal, website, or publisher name |
| reliability | enum | yes | high\|medium\|low -- source credibility assessment |
| license | string | no | Content license (e.g., CC-BY, proprietary) |

## When to use
- When a knowledge_card or intelligence report cites external evidence
- When grounding RAG outputs with verifiable provenance
- When building an auditable research corpus

## Builder
`archetypes/builders/citation-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind citation --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N01 or N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- researchers, auditors, compliance teams
- `{{DOMAIN_CONTEXT}}` -- research domain or industry vertical

## Example (minimal)
```yaml
---
id: citation_anthropic_claude_pricing_2026
kind: citation
pillar: P01
nucleus: n01
title: "Anthropic Claude Pricing 2026"
version: 1.0
quality: null
---
url: https://www.anthropic.com/pricing
accessed_date: 2026-04-17
author: Anthropic
reliability: high
license: proprietary
```

## Related kinds
- `knowledge_card` (P01) -- atomic facts that embed citations
- `competitive_matrix` (P01) -- battle cards that require cited data
- `rag_source` (P01) -- indexed sources that generate citations

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dataset_card]] | downstream | 0.48 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.47 |
| [[bld_schema_citation]] | downstream | 0.46 |
| [[bld_schema_benchmark_suite]] | downstream | 0.44 |
| [[bld_schema_search_strategy]] | downstream | 0.44 |
| [[bld_schema_usage_report]] | downstream | 0.44 |
| [[bld_schema_app_directory_entry]] | downstream | 0.44 |
| [[bld_schema_integration_guide]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.43 |
| [[bld_schema_voice_pipeline]] | downstream | 0.43 |
