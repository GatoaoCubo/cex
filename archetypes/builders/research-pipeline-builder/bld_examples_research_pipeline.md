---
kind: examples
id: bld_examples_research_pipeline
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of research pipeline configs
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: research-pipeline-builder

## Golden Example — E-commerce BR (CODEXA)
INPUT: "Create research pipeline config for Brazilian pet e-commerce marketplace intelligence"
OUTPUT:
```yaml
identity:
  empresa: "CODEXA"
  nicho: pet_ecommerce
  idioma: pt-BR
  pais: BR
sources:
  inbound: [mercadolivre, shopee, amazon_br, magalu, americanas, casas_bahia, shein, temu]
  outbound: [youtube, reddit, reclameaqui]
  search: [serper, exa, gemini_search, openai_search]
  trends: [pytrends, keepa]
  rag: [local_docs]
storm_perspectives:
  - {role: buyer, focus: "preco frete reviews confianca"}
  - {role: seller, focus: "positioning pricing quality listing"}
  - {role: analyst, focus: "tendencias volume sazonalidade crescimento"}
  - {role: marketer, focus: "keywords SEO content-gaps social-proof"}
  - {role: consumer_researcher, focus: "pain-points necessidades sentimento"}
multi_model:
  extraction: gemini-2.5-flash
  reasoning: gpt-5-mini
  social: gemini-2.5-flash
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
```
WHY GOOD: All source categories covered, STORM perspectives costmized to niche, budget caps defined, multi-model routing by task, quality gates explicit.

## Anti-Example — Single Source Research
```python
# BAD: single source, no quality gate, no verification
results = google_search(query)  # only 1 source
report = gpt4(f"analyze: {results}")  # no CRAG scoring
return report  # no CRITIC verification
```
WHY BAD: Single source (no STORM), no quality gate (no CRAG), no verification (no CRITIC), no budget control, no config.

## Golden Example — SaaS Global
```yaml
identity: { empresa: "TechCo", nicho: saas_analytics, idioma: en, pais: US }
sources:
  inbound: [g2, capterra, producthunt, crunchbase]
  outbound: [youtube, reddit, hackernews, twitter]
  search: [serper, exa, tavily]
  trends: [pytrends]
  rag: [internal_wiki, confluence]
storm_perspectives:
  - {role: buyer, focus: "pricing features integrations support"}
  - {role: competitor, focus: "market-share roadmap funding team-size"}
  - {role: analyst, focus: "TAM growth-rate churn-rate ARR"}
  - {role: developer, focus: "API docs SDK ease-of-integration"}
  - {role: reviewer, focus: "NPS satisfaction complaints switching-cost"}
multi_model:
  extraction: gemini-2.5-flash
  reasoning: claude-sonnet
  critic: o4-mini
budget:
  serper_daily: 50
  exa_monthly: 1000
quality: { crag_min_score: 0.7, critic_max_iterations: 3, final_min_score: 8.0 }
```
WHY GOOD: SaaS-specific sources (G2, Capterra), developer perspective, different model choices, apownte budget for SaaS research volume.
