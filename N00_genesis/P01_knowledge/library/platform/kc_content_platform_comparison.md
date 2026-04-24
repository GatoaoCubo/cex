---
id: kc_content_platform_comparison
kind: knowledge_card
8f: F3_inject
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: platform_analysis
quality: 9.1
tldr: "Cross-platform comparison — Hotmart vs Digistore24 vs Kiwify vs Teachable for content monetization across BR, EU, and global markets."
tags: [comparison, hotmart, digistore24, kiwify, teachable, platform, monetization]
density_score: 1.0
when_to_use: "Apply when cross-platform comparison — hotmart vs digistore24 vs kiwify vs teachable for content monetizatio..."
keywords: [knowledge-card, platform, comparison, platform_analysis, content]
linked_artifacts:
  primary: null
  related: []
related:
  - kc_digistore24_api
  - bld_knowledge_card_content_monetization
  - bld_tools_content_monetization
  - kc_digistore24_marketplace
  - bld_architecture_content_monetization
  - bld_schema_bugloop
  - bld_schema_content_monetization
  - bld_schema_quickstart_guide
  - bld_schema_sandbox_config
  - bld_schema_usage_report
---

# Content Platform Comparison

Side-by-side comparison of the major platforms for selling digital content (courses, e-books, memberships, coaching). Focus on the recommended pairing: **Hotmart (BR) + Digistore24 (EU)**, with alternatives for specific use cases.

## 1. Platform Overview

| Platform | HQ | Primary Market | Model | Founded |
|----------|-----|---------------|-------|---------|
| Hotmart | BR (Belo Horizonte) | BR/LATAM | Marketplace + checkout | 2011 |
| Digistore24 | DE (Hildesheim) | EU/DACH | MoR + marketplace | 2015 |
| Kiwify | BR (Sao Paulo) | BR | Checkout + member area | 2020 |
| Teachable | US (New York) | Global (EN) | LMS + checkout | 2014 |
| Thinkific | CA (Vancouver) | Global (EN) | LMS + checkout | 2012 |
| Udemy | US (San Francisco) | Global | Marketplace (their traffic) | 2010 |
| ClickBank | US (Boise) | US/EN | Marketplace + MoR | 1998 |

## 2. Feature Comparison Matrix

| Feature | Hotmart | DS24 | Kiwify | Teachable |
|---------|---------|------|--------|-----------|
| Merchant of Record | No | **Yes** | No | No |
| EU VAT handling | No | **Auto** | No | No |
| Affiliate marketplace | **500K+** | Strong EU | Growing | Built-in |
| Member area | **Hotmart Club** | Basic redirect | Native | **Full LMS** |
| Drip content | Yes | Via redirect | Yes | **Yes** |
| Multi-language | PT-BR only | **7 languages** | PT-BR only | EN-focused |
| Payment methods | PIX, cards, boleto | **SEPA, Sofort, iDEAL, cards, PayPal** | PIX, cards | Cards, PayPal |
| Webhook format | JSON | **form-encoded** | JSON | JSON |
| Webhook signature | sha256 HMAC | sha512 | sha256 | HMAC |
| API | REST (OAuth2) | REST (API key) | REST | REST |
| Sandbox | Developer portal | Product test mode | Test mode | Sandbox |
| Custom domain | Paid add-on | N/A (your sales page) | Yes | Yes |
| Subscription billing | Yes | **Yes** (SEPA dominant) | Yes | Yes |
| Installments | Yes (parcelamento) | Yes (Ratenzahlung) | Yes | No |
| Coupons | Yes | **Yes (API)** | Yes | Yes |
| Certificates | Hotmart Club | No (external) | No | **Yes** |

## 3. Pricing & Fees

