---
id: n06_content_factory_pricing
kind: content_monetization
8f: F6_produce
pillar: P11
title: "Content Factory Pricing -- Per-Format Tiers, Margins & Revenue Model"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: content-factory-pricing
quality: 8.9
tags: [pricing, content-factory, per-format, tiers, margins, revenue, monetization]
tldr: "Per-format pricing for Content Factory outputs. 9 format types, 3 tiers (Free/Pro/Enterprise), real cost basis from validated stack, margin analysis per output, a-la-carte + bundle economics, revenue projections by format mix."
density_score: 0.95
depends_on:
  - spec_content_factory_v1
  - output_content_factory_business_model
  - n06_strategy_claude_native
linked_artifacts:
  primary: output_content_factory_business_model
  related:
    - spec_content_factory_v1
    - n06_strategy_claude_native
    - p08_pat_pricing_framework
    - n06_kc_content_monetization
related:
  - n06_pricing_content_factory
  - n06_roi_content_factory
  - kc_pricing_strategy
  - n06_integration_content_factory
  - n06_funnel_content_factory
  - n06_funnel_cex_product
  - p01_kc_runway_api
  - kc_credit_system_design
  - n06_api_access_pricing
  - n06_input_schema_content_order
---

# Content Factory Pricing -- Per-Format Tiers, Margins & Revenue Model

> Every output has a cost. Every cost has a margin. Every margin has a ceiling.
> This artifact maps the economics of each Content Factory format so pricing
> decisions are data-driven, not gut-feel.

---

## 1. Cost Basis per Format (Validated Stack, April 2026)

Source: `_docs/specs/spec_content_factory_v1.md` (section: Stack Validada)

### 1.1 Direct Production Costs

| # | Format | LLM Tokens | API Calls | Infra Cost | Total Cost/Unit | Notes |
|---|--------|-----------|-----------|-----------|----------------|-------|
| 1 | **Blog post** (1500 words) | ~4K input + 6K output | 1 Claude call | R$0.00 | **R$0.55** | Pure LLM, no external API |
| 2 | **Social media set** (5 platforms) | ~3K input + 5K output | 1 Claude + 1 Canva create + 5 Canva exports | R$0.00 | **R$1.40** | Canva API included in subscription |
| 3 | **Video script** (90s short-form) | ~2K input + 3K output | 1 Claude call | R$0.00 | **R$0.35** | Script only, no production |
| 4 | **Video produced** (90s short-form) | ~5K tokens | Claude + ElevenLabs TTS + FFmpeg | R$2.50 TTS | **R$3.25** | ElevenLabs narration is main cost driver |
| 5 | **Video produced** (5min long-form) | ~8K tokens | Claude + ElevenLabs + FFmpeg | R$6.00 TTS | **R$7.20** | 45K chars narration |
| 6 | **Podcast episode** (15min) | ~6K tokens | Claude outline + NotebookLM Audio Overview | R$0.00 | **R$0.80** | NotebookLM is free (PRO account) |
| 7 | **Course module** (script+slides+quiz) | ~15K tokens | Claude + Marp/Canva + quiz gen | R$1.20 slides | **R$3.40** | High value, moderate cost |
| 8 | **eBook chapter** (3000 words) | ~5K input + 10K output | Claude + Typst/Pandoc | R$0.00 | **R$1.10** | Pure LLM + local tooling |
| 9 | **Presentation** (15 slides) | ~6K tokens | Claude + Canva create + export PPTX | R$0.00 | **R$1.20** | Canva in subscription |
| 10 | **Email sequence** (5 emails) | ~4K input + 8K output | 1-2 Claude calls | R$0.00 | **R$0.70** | Pure LLM |
| 11 | **Landing page** (HTML) | ~5K input + 12K output | 1-2 Claude calls | R$0.00 | **R$1.00** | Tailwind + responsive |

### 1.2 Full Brief Cost (All Formats)

| Bundle | Formats Included | Total Direct Cost | Value to Customer |
|--------|-----------------|-------------------|-------------------|
| **Lite** | Blog + social set + email sequence | R$2.65 | R$1,500+ in freelancer hours |
| **Standard** | Lite + video 90s + podcast + presentation | R$8.10 | R$5,000+ in production costs |
| **Complete** | Standard + course module + eBook chapter + landing page | R$12.60 | R$12,000+ in agency fees |
| **Full Factory** | Complete + video 5min + extra social | R$21.20 | R$20,000+ equivalent |

---

