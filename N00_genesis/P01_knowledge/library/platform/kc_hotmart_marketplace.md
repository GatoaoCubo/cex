---
id: kc_hotmart_marketplace
kind: knowledge_card
8f: F3_inject
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: affiliate_platform
quality: 9.1
tldr: "Hotmart Marketplace — affiliate ecosystem with 500K+ promoters, commission structures, cookie tracking, and promotion strategies for BR/LATAM."
tags: [hotmart, marketplace, affiliate, commission, brazil, latam, infoproduct]
density_score: 1.0
when_to_use: "Apply when hotmart marketplace — affiliate ecosystem with 500k+ promoters, commission structures, cookie tra..."
keywords: [knowledge-card, hotmart, ecosystem, marketplace, models]
linked_artifacts:
  primary: null
  related: []
related:
  - kc_digistore24_marketplace
  - tpl_launch_checklist
  - n06_monetization_audit_2026_04_08
  - kc_hotmart_api
  - kc_digistore24_api
  - kc_content_platform_comparison
  - p12_wf_cf_publish_hotmart
---

# Hotmart Marketplace — Affiliate Ecosystem

Hotmart Marketplace is the largest digital product affiliate network in Latin America, connecting producers (creators) with 500K+ affiliates (promoters) who earn commissions on referred sales.

## 1. How the Marketplace Works

```
Producer creates product → Lists on Marketplace
    │
    ▼
Affiliate discovers product → Generates affiliate link
    │
    ▼
Affiliate promotes (blog, social, email, ads)
    │
    ▼
Buyer clicks affiliate link → Cookie set (30-180 days)
    │
    ▼
Buyer purchases → Commission paid to affiliate automatically
```

**Key**: Hotmart handles all commission tracking, payment splitting, and affiliate payouts. The producer configures the program; Hotmart executes it.

## 2. Commission Models

| Model | How It Works | Best For |
|-------|-------------|----------|
| Per-sale (%) | Affiliate gets % of each sale | Standard digital products |
| Per-sale (fixed) | Affiliate gets fixed BRL amount per sale | Low-price products |
| Recurring | Affiliate gets % of each subscription renewal | SaaS/membership products |
| First-sale only | Commission on first purchase only | High-ticket with upsell |
| Tiered | Commission % increases with volume | Top-performer incentives |

### Typical Commission Ranges
| Product Type | Commission % | Rationale |
|-------------|-------------|-----------|
| E-book | 50-70% | Low production cost, high margin |
| Course | 30-50% | Moderate production cost |
| Mentorship | 20-30% | High-touch, limited seats |
| SaaS/tool | 20-40% recurring | Lifetime value justifies lower % |

**Rule**: Commission must be attractive enough to recruit affiliates but maintain floor_margin_pct >= 30% after platform fees. Hotmart charges ~9.9% + R$1 per transaction.

## 3. Cookie & Attribution

| Setting | Options | Default |
|---------|---------|---------|
| Cookie duration | 30-180 days | 180 days |
| Attribution model | First-click or last-click | Last-click |
| Cross-device | Via Hotmart login | Automatic |
| Organic fallback | No cookie = producer gets 100% | Automatic |

**Cookie mechanics**: When a buyer clicks an affiliate link, Hotmart sets a cookie. Any purchase within the cookie window attributes the sale to that affiliate, even if the buyer returns directly later.

**Gotcha**: Last-click attribution means the LAST affiliate link clicked gets the commission. If affiliate A drives awareness and affiliate B closes the sale, B gets paid. This is standard but frustrates top-of-funnel affiliates.

## 4. Marketplace Listing Optimization

### Product Page Elements
| Element | Impact | Best Practice |
|---------|--------|---------------|
| Title | Search discovery | Include niche keyword + benefit |
| Description | Conversion | Problem → solution → proof → CTA |
| Temperature | Social proof | Higher = more sales (snowball effect) |
| Average ticket | Affiliate attractiveness | Higher price = higher commission per sale |
| Commission % | Affiliate recruitment | Display prominently — it's the hook |
| Support score | Trust signal | Respond to affiliate questions within 24h |
| Refund rate | Risk indicator | Keep below 10% or affiliates avoid you |

### Temperature Score
Hotmart assigns a "temperature" score (thermometer icon) based on recent sales velocity. Higher temperature = more visibility in marketplace search = more affiliate applications.

**Hack**: Launch with a promotional price to spike initial sales velocity, increasing temperature. Then gradually raise price once marketplace position is established.

