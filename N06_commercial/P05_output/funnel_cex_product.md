---
id: n06_funnel_cex_product
kind: content_monetization
pillar: P11
title: "CEX Product Conversion Funnel -- AIDA Framework Applied"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: product-funnel
quality: 8.9
tags: [funnel, AIDA, conversion, cex-product, acquisition, monetization]
tldr: "Specific AIDA conversion funnel for CEX-as-product. 4 stages with exact touchpoints, content assets, metrics, and ownership. Not a generic pattern -- this is the executable funnel for launching CEX commercially."
density_score: 0.94
depends_on:
  - p08_pat_funnel_architecture
  - n06_strategy_claude_native
  - n06_content_factory_pricing
  - n06_api_access_pricing
linked_artifacts:
  primary: p08_pat_funnel_architecture
  related:
    - n06_strategy_claude_native
    - n06_content_factory_pricing
    - output_content_factory_business_model
    - n06_monetization_audit_2026_04_08
---

# CEX Product Conversion Funnel -- AIDA Framework Applied

> This is not a generic funnel template. This is THE funnel for launching CEX
> as a commercial product. Every stage has specific assets, channels, metrics,
> and conversion triggers mapped to CEX's actual product offering.

---

## 1. Funnel Overview

```
AWARENESS                    INTEREST                     DECISION                    ACTION
(Stranger -> Visitor)        (Visitor -> Lead)            (Lead -> Prospect)          (Prospect -> Customer)
                                                                                      
GitHub README                Free tier (/init)            Pricing page                Checkout (Stripe/MP)
YouTube shorts               Content Factory demo         Feature comparison          PIX payment
LinkedIn posts               eBook download (gated)       Case study (CEX-as-CEX)     Course enrollment
HackerNews "Show HN"         Newsletter signup            Free trial results          API key generation
Dev community posts          Discord/community join       ROI calculator              Annual commitment
SEO blog content             Template pack (free)         Testimonials                Upsell to next tier
                                                                                      
KPI: Qualified visitors      KPI: Signups/downloads       KPI: Pricing page visits    KPI: Conversion rate
Target: 5K/month             Target: 500/month (10%)      Target: 150/month (30%)     Target: 45/month (30%)
CAC contribution: R$0.50     CAC contribution: R$5.00     CAC contribution: R$15.00   CAC total: R$20.50
```

---

## 2. Stage 1: AWARENESS (Stranger -> Visitor)

**Goal**: Get qualified developers to discover CEX exists.

### 2.1 Channel Strategy

| Channel | Content Type | Frequency | Owner | Est. Traffic/Month |
|---------|-------------|-----------|-------|-------------------|
| **GitHub** | README + stars + SEO | Always-on | N05 | 2,000 visitors |
| **YouTube** | 90s demos + 15min tutorials | 2x/week | N02+N03 | 1,500 views |
| **LinkedIn** | Technical posts + build logs | 3x/week | N02 | 800 impressions |
| **HackerNews** | Show HN + comment threads | 1x/month (strategic) | N07 | 1,000 burst |
| **Twitter/X** | Build-in-public threads | Daily | N02 | 500 impressions |
| **Dev.to/Medium** | Long-form technical articles | 1x/week | N04 | 400 readers |
| **Reddit** | r/programming, r/artificial | 2x/month | N02 | 300 visitors |

### 2.2 Content Assets (AWARENESS)

| Asset | Format | Hook | CTA |
|-------|--------|------|-----|
| "CEX in 90 Seconds" | Video 9:16 | "5 words in, production-ready artifact out" | Link to GitHub |
| "I Built a Content Factory" | Blog + HN post | "1 brief = 11 outputs, zero intervention" | Link to repo |
| "123 Kinds of Knowledge" | LinkedIn carousel | "Most AI tools have 3 options. CEX has 123." | Link to docs |
| "8F Pipeline Explained" | YouTube tutorial | "Why your AI outputs are mediocre (and how to fix it)" | Subscribe + star |
| README.md | GitHub | Stars badge + feature matrix + quick demo | git clone |

