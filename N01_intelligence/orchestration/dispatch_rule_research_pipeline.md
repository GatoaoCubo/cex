---
id: n01_dr_research_pipeline
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule — Research Pipeline"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
nucleus: N01
quality: 9.1
tags: [dispatch-rule, research-pipeline, N01, routing, orchestration]
tldr: "Routes research/intelligence tasks to N01. Triggers on pesquisar/research/mercado/concorrente/analise keywords."
density_score: 0.88
---

# Dispatch Rule — Research Pipeline

## Routing
| Field | Value |
|-------|-------|
| Target Nucleus | N01_intelligence |
| Target Tool | N01_intelligence/tools/research_pipeline_intelligence.md |
| Builder | archetypes/builders/research-pipeline-builder/ |
| Priority | high |

## Trigger Keywords
```yaml
primary:
  - pesquisar
  - research
  - pesquisa de mercado
  - market intelligence
  - analise competitiva
  - competitive analysis
  - concorrente
  - competitor
  - mercado
  - market research
  - STORM
  - CRAG

secondary:
  - fontes de dados
  - data sources
  - marketplace analysis
  - scraping
  - firecrawl
  - trend analysis
  - tendencias
  - sentiment analysis
  - price comparison
```

## Routing Rules
| Intent Pattern | Route To | Confidence |
|---------------|----------|-----------|
| "pesquisar mercado de {nicho}" | N01 (execute pipeline) | 0.95 |
| "analise competitiva {empresa}" | N01 (execute pipeline) | 0.95 |
| "criar/build research pipeline" | N03 (build) → N01 (instance) | 0.90 |
| "configurar fontes de pesquisa" | N01 (fill config) | 0.90 |
| "tendencias de {nicho}" | N01 (trends stage only) | 0.85 |
| "implementar pipeline em Python" | N03 (code) | 0.80 |
| "deploy cron de pesquisa" | N01 (config) → N05 (deploy) | 0.85 |

## Cross-Nucleus Handoffs
| From | To | Trigger | Payload |
|------|-----|---------|---------|
| N07 | N01 | "research {topic}" | Research query + config |
| N01 | N02 | research complete | JSON insights for content strategy |
| N01 | N06 | research complete | Pricing data, competitor analysis |
| N01 | N03 | "implement pipeline" | Architecture spec |
| N01 | N05 | "deploy scheduled research" | Cron config |

## Validation
Before dispatching, verify:
1. Research query is specific enough (not just "pesquisar")
2. Company config exists or will be created
3. At least 1 source category has sources configured
4. Budget caps are defined
