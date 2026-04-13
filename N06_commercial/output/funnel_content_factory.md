---
id: n06_funnel_content_factory
kind: content_monetization
pillar: P11
title: "Content Factory Sales Funnel -- Free-to-Paid Conversion Pipeline"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: content-factory-funnel
quality: 8.9
tags: [funnel, content-factory, free-to-paid, lead-magnet, tripwire, core-offer, upsell, conversion]
tldr: "4-stage sales funnel for Content Factory: Lead magnet (free podcast/flashcards) -> Tripwire (single ebook R$19) -> Core offer (Full Content Pack R$147) -> Upsell (monthly subscription R$497/mo). Each stage has conversion targets, assets, copy hooks, and nucleus ownership."
density_score: 0.95
depends_on:
  - pricing_content_factory
  - spec_content_factory_v1
  - p08_pat_funnel_architecture
linked_artifacts:
  primary: pricing_content_factory
  related:
    - roi_content_factory
    - integration_content_factory
    - p08_pat_funnel_architecture
    - funnel_cex_product
---

# Content Factory Sales Funnel -- Free-to-Paid Conversion Pipeline

> The funnel IS the product demo. Each stage uses Content Factory to produce the
> deliverable that sells the next stage. The factory sells itself by showing what it makes.

---

## 1. Funnel Architecture

```
STRANGER (dev, creator, agency)
    |
    | Channels: GitHub, YouTube, LinkedIn, HackerNews
    |
    v
STAGE 1: LEAD MAGNET (R$0) -------- "Taste the output"
    |  Free audio overview (NotebookLM) or flashcard set
    |  Cost to produce: R$0.80 (podcast) or R$0.00 (flashcards)
    |  Gate: email capture
    |  Target: 500 leads/month
    |
    v
STAGE 2: TRIPWIRE (R$9-19) -------- "Low-risk first purchase"
    |  Single formatted eBook (PDF, 30 pages)
    |  Cost to produce: R$8.80 (8 chapters)
    |  Gate: credit card on file
    |  Target: 15% of leads = 75 purchases/month
    |
    v
STAGE 3: CORE OFFER (R$97-197) ---- "Full value demonstration"
    |  Full Content Pack: ALL 7 formats from 1 brief
    |  Cost to produce: R$15.60 (Full Factory Brief)
    |  Gate: experiencing the pipeline
    |  Target: 30% of tripwire = 22 purchases/month
    |
    v
STAGE 4: UPSELL (R$147-497/mo) ---- "Recurring revenue"
    |  Monthly Content Factory subscription
    |  Cost: per-credit usage (see pricing_content_factory.md)
    |  Gate: habit formation (3+ briefs executed)
    |  Target: 40% of core = 9 subscribers/month
    |
    v
RETAINED CUSTOMER (LTV: R$1,764-5,964)
```

---

## 2. Stage 1: Lead Magnet (R$0)

### 2.1 What the Customer Gets

**Option A: Free Audio Overview (Podcast)**
- 15-minute audio produced by NotebookLM Audio Overview
- Topic: "How to Turn 1 Brief into 7 Content Pieces"
- Format: MP3, playable on any device
- Production cost: R$0.80 (LLM outline + NotebookLM, free)
- Delivery: instant download after email capture

**Option B: Free Flashcard Set**
- 75+ flashcards generated from a knowledge card
- Topic: "Content Marketing Fundamentals" or "Course Creation in 30 Minutes"
- Format: digital (NotebookLM interactive) or PDF export
- Production cost: R$0.00 (NotebookLM generates from existing KC)
- Delivery: instant access after email capture

**Option C: Free Content Audit**
- AI-powered audit of customer's existing content
- Shows gaps: "You have blog posts but no video, no course, no podcast"
- Format: 1-page PDF report
- Production cost: R$0.55 (1 LLM call)
- Delivery: email within 5 minutes of submission

### 2.2 Why This Works

