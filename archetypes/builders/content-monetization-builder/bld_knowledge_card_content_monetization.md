---
kind: knowledge_card
id: bld_knowledge_card_content_monetization
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for content monetization — pricing, billing, credits, checkout patterns
sources: Stripe docs, Hotmart API, SaaS pricing literature (ProfitWell, OpenView), CEX production systems
---

# Domain Knowledge: content_monetization

## Executive Summary
Config-driven system that prices, bills, and delivers digital content via tiered
subscriptions, credit packs, or hybrid models. Three pillars: **pricing strategy**,
**credit economics**, and **checkout orchestration**.

## The 3 Core Pillars

### Pricing Strategy
- **Freemium**: free tier with limits → conversion to paid (typical 2-5% conversion)
- **Tiered**: good/better/best with feature gating (most common for SaaS)
- **Usage-based**: pay-per-use metered billing (API companies, compute)
- **Credit pack**: prepaid bundles consumed per operation (AI tools, marketplaces)
- **Hybrid**: base tier + overage credits (best of both: predictable + flexible)
- **Key metric**: floor margin >= 30% per tier after pipeline costs

### Credit Economics
- Map every pipeline operation to credit cost: research=50cr, publish=10cr, analyze=30cr
- Underlying costs: LLM tokens ($0.003-$0.06/1K), API calls ($0.001-$0.30), compute ($0.01/min)
- Credit pricing: 1 credit = ~R$0.05-0.10 (varies by niche and volume)
- Overdraft handling: block (safest), notify-then-block (UX friendly), allow-negative (risky)
- Rollover: disabled by default — simplifies revenue recognition

### Checkout Orchestration
- **Stripe**: global, cards + subscriptions + usage billing, webhook-first architecture
- **Hotmart**: BR leader for infoproducts, checkout page + affiliate network + Hotmart Club
- **Kiwify**: BR challenger, simpler UX, lower fees, growing fast
- **Monetizze**: BR, strong in health/finance niches, affiliate focus
- **Eduzz**: BR, digital products + physical, Sun (course platform)

## Platform KC Pointers
| Platform | KC Reference | Key Strength |
|----------|-------------|--------------|
| Stripe | kc_stripe_billing | Global, API-first, usage billing |
| Hotmart | kc_hotmart_checkout | BR infoproducts, affiliate network |
| Kiwify | kc_kiwify_checkout | BR, low fees, simple integration |
| Monetizze | kc_monetizze_checkout | BR, health/finance niches |
| Eduzz | kc_eduzz_checkout | BR, digital+physical hybrid |
| Resend | kc_resend_email | Dev-friendly transactional email |
| Meta Ads | kc_meta_ads | B2C awareness, pixel tracking |
| Google Ads | kc_google_ads | Intent capture, search/shopping |

## Anti-Patterns
| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Float prices (R$49.90) | Rounding errors compound — use centavos (4990) |
| No margin tracking | Pipeline costs silently eat profit — discover post-launch |
| Hardcoded provider | Switching from Stripe to Hotmart requires full rewrite |
| No mock mode | Dev hits live payment API — real charges, chargebacks |
| Webhook without idempotency | Duplicate events → double-charge or double-credit |
| Unlimited credits on free tier | Free users consume expensive LLM calls — margin collapses |
| No overdraft policy | Users go negative, dispute charges, support overload |
| Time-only email triggers | Misses behavioral signals — user who used feature X is warmer |

## 9-Stage Pipeline
| Stage | Name | Input | Output |
|-------|------|-------|--------|
| 1 | PARSE | Content inventory | Monetizable asset catalog |
| 2 | PRICING | Assets + costs + market | Tiers + strategy + margins |
| 3 | CREDITS | Pipeline ops + costs | Credit map + packs + overdraft |
| 4 | CHECKOUT | Provider + URLs | Webhook config + mock setup |
| 5 | COURSES | Content structure | Modules + lessons + certification |
| 6 | ADS | Budget + audience | Campaign config + pixel setup |
| 7 | EMAILS | Triggers + sequences | Email automation config |
| 8 | VALIDATE | Full config | Margin report + webhook test |
| 9 | DEPLOY | Validated config | Production cutover checklist |
