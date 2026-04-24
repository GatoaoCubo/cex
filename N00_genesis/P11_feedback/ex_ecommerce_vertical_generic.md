---
id: ex_ecommerce_vertical_generic
kind: ecommerce_vertical
8f: F1_constrain
pillar: P11
version: 1.0.0
title: "Ecommerce Vertical Template -- Direct-to-Consumer + B2B Hybrid"
description: "Master vertical template for ecommerce brands selling physical products via D2C + B2B/partner channels, with marketplace integrations and AI-assisted commerce features."
domain: ecommerce
nucleus: N06
quality: 9.1
tags: [ecommerce, vertical, d2c, b2b, marketplace, shopify, erp, partner-program]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_VERTICAL
  - BRAND_MARKETPLACE_A
  - BRAND_MARKETPLACE_B
  - BRAND_ERP
  - BRAND_AOV
  - BRAND_MONTHLY_VISITORS
  - BRAND_CONVERSION_RATE
  - BRAND_PERSONA_NAME
density_score: 1.0
related:
  - p01_kc_seo_content_strategy_ecommerce
  - bld_collaboration_ecommerce_vertical
  - bld_examples_ontology
  - bld_tools_supabase_data_layer
  - bld_tools_partner_listing
  - p12_mission_supabase_data_layer
  - bld_examples_action_prompt
  - p02_agent_commercial_nucleus
  - bld_tools_ecommerce_vertical
  - bld_collaboration_partner_listing
---

# Ecommerce Vertical Template -- D2C + B2B Hybrid

> Master architecture for {{BRAND_NAME}}. Replace all `{{BRAND_*}}` values
> from your `brand_config.yaml`. Example metrics use illustrative ranges; replace
> with your brand data.

---

## 1. Vertical Identity

| Attribute | Value |
|-----------|-------|
| Brand | {{BRAND_NAME}} |
| Domain | {{BRAND_DOMAIN}} |
| Vertical | {{BRAND_VERTICAL}} |
| Commerce model | D2C + B2B partner program |
| Primary marketplace | {{BRAND_MARKETPLACE_A}} |
| Secondary marketplace | {{BRAND_MARKETPLACE_B}} |
| ERP | {{BRAND_ERP}} |
| AI persona | {{BRAND_PERSONA_NAME}} |

---

## 2. Channel Architecture

```
CONSUMER CHANNELS                   PARTNER CHANNELS
------------------                  ----------------
{{BRAND_DOMAIN}}                    B2B Portal (/b2b)
  |-- B2C storefront                  |-- Partner registration
  |-- AI chat ({{BRAND_PERSONA_NAME}}) |-- B2B dashboard
  |-- Blog + SEO                      |-- Affiliate program
  |-- Cart + checkout                 |-- Wholesale orders

MARKETPLACE CHANNELS
--------------------
{{BRAND_MARKETPLACE_A}} <-- primary (D2C)
{{BRAND_MARKETPLACE_B}} <-- secondary (D2C)
```

---

## 3. Tech Stack Architecture

### 3.1 Data Layer (Supabase)

| Table | Purpose | Sync target |
|-------|---------|-------------|
| `{{BRAND_CRM_TABLE_PREFIX}}_products` | Product catalog master | {{BRAND_MARKETPLACE_A}}, {{BRAND_ERP}} |
| `{{BRAND_CRM_TABLE_PREFIX}}_orders` | Order records | {{BRAND_ERP}} |
| `{{BRAND_CRM_TABLE_PREFIX}}_partners` | B2B partner accounts | CRM |
| `{{BRAND_CRM_TABLE_PREFIX}}_content` | Content pipeline items | Social scheduler |

### 3.2 Integration Topology

```
Supabase (master DB)
  |-- {{BRAND_MARKETPLACE_A}} <-- bidirectional sync (products, orders, inventory)
  |-- {{BRAND_MARKETPLACE_B}} <-- product enrichment + listing
  |-- {{BRAND_ERP}} <-- product catalog + stock levels
  |-- Token manager <-- OAuth tokens for all integrations (auto-refresh)
```

### 3.3 AI Commerce Layer

