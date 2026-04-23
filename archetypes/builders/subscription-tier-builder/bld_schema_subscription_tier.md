---
kind: schema
id: bld_schema_subscription_tier
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for subscription_tier
quality: 9.2
title: "Schema Subscription Tier"
version: "1.0.0"
author: n03_builder
tags: [subscription_tier, builder, schema]
tldr: "Canonical SaaS subscription tier schema aligned with Stripe Billing, Chargebee, Recurly, and Paddle plan contracts."
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_eval_metric
  - bld_schema_audit_log
  - bld_schema_app_directory_entry
  - bld_schema_multimodal_prompt
  - bld_schema_nps_survey
  - bld_schema_usage_report
---

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "subscription_tier" | Fixed value |
| pillar | string | yes | "P11" | Fixed value |
| title | string | yes | null | Human-readable tier name (Starter, Pro, Business, Enterprise) |
| version | string | yes | "1.0.0" | Semantic versioning |
| created | date | yes | null | ISO 8601 |
| updated | date | yes | null | ISO 8601 |
| author | string | yes | null | Product/pricing owner |
| domain | string | yes | null | Product line |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for search |
| tldr | string | yes | null | Who this tier is for + why in one line |
| tier_name | string | yes | null | Free-form tier name (outcome-driven: Starter/Growth/Scale; not Bronze/Silver/Gold) |
| monetization_unit | string | yes | null | "flat" \| "per_seat" \| "per_usage" \| "hybrid" |
| price | object | yes | {} | `{unit_amount: <int cents>, currency: <ISO 4217>, interval: <day\|week\|month\|year>, interval_count: <int>}` (Stripe canonical) |
| feature_matrix | list | yes | [] | Rows: `{feature, included, quota, addon_price}` |

### Recommended
| Field | Type | Notes |
|---|---|---|
| trial_policy | object | `{duration_days, payment_required, auto_convert}` |
| grandfathering_policy | object | `{price_lock_months, feature_freeze, migration_offer}` -- required when replacing a live tier |
| seat_limit | integer | Max users (per_seat / hybrid tiers); null = unlimited |
| usage_limits | object | `{metric, included_quota, overage_price}` per metered unit |
| expansion_mrr | object | `{upgrade_to, add_on_catalog, seat_expansion_price}` |
| proration_behavior | string | "none" \| "create_prorations" \| "always_invoice" (Stripe values) |
| tax_behavior | string | "inclusive" \| "exclusive" \| "unspecified" |
| annual_discount_pct | number | Discount when `interval=year` vs `interval=month`; 15-25% industry norm |
| deprecation | object | `{status: active\|legacy\|sunset, sunset_date, successor_tier}` |

## ID Pattern
`^p11_st_[a-z][a-z0-9_]+\.yaml$`

## Body Structure
1. **Audience** -- target customer segment and JTBD.
2. **Pricing** -- Stripe-canonical price object + annual discount.
3. **Monetization Unit** -- flat / per_seat / per_usage / hybrid + rationale.
4. **Feature Matrix** -- explicit rows, no prose lists.
5. **Trial & Conversion** -- trial_policy, upgrade path, proration.
6. **Grandfathering** -- legacy protection when this tier replaces another.
7. **Expansion Design** -- how customers grow within and across tiers (expansion MRR).

## Constraints
- File size <= 3072 bytes.
- `price.unit_amount` MUST be an integer in smallest currency unit (cents, not dollars). Reject `9.99`; accept `999`.
- `price.currency` MUST be ISO 4217 3-letter code.
- `price.interval` MUST be one of `{day, week, month, year}` (Stripe canonical -- no "quarterly").
- `monetization_unit` MUST be one of `{flat, per_seat, per_usage, hybrid}`.
- `feature_matrix` MUST be non-empty; every row needs `{feature, included}` at minimum.
- `grandfathering_policy` REQUIRED when `deprecation.status in {legacy, sunset}`.
- Tier names MUST NOT use medal metaphors (Bronze/Silver/Gold/Platinum) -- use outcome language.
- Quality field MUST be null (peer review assigns).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.61 |
| [[bld_schema_reranker_config]] | sibling | 0.60 |
| [[bld_schema_benchmark_suite]] | sibling | 0.60 |
| [[bld_schema_sandbox_spec]] | sibling | 0.59 |
| [[bld_schema_eval_metric]] | sibling | 0.57 |
| [[bld_schema_audit_log]] | sibling | 0.57 |
| [[bld_schema_app_directory_entry]] | sibling | 0.57 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.56 |
| [[bld_schema_nps_survey]] | sibling | 0.56 |
| [[bld_schema_usage_report]] | sibling | 0.56 |
