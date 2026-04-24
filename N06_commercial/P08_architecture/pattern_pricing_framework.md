---
id: p08_pat_pricing_framework
kind: pattern
8f: F4_reason
pillar: P08
title: "Pattern — Value-Based Pricing Framework"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: pricing_strategy
quality: 9.0
tags: [pattern, pricing, framework, N06, architecture, value-based]
tldr: "Structured pricing methodology: research → value quantification → tier design → testing → optimization. Prevents gut-feel pricing."
density_score: 0.92
related:
  - pricing_optimization_memory
  - p02_ax_commercial_nucleus
  - kc_pricing_strategy
  - pricing_experiment_tool
  - bld_instruction_pricing_page
  - p02_mm_commercial_nucleus
  - subscription-tier-builder
  - p01_kc_commercial_nucleus
  - n06_intent_resolution_depth_spec
  - bld_instruction_subscription_tier
---

# Pattern: Value-Based Pricing Framework

## Problem

Pricing is the #1 revenue lever, yet most products price by gut feel or cost-plus. A 1% improvement in pricing yields 11% profit improvement (McKinsey), compared to 3.3% for volume and 7.8% for cost reduction.

**Cost of bad pricing**: Under-price by 20% → you need 25% more customers to match revenue. Over-price by 20% → conversion drops 30-50%. Both are expensive.

---

## Framework Stages

```
┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐
│ RESEARCH  │──▶│ QUANTIFY  │──▶│ DESIGN    │──▶│ TEST      │──▶│ OPTIMIZE  │
│           │   │           │   │           │   │           │   │           │
│ Competitor│   │ Value per │   │ Tier      │   │ A/B with  │   │ Iterate   │
│ + market  │   │ customer  │   │ structure │   │ real users│   │ quarterly │
└───────────┘   └───────────┘   └───────────┘   └───────────┘   └───────────┘
  AX09            AX02            AX05            AX06            AX11
```

### Stage 1: RESEARCH

**Inputs**:
- 2+ competitor pricing pages (AX09 mandate)
- Market size estimate (TAM/SAM/SOM)
- Customer willingness-to-pay signals

**Activities**:
1. Scrape competitor pricing via `fetch` MCP
2. Map feature sets per tier across competitors
3. Identify price anchors in the market
4. Note psychological price points ($9, $29, $49, $99, $199)

**Output**: Competitive pricing matrix

```markdown
| Competitor | Free | Pro | Enterprise | Key Differentiator |
|-----------|------|-----|-----------|-------------------|
| Comp A    | ✅   | $29 | $99/seat  | Feature X         |
| Comp B    | ❌   | $19 | Custom    | Integration Y     |
| Our range | ✅   | $?? | $??       | Our differentiator|
```

### Stage 2: QUANTIFY

**Goal**: Convert product value into dollar terms.

**Value calculation framework**:
```
Time saved: hours_saved × hourly_rate = $value_per_month
Errors prevented: errors_per_month × cost_per_error = $value_per_month
Revenue generated: additional_revenue_attributable = $value_per_month
Combined value: sum of above = Total Monthly Value (TMV)

Price = TMV × capture_rate (typically 10-30%)
```

**GDP required**: User must validate value assumptions.

### Stage 3: DESIGN

**Tier architecture** (AX05: minimum 3):

```yaml
tiers:
  free:
    price: 0
    purpose: "acquisition + qualification"
    limits: "usage cap or feature gate"
    conversion_trigger: "what makes them upgrade?"
    
  pro:
    price: "TMV × 0.10 to TMV × 0.20"
    purpose: "core revenue driver"
    features: "all free + power features"
    billing: "monthly with annual discount (20%)"
    
  enterprise:
    price: "TMV × 0.25 to TMV × 0.30 per seat"
    purpose: "price anchor + large accounts"
    features: "all pro + admin, SSO, SLA, support"
    billing: "annual contract, custom negotiation"
```

**Pricing psychology**:
- End in 9 ($29 not $30) for consumer
- Round numbers ($50, $100) for enterprise
- Annual = monthly × 10 (not × 12) — the "2 months free" anchor
- Show savings: "Save 20% with annual billing"

### Stage 4: TEST

**Method**: Sequential testing (not A/B if traffic is low)

```yaml
test_plan:
  week_1_2: "Launch with pro at price_high"
  week_3_4: "Drop to price_mid, compare conversion"
  week_5_6: "Drop to price_low, compare conversion"
  analysis: "Plot price vs. conversion × revenue = optimal"
```

**For sufficient traffic**: True A/B test with 95% confidence.

**Metrics to track**:
- Conversion rate per tier
- Revenue per visitor
- Upgrade rate (free → pro)
- Churn rate per tier
- ARPU (Average Revenue Per User)

### Stage 5: OPTIMIZE

**Quarterly review cycle**:
1. Pull metrics from Stripe MCP
2. Compare against targets in `pricing_optimization_memory.md`
3. Identify: which tier is underperforming?
4. Hypothesize fix → run test → measure → decide
5. Log results to memory

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|-------------|-----------------|
| "Match the cheapest competitor" | Race to zero margin | Differentiate on value, not price |
| "One price for everyone" | Misses willingness-to-pay variance | Segment with tiers |
| "Free forever, monetize later" | Never monetizes | Free with clear conversion gates |
| "Enterprise = Pro × 10" | Not value-justified | Enterprise based on org-level value |
| "Change price weekly" | Erodes trust | Test quietly, change quarterly max |

---

## Decision Record Template

Every pricing decision gets logged:

```yaml
decision_id: "PR-YYYY-MM-DD-NNN"
product: "product_name"
previous_price: "$X"
new_price: "$Y"
change_pct: "+/-Z%"
rationale: "Why this change"
data_source: "experiment PX-NNN | competitor analysis | user feedback"
expected_impact: "conversion +X% or revenue +$Y/mo"
actual_impact: "measured after 30 days"
keep_or_revert: "keep | revert"
```

---

## Integration with CEX Tools

| Tool | Role in Pricing |
|------|----------------|
| `fetch` MCP | Scrape competitor pricing pages |
| Stripe MCP | Pull revenue data, manage subscription tiers |
| Hotmart MCP | Course pricing, affiliate commission rates |
| `cex_evolve.py` | Auto-improve pricing page copy |
| `brand_audit.py` | Verify pricing aligns with brand positioning |
| `pricing_optimization_memory.md` | Store all pricing experiment results |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[pricing_optimization_memory]] | downstream | 0.45 |
| [[p02_ax_commercial_nucleus]] | upstream | 0.34 |
| [[kc_pricing_strategy]] | upstream | 0.33 |
| [[pricing_experiment_tool]] | downstream | 0.33 |
| [[bld_instruction_pricing_page]] | upstream | 0.32 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.32 |
| [[subscription-tier-builder]] | downstream | 0.31 |
| [[p01_kc_commercial_nucleus]] | upstream | 0.30 |
| [[n06_intent_resolution_depth_spec]] | downstream | 0.28 |
| [[bld_instruction_subscription_tier]] | upstream | 0.28 |
