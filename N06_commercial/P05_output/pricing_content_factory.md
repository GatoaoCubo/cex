---
id: n06_pricing_content_factory
kind: content_monetization
pillar: P11
title: "Content Factory Pricing Model -- Per-Format, Tiered, Bundled"
version: 2.0.0
created: 2026-04-08
updated: 2026-04-08
author: n06_commercial
nucleus: N06
domain: content-factory-pricing
quality: 8.9
tags: [pricing, content-factory, tiers, ai-only, human-reviewed, bundles, margins, competitor-benchmark]
tldr: "Complete pricing model for Content Factory v1. Per-content-type pricing across 11 formats, 2-tier quality model (AI-only vs human-reviewed), 6 pre-built bundles with 19-22% discount, competitor benchmark against 10 players, 5 subscription tiers R$0-3997/mo, margin analysis 76-93%."
density_score: 0.96
depends_on:
  - spec_content_factory_v1
  - output_content_factory_business_model
  - n06_strategy_claude_native
  - n06_content_factory_pricing
linked_artifacts:
  primary: spec_content_factory_v1
  related:
    - funnel_content_factory
    - roi_content_factory
    - integration_content_factory
related:
  - n06_content_factory_pricing
  - n06_roi_content_factory
  - kc_pricing_strategy
  - n06_funnel_content_factory
  - n06_report_intent_resolution_moat
  - n04_output_monetization_curriculum
  - p01_kc_commercial_nucleus
  - p08_pat_pricing_framework
  - n06_intent_resolution_depth_spec
  - p03_sp_content_monetization_builder
---

# Content Factory Pricing Model -- Per-Format, Tiered, Bundled

> Every output has a cost. Every cost has a margin. Every margin has a ceiling.
> This is the definitive pricing reference for Content Factory v1.

---

## 1. Per-Content-Type Pricing

### 1.1 Production Cost Basis (Validated Stack, April 2026)

Source: `spec_content_factory_v1.md` section "Stack Validada" -- all tools tested.

| # | Content Type | LLM Cost | External API Cost | Total Cost/Unit | Time to Produce |
|---|-------------|----------|------------------|----------------|-----------------|
| 1 | Blog post (1500 words) | R$0.55 | R$0.00 | **R$0.55** | 3 min |
| 2 | Social media set (5 platforms) | R$0.60 | R$0.80 (Canva) | **R$1.40** | 5 min |
| 3 | Video script (90s) | R$0.35 | R$0.00 | **R$0.35** | 2 min |
| 4 | Video produced (90s short) | R$0.50 | R$2.75 (TTS+FFmpeg) | **R$3.25** | 8 min |
| 5 | Video produced (5min long) | R$1.20 | R$6.00 (TTS) | **R$7.20** | 15 min |
| 6 | Podcast episode (15min) | R$0.80 | R$0.00 (NotebookLM free) | **R$0.80** | 10 min |
| 7 | Course module (script+slides+quiz) | R$1.40 | R$2.00 (Canva/Marp) | **R$3.40** | 12 min |
| 8 | eBook chapter (3000 words) | R$1.10 | R$0.00 (Typst/Pandoc) | **R$1.10** | 5 min |
| 9 | Presentation (15 slides) | R$0.40 | R$0.80 (Canva) | **R$1.20** | 6 min |
| 10 | Email sequence (5 emails) | R$0.70 | R$0.00 | **R$0.70** | 4 min |
| 11 | Landing page (HTML/Tailwind) | R$1.00 | R$0.00 | **R$1.00** | 8 min |

**Infrastructure cost: R$0.** User runs on their own Claude Code subscription. CEX has zero server costs.

### 1.2 Quality Tiers -- AI-Only vs Human-Reviewed

| Tier | Description | Price Multiplier | Margin Impact | SLA |
|------|-------------|-----------------|---------------|-----|
| **Basic (AI-Only)** | 8F pipeline, quality gate >= 8.5, automated compile | 1.0x | 89-93% | Output in minutes |
| **Premium (Human-Reviewed)** | AI-Only + expert review + revision cycle + brand compliance audit | 2.5x | 55-65% | 24-48h turnaround |

**Why 2.5x, not 2.0x?** Human review costs R$25-50/hour. A course module review takes 30min = R$15-25 labor. At Basic price of R$30 (course module), Premium = R$75. Labor cost R$20 + AI cost R$3.40 = R$23.40 COGS. Margin: 69%. The 2.5x multiplier ensures minimum 55% margin even on the most review-intensive formats.

**Premium tier pricing per format:**