| Factor | Rationale |
|--------|-----------|
| **Zero risk** | Free removes all friction |
| **Product demo** | The lead magnet IS a Content Factory output -- customer experiences the quality |
| **Fast delivery** | Instant download = immediate gratification |
| **Email capture** | Enables nurture sequence (5 emails over 7 days) |
| **Low cost** | R$0.00-0.80 per lead -- scales infinitely |

### 2.3 Channels and Distribution

| Channel | CTA | Expected Volume | CAC |
|---------|-----|----------------|-----|
| GitHub README | "Get the free audio guide" | 100/month | R$0 (organic) |
| YouTube video description | "Free flashcards in bio" | 150/month | R$12 (content cost) |
| LinkedIn posts | "Download the content audit" | 80/month | R$0 (organic) |
| HackerNews/Reddit | "Free course creation guide" | 50/month | R$0 (organic) |
| Blog SEO | "Content Factory explained (free)" | 120/month | R$8 (content cost) |
| **Total** | | **500/month** | **R$4 blended CAC** |

### 2.4 Email Nurture Sequence (Post Lead Magnet)

| Day | Email | Subject Line | CTA |
|-----|-------|-------------|-----|
| 0 | Welcome + delivery | "Your [podcast/flashcards] -- ready" | Download link |
| 1 | Social proof | "How [Name] turned 1 KC into a full course" | Read case study |
| 3 | Education | "The 7 formats you're not creating (and why)" | Watch 90s demo |
| 5 | Tripwire offer | "Your first eBook for R$19 (normally R$47)" | Buy tripwire |
| 7 | Scarcity | "24h left: R$19 eBook -- your topic, your brand" | Buy tripwire |

**Expected conversion (lead to tripwire)**: 15% (industry avg for dev tools: 8-12%, our advantage: product demo as lead magnet)

---

## 3. Stage 2: Tripwire (R$9-19)

### 3.1 What the Customer Gets

**Product: Single Formatted eBook**
- 30 pages, professionally typeset (Typst/Pandoc)
- Customer provides: topic + target audience (2-sentence brief)
- Content Factory produces: 8 chapters, cover page, table of contents, PDF + EPUB
- Includes: {{BRAND_*}} injection if customer has brand_config
- Delivery: 15-30 minutes after purchase

### 3.2 Pricing Psychology

| Price Point | Rationale |
|-------------|-----------|
| **R$9** (introductory) | Below "decision threshold" -- impulse buy territory |
| **R$19** (standard) | Still trivial but establishes payment habit |
| **R$47** (anchor/strikethrough) | Shown crossed out: "~~R$47~~ R$19 this week" |

**Why R$19, not R$29?**
- R$19 = no "let me think about it" friction
- Credit card goes on file (critical for upsell)
- R$19 on Stripe = R$18.05 after fee. Our cost: R$8.80. **Margin: 51%.**
- The tripwire doesn't need to be profitable. Its job is to create a BUYER.

### 3.3 Tripwire Variants (A/B Test)

| Variant | Format | Price | Expected Conversion |
|---------|--------|-------|-------------------|
| A | eBook (PDF+EPUB) | R$19 | 15% (baseline) |
| B | Video script (ready to record) | R$9 | 18% (lower price) |
| C | Social media kit (30 posts) | R$14 | 12% (niche appeal) |

### 3.4 Delivery Experience

```
Customer pays R$19
  |
  v
Stripe webhook fires -> Content Factory receives brief
  |
  v
8F pipeline runs (F1-F8, ~15 minutes)
  |
  v
Customer receives email:
  "Your eBook '{{TOPIC}}' is ready!"
  [Download PDF] [Download EPUB]
  
  "Loved it? Get ALL 7 formats from this same brief."
  [See Content Pack -- R$97] <-- Core Offer CTA
```

---

## 4. Stage 3: Core Offer (R$97-197)

### 4.1 What the Customer Gets

**Product: Full Content Pack**

From 1 brief, the customer receives ALL 7+ formats:

