---
id: n00_pricing_page_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Pricing Page -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, pricing_page, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_pricing_page
  - pricing-page-builder
  - bld_instruction_pricing_page
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_pitch_deck
  - bld_schema_usage_report
  - bld_architecture_pricing_page
  - bld_examples_pricing_page
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Pricing page produces a conversion-optimized pricing artifact with tier comparison table, feature matrix, FAQ, and CTAs. It communicates value differentiation between tiers, anchors on the recommended plan, and addresses the most common pricing objections. Output can be a standalone HTML page or a content block embedded in the main site.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `pricing_page` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Product name + "Pricing" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| tiers | list | yes | Pricing tier definitions with name, price, features |
| recommended_tier | string | yes | Tier name to highlight as "most popular" |
| billing_options | list | yes | monthly / annual / usage-based |
| enterprise_cta | string | no | CTA for custom enterprise pricing |
| faq_items | list | yes | Pricing objection FAQ (minimum 5 items) |

## When to use
- Launching a new pricing model or tier structure
- A/B testing pricing page copy, tier names, or feature gate positioning
- Building a standalone pricing page for a specific campaign or audience segment

## Builder
`archetypes/builders/pricing_page-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind pricing_page --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N06 commercial designs tiers; N02 marketing writes copy
- `{{SIN_LENS}}` -- Strategic Greed: maximize ARPU while minimizing churn
- `{{TARGET_AUDIENCE}}` -- buyers evaluating purchase decision at the bottom of funnel
- `{{DOMAIN_CONTEXT}}` -- tier feature sets, competitive price anchoring, target margins

## Example (minimal)
```yaml
---
id: pricing_page_cex_saas
kind: pricing_page
pillar: P05
nucleus: n06
title: "CEX Platform Pricing"
version: 1.0
quality: null
---
tiers:
  - {name: Starter, price: "$0/mo", features: [3 nuclei, 50 builds/mo]}
  - {name: Pro, price: "$99/mo", features: [7 nuclei, unlimited builds]}
recommended_tier: Pro
billing_options: [monthly, annual]
```

## Related kinds
- `landing_page` (P05) -- links to pricing page from the main CTA
- `content_monetization` (P11) -- pricing strategy that informs tier design
- `pitch_deck` (P05) -- business model slide references pricing page structure

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pricing_page]] | downstream | 0.53 |
| [[pricing-page-builder]] | related | 0.39 |
| [[bld_instruction_pricing_page]] | upstream | 0.38 |
| [[bld_schema_reranker_config]] | downstream | 0.37 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_pitch_deck]] | downstream | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.36 |
| [[bld_architecture_pricing_page]] | downstream | 0.36 |
| [[bld_examples_pricing_page]] | downstream | 0.36 |
| [[bld_schema_search_strategy]] | downstream | 0.36 |
