---
kind: knowledge_card
id: bld_knowledge_card_subscription_tier
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for subscription_tier production
quality: 9.2
title: "Knowledge Card Subscription Tier"
version: "1.0.0"
author: n03_builder
tags: [subscription_tier, builder, knowledge_card]
tldr: "SaaS subscription tier domain knowledge: Stripe/Chargebee billing contracts, monetization units, feature matrices, NRR / expansion MRR, and grandfathering discipline."
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_memory_subscription_tier
  - p03_sp_subscription_tier_builder
  - p11_qg_subscription_tier
  - bld_schema_subscription_tier
  - p08_pat_pricing_framework
  - kc_ai_saas_monetization
  - subscription-tier-builder
  - hybrid_review5_n03
  - p04_ex_content_monetization_saas
  - bld_instruction_subscription_tier
---

## Domain Overview
Subscription tiers are the structural unit of SaaS monetization: each tier is a priced bundle of features with a recurring billing cadence. Effective tier design balances simplicity (3-4 tiers max to avoid decision fatigue) with price discrimination across customer segments. Industry systems of record -- Stripe Billing, Chargebee, Recurly, Paddle, Zuora -- impose a canonical contract: an integer `unit_amount` in the smallest currency unit, an ISO 4217 `currency`, a `recurring.interval` in {day, week, month, year}, and an `interval_count`. Tier artifacts that deviate from these semantics break multi-region billing, tax calculation, and proration.

Beyond mechanics, tier design governs two SaaS metrics that determine enterprise value: Net Revenue Retention (NRR, target >= 110%) and Gross Revenue Retention (GRR, target >= 90%). Tiers drive NRR through expansion hooks: seat growth (per_seat models), usage growth (per_usage), and upgrade paths (tier -> tier). Bessemer's "State of the Cloud" and OpenView's SaaS Benchmarks publish these thresholds annually.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| Monetization Unit | The axis of value capture: flat, per_seat, per_usage, or hybrid. | OpenView SaaS Pricing Benchmarks (annual) |
| Feature Matrix | Table mapping features to tiers with `{included, quota, addon_price}` cells. | Stripe Billing product docs |
| Price Object (Stripe) | `{unit_amount, currency, recurring.interval, interval_count}` canonical shape. | Stripe API reference (`/v1/prices`) |
| Net Revenue Retention (NRR) | MRR retained and expanded from a cohort over 12 months. Target >= 110%. | Bessemer "State of the Cloud" |
| Expansion MRR | Incremental MRR from existing customers via seat / usage / upgrade growth. | OpenView SaaS Benchmarks |
| Grandfathering | Keeping legacy customers on old pricing/features after a tier change. | Stripe, Chargebee product docs |
| Proration Behavior | How mid-cycle plan changes are billed. Stripe values: none, create_prorations, always_invoice. | Stripe API (`proration_behavior`) |
| ARPU / ARPA | Average Revenue Per User / Account. | Standard SaaS metric (SaaStr, KeyBanc) |
| Churn Rate | Percentage of customers canceling per period. Logo vs revenue churn distinct. | KeyBanc SaaS Survey |
| Seat Expansion | Growth within a tier via additional licensed users (drives NRR for per_seat). | Salesforce, Slack, Linear playbooks |
| Annual Discount | Incentive to prepay; industry norm 15-25% vs monthly. | OpenView, ProfitWell data |
| Sample Ratio in Pricing Tests | Guardrail when A/B testing prices -- SRM invalidates conclusions. | Kohavi et al. (2020) "Trustworthy Online Controlled Experiments" |

## Industry Standards
- Stripe Billing API (`/v1/prices`, `/v1/products`, `/v1/subscriptions`) -- de-facto price object contract.
- Chargebee Plans API -- plan, addon, coupon, entitlement model.
- Recurly Plans & Add-ons -- tier + add-on + coupon decomposition.
- Paddle Billing -- Merchant-of-Record semantics (tax_behavior, geo pricing).
- Zuora Billing -- enterprise rate plan + charge model.
- ISO 4217 -- currency codes (mandatory for price.currency).
- Gartner Magic Quadrant: Subscription Management -- vendor landscape.
- OpenView SaaS Benchmarks -- NRR, GRR, CAC payback norms.

## Common Patterns
1. **3-4 tier ceiling** -- Starter, Growth/Pro, Business, Enterprise. More than 4 triggers decision fatigue (data: ProfitWell).
2. **Seat-based for collaboration tools** (Slack, Linear, Notion) -- seat count drives expansion MRR naturally.
3. **Usage-based for APIs/infra** (OpenAI, Stripe, AWS) -- meter + included quota + overage price.
4. **Hybrid (platform + usage)** (Zendesk, Intercom) -- flat platform fee + per-seat or per-conversation.
5. **Annual discount 15-25%** -- pulls cash forward, lifts retention.
6. **Enterprise = custom** -- "Contact us" pricing with negotiated contract; tier is a shell.

## Pitfalls
- **Medal naming** (Bronze/Silver/Gold): buyers self-select by outcome ("I'm a team", "I run a business"), not by metal.
- **Floating-point prices** (9.99): breaks Stripe, rounds wrong in multi-currency, fails exact-cents accounting.
- **Missing grandfathering**: legal risk + mass churn when live tier is repriced without lock.
- **Overlap collapse**: Pro and Enterprise differ only by "support SLA" -> buyers negotiate to Pro.
- **No expansion hooks**: flat tier with no seat/usage/upgrade path caps NRR below 100%.
- **Ignoring proration**: mid-cycle upgrades over-bill or lose revenue -- pick `create_prorations` and document.
- **Tax opacity**: omitting `tax_behavior` breaks EU VAT / US sales-tax compliance.
- **No sunset plan**: every tier accumulates debt -- design deprecation from day one.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_subscription_tier]] | downstream | 0.59 |
| [[p03_sp_subscription_tier_builder]] | downstream | 0.48 |
| [[p11_qg_subscription_tier]] | downstream | 0.42 |
| [[bld_schema_subscription_tier]] | downstream | 0.40 |
| [[p08_pat_pricing_framework]] | downstream | 0.35 |
| [[kc_ai_saas_monetization]] | sibling | 0.33 |
| [[subscription-tier-builder]] | downstream | 0.32 |
| [[hybrid_review5_n03]] | sibling | 0.30 |
| [[p04_ex_content_monetization_saas]] | downstream | 0.29 |
| [[bld_instruction_subscription_tier]] | downstream | 0.29 |
