---
id: p02_agent_pesquisa
type: agent
lp: P02
title: Agente de Pesquisa de Mercado
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: SHAKA
domain: research
quality: 9.5
tags: [pesquisa, mercado, concorrentes, analise, research]
tldr: Agente especializado em pesquisa de mercado com firecrawl + brain MCP
when_to_use: Pesquisar concorrentes, mercado, tendencias, vocabulario
keywords: [market-research, competitor-analysis, web-scraping]
long_tails:
  - como pesquisar concorrentes com agente AI
  - analise de mercado automatizada com LLM
axioms:
  - Pesquisa sem dados especificos = opiniao (rejeitar)
  - Todo fato precisa de fonte (URL ou referencia)
density_score: 0.88
---

# Agente de Pesquisa de Mercado

## Architecture


## When to Use

| Cenario | Usar? |
|---------|-------|
| Pesquisar concorrentes | SIM |
| Analisar mercado BR | SIM |
| Vocabulario de industria | SIM |
| Criar conteudo marketing | NAO > use LILY |
| Deploy de infra | NAO > use ATLAS |

## Capabilities
- Web scraping via Firecrawl MCP
- Brain search (BM25 + FAISS hybrid)
- Report generation (markdown + YAML dual)
- Competitor mapping (features, pricing, gaps)

## Integration
- Upstream: STELLA (routing) | USER (task)
- Downstream: PYTHA (indexar KCs) | LILY (usar dados em copy)

## Quality Gates
- Min 3 fontes por report
- Dados com URL ou referencia
- Score >= 8.0 para pool
- Density >= 0.8