---
id: p02_agent_web_researcher
kind: agent
8f: F2_become
pillar: P02
title: Web Researcher Agent
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
agent_group: research_agent
domain: research
quality: 9.1
tags: [research, web, scraping, data-extraction, competitive-intelligence]
tldr: Agente autonomo de pesquisa web que coleta, estrutura e sintetiza dados de multiplas fontes online com verificacao cruzada
when_to_use: Quando precisar de dados atualizados da web com sintese estruturada
related:
  - p02_agent_pesquisa
  - p02_agent_data_validator
  - p03_pv_pesquisa_system_v2
  - agent-builder
  - bld_collaboration_agent
  - p01_kc_agent
  - p04_browser_web_scraping
  - bld_architecture_agent
  - bld_knowledge_card_agent
  - bld_instruction_agent
---

# Web Researcher Agent

## Overview
web-researcher e o agente de pesquisa web autonoma do organization. Atua quando o usuario precisa de dados atualizados de fontes online e entrega relatorios estruturados com fontes verificadas e confianca por claim.

## Architecture
```text
[Query] -> [Query Expander] -> [Multi-Source Search] -> [Scraper Router] -> [Synthesizer] -> [Report]
                                      |                        |
                               [WebSearch API]          [Static/Dynamic/API]
                               [Firecrawl]              [Anti-bot Handler]
```

## File Structure
- `manifest.yaml`: Identidade, capabilities, routing keywords
- `system_instruction.md`: Persona pesquisador + guardrails de verificacao
- `instructions.md`: Pipeline 5-fase de pesquisa (discover -> collect -> verify -> synthesize -> report)
- `scraping_strategies.md`: Decision tree para scraper selection (static/dynamic/API/stealth)

## When to Use
| Cenario | Usar? |
|---------|-------|
| Pesquisa de mercado com dados web atuais | SIM |
| Analise competitiva de precos/produtos | SIM |
| Coleta de dados estruturados de marketplaces | SIM |
| Busca em base de dados interna (pool/brain) | NAO -> use retriever-agent |
| Scraping de alto volume (>1000 paginas) | NAO -> use scraper-stealth-agent |

## Input Output
```yaml
input:
  query: string        # Pergunta ou topico de pesquisa
  sources: list        # URLs especificas (opcional)
  depth: enum          # quick|medium|deep
  max_sources: int     # Limite de fontes (default: 10)
output:
  report: markdown     # Relatorio estruturado com findings
  sources: list        # URLs com confianca score por fonte
  data: json           # Dados extraidos em formato estruturado
```

## Integration
- Upstream: orchestrator (dispatch), gateway-agent (routing), usuario direto
- Downstream: anuncio-agent (dados de produto), pricing-agent (precos competitivos)
- Dependencies: WebSearch, WebFetch, Firecrawl MCP, Brain MCP

## Quality Gates
- Minimum 3 fontes independentes por claim factual
- Confianca score >= 0.7 para inclusao no report
- Zero URLs quebradas no output final
- Cross-reference: claims conflitantes marcados explicitamente

## Common Issues
- Rate limiting em buscas rapidas -> backoff exponencial com jitter (2s base)
- Sites com anti-bot (Cloudflare) -> escalar para scraper-stealth-agent
- Dados desatualizados em cache -> forcar freshness check via timestamp validation

## Invocation
```text
# Via orchestrator dispatch
/research "analise competitiva de pet toys no Mercado Livre" --depth deep

# Via subagent direto
Agent(subagent_type="pesquisa-agent", prompt="Pesquisar precos de [produto] em ML, Shopee, Amazon BR")
```

## Related Agents
- scraper-marketplace-agent: Extrai dados brutos de marketplaces brasileiros
- ux-researcher-agent: Analisa reviews e sentiment de produtos
- seo-agent: Pesquisa keywords e SERP features

## Footer
Agent_group: research_agent | Quality: 9.0 | Domain: research

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_pesquisa]] | sibling | 0.37 |
| [[p02_agent_data_validator]] | sibling | 0.35 |
| [[p03_pv_pesquisa_system_v2]] | downstream | 0.33 |
| [[agent-builder]] | related | 0.30 |
| [[bld_collaboration_agent]] | downstream | 0.29 |
| [[p01_kc_agent]] | related | 0.29 |
| [[p04_browser_web_scraping]] | downstream | 0.28 |
| [[bld_architecture_agent]] | downstream | 0.25 |
| [[bld_knowledge_card_agent]] | upstream | 0.23 |
| [[bld_instruction_agent]] | downstream | 0.23 |
