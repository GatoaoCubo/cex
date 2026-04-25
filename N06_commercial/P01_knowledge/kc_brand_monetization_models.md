---
id: p01_kc_brand_monetization_models
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Brand Monetization Models"
version: 1.0.0
created: 2026-04-01
author: shaka_research
domain: brand-identity
quality: 9.2
updated: 2026-04-07
tags: [brand, monetization, pricing, saas, e-commerce, brasil, pix, hotmart, ltv, cac]
tldr: "12 monetization models benchmarked (subscription, freemium, one-time, credits, marketplace, licensing, ads, data, API, white-label, consulting, hybrid), pricing psychology (7 techniques: anchoring, decoy, charm, framing, bundling, loss aversion, social proof), 4-tier SaaS structure, LTV:CAC framework (3:1 healthy ratio, <12mo payback), and payment provider comparison (Stripe vs MercadoPago vs Hotmart vs Kiwify)."
when_to_use: "When designing pricing strategy, evaluating monetization models, or building revenue projections for Brazilian digital products."
keywords: [monetization, pricing-psychology, ltv-cac, pix, hotmart, kiwify, saas-tiers, value-based-pricing]
density_score: 0.94
axioms:
  - "ALWAYS price to transformation value, never cost-plus."
  - "NEVER launch without a defined upsell path — first sale is smallest sale."
  - "ALWAYS present PIX/boleto with discount to recover parcelamento margin."
linked_artifacts:
  primary: n06_output_monetization_business_plan
  related: [p01_kc_commercial_nucleus, n06_output_pricing_page, p12_wf_content_monetization, p04_fn_content_monetization]
related:
  - p02_agent_ml_ads
  - p08_pat_pricing_framework
  - output_content_factory_business_model
  - pricing_optimization_memory
  - e2e_gold_petshop_marketing
  - subscription-tier-builder
  - kc_ai_saas_monetization
  - p03_fs_product_extraction
  - bld_instruction_subscription_tier
  - p01_kc_llm_benchmark_ecommerce_copy
---

# Brand Monetization Models

## 1. The 12 Monetization Models

| # | Model | Revenue Formula | When to Use |
|---|--------|--------------------|-------------|
| 1 | **Subscription** | MRR = users x monthly price | Product with recurring usage, high LTV |
| 2 | **Freemium** | Free-to-paid conversion (2-5% typical) | Viral product, low CAC, network effects |
| 3 | **One-time purchase** | Revenue = sales x unit price | Physical product, course, template |
| 4 | **Credits/Tokens** | Revenue = packs x price-per-credit | AI, API, variable usage |
| 5 | **Marketplace commission** | Take rate 5-20% on GMV | Platform connecting supply and demand |
| 6 | **Licensing** | License fee + royalty | Unique IP, B2B, white-label |
| 7 | **Advertising** | CPM or CPC on audience | High volume, segmented audience |
| 8 | **Data monetization** | Insight sales/licensing | Anonymized usage data |
| 9 | **API as product** | Per-call or volume tier | Infra/platform for developers |
| 10 | **White-label** | Setup fee + revenue share | Technology packaged for third parties |
| 11 | **Consulting/Services** | Day rate or project | High ticket, low volume, expands LTV |
| 12 | **Hybrid** | Combination of 2+ models | Product maturity, diversification |

> **Golden rule**: start with 1 model. Expand to hybrid only after proven product-market fit.

---

## 2. Value-Based Pricing

### Core Principle
```
Price = Perceived transformation value (NOT production cost)
```

The customer pays for the OUTCOME, not your effort.

### Calculation Framework
```
1. Identify the problem you solve
2. Quantify the outcome value in $ or time
3. Capture 10-30% of that value as price
4. Validate with 5-10 customers before setting

Example:
- Problem: store loses 40h/month on manual management
- Value: 40h x $50/h = $2,000/month saved
- Fair price: $200-600/month (10-30% of generated value)
```

### Value-Based vs Cost-Plus
| Approach | Formula | Result |
|-----------|---------|-----------|
| **Cost-plus** | cost x (1 + margin%) | Limits price to cost, leaves value on the table |
| **Value-based** | transformation x capture% | Price reflects outcome, higher margin |
| **Competitive** | competitor price +/- delta | Reactive, price war, commoditizes |

---

## 3. Pricing Psychology