| Feature | Kind | Description |
|---------|------|-------------|
| AI assistant | agent | {{BRAND_PERSONA_NAME}} handles product recs + behavioral advice |
| Sales composer | prompt_template | WhatsApp/Email message generator with brand voice |
| Product enrichment | agent | Fills missing product data from marketplace APIs |
| Media kit gen | workflow | Generates 9-slot product image kits |

---

## 4. Commerce Funnel

### 4.1 D2C Funnel

```
AWARENESS           CONSIDERATION       CONVERSION          RETENTION
(~30% content)      (~40% content)      (~20% content)      (~10% content)
Blog + Social       Product demos       Cart + checkout     Reorder prompts
AI persona          Comparison posts    Promo codes         Partner upsell
                    AI recommendations  Affiliate links     Loyalty signals
```

### 4.2 Key Metrics (example values -- replace with your brand data)

| Metric | Example range | Your target |
|--------|--------------|-------------|
| Monthly visitors | 5,000-50,000 | {{BRAND_MONTHLY_VISITORS}} |
| Avg order value (AOV) | R$80-300 | {{BRAND_AOV}} |
| Conversion rate | 1.5-3.5% | {{BRAND_CONVERSION_RATE}} |
| B2B partners active | 20-200 | (your data) |
| Cart abandonment | 65-80% | (your data) |
| Return rate | 5-15% | (your data) |

---

## 5. Sync Health Protocol

### 5.1 Sync Surfaces

| Surface | Direction | Trigger | Fallback |
|---------|-----------|---------|----------|
| Product titles/SEO | Supabase -> {{BRAND_MARKETPLACE_A}} | DB webhook | Manual batch |
| Inventory levels | {{BRAND_MARKETPLACE_A}} -> Supabase | Webhook + cron | Scheduled pull |
| New products | Supabase -> {{BRAND_ERP}} | On create | Batch cron |
| Token refresh | n/a | Proactive cron | On-demand |

### 5.2 Sync Conflict Rules

1. Supabase is master for product data; marketplaces are slaves.
2. Inventory discrepancies >10 units trigger alert, not auto-correct.
3. Encoding issues (double-UTF-8) are auto-fixed on ingest.
4. Missing marketplace data is enriched from secondary marketplace API.

---

## 6. B2B Program Architecture

| Feature | Description |
|---------|-------------|
| Registration | CNPJ validation + Supabase partner record creation |
| Dashboard | Orders, stats, product catalog access |
| Pricing | B2B pricing tier (separate from D2C) |
| Affiliate | Commission-based with UTM attribution |
| Approval flow | Manual review or auto-approve by CNPJ status |

---

## 7. Content -> Revenue Bridge

| Content pillar | Funnel stage | Commerce action |
|----------------|--------------|-----------------|
| Educational | Awareness | Brand follow + product awareness |
| Product demo | Consideration | Product page visit |
| Social proof | Consideration | Add to cart |
| Promo | Conversion | Purchase with code |
| Partner spotlight | Retention | B2B referral |

---

## 8. Quality Gates

| Gate | Check | Threshold |
|------|-------|-----------|
| Sync health | Products in sync / total | >95% |
| Token freshness | Hours until expiry | >2h |
| Partner approval lag | Hours to approve new partner | <24h |
| Content coverage | Posts with product CTA / total | 20-30% |
| AI persona uptime | Chat widget availability | >99.5% |

---

## New Brand Variables

> Add to your `brand_config.yaml` if not present:
- `BRAND_MARKETPLACE_A` -- primary marketplace (e.g. Shopify)
- `BRAND_MARKETPLACE_B` -- secondary marketplace
- `BRAND_ERP` -- ERP system name
- `BRAND_PERSONA_NAME` -- AI assistant persona name
- `BRAND_CRM_TABLE_PREFIX` -- Supabase table prefix (e.g. "brand")

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_seo_content_strategy_ecommerce]] | upstream | 0.24 |
| [[bld_collaboration_ecommerce_vertical]] | downstream | 0.22 |
| [[bld_examples_ontology]] | upstream | 0.21 |
| [[bld_tools_supabase_data_layer]] | upstream | 0.21 |
| [[bld_tools_partner_listing]] | upstream | 0.20 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.18 |
| [[bld_examples_action_prompt]] | upstream | 0.18 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.17 |
| [[bld_tools_ecommerce_vertical]] | upstream | 0.17 |
| [[bld_collaboration_partner_listing]] | downstream | 0.17 |