| # | Format | Specs | Value if Freelanced |
|---|--------|-------|-------------------|
| 1 | Course outline (8 modules) | Scripts + learning objectives | R$2,000 |
| 2 | eBook (30 pages, PDF+EPUB) | 8 chapters, formatted, cover | R$1,500 |
| 3 | Video demo (90s short-form) | Script + storyboard + produced MP4 | R$800 |
| 4 | Podcast episode (15min) | Audio overview via NotebookLM | R$500 |
| 5 | Presentation (15 slides, PPTX+PDF) | Canva/Marp, speaker notes | R$600 |
| 6 | Social campaign (5 platforms, 7 days) | Posts + Canva graphics | R$1,200 |
| 7 | Landing page (HTML, responsive) | Tailwind, dark mode, CTA | R$1,500 |
| **Total** | | | **R$8,100** |

**Price: R$97 (introductory) / R$147 (standard) / R$197 (premium + brand config)**

### 4.2 Pricing Tiers within Core Offer

| Tier | Price | Includes | Target |
|------|-------|---------|--------|
| **Essential** | R$97 | 7 formats, AI-only, generic brand | Budget buyers |
| **Professional** | R$147 | 7 formats, AI-only, custom brand_config injected | Most buyers |
| **Premium** | R$197 | 7 formats, human-reviewed, brand + revision cycle | Quality-focused |

**Decoy effect**: Essential exists to make Professional look like a deal. Professional is the target.

### 4.3 Conversion Mechanics

| Trigger | Mechanism | Expected Impact |
|---------|-----------|----------------|
| **Anchoring** | "R$8,100 value for R$147" | 25%+ conversion lift |
| **Social proof** | "327 Content Packs delivered this month" | 15% lift |
| **Urgency** | "Price increases to R$197 in 72h" | 10% lift (use sparingly) |
| **Guarantee** | "Hate it? Full refund, keep the content" | 20% lift (reduces risk) |
| **Demonstration** | Tripwire was 1 format. Core is 7. Customer already saw quality. | 30%+ lift |

**Expected conversion (tripwire to core)**: 30% (high because tripwire pre-qualified the buyer)

---

## 5. Stage 4: Upsell -- Monthly Subscription (R$147-497/mo)

### 5.1 What the Customer Gets

**Product: Content Factory Subscription**

| Feature | Creator R$147/mo | Pro R$497/mo |
|---------|-----------------|-------------|
| Credits/month | 150 | 600 |
| Full Factory Briefs (~140 credits each) | ~1/month | ~4/month |
| A-la-carte formats | YES | YES |
| Brand config injection | 1 brand | 3 brands |
| Priority processing | NO | YES |
| Premium (human-reviewed) | Add-on | 2/month included |
| API access | NO | YES |

### 5.2 Subscription Conversion Triggers

| Trigger | When | Conversion Rate |
|---------|------|----------------|
| **Habit formation** | Customer purchased 3+ Content Packs | 40% |
| **ROI realization** | Customer sees R$8,100 value for R$147 | 35% |
| **Convenience** | "Stop buying packs -- subscribe and save" | 25% |
| **Feature gate** | "Subscribers get brand injection + priority" | 20% |

### 5.3 Retention Strategy

| Month | Action | Goal |
|-------|--------|------|
| 1 | Onboarding email sequence (5 emails) | First brief within 24h |
| 2 | "Your month in review" report | Show ROI: hours saved, content produced |
| 3 | Feature unlock: Premium review (1 free) | Demonstrate Premium value |
| 4 | Community invite (Discord/Slack) | Social lock-in |
| 5 | Annual discount offer: "Lock in 20% savings" | Convert to annual |
| 6+ | Monthly content ideas email | Reduce "nothing to create" churn |

**Target churn**: <6%/month. **LTV at 6% churn**: R$147/0.06 = R$2,450 (Creator) or R$497/0.06 = R$8,283 (Pro).

---

