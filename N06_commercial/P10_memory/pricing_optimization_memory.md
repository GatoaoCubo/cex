---
id: pricing_optimization_memory
kind: memory_summary
8f: F3_inject
pillar: P10
title: "Pricing Optimization Memory — N06 Commercial"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: pricing_experiments
quality: 9.0
tags: [memory, pricing, optimization, A/B, conversion, N06]
tldr: "Tracks pricing experiments, tier performance, and conversion data to drive data-backed pricing decisions."
scope: pricing_performance_learning
density_score: 1.0
related:
  - p08_pat_pricing_framework
  - pricing_experiment_tool
  - kc_pricing_strategy
  - bld_output_template_subscription_tier
  - bld_instruction_pricing_page
  - p01_kc_commercial_nucleus
  - p02_mm_commercial_nucleus
  - p03_pt_commercial_nucleus
  - p02_ax_commercial_nucleus
  - subscription-tier-builder
---

# Pricing Optimization Memory

## Purpose

Pricing is the single highest-leverage commercial lever. A 1% price optimization outperforms a 1% traffic increase every time. This memory tracks what we've tried, what worked, and what the data says.

---

## Pricing Experiment Template

```yaml
experiment_id: "PX-YYYY-MM-DD-NNN"
date: "2026-MM-DD"
product: "product_name"
hypothesis: "What we expected"
variant_a: "control — current pricing"
variant_b: "test — proposed pricing"
metric: "conversion_rate | revenue_per_visitor | ARPU"
duration_days: 14
sample_size: 0
result:
  variant_a_value: 0.0
  variant_b_value: 0.0
  lift_pct: 0.0
  confidence: 0.0  # p-value or Bayesian credible interval
  winner: "a | b | inconclusive"
decision: "keep_a | adopt_b | extend_test | redesign"
learnings: "What we learned"
```

---

## Active Pricing Models

_No live products yet. Populate when first product launches._

### Template Entry
```yaml
product: "product_name"
model: "subscription | one_time | freemium | usage_based | hybrid"
tiers:
  - name: "Free"
    price: 0
    features: ["..."]
    target: "trial users"
    conversion_to_paid: 0.0
  - name: "Pro"
    price: 0
    features: ["..."]
    target: "power users"
    churn_rate: 0.0
  - name: "Enterprise"
    price: "custom"
    features: ["..."]
    target: "teams/orgs"
    avg_contract_value: 0
last_updated: "2026-MM-DD"
```

---

## Pricing Insights Log

### Insight Template
```yaml
insight_id: "PI-NNN"
date: "2026-MM-DD"
source: "experiment | competitor_analysis | user_feedback | market_research"
insight: "What we learned"
confidence: "high | medium | low"
actionable: true | false
action_taken: "What we did about it (if any)"
```

---

## Competitor Pricing Benchmarks

| Competitor | Model | Free Tier | Pro Price | Enterprise | Source | Date |
|-----------|-------|-----------|-----------|-----------|--------|------|
| _TBD_ | — | — | — | — | — | — |

_Populate via `fetch` MCP + manual research. Update quarterly._

---

## Pricing Principles (Earned Through Experience)

1. **Price on value, not cost** — what does it save/earn the customer?
2. **Anchor high** — the enterprise tier makes pro look reasonable
3. **Free must convert** — if free doesn't feed paid, kill it
4. **Annual discount = cash flow** — offer 20% annual discount to lock revenue
5. **Price increases are easier than you think** — existing customers tolerate 10-15% if value grew

---

## Metrics Dashboard

| Metric | Current | Target | Gap | Trend |
|--------|---------|--------|-----|-------|
| ARPU | — | — | — | — |
| Conversion (free→paid) | — | — | — | — |
| Churn (monthly) | — | — | — | — |
| LTV | — | — | — | — |
| CAC | — | — | — | — |
| LTV/CAC ratio | — | ≥3.0 | — | — |

_Update after first product launch._

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_pricing_framework]] | upstream | 0.51 |
| [[pricing_experiment_tool]] | downstream | 0.35 |
| [[kc_pricing_strategy]] | upstream | 0.29 |
| [[bld_output_template_subscription_tier]] | upstream | 0.27 |
| [[bld_instruction_pricing_page]] | upstream | 0.27 |
| [[p01_kc_commercial_nucleus]] | upstream | 0.26 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.26 |
| [[p03_pt_commercial_nucleus]] | upstream | 0.26 |
| [[p02_ax_commercial_nucleus]] | upstream | 0.26 |
| [[subscription-tier-builder]] | downstream | 0.26 |
