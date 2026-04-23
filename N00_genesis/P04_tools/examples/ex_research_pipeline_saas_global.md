---
id: ex_research_pipeline_saas_global
kind: cli_tool
pillar: P04
title: "Research Pipeline — Global SaaS Competitive Intelligence"
version: 1.0.0
created: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
quality: 9.1
tags: [research-pipeline, example, saas, global, competitive-intelligence]
tldr: "Config for SaaS competitive research — G2/Capterra/ProductHunt, papers via Exa, developer community via HackerNews."
density_score: 0.88
updated: "2026-04-07"
related:
  - bld_examples_research_pipeline
  - ex_research_pipeline_academic
  - tpl_research_pipeline
  - p04_rp_weekly_market_intelligence_brief_output_template
  - ex_research_pipeline_ecommerce_br
  - bld_output_template_research_pipeline
  - p04_rp_marketing_nucleus
  - p02_agent_research_pipeline_intelligence
  - ex_research_pipeline_food_local
  - bld_schema_research_pipeline
---

# Research Pipeline — Global SaaS

## About
Config for a SaaS analytics company researching competitors, market trends, and developer sentiment. Focuses on review platforms (G2, Capterra), academic papers (Exa), and developer communities (HackerNews, Reddit).

## Config
```yaml
identity:
  empresa: "CloudMetrics"
  nicho: saas_analytics
  idioma: en
  pais: US

sources:
  inbound:
    - g2              # review platform, competitor features
    - capterra        # review platform, pricing comparison
    - producthunt     # new product launches
    - crunchbase      # funding, team size, growth signals
  outbound:
    - youtube         # product demos, conference talks
    - reddit          # r/devops, r/dataengineering
    - hackernews      # developer sentiment, product launches
    - twitter         # founder announcements, feature drops
  search:
    - serper          # Google SERP
    - exa             # academic papers, technical docs
    - tavily          # research-grade search with extraction
  trends:
    - pytrends        # search interest for product categories
  rag:
    - internal_wiki   # company product docs
    - confluence      # engineering specs

storm_perspectives:
  - role: buyer
    focus: "pricing features integrations support onboarding"
  - role: competitor
    focus: "market-share roadmap funding team-size acquisition"
  - role: analyst
    focus: "TAM growth-rate churn-rate ARR NRR"
  - role: developer
    focus: "API-docs SDK ease-of-integration latency reliability"
  - role: reviewer
    focus: "NPS satisfaction complaints switching-cost alternatives"

multi_model:
  extraction: gemini-2.5-flash
  reasoning: claude-sonnet
  social: gemini-2.5-flash
  critic: o4-mini

budget:
  serper_daily: 50
  exa_monthly: 1000
  firecrawl_monthly: 500

output:
  formats: [html, json, md]
  idioma: en
  template: consulting

quality:
  crag_min_score: 0.7
  critic_max_iterations: 3
  final_min_score: 8.0
```

## Niche Notes
- **G2/Capterra focus**: SaaS buyer journey starts with review platforms (72% of B2B buyers check G2)
- **Exa for papers**: technical SaaS needs academic papers on observability, distributed systems
- **HackerNews**: developer sentiment is a leading indicator of SaaS adoption
- **Crunchbase**: funding rounds signal competitive threat level
- **Higher reasoning model**: competitive analysis needs nuanced reasoning (Claude Sonnet over Flash)
- **Lower Firecrawl budget**: SaaS platforms have structured APIs, less scraping needed

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_research_pipeline_saas_global`
- **Tags**: [research-pipeline, example, saas, global, competitive-intelligence]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_research_pipeline]] | downstream | 0.54 |
| [[ex_research_pipeline_academic]] | sibling | 0.33 |
| [[tpl_research_pipeline]] | sibling | 0.32 |
| [[p04_rp_weekly_market_intelligence_brief_output_template]] | related | 0.30 |
| [[ex_research_pipeline_ecommerce_br]] | sibling | 0.29 |
| [[bld_output_template_research_pipeline]] | downstream | 0.28 |
| [[p04_rp_marketing_nucleus]] | sibling | 0.26 |
| [[p02_agent_research_pipeline_intelligence]] | upstream | 0.25 |
| [[ex_research_pipeline_food_local]] | sibling | 0.25 |
| [[bld_schema_research_pipeline]] | downstream | 0.22 |