## 2. Per-Format Pricing Tiers

### 2.1 A-la-Carte Pricing (credit-based)

1 credit = R$1.00 (integer, no decimals). Minimum purchase: 50 credits.

| # | Format | Credits (Free) | Credits (Pro) | Credits (Enterprise) | Cost Basis | Pro Margin |
|---|--------|---------------|--------------|---------------------|-----------|-----------|
| 1 | Blog post | 5/month free | 8 credits | 6 credits | R$0.55 | 93% |
| 2 | Social media set (5 platforms) | 2/month free | 12 credits | 9 credits | R$1.40 | 88% |
| 3 | Video script only | 3/month free | 5 credits | 4 credits | R$0.35 | 93% |
| 4 | Video produced (90s) | -- | 25 credits | 18 credits | R$3.25 | 87% |
| 5 | Video produced (5min) | -- | 45 credits | 32 credits | R$7.20 | 84% |
| 6 | Podcast episode | 1/month free | 10 credits | 7 credits | R$0.80 | 92% |
| 7 | Course module | -- | 30 credits | 22 credits | R$3.40 | 89% |
| 8 | eBook chapter | 1/month free | 10 credits | 7 credits | R$1.10 | 89% |
| 9 | Presentation (15 slides) | 1/month free | 12 credits | 9 credits | R$1.20 | 90% |
| 10 | Email sequence (5 emails) | 2/month free | 8 credits | 6 credits | R$0.70 | 91% |
| 11 | Landing page | -- | 15 credits | 11 credits | R$1.00 | 93% |

**Free tier strategy**: Limited outputs to demonstrate value. Enough to produce 1 blog + 1 social set + 1 podcast per month. Converts by showing what Pro unlocks (video, courses, landing pages).

### 2.2 Subscription Tiers (Monthly Bundles)

| Tier | Price BRL | Price USD | Credits/Month | Overage Rate | Target ICP |
|------|----------|----------|--------------|-------------|-----------|
| **Free** | R$0 | $0 | ~15 credits equivalent (capped per format) | N/A | Developers exploring |
| **Creator** | R$147/month | $29/month | 150 credits | R$1.20/credit | Solo infoproducers |
| **Pro** | R$497/month | $99/month | 600 credits | R$1.00/credit | Active content creators |
| **Studio** | R$1,497/month | $297/month | 2,000 credits | R$0.85/credit | Agencies, teams |
| **Factory** | R$3,997/month | $799/month | 6,000 credits + API access | R$0.70/credit | Enterprise, white-label |

### 2.3 Credit Pack Purchases (One-Time Top-Ups)

| Pack | Credits | Price BRL | Price USD | Per-Credit Cost | Discount vs Overage |
|------|---------|----------|----------|----------------|-------------------|
| Starter | 50 | R$60 | $12 | R$1.20 | 0% (baseline) |
| Standard | 200 | R$200 | $40 | R$1.00 | 17% |
| Pro | 500 | R$425 | $85 | R$0.85 | 29% |
| Bulk | 1,000 | R$750 | $150 | R$0.75 | 37% |
| Enterprise | 5,000 | R$3,250 | $650 | R$0.65 | 46% |

---

## 3. Bundle Economics

### 3.1 Pre-Built Content Bundles (One-Click)

| Bundle | Formats | Credits Required | Suggested Price | Savings vs A-la-Carte |
|--------|---------|-----------------|----------------|----------------------|
| **Launch Kit** | Blog + social set + email + landing page | 43 credits | 35 credits | 19% |
| **Course Pack** | 8 modules + quiz + certificate page | 240 credits | 195 credits | 19% |
| **Full Campaign** | Video 90s + social set + email + blog + landing | 65 credits | 52 credits | 20% |
| **eBook Complete** | 8 chapters + cover + landing page | 95 credits | 75 credits | 21% |
| **Podcast Series** | 4 episodes + social promotion + landing | 60 credits | 48 credits | 20% |
| **Full Factory Brief** | ALL formats (1 topic, 11 outputs) | ~180 credits | 140 credits | 22% |

### 3.2 Annual Discount

| Tier | Monthly | Annual (per month) | Annual Total | Savings |
|------|---------|-------------------|-------------|---------|
| Creator | R$147 | R$117 | R$1,404 | 20% (2.4 months free) |
| Pro | R$497 | R$397 | R$4,764 | 20% |
| Studio | R$1,497 | R$1,197 | R$14,364 | 20% |
| Factory | R$3,997 | R$3,197 | R$38,364 | 20% |

