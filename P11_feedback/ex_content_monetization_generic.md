---
id: ex_content_monetization_generic
kind: content_monetization
pillar: P11
version: 1.0.0
title: "Content Monetization Framework -- D2C Ecommerce Funnel"
description: "Content-to-revenue funnel for D2C ecommerce brands. Maps content pillars to funnel stages, engagement targets, CTA types, and product mention rules. Generic template with {{BRAND_*}} placeholders."
domain: content_monetization
nucleus: N06
quality: null
tags: [content-monetization, funnel, ecommerce, cta, attribution, d2c, revenue]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_VERTICAL
  - BRAND_PRODUCT_CATALOG
  - BRAND_UTM_SOURCE
  - BRAND_MONTHLY_VISITORS
  - BRAND_AOV
  - BRAND_CONVERSION_RATE
  - BRAND_PERSONA_NAME
---

# Content Monetization Framework -- D2C Ecommerce Funnel

> Generic funnel map for {{BRAND_NAME}} in the {{BRAND_VERTICAL}} vertical.
> Replace example metrics with your brand data. Metric ranges are illustrative.

---

## 1. Funnel Architecture

```
AWARENESS (30%)         CONSIDERATION (40%)     CONVERSION (20%)        RETENTION (10%)
~30% of content         ~40% of content         ~20% of content         ~10% of content

Goal: REACH             Goal: TRUST             Goal: PURCHASE          Goal: REPEAT
KPI: impressions,       KPI: saves, profile     KPI: clicks,            KPI: reorder rate,
     shares, new        visits, blog time-on-   add-to-cart,            NPS, UGC
     followers          page                    checkout starts         submissions
```

---

## 2. Stage 1: AWARENESS (~30% of content budget)

### Content Types

| Type | Format | Frequency | Goal |
|------|--------|-----------|------|
| Memes / relatable humor | Reel 7-15s | 2x/week | Shares, discovery |
| Trending audio Reels | Reel 7-15s | 1x/week | Algorithm reach |
| Educational facts | Carousel 5-7 slides | 1x/week | Saves + shares |
| Seasonal hooks | Carousel or Reel | Per calendar | Topical relevance |

### Engagement Targets (example ranges)

| Metric | Example range | Your target |
|--------|--------------|-------------|
| Reach per post | 3-5x follower count | (your data) |
| Share rate | 2-4% of reach | (your data) |
| New followers/week | 150-600 | (your data) |

### CTA Rules (Awareness)

- **Follow** on every awareness post
- **Share** on humor/meme content
- **Save** on educational content
- NEVER: product links (kills shareability at awareness stage)

---

## 3. Stage 2: CONSIDERATION (~40% of content budget)

### Content Types

| Type | Format | Goal |
|------|--------|------|
| Product demos | Reel 30-60s | Product page visits |
| Before/after or comparison | Carousel | Trust + authority |
| AI persona ({{BRAND_PERSONA_NAME}}) | Q&A Reel or Stories | Brand differentiation |
| Educational long-form | Blog 800-1500w | SEO + qualified traffic |

### Engagement Targets

| Metric | Example range | Your target |
|--------|--------------|-------------|
| Blog time-on-page | 3-5 min | (your data) |
| Profile visit rate | 5-10% of reach | (your data) |
| Link-in-bio CTR | 1-3% | (your data) |

### CTA Rules (Consideration)

- Link in bio to product catalog or blog
- "Ver mais" / "Saiba mais" to specific product page
- Save for later (educational content)
- AI persona chat link

---

## 4. Stage 3: CONVERSION (~20% of content budget)

### Content Types

| Type | Format | Goal |
|------|--------|------|
| Limited offer / promo | Reel + Stories | Purchase with urgency |
| UGC / testimonials | Repost | Social proof -> conversion |
| Product bundles | Carousel | AOV uplift |
| Affiliate codes | Stories | Tracked conversion |

### Conversion Metrics (example ranges)

| Metric | Example range | Your target |
|--------|--------------|-------------|
| {{BRAND_DOMAIN}} monthly visitors | 5,000-50,000 | {{BRAND_MONTHLY_VISITORS}} |
| Avg order value | R$80-300 | {{BRAND_AOV}} |
| Conversion rate | 1.5-3.5% | {{BRAND_CONVERSION_RATE}} |
| Cart abandonment | 65-80% | (your data) |

### UTM Convention

```
utm_source={{BRAND_UTM_SOURCE}}
utm_medium=social|blog|email
utm_campaign={content_pillar}_{month}
utm_content={post_id}
```

---

## 5. Stage 4: RETENTION (~10% of content budget)

### Retention Levers

| Lever | Tactic | Expected impact |
|-------|--------|-----------------|
| Reorder prompt | Email/WhatsApp 30 days post-purchase | +15-25% reorder rate |
| Partner upsell | B2B invite after 2nd purchase | Channel diversification |
| UGC campaign | Branded hashtag + repost | Organic reach + social proof |
| Loyalty program | Points / early access | LTV increase |

---

## 6. Product Mention Rules

| Stage | Product mention rule |
|-------|---------------------|
| Awareness | NONE -- brand implicit only |
| Consideration | Mention product category, not specific SKU |
| Conversion | Specific SKU + direct product link |
| Retention | Personalized based on past purchase |

---

## 7. Revenue Model

| Revenue stream | Source | Example benchmark |
|----------------|--------|-------------------|
| D2C sales | Own website + marketplace | Core revenue |
| B2B/wholesale | Partner program | 20-40% of revenue at scale |
| Affiliate commissions | Partner program | 5-15% affiliate share |
| Content IP | Templates, training | Optional secondary |

---

## 8. Content ROI Formula

```
Monthly content revenue = Monthly visitors
  x Conversion rate
  x AOV
  = Example: 10,000 x 2% x R$150 = R$30,000/month

Content cost = Team hours x hourly rate + tools
Break-even = Content cost / (Conversion rate x AOV)
```

---

## New Brand Variables

- `BRAND_UTM_SOURCE` -- primary UTM source (e.g. instagram, blog)
- `BRAND_MONTHLY_VISITORS` -- current monthly website visitors
- `BRAND_AOV` -- average order value in brand currency
- `BRAND_CONVERSION_RATE` -- current website conversion rate (%)
