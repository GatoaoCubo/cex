---
id: ex_research_pipeline_ecommerce_br
kind: cli_tool
pillar: P04
title: "Research Pipeline — Brazilian E-commerce (CODEXA Real Production)"
version: 1.0.0
created: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
quality: 9.1
tags: [research-pipeline, example, ecommerce, brazil, marketplace, production]
tldr: "Real production config from CODEXA — pet e-commerce BR. 8 marketplaces, 30+ sources, Ayrshare+Serper+Firecrawl, STORM 5 perspectives."
density_score: 0.93
updated: "2026-04-07"
---

# Research Pipeline — Brazilian E-commerce (CODEXA)

## About
Real production config distilled from CODEXA's 13,908-line research system. Covers 8 Brazilian marketplaces, social intelligence, and trend analysis for pet e-commerce.

## Config
```yaml
identity:
  empresa: "CODEXA"
  nicho: pet_ecommerce
  idioma: pt-BR
  pais: BR

sources:
  inbound:
    - mercadolivre    # REST API v3 — 60% BR e-commerce
    - shopee          # Affiliate API + Firecrawl
    - amazon_br       # Keepa + Firecrawl
    - magalu          # Firecrawl deep scrape
    - americanas      # Firecrawl deep scrape
    - casas_bahia     # Firecrawl deep scrape
    - shein           # Firecrawl deep scrape
    - temu            # Firecrawl deep scrape
  outbound:
    - youtube         # Data API + transcript extraction
    - reddit          # r/gatos, r/pets, r/brasil
    - reclameaqui     # Complaint analysis
  search:
    - serper          # Google SERP ($0.30/1K)
    - exa             # Neural search (papers)
    - gemini_search   # Google grounding
    - openai_search   # GPT web search
  trends:
    - pytrends        # Google Trends
    - keepa           # Amazon price history
  rag:
    - local_docs      # {{BRAND_NAME}} product catalog + internal research

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
  extraction: gemini-2.5-flash    # structured marketplace data
  reasoning: gpt-5-mini           # competitive analysis
  social: gemini-2.5-flash        # YouTube/Reddit volume
  trends: gemini-2.5-flash        # numerical trend data
  critic: o4-mini                 # thinking-hard verification

budget:
  firecrawl_monthly: 3000         # $19/mo tier
  firecrawl_per_research: 10      # ~10 credits per deep scrape
  serper_daily: 100               # $0.30/1K — ~$1/day budget

output:
  formats: [html, pptx, json]
  idioma: pt-BR
  template: consulting            # navy theme, executive summary

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
```

## Production Stats
- 500+ researches executed (6 months)
- Avg 85-120 quality results per research (after CRAG)
- 18% synthesis errors caught by CRITIC
- Budget: ~$45/month (Firecrawl $19 + Serper $15 + LLM ~$11)

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_research_pipeline_ecommerce_br`
- **Tags**: [research-pipeline, example, ecommerce, brazil, marketplace, production]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |
