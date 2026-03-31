---
id: inst_research_pipeline_codexa
kind: cli_tool
pillar: P04
title: "Research Pipeline Config — CODEXA (Production)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
nucleus: N01
instance: codexa
quality: 8.9
tags: [research-pipeline, instance, codexa, gato3, production, ecommerce-br]
tldr: "Production config for CODEXA/GATO3 research pipeline. 8 BR marketplaces, 30+ sources, STORM 5 perspectives, multi-model, $45/mo budget."
density_score: 0.95
---

# Research Pipeline Config — CODEXA

## Company Profile
| Field | Value |
|-------|-------|
| Empresa | CODEXA / GATO3 |
| Nicho | Pet e-commerce (acessórios para gatos, design minimalista) |
| Idioma | pt-BR |
| País | Brasil |
| Marketplaces | 8 (ML, Shopee, Amazon, Magalu, Americanas, CB, Shein, Temu) |
| Pipeline | 7-stage STORM+CRAG+CRITIC |

## Production Config
```yaml
identity:
  empresa: "CODEXA"
  nicho: pet_ecommerce
  idioma: pt-BR
  pais: BR

sources:
  inbound:
    - mercadolivre
    - shopee
    - amazon_br
    - magalu
    - americanas
    - casas_bahia
    - shein
    - temu
  outbound:
    - youtube
    - reddit
    - reclameaqui
  search:
    - serper
    - exa
    - gemini_search
    - openai_search
  trends:
    - pytrends
    - keepa
  rag:
    - local_docs

storm_perspectives:
  - role: buyer
    focus: "preco frete reviews confianca avaliacao entrega"
  - role: seller
    focus: "posicionamento pricing qualidade-listing anuncio vendas"
  - role: analyst
    focus: "tendencias volume sazonalidade crescimento market-share"
  - role: marketer
    focus: "keywords SEO content-gaps social-proof hashtags"
  - role: consumer_researcher
    focus: "pain-points necessidades sentimento reclamacoes desejos"

multi_model:
  extraction: gemini-2.5-flash
  reasoning: gpt-5-mini
  social: gemini-2.5-flash
  trends: gemini-2.5-flash
  critic: o4-mini

budget:
  firecrawl_monthly: 3000
  firecrawl_per_research: 10
  serper_daily: 100

output:
  formats: [html, pptx, json]
  idioma: pt-BR
  template: consulting

quality:
  crag_min_score: 0.7
  critic_max_iterations: 3
  final_min_score: 8.0

marketplace_schemas:
  mercadolivre:
    fields: [title, price, sold_qty, rating, seller, shipping, brand, specs, EAN]
  shopee:
    fields: [title, price, sold_qty, shop_rating, flash_sale, reviews]
  amazon_br:
    fields: [title, price, BSR, reviews, review_summary, keepa_history]
  magalu:
    fields: [title, price, rating, seller, shipping]
  americanas:
    fields: [title, price, rating, seller]
  casas_bahia:
    fields: [title, price, rating, seller]
  shein:
    fields: [title, price, reviews, sold_qty]
  temu:
    fields: [title, price, sold_qty]
```

## Environment Variables Required
```bash
# .env (NEVER commit)
SERPER_API_KEY=...
FIRECRAWL_API_KEY=...
EXA_API_KEY=...
YOUTUBE_API_KEY=...
OPENAI_API_KEY=...
LITELLM_URL=...
LITELLM_MASTER_KEY=...
KEEPA_API_KEY=...
```

## Origin
Distilled from `codexa-core/api/core/` — 20 Python files (13,908 lines). Pipeline in production since 2025-Q2, handling 500+ researches with 85-120 quality results per query. Monthly cost: ~$45 (Firecrawl $19 + Serper $15 + LLM ~$11).