## 6. Funnel Economics

### 6.1 Unit Economics per Funnel Pass

| Stage | Volume/Mo | Revenue | Cost | Gross Profit |
|-------|-----------|---------|------|-------------|
| Lead Magnet | 500 leads | R$0 | R$400 (content + hosting) | -R$400 |
| Tripwire | 75 purchases | R$1,425 | R$660 (production) | R$765 |
| Core Offer | 22 purchases | R$3,234 | R$343 (production) | R$2,891 |
| Subscription | 9 new subs | R$2,655/mo (recurring) | R$230/mo | R$2,425/mo |
| **Total** | | **R$7,314 one-time + R$2,655 MRR** | | |

### 6.2 Blended CAC and LTV

| Metric | Value | Benchmark |
|--------|-------|-----------|
| Cost per lead | R$4.00 | Industry: R$15-30 |
| Cost per tripwire buyer | R$26.67 | Industry: R$50-100 |
| Cost per core buyer | R$88.89 | Industry: R$150-300 |
| Cost per subscriber | R$222.22 | Industry: R$300-500 |
| Blended LTV (all stages) | R$5,367 | Calculated: tripwire + core + 12mo subscription |
| LTV:CAC ratio | **24:1** | Target: >3:1 |

### 6.3 Monthly Revenue Projection (Funnel at Scale)

| Month | New Leads | Tripwire | Core | New Subs | Cumulative Subs | MRR |
|-------|-----------|---------|------|---------|----------------|-----|
| M01 | 500 | 75 | 22 | 9 | 9 | R$2,655 |
| M03 | 750 | 112 | 34 | 14 | 35 | R$8,820 |
| M06 | 1,200 | 180 | 54 | 22 | 78 | R$21,060 |
| M09 | 1,800 | 270 | 81 | 32 | 130 | R$37,440 |
| M12 | 2,500 | 375 | 112 | 45 | 195 | R$58,500 |

**Year 1 total revenue**: ~R$380,000 (one-time purchases + cumulative MRR)

---

## 7. Funnel Assets by Nucleus

| Asset | Owner | Format | Status |
|-------|-------|--------|--------|
| Lead magnet: podcast | N04 (NotebookLM) | .mp3 | Build with existing pipeline |
| Lead magnet: flashcards | N04 (NotebookLM) | digital | Build with existing pipeline |
| Lead magnet: content audit | N06 + N03 | PDF report | Template needed |
| Tripwire: eBook template | N03 (Typst/Pandoc) | PDF+EPUB | Existing: fn_cf_ebook_compile |
| Core: Full Content Pack workflow | N03 (DAG master) | Multi-format | Existing: dag_cf_master |
| Nurture emails (5) | N02 (copy) | Email HTML | Template needed |
| Landing page: tripwire | N03 | HTML | Template: landing-page-builder |
| Landing page: core offer | N03 | HTML | Template: landing-page-builder |
| Checkout: Stripe integration | N05 | API | Stripe MCP configured |
| Checkout: Hotmart (courses) | N06 | API | Hotmart MCP configured |

---

## 8. A/B Test Plan (Month 1-3)

| Test | Variant A | Variant B | Metric | Duration |
|------|-----------|-----------|--------|---------|
| Lead magnet format | Podcast audio | Flashcard set | Email capture rate | 2 weeks |
| Tripwire price | R$9 | R$19 | Revenue per lead | 2 weeks |
| Core offer price | R$97 | R$147 | Conversion rate x revenue | 4 weeks |
| Subscription CTA timing | Email day 5 | Email day 10 | Sub conversion rate | 4 weeks |
| Landing page headline | "1 Brief, 7 Outputs" | "Replace Your Agency" | Click-through rate | 2 weeks |

---

*Generated by N06 Commercial Nucleus -- Content Factory Funnel*
*The funnel sells itself: each stage is a Content Factory output.*
*Lead cost: R$4. LTV: R$5,367. LTV:CAC = 24:1.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**
