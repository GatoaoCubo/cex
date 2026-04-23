---
id: roi_calculator_n06
kind: roi_calculator
pillar: P11
nucleus: n06
title: "ROI Calculator -- Customer Value Proof Model"
version: 1.0.0
quality: 9.0
tags: [roi, value, calculator, sales, proof, commercial, ltv]
density_score: 1.0
updated: "2026-04-17"
related:
  - n06_roi_content_factory
  - n06_report_intent_resolution_moat
  - n06_intent_resolution_depth_spec
  - n06_funnel_cex_product
  - n06_strategy_claude_native
  - n06_api_access_pricing
  - kc_pricing_page
  - bld_collaboration_roi_calculator
  - n06_content_factory_pricing
  - bld_examples_roi_calculator
---

# ROI Calculator: Customer Value Proof Model

## Purpose

Quantifies the value CEX delivers to customers by tier and persona. Used in sales conversations, pricing pages, and renewal negotiations. Strategic Greed principle: customers buy when value > price is undeniable.

## Input Variables

```yaml
inputs:
  # Customer profile
  team_size: integer          # number of people who would use CEX
  hourly_rate_usd: integer    # average hourly fully-loaded cost per person
  
  # Current state (before CEX)
  builds_per_week: integer    # artifacts/content pieces produced manually
  hours_per_build: float      # avg hours to produce one artifact manually
  revision_cycles: integer    # avg revision rounds per artifact
  hours_per_revision: float   # avg hours per revision round
  
  # CEX performance
  cex_build_time_hours: float         # default: 0.05 (3 minutes)
  cex_revision_time_hours: float      # default: 0.02 (1 minute with 8F)
  cex_quality_improvement_pct: float  # default: 40% (fewer revision cycles)
```

## Calculation Model

```python
def calculate_roi(inputs: dict, tier_price_monthly: int) -> dict:
    # Weekly time saved per build
    manual_build_time = (
        inputs["hours_per_build"] + 
        (inputs["revision_cycles"] * inputs["hours_per_revision"])
    )
    cex_build_time = (
        inputs["cex_build_time_hours"] + 
        (inputs["revision_cycles"] * (1 - inputs["cex_quality_improvement_pct"] / 100) 
         * inputs["cex_revision_time_hours"])
    )
    hours_saved_per_build = manual_build_time - cex_build_time
    
    # Monthly savings
    builds_per_month = inputs["builds_per_week"] * 4.33
    hours_saved_per_month = hours_saved_per_build * builds_per_month
    dollar_saved_per_month = hours_saved_per_month * inputs["hourly_rate_usd"]
    
    # ROI
    net_value = dollar_saved_per_month - tier_price_monthly
    roi_pct = (net_value / tier_price_monthly) * 100
    payback_days = (tier_price_monthly / dollar_saved_per_month) * 30
    
    return {
        "hours_saved_monthly": round(hours_saved_per_month, 1),
        "dollar_saved_monthly": round(dollar_saved_per_month, 0),
        "net_value_monthly": round(net_value, 0),
        "roi_pct": round(roi_pct, 0),
        "payback_days": round(payback_days, 0),
        "annual_savings": round(dollar_saved_per_month * 12, 0)
    }
```

## Pre-Computed Scenarios

### Solo Consultant (STARTER target)

```
Inputs: team=1, rate=$75/hr, builds=10/week, hours_per_build=2.5, revisions=2, rev_hours=1
Result:
  Hours saved/month: 92 hours
  Dollar saved/month: $6,900
  CEX cost (STARTER): $49/month
  ROI: 13,978% | Payback: <1 day
  Annual savings vs CEX: $82,212
```

### Marketing Team 3-5 people (PRO target)

```
Inputs: team=4, rate=$65/hr, builds=30/week, hours_per_build=3, revisions=3, rev_hours=1.5
Result:
  Hours saved/month: 450 hours
  Dollar saved/month: $29,250
  CEX cost (PRO): $149/month
  ROI: 19,530% | Payback: <1 day
  Annual savings vs CEX: $350,412
```

### Enterprise Marketing Dept 20+ people (ENTERPRISE target)

```
Inputs: team=20, rate=$80/hr, builds=200/week, hours_per_build=4, revisions=4, rev_hours=2
Result:
  Hours saved/month: 7,800 hours
  Dollar saved/month: $624,000
  CEX cost (ENTERPRISE): $2,000/month (example)
  ROI: 31,100% | Payback: <1 hour
  Annual savings vs CEX: $7,464,000
```

## Sales Conversation Script

```
"Let me show you the math on YOUR situation.
 
 [Input their numbers]
 
 So right now, your team spends [X] hours/month on [artifact type].
 At [$Y] fully loaded cost, that's [$Z] per month.
 
 With CEX, that drops to [X * 0.05] hours -- the 8F pipeline handles the rest.
 You'd save [$savings] per month. CEX costs [$price].
 
 That's a [ROI%] return. Your payback period: [days].
 
 Even if we're only half right, you're still up [net_value/2].
 
 The question isn't whether CEX pays for itself -- it's how much faster
 you want to capture [annual_savings] in annual value."
```

## Objection Handlers by ROI Band

| ROI Band | Typical Objection | Response |
|----------|-------------------|---------|
| <500% | "Not sure if it's worth it" | Focus on non-quantified value: quality, consistency, brand voice |
| 500-2000% | "Seems high, is this realistic?" | Share scenario most similar to their size. Offer trial. |
| >2000% | "I need to show this to my manager" | Offer ROI one-pager export. Offer pilot on 1 use case. |

## Pricing Page Integration

The calculator embeds on the pricing page with default values pre-filled by detected company size (from IP lookup or signup form):
- Solo -> default: team=1, rate=75, builds=10/week
- SMB -> default: team=5, rate=65, builds=25/week
- Enterprise -> default: team=20, rate=80, builds=100/week


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_roi_content_factory]] | related | 0.40 |
| [[n06_report_intent_resolution_moat]] | related | 0.38 |
| [[n06_intent_resolution_depth_spec]] | related | 0.36 |
| [[n06_funnel_cex_product]] | related | 0.31 |
| [[n06_strategy_claude_native]] | upstream | 0.25 |
| [[n06_api_access_pricing]] | related | 0.22 |
| [[kc_pricing_page]] | upstream | 0.21 |
| [[bld_collaboration_roi_calculator]] | downstream | 0.20 |
| [[n06_content_factory_pricing]] | related | 0.19 |
| [[bld_examples_roi_calculator]] | upstream | 0.19 |
