---
kind: memory
id: bld_memory_subscription_tier
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for subscription_tier artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Subscription Tier"
version: "1.0.0"
author: n03_builder
tags: [subscription_tier, builder, memory]
tldr: "Golden and anti-patterns for SaaS subscription tier construction: Stripe-aligned billing intervals, feature matrix rows, grandfathering explicit, expansion MRR designed-in."
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
---
# Memory: subscription-tier-builder

## Summary
Tiers fail when they mirror the pricing page instead of modeling billing reality. The most common defect is ambiguous billing_interval (silently monthly when customer expected annual -> chargebacks). The second is absent grandfathering: a price change breaks legacy contracts and triggers mass churn. The third is feature creep across tiers: Pro and Enterprise become indistinguishable, collapsing ARPU.

## Pattern
1. Use Stripe/Chargebee/Paddle canonical fields: price.unit_amount (cents), price.currency (ISO 4217), price.recurring.interval (day/week/month/year), price.recurring.interval_count, tax_behavior (inclusive/exclusive).
2. Model billing_interval + interval_count together. "Every 3 months" = interval=month, interval_count=3 (Stripe semantics), not a custom "quarterly" string.
3. Feature_matrix is a table: rows = features, columns = tiers, cells = {included, quota, addon_price}. No prose feature lists.
4. Model monetization unit: per_seat (Slack, Linear), per_usage (Stripe, OpenAI), hybrid (Zendesk), flat (Basecamp). Tier_type field mandatory.
5. Grandfathering_policy is REQUIRED: specify price_lock (months), feature_freeze (yes/no), migration_offer. Salesforce/HubSpot have written grandfathering playbooks.
6. Design expansion_mrr hooks: upgrade_path_to (next tier id), add_on_catalog, seat_expansion_price. 30-40% of SaaS revenue is expansion -- treat it as first-class.
7. Include trial_policy (duration_days, payment_required, auto_convert) and proration_behavior (none/create_prorations/always_invoice per Stripe).

## Evidence
Stripe Billing API schema and Chargebee plan docs are the de-facto industry contract for subscription models. Bessemer's "10 Laws of Cloud" and OpenView's SaaS Benchmarks report confirm: (a) 3-4 tier ceiling, (b) annual-over-monthly discount 15-25%, (c) net revenue retention >= 110% is the expansion-MRR target. Gartner (Magic Quadrant: Subscription Management) names Zuora, Chargebee, Recurly, Stripe Billing, Paddle as canonical systems.

## Pitfalls
- **Hardcoded free tier (H06-style)**: not all SaaS are freemium (Salesforce, HubSpot Enterprise, Notion Business) -- free tier is a GTM choice, not a schema constraint.
- **Bronze/Silver/Gold naming**: metaphor-driven tiers lose to outcome-driven (Starter/Growth/Scale, Solo/Team/Business) because customers self-select by role not medal.
- **Feature overlap collapse**: Pro and Enterprise differ by "support SLA only" -> buyers negotiate down to Pro.
- **Currency as string**: "USD$9.99" instead of {amount: 999, currency: "USD"} breaks multi-region billing.
- **Tax opacity**: ignoring tax_behavior causes EU VAT compliance failures.
- **Plan change without proration policy**: mid-cycle upgrades either over-charge or lose revenue -- pick create_prorations and document.
- **No deprecation path**: legacy tier with 300 customers accumulates tech debt -- every tier needs a sunset plan.
