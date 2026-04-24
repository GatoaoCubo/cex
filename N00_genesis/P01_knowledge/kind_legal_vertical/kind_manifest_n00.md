---
id: n00_legal_vertical_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Legal Vertical -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, legal_vertical, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_legal_vertical
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_govtech_vertical
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_data_residency
  - bld_schema_tts_provider
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Legal Vertical packages domain knowledge for the Legal Technology sector: legal practice areas, court system structures, regulatory frameworks, contract lifecycle management, and legal buyer personas. Enables nuclei to generate jurisdiction-aware and compliance-sensitive content for law firms, in-house legal teams, and LegalTech platforms.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `legal_vertical` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Vertical name and jurisdiction |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| practice_areas | list | yes | Corporate, litigation, IP, labor, tax |
| key_kpis | list | yes | Matter cost, billing realization, client NPS |
| regulatory | list | yes | OAB, LGPD, CPC, CLT, applicable codes |
| jurisdiction | string | yes | Primary legal system (Civil Law, Common Law) |
| buyer_personas | list | yes | General Counsel, law firm partner, compliance officer |

## When to use
- When building LegalTech solutions or AI tools for legal professionals
- When generating jurisdiction-aware contract or compliance content
- When analyzing legal market opportunities

## Builder
`archetypes/builders/legal_vertical-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind legal_vertical --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N01, N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- legal professionals, LegalTech operators
- `{{DOMAIN_CONTEXT}}` -- jurisdiction and practice area

## Example (minimal)
```yaml
---
id: legal_vertical_corporate_brazil
kind: legal_vertical
pillar: P01
nucleus: n01
title: "Corporate Law Brazil"
version: 1.0
quality: null
---
practice_areas: [corporate, M_and_A, contracts, compliance]
key_kpis: [matter_cost, billing_realization, client_satisfaction]
regulatory: [Lei_SA, CPC, LGPD, CVM_instructions]
jurisdiction: Civil Law (Romano-Germanic)
buyer_personas: [general_counsel, M_and_A_partner]
```

## Related kinds
- `govtech_vertical` (P01) -- government regulatory overlap
- `context_doc` (P01) -- broader legal domain context
- `customer_segment` (P02) -- legal ICPs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_legal_vertical]] | downstream | 0.57 |
| [[bld_schema_integration_guide]] | downstream | 0.44 |
| [[bld_schema_reranker_config]] | downstream | 0.41 |
| [[bld_schema_govtech_vertical]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | downstream | 0.41 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_quickstart_guide]] | downstream | 0.40 |
| [[bld_schema_data_residency]] | downstream | 0.40 |
| [[bld_schema_tts_provider]] | downstream | 0.40 |
| [[bld_schema_usage_report]] | downstream | 0.39 |