## 5. Affiliate Management via API

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/affiliation/api/v1/affiliations` | GET | List affiliates for your product |
| `/affiliation/api/v1/affiliations/{id}` | GET | Affiliate details + performance |
| `/payments/api/v1/sales/commissions` | GET | Commission history |

### Affiliate Approval Modes
| Mode | Behavior |
|------|----------|
| Auto-approve | Any affiliate can promote immediately |
| Manual approval | Producer reviews each application |
| Invite-only | Only affiliates with a direct link can apply |

**Recommendation**: Start with auto-approve to maximize reach. Switch to manual once you have 50+ affiliates and want to curate quality promoters.

## 6. Affiliate Promo Materials

Successful affiliate programs provide ready-to-use promotional materials:

| Material | Format | Purpose |
|----------|--------|---------|
| Email swipes | Text templates | Affiliate email campaigns |
| Banner ads | JPG/PNG (300x250, 728x90, 160x600) | Blog/website placement |
| Social posts | Copy + image suggestions | Instagram, Facebook, Twitter |
| Video scripts | Text outlines | YouTube/TikTok reviews |
| Comparison pages | Template HTML | "Product X vs Y" affiliate SEO |
| Webinar slides | PDF/PPT | Affiliate webinar promotions |

Upload materials to the Hotmart affiliate dashboard so promoters can access them directly.

## 7. Affiliate Fraud Prevention

| Fraud Type | Detection | Prevention |
|------------|-----------|------------|
| Self-referral | Same email as buyer/affiliate | Block same-email commissions |
| Cookie stuffing | Abnormal click-to-sale ratio | Monitor CTR anomalies |
| Refund abuse | Affiliate + buyer collude on refund | Track refund rate per affiliate |
| Brand bidding | Affiliate bids on your brand name in ads | Prohibit in affiliate terms, monitor |
| Incentivized traffic | "Buy through my link for a bonus" | Against Hotmart ToS — report |

**Rule**: Monitor per-affiliate refund rate. If any affiliate exceeds 15% refund rate, investigate and potentially remove from program.

## 8. Marketplace vs Direct Sales

| Aspect | Marketplace Affiliates | Direct Sales |
|--------|----------------------|-------------|
| CAC | Commission-based (variable) | Ad spend (upfront risk) |
| Reach | Leverages 500K+ promoters | Your audience only |
| Control | Less control over messaging | Full control |
| Margin | Lower per-sale (commission) | Higher per-sale |
| Scale | Exponential (network effect) | Linear (your effort) |

**Strategy**: Use both. Direct sales for warm audience (email list, social followers). Marketplace affiliates for cold audience at scale. Target: 40% revenue from affiliates, 60% from direct.

## 9. Hotmart Marketplace vs DS24 Marketplace

| Aspect | Hotmart | Digistore24 |
|--------|---------|-------------|
| Market | BR/LATAM | EU/DACH/Global |
| Affiliates | 500K+ (PT-BR focused) | Strong in DE/EN markets |
| Commission payment | BRL, bi-weekly | EUR, monthly |
| Cookie default | 180 days | 180 days |
| Language | PT-BR | 7 languages (DE,EN,ES,FR,IT,NL,PL) |
| MoR | Seller | DS24 (handles VAT) |
| Platform fee | ~9.9% + R$1 | Varies, included in MoR |

**Dual-platform**: List on Hotmart Marketplace for BR reach + DS24 Marketplace for EU reach. Same product, different pricing (BRL vs EUR), different affiliate pools.

## Regras de Ouro

1. **Commission >= 30%** — below this, serious affiliates won't promote.
2. **180-day cookie** — maximize attribution window; longer = more conversions.
3. **Promo materials ready** — affiliates with assets promote 3x more than those without.
4. **Monitor refund rate per affiliate** — >15% = investigate fraud.
5. **Dual marketplace** — Hotmart (BR) + DS24 (EU) for maximum global affiliate reach.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_digistore24_marketplace]] | sibling | 0.55 |
| [[tpl_launch_checklist]] | downstream | 0.37 |
| [[n06_monetization_audit_2026_04_08]] | related | 0.29 |
| [[kc_hotmart_api]] | sibling | 0.28 |
| [[kc_digistore24_api]] | sibling | 0.27 |
| [[kc_content_platform_comparison]] | sibling | 0.24 |
| [[p12_wf_cf_publish_hotmart]] | downstream | 0.15 |
