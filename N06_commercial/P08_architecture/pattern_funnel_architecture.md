---
id: p08_pat_funnel_architecture
kind: pattern
8f: F4_reason
pillar: P08
title: "Pattern — Conversion Funnel Architecture"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: funnel_optimization
quality: 9.0
tags: [pattern, funnel, conversion, N06, architecture, AIDA]
tldr: "5-stage funnel framework: Attract → Engage → Convert → Retain → Expand. Each stage has metrics, tools, and cross-nucleus handoffs."
density_score: 0.93
related:
  - n06_funnel_cex_product
  - funnel_diagnostic_tool
  - p02_mm_commercial_nucleus
  - n06_commercial
  - agent_card_n06
  - n02_kc_campaign
  - n06_funnel_content_factory
  - n06_self_audit_20260408
  - n06_monetization_audit_2026_04_08
  - cross_nucleus_handoffs
---

# Pattern: Conversion Funnel Architecture

## Overview

Every commercial system is a funnel. The funnel pattern ensures N06 can design, measure, and optimize the path from stranger to revenue. Without structure, funnel optimization is guesswork. With it, every stage has clear metrics and ownership.

**ROI**: A structured funnel with stage-level metrics typically improves conversion 15-40% over untracked funnels — because you can see where people drop.

---

## Funnel Stages

```
                    ┌─────────────────────┐
                    │     ATTRACT          │  ← Content, SEO, ads, social
                    │  (Awareness)         │     Owner: N02 Marketing
                    │  Metric: reach       │
                    └────────┬────────────┘
                             │ CTR
                    ┌────────▼────────────┐
                    │     ENGAGE           │  ← Landing pages, lead magnets, demos
                    │  (Consideration)     │     Owner: N02+N06
                    │  Metric: engagement  │
                    └────────┬────────────┘
                             │ Signup/Trial Rate
                    ┌────────▼────────────┐
                    │     CONVERT          │  ← Pricing page, checkout, onboarding
                    │  (Decision)          │     Owner: N06 Commercial
                    │  Metric: conversion  │
                    └────────┬────────────┘
                             │ Activation Rate
                    ┌────────▼────────────┐
                    │     RETAIN           │  ← Product value, support, engagement
                    │  (Loyalty)           │     Owner: N05+N06
                    │  Metric: churn       │
                    └────────┬────────────┘
                             │ Expansion Rate
                    ┌────────▼────────────┐
                    │     EXPAND           │  ← Upsell, cross-sell, referrals
                    │  (Advocacy)          │     Owner: N06 Commercial
                    │  Metric: NRR         │
                    └─────────────────────┘
```

---

## Stage Details

### 1. ATTRACT (Top of Funnel)

| Element | Detail |
|---------|--------|
| **Goal** | Get qualified eyeballs |
| **Owner** | N02 Marketing (copy) + N06 (strategy) |
| **Channels** | Content marketing, SEO, social, paid ads, PR |
| **Key Metric** | Qualified traffic (not vanity pageviews — AX11) |
| **Tools** | NotebookLM (content), fetch MCP (research) |
| **Handoff to N02** | Content brief with target keywords + audience |

### 2. ENGAGE (Mid-Funnel)

| Element | Detail |
|---------|--------|
| **Goal** | Convert visitors to leads/trials |
| **Owner** | N02 (copy) + N06 (offer structure) + N03 (build) |
| **Assets** | Landing pages, lead magnets, free tools, demos |
| **Key Metric** | Signup/trial rate (visitors → leads) |
| **Tools** | Landing page builder, email sequences |
| **GDP needed** | Lead magnet topic, form fields, value proposition |

### 3. CONVERT (Decision Point)

| Element | Detail |
|---------|--------|
| **Goal** | Turn leads into paying customers |
| **Owner** | N06 Commercial (pricing, checkout) |
| **Assets** | Pricing page, checkout flow, payment processing |
| **Key Metric** | Conversion rate (leads → customers) |
| **Tools** | Stripe MCP (payments), Hotmart MCP (courses) |
| **Critical** | AX05 (3+ tiers), AX02 (value-based pricing) |

