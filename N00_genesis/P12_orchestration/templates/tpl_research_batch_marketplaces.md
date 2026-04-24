---
id: tpl_research_batch_marketplaces
kind: template
8f: F6_produce
pillar: P12
title: "Research Batch — Marketplace & Delivery Discovery"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/batch_d_marketplaces.md
variables: [INDUSTRY, MARKETPLACES, SEARCH_TERMS, CITIES, OUTPUT_FILE, SIGNAL_TAG]
density_score: 0.95
tags: [template, research-batch, marketplaces, delivery, e-commerce, crm, instance-extraction]
tldr: "Marketplace business discovery — find digitally active sellers via iFood, Rappi, Mercado Livre, Shopee, etc."
updated: "2026-04-13"
related:
  - tpl_research_batch_directories
  - tpl_research_batch_maps
  - bld_schema_model_registry
  - tpl_research_batch_social
  - tpl_research_batch_reputation
  - n06_schema_brand_config
  - tpl_research_batch_cnae
  - bld_schema_experiment_tracker
  - bld_schema_marketplace_app_manifest
  - bld_schema_tagline
---

# BATCH D — Marketplace & Delivery Discovery

**Output**: `N01_research/P05_output/data/{{OUTPUT_FILE | default: 'crm_batch_d_marketplaces.json'}}`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 {{SIGNAL_TAG | default: 'BATCH_D_MARKETPLACES'}}`

---

## Prerequisites

1. `P05_output/p05_rf_crm_output_standard.md` — JSON output format
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake validation
3. Existing CRM data file (for dedup)

---

## Objective

Find {{INDUSTRY}} businesses selling via delivery and marketplace platforms in {{REGION}}. These are the **most digitally active** prospects — they already sell online, understand e-commerce, and have operational infrastructure.

---

## Marketplace Sources

{{#MARKETPLACES}}
### {{position}}. {{name}}

```
{{#queries}}
SERPER: site:{{domain}} "{{search_term}}" "{{city}}"
{{/queries}}

{{#scrape_urls}}
FIRECRAWL: {{url}}
{{/scrape_urls}}

Extract:
  - Seller/store name
  - Address (if listed)
  - Rating / reviews on platform
  - Product category
  - Delivery availability
  - Price range signal
```

**Why this matters**: {{rationale}}

{{/MARKETPLACES}}

---

## Generic Marketplace Template

If your market doesn't have the specific marketplaces above:

| Platform Type | Examples | Value Signal |
|--------------|----------|-------------|
| Food/delivery | iFood, Rappi, UberEats, DoorDash | Active operations, delivery infrastructure |
| E-commerce | Amazon, Mercado Livre, Shopee, Etsy | Digital maturity, pricing data |
| Classifieds | OLX, Craiglist, Gumtree | Informal businesses, local reach |
| Specialized | Industry-specific platforms | Niche authority |

---

## Data Schema

```json
{
  "nome_fantasia": "string (store name on platform)",
  "cidade": "string",
  "uf": "string",
  "marketplace": "string (platform name)",
  "marketplace_url": "string",
  "rating_marketplace": "float",
  "reviews_marketplace": "integer",
  "categorias": ["string"],
  "faixa_preco": "string (low/medium/high)",
  "delivery": "boolean",
  "segmento": "string",
  "fonte": "{{marketplace_name}}",
  "digital_maturity": "high"
}
```

---

## Quality Rules

1. **Local sellers only** — filter out national chains and dropshippers
2. **Active listings** — must have recent (< 30 days) activity
3. **Location verification** — confirm city matches target region
4. **Cross-reference** — check if seller exists in other batches (dedup)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_research_batch_directories]] | sibling | 0.38 |
| [[tpl_research_batch_maps]] | sibling | 0.30 |
| [[bld_schema_model_registry]] | upstream | 0.29 |
| [[tpl_research_batch_social]] | sibling | 0.28 |
| [[tpl_research_batch_reputation]] | sibling | 0.27 |
| [[n06_schema_brand_config]] | upstream | 0.26 |
| [[tpl_research_batch_cnae]] | sibling | 0.26 |
| [[bld_schema_experiment_tracker]] | upstream | 0.25 |
| [[bld_schema_marketplace_app_manifest]] | upstream | 0.25 |
| [[bld_schema_tagline]] | upstream | 0.25 |
