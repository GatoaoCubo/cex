---
id: p01_kc_commercial_nucleus
kind: knowledge_card
8f: F3_inject
pillar: P01
title: Commercial Monetization — Pricing, Courses & Funnels
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n06_commercial
domain: commercial-monetization
quality: 9.2
tags: [commercial, pricing, funnels, courses, monetization, N06, revenue]
tldr: "N06 commercial playbook: value-based pricing (price=transformation x certainty x speed), 3-tier anchor strategy (70-80% mid-tier conversion), TOFU/MOFU/BOFU funnel benchmarks (2-5% BOFU, 15-30% OTO), LTV calculation (AOV x frequency x lifespan), and upsell architecture (order bump + OTO1 + OTO2 + downsell chain)."
when_to_use: "When pricing a new product (use value-based formula), launching a course (needs transformation arc + tier design), building a conversion funnel (TOFU/MOFU/BOFU with stage benchmarks), optimizing post-purchase revenue (upsell/downsell architecture), or projecting revenue (MRR/LTV scenario modeling). Trigger: any task involving revenue generation, pricing decisions, or funnel optimization."
keywords: [pricing, funnel, course, conversion, upsell, LTV, MRR, transformation, launch, hotmart, kiwify, infoproduct, value-based-pricing, anchor-pricing, tiered-pricing]
long_tails:
  - "How to price an online course using value-based pricing"
  - "Sales funnel strategy for digital information products"
  - "Revenue models for online courses: one-time vs subscription vs cohort"
  - "How to structure upsell sequences to maximize customer LTV"
  - "Platform comparison for selling courses: Hotmart vs Kiwify vs Kajabi"
  - "How to calculate AOV and LTV for digital products"
  - "Anchor pricing strategy for 3-tier SaaS pricing pages"
axioms:
  - "ALWAYS price to the transformation, never to the production cost."
  - "NEVER launch without a defined upsell path — the first sale is the smallest sale."
  - "ALWAYS validate conversion benchmarks before setting funnel revenue projections."
  - "NEVER write a course outline without a transformation arc — the arc IS the price anchor."
linked_artifacts:
  primary: p02_agent_commercial_nucleus
  related: [p03_sp_commercial_nucleus, p12_wf_commercial_nucleus, p11_qg_commercial_nucleus]
density_score: 0.93
related:
  - p03_pt_commercial_nucleus
  - p08_pat_pricing_framework
  - pricing_optimization_memory
  - p03_sp_commercial_nucleus
  - p01_kc_content_monetization
  - n06_pricing_content_factory
  - kc_pricing_strategy
  - pricing-page-builder
  - subscription-tier-builder
  - bld_knowledge_card_pricing_page
---

# Commercial Monetization — Pricing, Courses & Funnels

## Quick Reference

```yaml
domain: commercial-monetization
nucleus: N06
cli: claude-sonnet
scope: pricing, online courses, sales funnels, conversion optimization
criticality: high
```

## Pricing Frameworks

### Value-Based Pricing
Price = perceived transformation value to the buyer, not cost to produce.
- Formula: `Price = (Outcome Value) × (Certainty Factor) × (Speed Factor)`
- Example: Course that helps land a R$10k/month job → price R$1,500-R$3,000

### Anchor Pricing
Always present a higher anchor before the real price.
- "Would normally cost R$5,000. Today: R$997."
- Anchors shift perceived value and justify the actual price

### Tiered Pricing (3-tier standard)
| Tier | Price Ratio | What it includes |
|------|-------------|-----------------|
| Basic | 1x | Core content only |
| Pro | 2.5x | Core + community + Q&A |
| VIP/Mentorship | 5x | Core + community + live sessions + 1:1 |

Rule: 70-80% of buyers choose middle tier when anchored by VIP.

### Psychological Pricing
- Charm pricing: R$997 not R$1,000 (3x cheaper perception)
- Round pricing for premium: R$2,000 feels MORE premium than R$1,997
- Payment plans: 12x R$97 vs. R$997 à vista — installments increase access, reduce perceived barrier

## Course Monetization Models

| Model | Structure | Best For |
|-------|-----------|----------|
| One-time | Single payment, lifetime access | Low-ticket (<R$500), lead gen |
| Cohort | Fixed start/end, group learning | Premium (R$2k+), community-driven |
| Subscription | Monthly/annual, library access | Content depth, recurring revenue |
| Hybrid | One-time + upsell to subscription | Most scalable — entry + LTV |

