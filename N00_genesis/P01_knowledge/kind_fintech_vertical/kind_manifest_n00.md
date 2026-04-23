---
id: n00_fintech_vertical_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Fintech Vertical -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, fintech_vertical, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_fintech_vertical
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_action_paradigm
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_voice_pipeline
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Fintech Vertical packages domain knowledge for the Financial Technology sector: regulatory frameworks, core KPIs, buyer personas, risk management terminology, and technology stack patterns. Enables nuclei to generate compliance-aware content and analyses for banking, payments, lending, and investment platforms without repeated domain briefing.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `fintech_vertical` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Vertical name and geography |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sub_verticals | list | no | Payments, lending, WealthTech, InsurTech |
| key_kpis | list | yes | TPV, take rate, NPL ratio, CAC, LTV |
| regulatory | list | yes | PCI-DSS, AML, KYC, PSD2, BACEN, CVM |
| tech_stack | list | no | Stripe, Adyen, Open Banking APIs |
| buyer_personas | list | yes | CFO, CTO, compliance officer, retail customer |

## When to use
- When building agents or content for financial services clients
- When analyzing fintech market segments or pricing models
- When generating compliance-aware documentation or workflows

## Builder
`archetypes/builders/fintech_vertical-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind fintech_vertical --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N01, N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- fintech operators, compliance teams
- `{{DOMAIN_CONTEXT}}` -- geography and financial sub-sector

## Example (minimal)
```yaml
---
id: fintech_vertical_payments_brazil
kind: fintech_vertical
pillar: P01
nucleus: n01
title: "Payments Fintech Brazil"
version: 1.0
quality: null
---
sub_verticals: [payments, open-banking]
key_kpis: [TPV, take_rate, chargeback_rate]
regulatory: [BACEN, PIX_rules, LGPD]
tech_stack: [Pagar.me, EBANX, Open Finance Brazil]
buyer_personas: [e-commerce_merchant, bank_CTO]
```

## Related kinds
- `ecommerce_vertical` (P01) -- adjacent vertical for merchant payments
- `context_doc` (P01) -- broader fintech domain context
- `customer_segment` (P02) -- ICPs within fintech

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_fintech_vertical]] | downstream | 0.50 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[bld_schema_reranker_config]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
| [[bld_schema_action_paradigm]] | downstream | 0.38 |
| [[bld_schema_quickstart_guide]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
| [[bld_schema_voice_pipeline]] | downstream | 0.37 |
| [[bld_schema_benchmark_suite]] | downstream | 0.37 |