| Platform | Transaction Fee | Monthly Fee | Payout Frequency |
|----------|----------------|-------------|-----------------|
| Hotmart | ~9.9% + R$1 | Free | Bi-weekly (BRL) |
| DS24 | Varies (included in MoR) | Free | Monthly (EUR) |
| Kiwify | 8.99% (no monthly) | Free | Bi-weekly (BRL) |
| Teachable | 5% (Free plan) / 0% (Pro $119/mo) | $0-$499/mo | Weekly (USD) |
| Thinkific | 0% (paid plans) | $49-$499/mo | Monthly (USD) |
| Udemy | 37-63% revenue share | Free | Monthly (USD) |
| ClickBank | 7.5% + $1 | $49.95 activation | Bi-weekly (USD) |

**True cost analysis** for a EUR 97 course sale:
| Platform | Fee | Affiliate (40%) | VAT (19% DE) | You Receive |
|----------|-----|-----------------|-------------|-------------|
| DS24 | ~EUR 8 | EUR 38.80 | EUR 0 (DS24 handles) | **~EUR 50.20** |
| Teachable Pro | EUR 0 | EUR 38.80 (manual) | EUR 18.43 (YOU pay) | EUR 39.77 - VAT admin |
| Stripe direct | EUR 2.82 | EUR 38.80 (manual) | EUR 18.43 (YOU pay) | EUR 36.95 - VAT admin |

**Verdict**: DS24's MoR fee looks higher but INCLUDES EU VAT handling. Without DS24, you need VAT registration (~EUR 500/year accounting) + quarterly filings.

## 4. Webhook / Integration Comparison

| Aspect | Hotmart | DS24 | Kiwify | Teachable |
|--------|---------|------|--------|-----------|
| Format | JSON | **form-encoded** | JSON | JSON |
| Signature | sha256 HMAC | sha512 | sha256 | HMAC |
| Secret storage | HOTMART_HOTTOK | DS24_IPN_PASSPHRASE | KIWIFY_SECRET | TEACHABLE_SECRET |
| Response requirement | HTTP 200 | **body = "OK"** | HTTP 200 | HTTP 200 |
| Events | 8 types | 8 types | 6 types | 5 types |
| Retry behavior | Limited | Until "OK" | Limited | 3 retries |
| Idempotency key | transaction_id | order_id | purchase_id | enrollment_id |
| Test mode | Developer portal | Product test mode | Test mode | Sandbox |

### Handler Architecture for Multi-Platform
```python
# Router pattern for multi-platform webhooks
@app.post("/webhooks/{platform}")
async def webhook_router(platform: str, request: Request):
    body = await request.body()

    handlers = {
        "hotmart": handle_hotmart,    # JSON, sha256
        "ds24": handle_ds24,          # form-encoded, sha512, return "OK"
        "kiwify": handle_kiwify,      # JSON, sha256
        "stripe": handle_stripe,      # JSON, sha256
    }

    handler = handlers.get(platform)
    if not handler:
        raise HTTPException(404, "Unknown platform")

    return await handler(body, request.headers)
```

## 5. Affiliate Ecosystem Comparison

| Aspect | Hotmart | DS24 | ClickBank |
|--------|---------|------|-----------|
| Affiliate pool | 500K+ (BR/LATAM) | Strong (EU/DACH) | 100K+ (US/EN) |
| Languages | PT-BR | DE,EN,ES,FR,IT,NL,PL | EN |
| Commission payment | BRL, bi-weekly | EUR, monthly | USD, bi-weekly |
| Cookie duration | 180 days | 180 days | 60 days |
| Ranking metric | Temperature (velocity) | EPC (earnings/click) | Gravity score |
| Promo tools | Dashboard | Promo page | HopLink |
| Fraud detection | Basic | Moderate | Advanced |
| Marketplace fee | Included in tx fee | Included in MoR fee | 7.5% + $1 |

## 6. Course Delivery Comparison

| Aspect | Hotmart Club | Teachable | Thinkific | DS24 |
|--------|-------------|-----------|-----------|------|
| Native LMS | **Yes** | **Yes** | **Yes** | No (redirect) |
| Video hosting | CDN included | CDN included | CDN included | External needed |
| Quizzes | Yes (basic) | **Yes (advanced)** | **Yes (advanced)** | No |
| Certificates | Yes | **Yes** | **Yes** | No |
| Drip content | Yes | Yes | Yes | Via redirect |
| Community | Comments | **Comments + community** | **Community** | No |
| Custom domain | Paid | Yes | Yes | N/A |
| White-label | Limited | Yes (Pro+) | Yes | N/A |
| Analytics | Basic | **Detailed** | **Detailed** | Sales only |
| Price | Free (included) | $0-$499/mo | $49-$499/mo | Free (no LMS) |

