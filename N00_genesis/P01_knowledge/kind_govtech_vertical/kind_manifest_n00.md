---
id: n00_govtech_vertical_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "GovTech Vertical -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, govtech_vertical, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_govtech_vertical
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_action_paradigm
  - bld_schema_usage_report
  - bld_schema_fintech_vertical
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
GovTech Vertical packages domain knowledge for the Government Technology sector: procurement processes, regulatory compliance, digital service standards, and public sector buyer personas. Enables nuclei to generate governance-aware content and analyses for e-government, smart city, and civic technology platforms without repeated domain briefing.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `govtech_vertical` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Vertical name and jurisdiction |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sub_verticals | list | no | Smart city, e-procurement, digital ID, civic AI |
| key_kpis | list | yes | Citizen satisfaction, service digitization %, cost per transaction |
| regulatory | list | yes | LGPD, GDPR, accessibility, public procurement law |
| tech_stack | list | no | Serpro, GOVBR, ServiceNow, Salesforce Public Sector |
| buyer_personas | list | yes | CIO, procurement officer, city manager |

## When to use
- When building solutions for government or public sector clients
- When designing procurement-compliant AI workflows
- When analyzing GovTech market opportunities

## Builder
`archetypes/builders/govtech_vertical-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind govtech_vertical --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N01, N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- government agencies, public sector vendors
- `{{DOMAIN_CONTEXT}}` -- jurisdiction and level of government

## Example (minimal)
```yaml
---
id: govtech_vertical_federal_brazil
kind: govtech_vertical
pillar: P01
nucleus: n01
title: "Federal GovTech Brazil"
version: 1.0
quality: null
---
sub_verticals: [e-procurement, digital-ID, citizen-services]
key_kpis: [service_digitization_pct, citizen_NPS, cost_per_transaction]
regulatory: [LGPD, Lei_8666, decreto_10332]
tech_stack: [GOVBR, Serpro, SIAFI]
buyer_personas: [federal_CIO, procurement_officer]
```

## Related kinds
- `context_doc` (P01) -- broader domain context for government
- `legal_vertical` (P01) -- adjacent legal/regulatory vertical
- `customer_segment` (P02) -- public sector ICPs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_govtech_vertical]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_quickstart_guide]] | downstream | 0.36 |
| [[bld_schema_action_paradigm]] | downstream | 0.36 |
| [[bld_schema_usage_report]] | downstream | 0.35 |
| [[bld_schema_fintech_vertical]] | downstream | 0.35 |
| [[bld_schema_benchmark_suite]] | downstream | 0.35 |
| [[bld_schema_search_strategy]] | downstream | 0.35 |