| Technique | Description | Example |
|---------|-----------|---------|
| **Anchoring** | Presenting high price first shifts perception of subsequent options | Enterprise plan listed before Pro |
| **Decoy pricing** | Bad middle option makes premium seem obvious | 3 plans where middle is "worst value" |
| **Charm pricing** | Price ending in 7, 9, or 97 | $97, $297, $997 |
| **Price framing** | Show price per smallest time unit | "$3/day" instead of "$89/month" |
| **Bundle discount** | Package to increase ticket without reducing perceived value | Course + mentoring + templates = $1,997 |
| **Loss aversion** | Emphasize what user LOSES without the product | "Every day without X costs $Y in lost opportunity" |
| **Social proof pricing** | Mention that others pay the same | "Over 3,000 companies pay this price" |

---

## 4. Tier Structure (SaaS Standard)

```
FREE       -> Hook. No credit card. Limited usage/features.
STARTER    -> $47-97/mo. 1 user. Essential features.
PRO        -> $197-397/mo. 3-5 users. Full features.
ENTERPRISE -> Custom. Volume + SLA + dedicated support.
```

### Tier Design Rules
1. **Free** must have real value (don't make it a bad demo)
2. **Pro must be obvious** — 80% of features for 80% of customers
3. **Enterprise has no public price** — ensures flexibility for large accounts
4. **Differentiate by outcome, not feature count** — "up to 100 products" vs "up to 1,000 products"
5. **Annual discount of 15-20%** on monthly rate to accelerate revenue recognition

---

## 5. Brazilian Market: Specificities

### Payment Methods
| Method | Usage % | Key Characteristic |
|--------|-------|---------------------|
| **PIX** | 62% (most frequent) | Instant, zero fee for individuals, 93% adult population uses it |
| **Credit card installments** | 80% of e-commerce | Split into 2-12x interest-free (merchant absorbs cost) |
| **Boleto bancario** | ~15% | Unbanked population, 3 business day settlement |
| **Debit card** | Minor | In-person purchases, no installments |

### PIX Installments (launched 2025)
- Central Bank authorized installment PIX (Sep 2025)
- Merchant receives full amount upfront
- Customer pays installments via their banking app
- Zero credit risk for the seller

### BRL Price Psychology
```
WRONG: "$990 upfront"
RIGHT: "10x of $99 interest-free"

WRONG: "Subscribe for $297/month"
RIGHT: "Less than $10 per day"
```

**Rule**: always present the smaller price first (installment or daily), total in smaller text.

### Interest-Free Installments
- Up to 6x: common for digital products
- Up to 12x: standard for tickets $500+
- Financial cost (~2-3%/month): absorbed in price or passed through
- Offering PIX/wire with discount (5-10%) recovers margin

---

## 6. Digital Courses: Hotmart / Kiwify / Kajabi

### Platform Comparison
| Platform | Fee | Model | Best For |
|------------|------|--------|-------------|
| **Hotmart** | 9.9% + $1 per sale | Marketplace + independent | Own audience + affiliates |
| **Kiwify** | ~4.99% | Independent, cheaper | Fast launches, better margins |
| **Kajabi** | 0% commission ($119-399/mo subscription) | All-in-one | Established business, high ticket |
| **Eduzz** | Similar to Hotmart | Marketplace | Alternative with affiliate network |

### Course Monetization Models
```
ONE-TIME PAYMENT
├── Self-paced: R$97 - R$997
├── Cohort (turma ao vivo): R$997 - R$5.000+
└── High-ticket (mentoria/coaching): R$5.000 - R$50.000+

SUBSCRIPTION
├── Comunidade + conteudo recorrente: R$47-197/mes
├── Plataforma SaaS + aprendizado: bundle com produto
└── Assinatura anual com desconto: R$497-1.997/ano

HYBRID (recomendado)
├── One-time course (lancamento)
├── + Comunidade subscription (retencao)
└── + Upsell mentoria individual (expansao)
```

### Digital Course Pricing Benchmarks
- Mini-course (2-4h): $47 - $197
- Full course (10-40h): $297 - $997
- Immersion (3-5 days): $1,497 - $4,997
- Group mentoring (3 months): $3,000 - $15,000
- High-ticket individual: $10,000 - $50,000+

---

## 7. E-commerce: Marketplace Commissions

### Commission by Platform
| Plataforma | Comissao | Outros Custos |
|------------|----------|---------------|
| **Mercado Livre** | 11-17% (BR), varia por categoria | Anuncio gratis/pago, Flex fulfillment |
| **Shopee** | 2.24-5.60% comissao + 2.4% taxa transacao | Frete subsidiado em lancamentos |
| **Amazon BR** | 8-15% por categoria | FBA (fulfillment) disponivel |
| **Magalu** | ~12-16% | Fulfillment proprio, Entrega Magalu |

### Margin Rule for Marketplaces
```
Preco de venda minimo = Custo × (1 + margem_alvo + comissao_plataforma + frete%)

Exemplo:
Custo produto: R$30
Margem desejada: 40%
Comissao ML: 15%
Frete estimado: 8%
Preco minimo = R$30 / (1 - 0.40 - 0.15 - 0.08) = R$30 / 0.37 = R$81
```

---

## 8. LTV / CAC Framework

### Essential Formulas
```
CAC = (custo total de marketing + vendas) / novos clientes adquiridos

LTV = ARPU × margem_bruta × (1 / churn_rate)
     onde ARPU = receita media por usuario por mes

LTV:CAC ratio saudavel = 3:1 ou maior
Payback period ideal = < 12 meses
```

### When to Invest in What
| LTV:CAC | Recommended Action |
|---------|-----------------|
| < 1:1 | Stop acquisition — the product doesn't retain |
| 1:1 - 3:1 | Optimize retention before scaling acquisition |
| 3:1 - 5:1 | Healthy zone — scale acquisition with controls |
| > 5:1 | May be under-investing in growth |

### Revenue Modeling Metrics
```
MRR (Monthly Recurring Revenue)     = usuarios_ativos × ARPU
ARR (Annual Recurring Revenue)      = MRR × 12
Churn Rate                          = cancelamentos / total_clientes
Net Revenue Retention (NRR)         = (MRR_inicio + expansao - churn) / MRR_inicio
Expansion Revenue                   = upsells + cross-sells em base existente
```

---

## 9. Pricing Page: Design Patterns

### High-Conversion Structure
```
1. HEADLINE: [Resultado claro], nao "nossos planos"
2. TOGGLE: mensal / anual (anual destacado como "economize 20%")
3. CARDS: 3 planos (free/pro/enterprise)
4. DESTAQUE: Pro com borda colorida, badge "mais popular"
5. FEATURES: lista de 5-8 itens, checkmarks verdes
6. CTA: "Comecar gratis" (free) | "Assinar" (pro) | "Falar com vendas" (enterprise)
7. FAQ: 5-7 perguntas sobre billing, cancelamento, suporte
8. SOCIAL PROOF: logos de clientes ou numero de usuarios
9. GUARANTEE: "Cancele quando quiser, sem perguntas"
```

### Common Pricing Page Mistakes
- Too many plans (> 4 confuses)
- Features listed without benefit context
- No high-price anchor (Enterprise without price scares off)
- Same CTA for all plans
- No guarantee or clear cancellation policy

---

## Referencias
- [SaaS Monetization Models — Schematic HQ](https://schematichq.com/blog/software-monetization-models)
- [Brazil PIX Payment Opportunity — Substack](https://dwaynegefferie.substack.com/p/brazil-the-346-billion-opportunity)
- [Pix Parcelado — PagBrasil](https://www.pagbrasil.com/blog/pix/installment-pix/)
- [LTV, CAC & Payback — Passion.io](https://passion.io/blog/creator-course-metrics-ltv-cac-payback)
- [Cohort Course Pricing — Passion.io](https://passion.io/blog/cohort-course-pricing-guide-one-time-payment-vs-subscription-models)
- [Mercado Libre Selling Fees](https://global-selling.mercadolibre.com/landing/selling-fee)
- [Brazil SaaS Market Guide — PayPro Global](https://blog.payproglobal.com/saas-conversion-rate-in-brazilian-market)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_ml_ads]] | downstream | 0.25 |
| [[p08_pat_pricing_framework]] | downstream | 0.21 |
| [[output_content_factory_business_model]] | downstream | 0.20 |
| [[pricing_optimization_memory]] | downstream | 0.19 |
| [[e2e_gold_petshop_marketing]] | related | 0.18 |
| [[subscription-tier-builder]] | downstream | 0.18 |
| [[kc_ai_saas_monetization]] | sibling | 0.17 |
| [[p03_fs_product_extraction]] | downstream | 0.16 |
| [[bld_instruction_subscription_tier]] | downstream | 0.16 |
| [[p01_kc_llm_benchmark_ecommerce_copy]] | sibling | 0.16 |
