---
id: p02_agent_pesquisa
kind: agent
pillar: P02
title: Agente de Pesquisa de Mercado
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: research_agent
domain: research
quality: 9.1
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

```
INPUT                    BRAIN                     OUTPUT
  |                        |                         |
  v                        v                         v
[user_query]  --->  [query_expansion]  --->  [structured_report]
[domain]             |           |            |
[depth]              v           v            v
                 [BM25]    [FAISS]       [markdown_table]
                     \       /            [yaml_summary]
                      v     v             [confidence]
                  [hybrid_rank]           [sources]
                       |
                       v
               [firecrawl_enrich]
                       |
                       v
                [quality_filter]
                  (score >= 8.0)
```

### Input Schema

```yaml
input:
  query:
    type: string
    required: true
    description: Pergunta de pesquisa em linguagem natural
    example: "concorrentes de fone bluetooth TWS no Mercado Livre"
  domain:
    type: string
    required: false
    default: "ecommerce"
    enum: [ecommerce, tech, finance, general]
  depth:
    type: integer
    required: false
    default: 3
    description: Nivel de profundidade (1=rapido, 5=exaustivo)
  sources_limit:
    type: integer
    required: false
    default: 5
    description: Numero maximo de fontes a consultar
```

### Output Schema

```yaml
output:
  summary:
    type: string
    description: Resumo executivo em 2-3 frases
  findings:
    type: array
    items:
      fact: string
      source: string (URL ou referencia)
      confidence: float (0.0-1.0)
  recommendations:
    type: array
    items:
      action: string
      priority: enum [high, medium, low]
      rationale: string
  metadata:
    sources_consulted: integer
    firecrawl_credits_used: integer
    execution_time_s: float
    quality_score: float
```

## When to Use

| Cenario | Usar? |
|---------|-------|
| Pesquisar concorrentes | SIM |
| Analisar mercado BR | SIM |
| Vocabulario de industria | SIM |
| Criar conteudo marketing | NAO > use marketing_agent |
| Deploy de infra | NAO > use operations_agent |

## Capabilities
- Web scraping via Firecrawl MCP
- Brain search (BM25 + FAISS hybrid)
- Report generation (markdown + YAML dual)
- Competitor mapping (features, pricing, gaps)

## Integration
- Upstream: orchestrator (routing) | USER (task)
- Downstream: knowledge_agent (indexar KCs) | marketing_agent (usar dados em copy)

## When NOT to Use

| Cenario | Por que NAO | Use em vez |
|---------|-------------|------------|
| Gerar copy/anuncio de marketing | Pesquisa coleta dados, nao cria conteudo | marketing_agent (mlabs-content-agent, anuncio-agent) |
| Deploy, infra, database ops | Fora do dominio research | operations_agent (gateway-agent) |
| Indexar/catalogar conhecimento existente | Pesquisa descobre, nao organiza | knowledge_agent (indexer-agent, mentor-agent) |

## Common Issues

| Problema | Causa | Solucao |
|----------|-------|---------|
| Resultados genericos sem dados | Depth=1 e query vaga | Aumentar depth para 3+, refinar query com termos especificos |
| Firecrawl credits esgotados | Pesquisa em >10 URLs sem conservation mode | Ativar conservation mode (<20% budget), limitar sources_limit |
| Fontes sem URL/referencia | Brain search retornou KCs internas sem source | Filtrar resultados: exigir `source` field preenchido |

## Quality Gates
- Min 3 fontes por report
- Dados com URL ou referencia
- Score >= 8.0 para pool
- Density >= 0.8