### 4. RETAIN (Post-Sale)

| Element | Detail |
|---------|--------|
| **Goal** | Keep customers paying |
| **Owner** | N05 (product ops) + N06 (engagement strategy) |
| **Assets** | Onboarding sequences, support, feature updates |
| **Key Metric** | Monthly churn rate (target: < 5%) |
| **Tools** | Stripe MCP (subscription management) |
| **Warning** | Churn > 5%/month = leaky bucket. Fix before spending on ATTRACT |

### 5. EXPAND (Revenue Growth)

| Element | Detail |
|---------|--------|
| **Goal** | Increase revenue per customer |
| **Owner** | N06 Commercial |
| **Strategies** | Upsell to higher tier, cross-sell products, referral programs |
| **Key Metric** | Net Revenue Retention (NRR, target: > 110%) |
| **Tools** | Stripe MCP (upgrade tracking), pricing_optimization_memory.md |
| **ROI note** | Expanding existing customers costs 5-7× less than acquiring new ones |

---

## Funnel Metrics Dashboard

```yaml
funnel_metrics:
  attract:
    traffic_monthly: 0
    qualified_pct: 0.0
    cost_per_visitor: 0.00
  engage:
    landing_page_views: 0
    signups: 0
    signup_rate: 0.0  # signups / views
  convert:
    trials: 0
    paid: 0
    conversion_rate: 0.0  # paid / trials
    avg_deal_value: 0.00
  retain:
    active_customers: 0
    churned_this_month: 0
    churn_rate: 0.0  # churned / active
    mrr: 0.00
  expand:
    upgrades: 0
    cross_sells: 0
    nrr: 0.0  # (mrr + expansion - churn) / mrr_start
  
  derived:
    cac: 0.00  # total spend / paid customers
    ltv: 0.00  # arpu / churn_rate
    ltv_cac: 0.0  # must be > 3.0 (AX07)
    payback_months: 0  # cac / arpu
```

---

## Cross-Nucleus Ownership Map

| Stage | N01 | N02 | N03 | N04 | N05 | N06 |
|-------|-----|-----|-----|-----|-----|-----|
| ATTRACT | Research | Copy | — | Content | — | Strategy |
| ENGAGE | — | Landing copy | Build pages | Lead magnets | — | Offer design |
| CONVERT | — | — | Checkout flow | — | Payment ops | Pricing |
| RETAIN | — | Email nurture | Feature dev | Docs | Support ops | Engagement |
| EXPAND | — | Upgrade copy | Upsell UX | — | Billing ops | Revenue strategy |

---

## Diagnostic: Where's the Leak?

```
IF conversion_rate < 2% → Fix CONVERT (pricing, checkout friction)
IF signup_rate < 10% → Fix ENGAGE (landing page, value prop)
IF churn_rate > 5% → Fix RETAIN (onboarding, product value)
IF NRR < 100% → Fix EXPAND (upsell opportunities)
IF qualified_traffic < threshold → Fix ATTRACT (content, SEO, ads)
```

**Rule**: Always fix the leakiest stage first. Pouring more traffic into a leaky funnel wastes money.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_funnel_cex_product]] | downstream | 0.33 |
| [[funnel_diagnostic_tool]] | downstream | 0.32 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.31 |
| [[n06_commercial]] | upstream | 0.28 |
| [[agent_card_n06]] | upstream | 0.27 |
| [[n02_kc_campaign]] | upstream | 0.27 |
| [[n06_funnel_content_factory]] | downstream | 0.26 |
| [[n06_self_audit_20260408]] | upstream | 0.24 |
| [[n06_monetization_audit_2026_04_08]] | upstream | 0.22 |
| [[cross_nucleus_handoffs]] | downstream | 0.22 |
