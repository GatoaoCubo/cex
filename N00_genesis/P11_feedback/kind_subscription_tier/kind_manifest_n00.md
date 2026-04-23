---
id: n00_subscription_tier_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Subscription Tier -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, subscription_tier, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_pricing_page
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_scoring_rubric
  - bld_schema_sandbox_config
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A subscription_tier defines a SaaS subscription tier with its pricing, feature matrix, usage limits, and upgrade/downgrade logic. It is the canonical definition of a pricing level that content_monetization pipelines, referral_programs, and ROI calculators reference, ensuring consistent commercial logic across all N06 commercial artifacts.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `subscription_tier` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| tier_name | string | yes | Tier label (e.g. free \| starter \| pro \| enterprise) |
| price_monthly | float | yes | Monthly price in base currency |
| price_annual | float | no | Annual price (typically 20% discount from monthly x12) |
| currency | string | yes | ISO 4217 currency code |
| features | array | yes | List of included features with limits |
| usage_limits | object | yes | Resource limits (API calls, seats, storage, etc.) |
| upgrade_triggers | array | no | Usage thresholds that prompt tier upgrade suggestion |

## When to use
- When designing the pricing tiers for a CEX-powered SaaS product
- When updating feature access rules for an existing subscription
- When building the pricing page that references multiple tiers

## Builder
`archetypes/builders/subscription_tier-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind subscription_tier --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: st_cex_pro_tier
kind: subscription_tier
pillar: P11
nucleus: n06
title: "Example Subscription Tier"
version: 1.0
quality: null
---
# Subscription Tier: CEX Pro
tier_name: pro
price_monthly: 97.00
price_annual: 934.00
currency: USD
usage_limits: {api_calls_per_month: 10000, seats: 3, nuclei: 5}
```

## Related kinds
- `content_monetization` (P11) -- monetization pipeline that sells this tier
- `referral_program` (P11) -- referral rewards denominated in tier access
- `enterprise_sla` (P11) -- SLA that applies to enterprise tier customers

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pricing_page]] | upstream | 0.48 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_sandbox_spec]] | upstream | 0.42 |
| [[bld_schema_dataset_card]] | upstream | 0.42 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_scoring_rubric]] | upstream | 0.41 |
| [[bld_schema_sandbox_config]] | upstream | 0.41 |