### Transformation Arc (mandatory for every course)
```
BEFORE: [Student situation, pain, frustration]
    ↓ [Course journey — modules as milestones]
AFTER: [Concrete outcome, skill, status, income]
```
Without a transformation arc, the course has no pricing anchor.

### Platform Considerations
| Platform | Best For | Pricing Behavior |
|----------|----------|-----------------|
| Hotmart | Brazilian market, affiliates | 3-tier + order bump native |
| Kiwify | PT-BR, lower fees | Simple checkout, fast setup |
| Kajabi | International, all-in-one | Higher ticket, community |
| Teachable | International, clean UX | Standard course delivery |

## Sales Funnel Stages

```
TOFU (Top of Funnel) → MOFU (Middle) → BOFU (Bottom) → CHECKOUT → POST-PURCHASE
```

### Stage Benchmarks
| Stage | Artifact | Conversion Benchmark |
|-------|----------|---------------------|
| TOFU | Ad / organic post | 1-3% click-through |
| MOFU | Lead magnet / webinar | 20-40% opt-in |
| BOFU | Sales page / VSL | 2-5% of traffic → purchase |
| Checkout | Checkout page | 60-80% completion (of initiated) |
| Post-purchase | OTO / order bump | 15-30% OTO take rate |

### VSL (Video Sales Letter) Structure
1. **Hook** (0-30s): Call out the avatar + pain. "Se você é [X] e ainda não consegue [Y]..."
2. **Problem** (30s-2min): Agitate the pain. Cost of inaction.
3. **Revelation** (2-4min): The mechanism — why other solutions fail, why THIS works
4. **Proof** (4-6min): Results, testimonials, case studies
5. **Offer** (6-8min): What's included, price reveal, anchor + discount
6. **CTA** (8-end): Urgency + guarantee + call to action

## Upsell Architecture

### Standard Sequence
```
PURCHASE → Order Bump (15-30% take rate, low-ticket add-on)
         → OTO1 (complementary high-value, 20-35% take rate)
         → OTO2 (implementation/done-for-you, 10-20% take rate)
         → Downsell (payment plan / lite version if OTO declined, 25-40% of declinees)
```

### LTV Calculation
```
LTV = AOV × Purchase Frequency × Customer Lifespan
AOV = (Base Price × % buyers) + (OTO1 × % take) + (OTO2 × % take) + (Bump × % take)
```

## Revenue Modeling

### Key Metrics
| Metric | Definition | Target |
|--------|-----------|--------|
| AOV | Average Order Value | 1.5-2.5x base price (with upsells) |
| LTV | Lifetime Customer Value | 3-5x AOV |
| CAC | Customer Acquisition Cost | < 30% of AOV |
| Funnel ROI | Revenue / Ad Spend | >= 3x (ROAS 3+) |
| Refund Rate | Refunds / Sales | < 5% |

### MRR Scenarios (course launch example)
```
Conservative: 100 sales × R$997 = R$99,700
Realistic:    250 sales × R$997 + 30% OTO (R$497) = R$286,700
Optimistic:   500 sales × R$997 + 25% OTO + order bump = R$560,000+
```

## Golden Rules

1. Price = transformation value. Justify with outcome, not effort.
2. Every offer needs 3 tiers. Middle tier anchored by VIP.
3. Every funnel needs a post-purchase upsell. First sale is smallest.
4. Every course needs a transformation arc. Start → end state.
5. Every revenue projection needs units × price × conversion rate.
6. Validate conversion benchmarks before committing to projections.

## Flow

```
[Intent] → [Identify Artifact Type] → [Load Framework] → [Apply Benchmarks] → [Produce Artifact] → [Validate]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_commercial_nucleus]] | downstream | 0.54 |
| [[p08_pat_pricing_framework]] | downstream | 0.38 |
| [[pricing_optimization_memory]] | downstream | 0.34 |
| [[p03_sp_commercial_nucleus]] | downstream | 0.32 |
| [[p01_kc_content_monetization]] | sibling | 0.29 |
| [[n06_pricing_content_factory]] | downstream | 0.29 |
| [[kc_pricing_strategy]] | sibling | 0.28 |
| [[pricing-page-builder]] | downstream | 0.27 |
| [[subscription-tier-builder]] | downstream | 0.27 |
| [[bld_knowledge_card_pricing_page]] | sibling | 0.26 |