| # | Content Type | Basic Price (credits) | Premium Price (credits) | Review Scope |
|---|-------------|----------------------|------------------------|-------------|
| 1 | Blog post | 8 | 20 | SEO audit + fact-check + tone alignment |
| 2 | Social media set | 12 | 30 | Platform compliance + brand voice + hashtag strategy |
| 3 | Video script | 5 | 12 | Timing + hook review + CTA effectiveness |
| 4 | Video produced (90s) | 25 | 62 | A/V quality + pacing + thumbnail + captions |
| 5 | Video produced (5min) | 45 | 112 | Full editorial review + chapter marks |
| 6 | Podcast episode | 10 | 25 | Audio quality + intro/outro + show notes |
| 7 | Course module | 30 | 75 | Pedagogical review + quiz validation + learning objectives |
| 8 | eBook chapter | 10 | 25 | Structure + flow + citations + formatting |
| 9 | Presentation | 12 | 30 | Slide design + data accuracy + speaker notes |
| 10 | Email sequence | 8 | 20 | Deliverability + subject lines + CTA tracking |
| 11 | Landing page | 15 | 38 | Conversion audit + mobile QA + load time |

---

## 2. Subscription Tiers

### 2.1 Monthly Plans

| Tier | Price BRL | Price USD | Credits/Mo | Overage | Target ICP | ROI for Customer |
|------|----------|----------|-----------|---------|-----------|-----------------|
| **Free** | R$0 | $0 | ~15 (capped per format) | N/A | Developers exploring | Proves value |
| **Creator** | R$147/mo | $29/mo | 150 | R$1.20/credit | Solo infoproducers | 1 blog + 1 social/day = R$4,500 value |
| **Pro** | R$497/mo | $99/mo | 600 | R$1.00/credit | Active content creators | Full campaign/week |
| **Studio** | R$1,497/mo | $297/mo | 2,000 | R$0.85/credit | Agencies (5+ clients) | 10+ client campaigns/mo |
| **Factory** | R$3,997/mo | $799/mo | 6,000 + API | R$0.70/credit | Enterprise, white-label | Unlimited pipeline |

### 2.2 Annual Plans (20% Discount)

| Tier | Monthly | Annual/Mo | Annual Total | Savings |
|------|---------|----------|-------------|---------|
| Creator | R$147 | R$117 | R$1,404 | R$360 (2.4 months free) |
| Pro | R$497 | R$397 | R$4,764 | R$1,200 |
| Studio | R$1,497 | R$1,197 | R$14,364 | R$3,600 |
| Factory | R$3,997 | R$3,197 | R$38,364 | R$9,600 |

### 2.3 Credit Packs (One-Time Top-Ups)

| Pack | Credits | Price BRL | Price USD | Per-Credit | Discount |
|------|---------|----------|----------|-----------|---------|
| Starter | 50 | R$60 | $12 | R$1.20 | 0% |
| Standard | 200 | R$200 | $40 | R$1.00 | 17% |
| Pro | 500 | R$425 | $85 | R$0.85 | 29% |
| Bulk | 1,000 | R$750 | $150 | R$0.75 | 37% |
| Enterprise | 5,000 | R$3,250 | $650 | R$0.65 | 46% |

---

## 3. Bundle Discounts -- "Content Packs"

### 3.1 Pre-Built Bundles (One-Click, 19-22% Savings)

| Bundle | Formats Included | A-la-Carte Credits | Bundle Price | Savings | Use Case |
|--------|-----------------|-------------------|-------------|---------|----------|
| **Launch Kit** | Blog + social set + email + landing | 43 | 35 credits | 19% | Product launch |
| **Course Pack** | 8 modules + quiz + certificate page | 240 | 195 credits | 19% | Full online course |
| **Campaign Kit** | Video 90s + social set + email + blog + landing | 65 | 52 credits | 20% | Marketing campaign |
| **eBook Complete** | 8 chapters + cover page + landing | 95 | 75 credits | 21% | Digital product |
| **Podcast Series** | 4 episodes + social promo + landing | 60 | 48 credits | 20% | Podcast launch |
| **Full Factory Brief** | ALL 11 formats, 1 topic | ~180 | 140 credits | 22% | Complete content operation |

### 3.2 Bundle Economics

| Bundle | Credits (Bundle Price) | Our Cost | Revenue at R$1/credit | Margin |
|--------|----------------------|----------|----------------------|--------|
| Launch Kit | 35 | R$3.65 | R$35 | 90% |
| Course Pack | 195 | R$27.20 | R$195 | 86% |
| Campaign Kit | 52 | R$6.70 | R$52 | 87% |
| eBook Complete | 75 | R$9.80 | R$75 | 87% |
| Podcast Series | 48 | R$4.40 | R$48 | 91% |
| Full Factory Brief | 140 | R$15.60 | R$140 | 89% |

