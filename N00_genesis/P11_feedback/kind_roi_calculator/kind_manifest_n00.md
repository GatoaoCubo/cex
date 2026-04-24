---
id: n00_roi_calculator_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "ROI Calculator -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, roi_calculator, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_roi_calculator
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - bld_schema_pricing_page
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_nps_survey
  - bld_schema_integration_guide
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An roi_calculator specifies the inputs, formulas, and TCO (Total Cost of Ownership) comparison methodology for calculating return on investment from a CEX deployment or product. It transforms financial assumptions into computable models that support enterprise sales, pricing decisions, and internal investment justification.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `roi_calculator` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| inputs | array | yes | Financial input variables (cost, volume, price) with types and defaults |
| formulas | array | yes | Named calculation formulas with LaTeX or pseudocode expressions |
| tco_components | array | yes | Cost components (license, compute, implementation, training) |
| comparison_baseline | string | yes | What the ROI is compared against (manual process, competitor) |
| payback_period_formula | string | yes | Formula to compute months until breakeven |
| currency | string | yes | ISO 4217 currency code (e.g. USD, EUR, BRL) |

## When to use
- When building sales materials that quantify CEX value for enterprise prospects
- When justifying infrastructure spend against productivity gains
- When designing pricing tiers that align with demonstrable customer ROI

## Builder
`archetypes/builders/roi_calculator-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind roi_calculator --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: roi_cex_enterprise_deployment
kind: roi_calculator
pillar: P11
nucleus: n06
title: "Example ROI Calculator"
version: 1.0
quality: null
---
# ROI Calculator: CEX Enterprise Deployment
comparison_baseline: "Manual knowledge management + 3 FTE researchers"
currency: USD
tco_components: [license, compute, onboarding]
payback_period_formula: "implementation_cost / monthly_savings"
```

## Related kinds
- `content_monetization` (P11) -- monetization pipeline whose ROI this calculator measures
- `subscription_tier` (P11) -- tier pricing informed by this ROI model
- `enterprise_sla` (P11) -- SLA commitments that affect ROI calculation inputs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_roi_calculator]] | upstream | 0.56 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.48 |
| [[bld_schema_reranker_config]] | upstream | 0.46 |
| [[bld_schema_pricing_page]] | upstream | 0.46 |
| [[bld_schema_dataset_card]] | upstream | 0.46 |
| [[bld_schema_usage_report]] | upstream | 0.46 |
| [[bld_schema_benchmark_suite]] | upstream | 0.45 |
| [[bld_schema_nps_survey]] | upstream | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_search_strategy]] | upstream | 0.44 |