### 2.3 Metrics & Targets

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| Monthly unique visitors | 500 | 2,000 | 5,000 | 12,000 |
| GitHub stars | 100 | 500 | 2,000 | 5,000 |
| YouTube subscribers | 50 | 200 | 800 | 2,500 |
| Total impressions | 5,000 | 25,000 | 80,000 | 200,000 |

---

## 3. Stage 2: INTEREST (Visitor -> Lead)

**Goal**: Convert visitors into engaged users who have tried CEX.

### 3.1 Conversion Mechanisms

| Mechanism | Trigger | What They Get | What We Get |
|-----------|---------|--------------|-------------|
| **git clone + /init** | "Try it free" CTA | Full CEX repo, free tier | Qualified user, brand_config data |
| **eBook download** | Gated landing page | "CEX in 30 Pages" PDF | Email address |
| **Newsletter signup** | Blog footer + YouTube desc | Weekly CEX insights | Email for nurture sequence |
| **Discord join** | Community CTA everywhere | Peer support + office hours | Community engagement data |
| **Free template pack** | After /init completion | 5 pre-built configs | Usage data, upgrade signal |
| **Content Factory demo** | "See it in action" CTA | 3 free briefs/month | Product experience |

### 3.2 Lead Magnets

| Lead Magnet | Format | Production Cost | Conversion Target |
|-------------|--------|----------------|-------------------|
| "CEX in 30 Pages" eBook | PDF (Typst) | R$0 (CF produces it) | 15% of landing page visitors |
| "5-Minute Quick Start" video | YouTube | R$0 (CF produces it) | 8% of video viewers |
| Free tier experience | Product trial | R$0 (user's machine) | 20% of git clones |
| "123 Kinds Cheat Sheet" | PDF 1-page | R$0 (CF produces it) | 12% of blog readers |
| Template starter pack | .md bundle | R$0 (already exists) | 10% of /init completions |

### 3.3 Email Nurture Sequence (5 emails, 10 days)

| Day | Subject | Content | CTA |
|-----|---------|---------|-----|
| 0 | "Your CEX brain is ready" | Welcome + quickstart link | Complete /init |
| 2 | "Your first artifact in 60 seconds" | Tutorial: /build knowledge_card | Try /build |
| 4 | "The 8F Pipeline (why your output is better now)" | Explains the value engine | Watch YouTube tutorial |
| 7 | "What 5 words can produce" | Case study: 5-word input -> full course | Try Content Factory |
| 10 | "Ready for more?" | Feature comparison: Free vs Pro | View pricing page |

### 3.4 Metrics & Targets

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| Git clones | 50 | 200 | 500 | 1,200 |
| Email signups | 30 | 150 | 400 | 1,000 |
| Free tier active users | 20 | 100 | 250 | 600 |
| Discord members | 15 | 80 | 200 | 500 |
| Newsletter open rate | 45% | 40% | 38% | 35% |

---

## 4. Stage 3: DECISION (Lead -> Prospect)

**Goal**: Move engaged users to the pricing page and convince them to buy.

### 4.1 Decision Triggers

| Trigger | Signal | Response |
|---------|--------|----------|
| Hit free tier limit | 15 credits exhausted | "Unlock all formats with Creator at R$147/mo" |
| Tried Content Factory | 3 free briefs used | "Your 3 free briefs are done. Go Pro for 600 credits/month." |
| Downloaded 2+ lead magnets | High intent signal | Email: "You're learning fast. The course accelerates by 10x." |
| Discord active 7+ days | Community-engaged | DM: "Early bird pricing closes in 5 days" |
| API Dev tier at 80% quota | 80/100 calls used | Dashboard banner: "Upgrade to Startup for 2,000 calls" |
| Visited pricing page 2x | Consideration stage | Retarget email with comparison table |

### 4.2 Decision Assets

| Asset | Purpose | Key Message |
|-------|---------|-------------|
| **Pricing page** | Central conversion point | 5 tiers, clear feature comparison, "Most Popular" badge on Pro |
| **ROI calculator** | Quantify value | "Enter your hourly rate -> see how much CEX saves you" |
| **Case study: CEX builds CEX** | Social proof via self-reference | "This entire content factory was built by the content factory" |
| **Feature comparison matrix** | Reduce decision friction | CEX vs Jasper+HeyGen+Coursebox (saves R$700+/month) |
| **FAQ** | Handle objections | "Do I need to know Python?" "What if I outgrow the tier?" |
| **Testimonial wall** | Social proof | Early adopter quotes with avatar + role + result |

### 4.3 Objection Handling

| Objection | Response | Asset |
|-----------|----------|-------|
| "It's too expensive" | "You already pay R$1,200+ for 3 separate tools" | Comparison matrix |
| "I can do this manually" | "Sure -- in 40 hours. Or in 4 hours with CEX." | ROI calculator |
| "I need to learn Python" | "No. git clone + /init + /build. That's it." | Quickstart video |
| "What if the quality is bad?" | "8F pipeline + quality gates. Below 8.0 gets rebuilt automatically." | Quality gate demo |
| "I'll try it later" | "Early bird pricing: 30% off, closes in 7 days" | Urgency timer |
| "Can I cancel anytime?" | "Monthly. Cancel in 1 click. No contracts." | Pricing page footer |

### 4.4 Metrics & Targets

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| Pricing page views | 30 | 150 | 400 | 1,000 |
| ROI calculator uses | 10 | 50 | 150 | 400 |
| Checkout initiated | 8 | 45 | 120 | 300 |
| Checkout abandoned | 3 | 15 | 36 | 75 |

---

## 5. Stage 4: ACTION (Prospect -> Customer)

**Goal**: Complete the purchase with minimum friction.

### 5.1 Checkout Flow

```
[Pricing Page]
     |
     v
[Select Tier] -- Creator / Pro / Studio / Factory / Course
     |
     v
[Select Billing] -- Monthly / Annual (20% off shown)
     |
     v
[Payment Method]
     |-- Brazil: PIX (instant, 0% fee) <-- DEFAULT for BRL
     |-- Brazil: Boleto (3 business days)
     |-- Brazil: Credit card (up to 12x)
     |-- International: Credit card (Stripe)
     |-- International: PayPal (future)
     |
     v
[Confirmation]
     |-- Instant: API key generated
     |-- Instant: Email with onboarding link
     |-- Instant: Discord invite (Pro+)
     |-- Instant: /init instructions with paid features unlocked
     |
     v
[Post-Purchase Activation]
     |-- Day 0: Welcome email + quickstart
     |-- Day 1: "Your first paid artifact" tutorial
     |-- Day 3: "Content Factory: your first brief" push
     |-- Day 7: "Check your dashboard" (usage stats)
     |-- Day 14: "You've produced {N} artifacts" celebration
```

### 5.2 Payment Providers by Geography

| Market | Primary | Secondary | Tertiary |
|--------|---------|-----------|----------|
| Brazil | MercadoPago (PIX) | Hotmart (courses) | Stripe (cards) |
| LATAM | Stripe | MercadoPago | -- |
| US/EU | Stripe | -- | -- |
| Course (BR) | Hotmart | Kiwify | Digistore24 |
| Course (INT) | Digistore24 | Stripe | -- |

### 5.3 Conversion Optimizations

| Optimization | Expected Lift | Effort |
|-------------|--------------|--------|
| PIX as default for BR (40% lower abandonment) | +15% conversion | Low |
| Annual toggle pre-selected with savings shown | +8% annual adoption | Low |
| "Most Popular" badge on Pro tier | +5% Pro selection | Low |
| Trust badges (SSL, payment provider logos) | +3% completion | Low |
| Exit-intent popup ("Still deciding? Start free") | +2% recovery | Low |
| Abandoned cart email sequence (1h, 24h, 72h) | +10% recovery | Medium |
| 7-day money-back guarantee | +5% conversion | Low |

### 5.4 Metrics & Targets

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| New customers/month | 5 | 30 | 80 | 200 |
| Checkout completion rate | 60% | 65% | 70% | 75% |
| PIX adoption (BR) | 50% | 55% | 60% | 65% |
| Annual vs monthly split | 20/80 | 25/75 | 30/70 | 35/65 |
| Average order value | R$347 | R$397 | R$447 | R$497 |

---

## 6. Post-Purchase: EXPAND (Customer -> Advocate)

### 6.1 Expansion Paths

```
Creator (R$147) ──[hit limit]──> Pro (R$497)
Pro (R$497) ──[need multi-brand]──> Studio (R$1,497)
Studio (R$1,497) ──[need API+SLA]──> Factory (R$3,997)
Any tier ──[one-time need]──> Credit Pack purchase
Course student ──[want automation]──> SaaS subscription
SaaS customer ──[want learning]──> Course purchase
Any customer ──[happy]──> Affiliate (earn 25%)
```

### 6.2 Referral Program

| Referrer Action | Reward |
|----------------|--------|
| Share referral link | Both parties: 1 month free on any paid tier |
| 3 successful referrals | Permanent 10% discount on current tier |
| 10 successful referrals | Free upgrade to next tier for 3 months |
| Become affiliate (25% commission) | Available to any customer after 30 days |

### 6.3 Retention Checkpoints

| Day | Check | Action if At-Risk |
|-----|-------|-------------------|
| 7 | First artifact produced? | If NO: personal onboarding email |
| 14 | 5+ artifacts? | If NO: "Need help?" + office hours invite |
| 30 | Using 50%+ of credits? | If NO: usage tips email + "did you know?" features |
| 60 | Approaching renewal? | If usage >70%: suggest annual (save 20%). If usage <30%: check in |
| 90 | Second renewal | If churning: exit survey + 30% win-back offer |

---

## 7. Full Funnel Metrics Dashboard

```yaml
funnel_dashboard:
  awareness:
    monthly_visitors: 0
    github_stars: 0
    youtube_subs: 0
    cost_per_visitor: 0.00
    
  interest:
    git_clones: 0
    email_signups: 0
    free_tier_users: 0
    visitor_to_lead_rate: 0.0  # target: 10%
    
  decision:
    pricing_page_views: 0
    checkout_initiated: 0
    lead_to_prospect_rate: 0.0  # target: 30%
    
  action:
    new_customers: 0
    checkout_completion: 0.0  # target: 70%
    avg_order_value: 0.00
    prospect_to_customer_rate: 0.0  # target: 30%
    
  expand:
    upgrades: 0
    referrals: 0
    nrr: 0.0  # target: >110%
    churn_rate: 0.0  # target: <5%
    
  derived:
    total_cac: 0.00  # target: <R$90
    ltv: 0.00  # target: >R$500
    ltv_cac_ratio: 0.0  # target: >5.0
    payback_months: 0  # target: <2
```

---

## 8. Implementation Timeline

| Week | Stage | Deliverables | Owner |
|------|-------|-------------|-------|
| W1-2 | AWARENESS | README rewrite, 3 YouTube shorts, 5 LinkedIn posts | N02+N05 |
| W2-3 | INTEREST | eBook generated (CF), landing page, email sequence | N03+N02 |
| W3-4 | DECISION | Pricing page live, ROI calculator, comparison matrix | N03+N06 |
| W4-5 | ACTION | Stripe products, MercadoPago PIX, checkout flow | N05+N06 |
| W5-6 | EXPAND | Referral program, onboarding automation, retention emails | N02+N06 |
| W6-8 | OPTIMIZE | A/B test pricing page, track metrics, iterate | N06 |

**Total time to full funnel**: 8 weeks from start.

---

*Generated by N06 Commercial Nucleus -- CEX Product Funnel*
*Not a template. Not a pattern. This is THE funnel. Every stage has a price tag and an ROI.*
*Awareness costs R$0.50/visitor. The funnel converts at 0.9%. Each customer is worth R$500+.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**
