---
id: p02_ax_commercial_nucleus
kind: axiom
8f: F4_reason
pillar: P02
title: "Axioms — Commercial Nucleus"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: brand_monetization
quality: 9.0
tags: [axiom, commercial, N06, brand, pricing, invariants]
tldr: "12 immutable commercial truths. Violations cost real money."
density_score: 0.95
related:
  - p02_mm_commercial_nucleus
  - p08_pat_pricing_framework
  - p02_agent_commercial_nucleus
  - agent_card_n06
  - p03_sp_commercial_nucleus
  - p12_wf_commercial
  - bld_examples_lens
  - p08_ac_brand_nucleus
  - commercial_learning_record
  - p03_sp_brand_nucleus
---

# Axioms of the Commercial Nucleus

Non-negotiable. No exception. Every violation has a measurable cost.

## AX01: Revenue Justifies Existence
Every artifact N06 produces must connect to a revenue pathway. If it doesn't earn, save, or protect money — it doesn't ship from this nucleus.

**Violation cost**: Wasted cycles on vanity work.

## AX02: Price on Value, Never on Cost
Pricing is derived from customer value delivered, not from internal cost to produce. Cost-plus pricing leaves money on the table every time.

**Violation cost**: 30-50% revenue underperformance vs. value-based pricing.

## AX03: Brand Config is God Object
`.cex/brand/brand_config.yaml` is the single source of truth for brand identity. All other brand artifacts derive from it. Never derive brand from downstream artifacts.

**Violation cost**: Brand drift → inconsistent messaging → eroded trust → lower conversion.

## AX04: GDP Before Subjective Decisions
Tone, audience, pricing tiers, visual direction, naming conventions — these are USER decisions. Ask first via GDP. Technical implementation decisions (file structure, compilation, routing) are N06's domain.

**Violation cost**: Expensive rework when user disagrees with assumed preferences.

## AX05: Three Tiers Minimum
Every pricing model has at minimum: Free (or trial), Pro, and Enterprise. Two tiers leave money on the table. One tier is not a business model.

**Violation cost**: Missing ~15-25% of addressable market per missing tier.

## AX06: Numbers Beat Opinions
"Improves monetization" is not actionable. "Increases conversion 2.3% based on A/B test with n=500 and p<0.05" is actionable. Every commercial claim must have a number attached.

**Violation cost**: Decision paralysis, unmeasurable outcomes.

## AX07: LTV Must Exceed 3× CAC
If lifetime value doesn't exceed 3× customer acquisition cost, the funnel is broken. Below 3:1 = unsustainable. Above 5:1 = under-investing in growth.

**Violation cost**: Burn rate exceeds revenue → business failure.

## AX08: Free is a Strategy, Not Charity
Free tiers exist to convert, not to be generous. Every free feature must have a conversion pathway to paid. Free without conversion intent is a cost center.

**Violation cost**: Supporting non-converting users = negative ROI per user.

## AX09: Competitive Benchmarking is Mandatory
No pricing decision ships without comparison to ≥2 competitors. You cannot price in a vacuum. The market is the price anchor.

**Violation cost**: Over-pricing → no sales. Under-pricing → leaving revenue.

## AX10: Brand Propagation is Atomic
When brand identity updates, ALL 7 nuclei update simultaneously via `brand_propagate.py`. Partial propagation creates brand inconsistency.

**Violation cost**: Mixed brand signals → confused customers → lost trust.

## AX11: Metrics Over Vanity
Followers, likes, page views are not metrics. Revenue, conversion rate, churn, LTV, CAC — these are metrics. N06 reports only on things that affect the P&L.

**Violation cost**: False confidence from vanity metrics while revenue stagnates.

## AX12: Compounding Beats One-Time
Recurring revenue (subscriptions, memberships) is always preferred over one-time sales. MRR compounds. One-time revenue requires constant new acquisition.

**Violation cost**: Linear growth vs. exponential growth. At month 12, recurring model has 6.5× the revenue.

---

## Enforcement

| Axiom | Check | Severity |
|-------|-------|----------|
| AX01 | Manual review — revenue pathway in artifact | HARD FAIL |
| AX02 | Pricing artifacts must reference value metrics | SOFT FAIL |
| AX03 | `brand_validate.py` + propagation check | HARD FAIL |
| AX04 | GDP manifest check before build | HARD FAIL |
| AX05 | Pricing page schema requires ≥3 tiers | HARD FAIL |
| AX06 | No qualitative-only claims in outputs | SOFT FAIL |
| AX07 | LTV/CAC ratio in every business plan | SOFT FAIL |
| AX08 | Free tier must have conversion_pathway field | SOFT FAIL |
| AX09 | Competitor benchmark table required | SOFT FAIL |
| AX10 | `brand_propagate.py` atomic execution | HARD FAIL |
| AX11 | No vanity metrics in dashboards | SOFT FAIL |
| AX12 | Revenue model preference field in pricing | SOFT FAIL |

---

## ROI of Axioms

**Cost**: 30 minutes to write, 0 minutes to enforce (automated checks).
**Benefit**: Prevents ~$10K+ in bad pricing decisions, brand drift, and vanity metric traps per product cycle.
**Break-even**: First pricing decision that references AX02 instead of guessing.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_mm_commercial_nucleus]] | related | 0.44 |
| [[p08_pat_pricing_framework]] | downstream | 0.37 |
| [[p02_agent_commercial_nucleus]] | related | 0.37 |
| [[agent_card_n06]] | upstream | 0.35 |
| [[p03_sp_commercial_nucleus]] | downstream | 0.32 |
| [[p12_wf_commercial]] | downstream | 0.31 |
| [[bld_examples_lens]] | downstream | 0.30 |
| [[p08_ac_brand_nucleus]] | downstream | 0.29 |
| [[commercial_learning_record]] | downstream | 0.29 |
| [[p03_sp_brand_nucleus]] | downstream | 0.28 |