---

## 4. Margin Analysis by Tier

### 4.1 Worst-Case Credit Utilization (100% usage, heaviest formats)

| Tier | Monthly Revenue | Max Credits | If ALL Spent on Video 5min (R$7.20 cost) | Margin |
|------|----------------|------------|------------------------------------------|--------|
| Creator (R$147) | R$147 | 150 | 150/45 = 3.3 videos = R$23.76 cost | **84%** |
| Pro (R$497) | R$497 | 600 | 600/45 = 13.3 videos = R$95.76 cost | **81%** |
| Studio (R$1,497) | R$1,497 | 2,000 | 2000/45 = 44.4 videos = R$319.68 cost | **79%** |
| Factory (R$3,997) | R$3,997 | 6,000 | 6000/45 = 133.3 videos = R$959.76 cost | **76%** |

### 4.2 Expected-Case (Typical Format Mix)

Typical mix: 40% text-only (blog, email, scripts) + 30% visual (social, slides, landing) + 20% audio (podcast) + 10% video (produced).

| Tier | Revenue | Expected Cost (typical mix) | Expected Margin | Gross Profit |
|------|---------|---------------------------|----------------|-------------|
| Creator | R$147 | R$12.80 | **91%** | R$134.20 |
| Pro | R$497 | R$48.00 | **90%** | R$449.00 |
| Studio | R$1,497 | R$152.00 | **90%** | R$1,345.00 |
| Factory | R$3,997 | R$432.00 | **89%** | R$3,565.00 |

### 4.3 Break-Even Analysis