**Decision tree**:
- BR-only course → **Hotmart Club** (free, integrated)
- EU course with LMS needs → **Teachable** or **Thinkific** + DS24 checkout
- Simple digital product (no LMS) → **DS24** redirect to your delivery system

## 7. Recommended Platform Strategy

### Solo Creator (BR Market)
```
Hotmart (checkout + Club + affiliates)
├── Simple, all-in-one
├── PIX + boleto + cards
└── 500K affiliates for reach
```

### Solo Creator (EU Market)
```
DS24 (checkout + affiliates + VAT) + Teachable (course delivery)
├── DS24 handles payments, VAT, affiliates
├── Teachable hosts courses
└── DS24 IPN → Teachable enrollment API
```

### Multi-Market (BR + EU) — Recommended
```
Hotmart (BR) + DS24 (EU)
├── Same product, different checkout
├── Hotmart Club for BR delivery
├── Teachable or custom for INT delivery
├── Geo-routing: BR visitors → Hotmart, EU → DS24
└── Separate affiliate programs per platform
```

### Scale-Up (BR + EU + US)
```
Hotmart (BR) + DS24 (EU) + ClickBank or Stripe (US)
├── Three checkout paths
├── Unified webhook router
├── Single CRM/email system (tag by source)
└── Per-region pricing (BRL/EUR/USD)
```

## 8. Migration Paths

| From | To | Complexity | Key Challenge |
|------|-----|-----------|---------------|
| Hotmart only | + DS24 | Medium | DS24 IPN (form-encoded), EU compliance |
| Teachable only | + DS24 | Medium | Separate checkout, IPN integration |
| Stripe only | + DS24 + Hotmart | High | Two new webhook formats, affiliate setup |
| Udemy | Hotmart + DS24 | High | No data export, rebuild audience |

## 9. Decision Framework

| If You Need... | Use |
|----------------|-----|
| BR market, fast launch | **Hotmart** |
| EU market, no VAT headaches | **DS24** |
| Advanced LMS features | **Teachable** or **Thinkific** |
| Maximum affiliate reach (BR) | **Hotmart Marketplace** |
| Maximum affiliate reach (EU) | **DS24 Marketplace** |
| Maximum affiliate reach (US) | **ClickBank** |
| Global SaaS billing | **Stripe** |
| Cheap BR alternative | **Kiwify** |
| Mass market, their traffic | **Udemy** (but low margin) |

## Regras de Ouro

1. **Hotmart + DS24 = global** — BR/LATAM + EU/DACH covers 70%+ of infoproduct market.
2. **DS24 for EU VAT** — MoR eliminates tax complexity; worth the higher fee.
3. **LMS separate from checkout** — Teachable/Thinkific for course delivery, DS24/Hotmart for money.
4. **Geo-routing at sales page** — detect visitor country, route to correct checkout.
5. **Unified webhook router** — single handler architecture for all platforms.
6. **Per-region pricing** — don't just convert; price for local purchasing power.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_digistore24_api]] | sibling | 0.40 |
| [[bld_knowledge_card_content_monetization]] | sibling | 0.40 |
| [[bld_tools_content_monetization]] | downstream | 0.36 |
| [[kc_digistore24_marketplace]] | sibling | 0.35 |
| [[bld_architecture_content_monetization]] | downstream | 0.34 |
| [[bld_schema_bugloop]] | downstream | 0.33 |
| [[bld_schema_content_monetization]] | downstream | 0.31 |
| [[bld_schema_quickstart_guide]] | downstream | 0.31 |
| [[bld_schema_sandbox_config]] | downstream | 0.31 |
| [[bld_schema_usage_report]] | downstream | 0.31 |
