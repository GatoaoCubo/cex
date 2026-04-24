---
id: ex_research_pipeline_food_local
kind: cli_tool
8f: F5_call
pillar: P04
title: "Research Pipeline — Local Food Business Intelligence"
version: 1.0.0
created: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
quality: 9.1
tags: [research-pipeline, example, food, local, social, trends]
tldr: "Config for local food business — social-first research (YouTube, Instagram, TikTok), Google Trends for seasonality, iFood/Rappi for delivery landscape."
density_score: 0.88
updated: "2026-04-07"
related:
  - bld_examples_research_pipeline
  - p04_rp_marketing_nucleus
  - ex_research_pipeline_ecommerce_br
  - tpl_research_pipeline
  - ex_social_publisher_bakery
  - bld_output_template_research_pipeline
  - p02_agent_research_pipeline_intelligence
  - ex_research_pipeline_saas_global
  - p04_rp_weekly_market_intelligence_brief_output_template
  - tpl_research_batch_marketplaces
---

# Research Pipeline — Local Food Business

## About
Config for a local artisan bakery researching food trends, delivery landscape, and social media content strategy. Social-first approach with heavy YouTube and TikTok analysis.

## Config
```yaml
identity:
  empresa: "Forno & Massa"
  nicho: food_artisan
  idioma: pt-BR
  pais: BR

sources:
  inbound:
    - ifood           # delivery marketplace — pricing, competitors
    - rappi           # delivery marketplace — coverage, promotions
  outbound:
    - youtube         # recipe videos, bakery vlogs, food trends
    - reddit          # r/culinaria, r/saopaulo
    - reclameaqui     # delivery complaint analysis
    - instagram       # via Serper site search — visual trends
    - tiktok          # via Serper site search — viral food content
  search:
    - serper          # Google SERP — local bakery search
    - brave           # local business reviews
  trends:
    - pytrends        # "pao artesanal", "fermentacao natural" trends
  rag:
    - local_docs      # recipes, supplier contacts, cost sheets

storm_perspectives:
  - role: customer
    focus: "sabor preco localizacao entrega horario frescor"
  - role: competitor
    focus: "cardapio precificacao delivery diferencial-unico"
  - role: trend_analyst
    focus: "ingredientes-moda sazonalidade dietas restricoes"
  - role: food_critic
    focus: "qualidade apresentacao embalagem experiencia"
  - role: marketer
    focus: "conteudo-visual hashtags reels stories engajamento"

multi_model:
  extraction: gemini-2.5-flash
  reasoning: gemini-2.5-flash    # food analysis is less complex
  social: gemini-2.5-flash       # high volume social data
  critic: o4-mini

budget:
  firecrawl_monthly: 500          # less marketplace scraping
  firecrawl_per_research: 5
  serper_daily: 30                # local search volume is lower

output:
  formats: [html, json]
  idioma: pt-BR
  template: brief                 # shorter reports for local business

quality:
  crag_min_score: 0.6             # social data is noisier — lower threshold
  critic_max_iterations: 2        # simpler analysis — fewer iterations
  final_min_score: 7.5            # local research has less data
```

## Niche Notes
- **Social-first**: food content discovery happens on Instagram/TikTok/YouTube, not marketplaces
- **iFood/Rappi**: delivery platforms reveal local competitor landscape and pricing
- **Lower CRAG threshold (0.6)**: social media data is inherently noisier
- **Fewer CRITIC iterations (2)**: local food analysis is less complex than market research
- **Seasonal focus**: pytrends reveals "panetone" in Dec, "ovo de Pascoa" in Apr
- **Brief template**: small business owners need actionable summaries, not 20-page reports
- **Lower budget**: local businesses have tighter budgets — optimize for free/cheap sources

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_research_pipeline_food_local`
- **Tags**: [research-pipeline, example, food, local, social, trends]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_research_pipeline]] | downstream | 0.37 |
| [[p04_rp_marketing_nucleus]] | sibling | 0.31 |
| [[ex_research_pipeline_ecommerce_br]] | sibling | 0.31 |
| [[tpl_research_pipeline]] | sibling | 0.31 |
| [[ex_social_publisher_bakery]] | sibling | 0.30 |
| [[bld_output_template_research_pipeline]] | downstream | 0.30 |
| [[p02_agent_research_pipeline_intelligence]] | upstream | 0.27 |
| [[ex_research_pipeline_saas_global]] | sibling | 0.26 |
| [[p04_rp_weekly_market_intelligence_brief_output_template]] | related | 0.25 |
| [[tpl_research_batch_marketplaces]] | downstream | 0.24 |