| Tier | Monthly Revenue | Fixed Costs (infra) | Variable Cost Floor | Break-Even Customers |
|------|----------------|--------------------|--------------------|---------------------|
| Creator | R$147 | R$0 (user's machine) | R$12.80/customer | 1 (already profitable) |
| Pro | R$497 | R$0 | R$48.00/customer | 1 |
| Studio | R$1,497 | R$500 (support) | R$152.00/customer | 1 |
| Factory | R$3,997 | R$2,000 (SLA+support) | R$432.00/customer | 1 |

**Key insight**: Because CEX runs on the user's Claude Code subscription, our infrastructure cost is R$0. The only variable cost is API calls (ElevenLabs, Canva). This creates near-zero marginal cost at scale.

---

## 5. Revenue Projections by Format (12 Months)

### 5.1 Assumptions

| Variable | Value | Source |
|----------|-------|--------|
| Month 1 subscribers | 15 Creator + 5 Pro + 1 Studio | Conservative |
| Monthly growth | 18% | Industry average for dev tools |
| Format mix | 40/30/20/10 (text/visual/audio/video) | Estimated |
| Credit utilization | 65% of allocation (industry avg) | SaaS benchmark |
| Churn | 6% monthly | Dev tool average |
| Upsell rate | 8% monthly (Creator->Pro, Pro->Studio) | Estimated |

### 5.2 Monthly Revenue Projection

| Month | Creator | Pro | Studio | Factory | Credit Packs | Total MRR |
|-------|---------|-----|--------|---------|-------------|----------|
| M01 | 15 x R$147 | 5 x R$497 | 1 x R$1,497 | 0 | R$800 | **R$6,392** |
| M03 | 22 x R$147 | 9 x R$497 | 2 x R$1,497 | 0 | R$1,600 | **R$12,311** |
| M06 | 38 x R$147 | 18 x R$497 | 5 x R$1,497 | 1 x R$3,997 | R$3,500 | **R$28,427** |
| M09 | 55 x R$147 | 28 x R$497 | 9 x R$1,497 | 2 x R$3,997 | R$6,000 | **R$49,435** |
| M12 | 78 x R$147 | 42 x R$497 | 15 x R$1,497 | 4 x R$3,997 | R$10,000 | **R$82,301** |

**Year 1 total**: ~R$480,000 (cumulative, subscription + credit packs)

### 5.3 Revenue by Format Type (Year 1 Estimate)

Based on credit consumption patterns:

| Format Category | % of Credits Used | Est. Revenue Attributed | Growth Driver |
|----------------|-------------------|----------------------|--------------|
| Text (blog, email, script) | 40% | R$192,000 | Volume, low cost, high frequency |
| Visual (social, slides, landing) | 30% | R$144,000 | Social media demand, agency upsell |
| Audio (podcast, narration) | 20% | R$96,000 | NotebookLM free tier, growing podcast market |
| Video (produced) | 10% | R$48,000 | Highest credit cost, premium feature lock-in |

---

## 6. Pricing Psychology & Conversion Triggers

### 6.1 Anchoring Strategy

```
Factory R$3,997/mo (anchor -- makes Studio look reasonable)
  |
  v
Studio R$1,497/mo (target -- agencies, highest LTV)
  |
  v
Pro R$497/mo (volume -- individual creators)
  |
  v
Creator R$147/mo (entry -- converts free to paid)
  |
  v
Free R$0 (funnel -- proves value)
```

### 6.2 Conversion Triggers (Free -> Paid)

| Trigger | Mechanism | Expected Lift |
|---------|-----------|--------------|
| Format gate | Free cannot produce video/courses/landing pages | 15-25% conversion |
| Quality gate | Free outputs have "Made with CEX" watermark | 10-15% conversion |
| Volume gate | Free limited to ~15 credits/month | 20-30% conversion |
| Speed gate | Free queued (5min delay), paid instant | 5-10% conversion |
| Brand gate | Free uses generic brand, paid injects custom brand_config | 12-18% conversion |

### 6.3 Upsell Triggers (Creator -> Pro -> Studio)

| From | To | Trigger | Expected Rate |
|------|-----|---------|-------------|
| Creator | Pro | Hit credit limit 2 months in a row | 12%/month |
| Pro | Studio | Need 2+ brand configs (agency scenario) | 8%/month |
| Studio | Factory | Need API access or white-label | 3%/month |
| Any | Credit Pack | One-time burst need (course launch, campaign) | 15%/month |

---

## 7. Competitive Pricing Comparison

| Feature | CEX Free | CEX Pro (R$497) | Jasper ($69) | Coursebox ($210) | HeyGen ($99) |
|---------|---------|----------------|-------------|-----------------|-------------|
| Blog posts | 5/mo | 75/mo | Unlimited | -- | -- |
| Social sets | 2/mo | 50/mo | Limited | -- | -- |
| Video scripts | 3/mo | 120/mo | -- | -- | -- |
| Video produced | -- | 13/mo | -- | -- | 30 min/mo |
| Course modules | -- | 20/mo | -- | 10/mo | -- |
| Podcast | 1/mo | 60/mo | -- | -- | -- |
| eBook chapters | 1/mo | 60/mo | -- | -- | -- |
| Brand injection | -- | 1 brand | -- | Basic | -- |
| Multi-format pipeline | -- | YES | NO | NO | NO |
| **Monthly cost** | **R$0** | **R$497** | **R$380** | **R$1,155** | **R$545** |

**Positioning**: "You already pay R$1,200+/month for 3 separate tools that don't talk to each other. CEX Pro gives you ALL formats from 1 brief for R$497/month."

---

## 8. Implementation Checklist

| # | Task | Owner | Status | Dependency |
|---|------|-------|--------|-----------|
| 1 | Credit system (integer, BRL centavos) | N05 | Planned | KC content_monetization |
| 2 | Stripe subscription products (5 tiers) | N06 | Planned | Stripe MCP |
| 3 | MercadoPago credit pack checkout (PIX) | N06 | Planned | MP MCP |
| 4 | Usage tracking per format per user | N05 | Planned | Supabase |
| 5 | Overage billing automation | N05 | Planned | Stripe webhooks |
| 6 | Free tier rate limiting | N05 | Planned | Credit system |
| 7 | Pricing page (landing) | N03 | Planned | This artifact |
| 8 | A/B test Creator R$147 vs R$127 | N06 | Future | 30 days post-launch |

---

*Generated by N06 Commercial Nucleus -- Content Factory Pricing*
*Cost basis: validated stack (spec_content_factory_v1.md). Margins: 76-93% depending on format mix.*
*Every credit has a cost. Every tier has a margin. Zero infrastructure overhead.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_pricing_content_factory]] | sibling | 0.56 |
| [[n06_roi_content_factory]] | sibling | 0.35 |
| [[kc_pricing_strategy]] | upstream | 0.30 |
| [[n06_integration_content_factory]] | sibling | 0.29 |
| [[n06_funnel_content_factory]] | sibling | 0.28 |
| [[n06_funnel_cex_product]] | sibling | 0.27 |
| [[p01_kc_runway_api]] | upstream | 0.26 |
| [[kc_credit_system_design]] | upstream | 0.26 |
| [[n06_api_access_pricing]] | sibling | 0.24 |
| [[n06_input_schema_content_order]] | upstream | 0.24 |