**Key insight**: Even at 22% bundle discount, margins stay above 85% because production costs are near-zero (user's Claude subscription + our validated stack).

---

## 4. Competitor Benchmark (April 2026 Real Prices)

### 4.1 Point-Tool Pricing

| Competitor | Category | Starter | Pro | What's Missing |
|-----------|----------|---------|-----|---------------|
| Jasper | Copy AI | $49/mo | $69/mo | No video, no course, no slides |
| Copy.ai | Copy AI | $29/mo | $249/mo | No video, no course |
| HeyGen | AI Video | $29/mo | $99/mo | No copy, no course, no ebook |
| Synthesia | AI Video | $29/mo | $89/mo | Video only |
| Coursebox | AI Courses | $21/mo | $210/mo | Courses only, no video, no copy |
| ElevenLabs | AI Voice | $5/mo | $22/mo | Voice only, no pipeline |
| Gamma | AI Slides | $10/mo | $20/mo | Slides only |
| Pictory | Repurpose | $25/mo | $49/mo | Text-to-video only |
| InVideo | Video | $28/mo | $60/mo | Video creation only |
| Writesonic | Copy+SEO | $49/mo | $249/mo | No video, no course |

### 4.2 Stack Cost Comparison

| Approach | Monthly Cost | Formats Covered | Pipeline? | Brand Consistent? |
|----------|-------------|----------------|----------|------------------|
| **5-tool stack** (Jasper+HeyGen+Coursebox+ElevenLabs+Gamma) | **R$1,210** (~$242) | 5 of 11 | NO | NO |
| **CEX Pro** | **R$497** | 11 of 11 | YES | YES |
| **Savings** | **R$713/mo** (59% less) | +6 formats | Automated | Auto-injected |

### 4.3 Agency Comparison

| Approach | Cost per Full Brief | Turnaround | Quality Control |
|----------|-------------------|-----------|----------------|
| Freelancer (video+copy+design) | R$3,000-8,000 | 2-4 weeks | Manual review |
| Marketing agency | R$5,000-15,000 | 3-6 weeks | Account manager |
| Content studio (specialized) | R$2,000-5,000 | 1-2 weeks | Editorial process |
| **CEX Full Factory Brief** | **R$140 credits** (~R$140) | **Minutes** | 8F quality gate |

**Positioning**: "What agencies charge R$5,000 for, CEX produces in minutes for R$140."

---

## 5. Margin Analysis

### 5.1 Worst-Case (100% Usage, Heaviest Formats -- All Video 5min)

| Tier | Revenue | Max Credits | Worst Case Cost | Margin |
|------|---------|------------|----------------|--------|
| Creator R$147 | R$147 | 150 | 3.3 long videos = R$23.76 | **84%** |
| Pro R$497 | R$497 | 600 | 13.3 long videos = R$95.76 | **81%** |
| Studio R$1,497 | R$1,497 | 2,000 | 44.4 long videos = R$319.68 | **79%** |
| Factory R$3,997 | R$3,997 | 6,000 | 133.3 long videos = R$959.76 | **76%** |

### 5.2 Expected-Case (Typical Mix: 40% Text, 30% Visual, 20% Audio, 10% Video)

| Tier | Revenue | Expected Cost | Expected Margin | Gross Profit |
|------|---------|--------------|----------------|-------------|
| Creator | R$147 | R$12.80 | **91%** | R$134.20 |
| Pro | R$497 | R$48.00 | **90%** | R$449.00 |
| Studio | R$1,497 | R$152.00 | **90%** | R$1,345.00 |
| Factory | R$3,997 | R$432.00 | **89%** | R$3,565.00 |

### 5.3 Premium Tier Margin (Human-Reviewed)

| Format | Premium Price | AI Cost | Review Cost | Total COGS | Margin |
|--------|-------------|---------|------------|-----------|--------|
| Blog post | R$20 | R$0.55 | R$12.50 | R$13.05 | 35% |
| Course module | R$75 | R$3.40 | R$25.00 | R$28.40 | 62% |
| Video produced (90s) | R$62 | R$3.25 | R$20.00 | R$23.25 | 63% |
| Landing page | R$38 | R$1.00 | R$15.00 | R$16.00 | 58% |
| **Blended average** | -- | -- | -- | -- | **55%** |

**Decision**: Premium tier is profitable but labor-intensive. Start Basic-only (AI-Only) at launch. Add Premium when demand validated and reviewer pool established.

---

## 6. Pricing Psychology

### 6.1 Anchoring Architecture

```
Factory R$3,997/mo ---- (anchor -- makes Studio look like a deal)
  |
Studio R$1,497/mo ---- (target -- agencies, highest LTV)
  |
Pro R$497/mo ---------- (volume -- individual creators, main revenue)
  |
Creator R$147/mo ------ (entry -- converts free to paid)
  |
Free R$0 -------------- (funnel -- proves value, captures leads)
```

### 6.2 Conversion Triggers (Free to Paid)

| Gate | Mechanism | Expected Conversion Lift |
|------|-----------|------------------------|
| Format gate | Free: no video, courses, landing pages | 15-25% |
| Volume gate | Free: ~15 credits/month | 20-30% |
| Brand gate | Free: generic output; Paid: custom brand_config injection | 12-18% |
| Speed gate | Free: 5min queue; Paid: instant | 5-10% |
| Watermark | Free: "Made with CEX" footer | 10-15% |

### 6.3 Why R$497 and Not R$500

- Odd pricing (R$497): perceived as "under R$500" -- psychological threshold effect
- Parcelamento: 12x R$41.42 (more palatable than 12x R$41.67)
- Matches existing CEX course pricing (Builder tier) -- pricing consistency

---

## 7. Revenue Projections (12 Months)

### 7.1 Monthly Revenue Model

| Month | Creator | Pro | Studio | Factory | Credit Packs | Total MRR |
|-------|---------|-----|--------|---------|-------------|----------|
| M01 | 15 x R$147 | 5 x R$497 | 1 x R$1,497 | 0 | R$800 | **R$6,392** |
| M03 | 22 x R$147 | 9 x R$497 | 2 x R$1,497 | 0 | R$1,600 | **R$12,311** |
| M06 | 38 x R$147 | 18 x R$497 | 5 x R$1,497 | 1 x R$3,997 | R$3,500 | **R$28,427** |
| M09 | 55 x R$147 | 28 x R$497 | 9 x R$1,497 | 2 x R$3,997 | R$6,000 | **R$49,435** |
| M12 | 78 x R$147 | 42 x R$497 | 15 x R$1,497 | 4 x R$3,997 | R$10,000 | **R$82,301** |

**Year 1 cumulative**: ~R$480,000

### 7.2 Revenue by Quality Tier (Projected Mix)

| Quarter | Basic (AI-Only) | Premium (Human-Reviewed) | Premium % |
|---------|----------------|------------------------|-----------|
| Q1 | 100% | 0% | Launch Basic only |
| Q2 | 85% | 15% | Introduce Premium |
| Q3 | 75% | 25% | Premium grows with trust |
| Q4 | 70% | 30% | Steady state |

---

## 8. Implementation Checklist

| # | Task | Owner | Status | Dependency |
|---|------|-------|--------|-----------|
| 1 | Credit system backend (integer, BRL centavos) | N05 | Planned | Supabase schema |
| 2 | Stripe subscription products (5 tiers) | N06 | Planned | Stripe MCP |
| 3 | MercadoPago/PIX for credit packs | N06 | Planned | MP integration |
| 4 | Usage tracking per format per user | N05 | Planned | Supabase |
| 5 | Overage billing automation | N05 | Planned | Stripe webhooks |
| 6 | Free tier rate limiting | N05 | Planned | Credit system |
| 7 | Pricing page (landing) | N03 | Planned | This artifact |
| 8 | Premium reviewer onboarding flow | N06 | Future | Demand validation |

---

*Generated by N06 Commercial Nucleus -- Content Factory Pricing v2.0*
*Cost basis: validated stack. Margins: 76-93% (Basic), 55-65% (Premium).*
*Zero infrastructure overhead. Every credit has ROI.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_content_factory_pricing]] | sibling | 0.44 |
| [[n06_roi_content_factory]] | sibling | 0.40 |
| [[kc_pricing_strategy]] | upstream | 0.33 |
| [[n06_funnel_content_factory]] | sibling | 0.28 |
| [[n06_report_intent_resolution_moat]] | sibling | 0.25 |
| [[n04_output_monetization_curriculum]] | upstream | 0.24 |
| [[p01_kc_commercial_nucleus]] | upstream | 0.22 |
| [[p08_pat_pricing_framework]] | upstream | 0.22 |
| [[n06_intent_resolution_depth_spec]] | sibling | 0.21 |
| [[p03_sp_content_monetization_builder]] | upstream | 0.21 |
