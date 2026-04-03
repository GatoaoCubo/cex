---
id: p02_agent_crm_research_orchestrator
kind: agent
pillar: P02
title: CRM Research Orchestrator Agent
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: builder_agent
agent_node: research_agent
domain: crm-research
llm_function: BECOME
capabilities_count: 6
tools_count: 4
routing_keywords: [crm, research, discovery, pet-business, pipeline, multi-city, lead-gen]
tags: [agent, crm, research, pet-business, orchestrator, pipeline, GATO3]
tldr: "Orquestra pipeline 8-fases de descoberta CRM pet multi-cidade — coordena busca multi-fonte, validacao, scoring e output padronizado para escalar prospecao B2B."
when_to_use: "Quando precisar descobrir e catalogar businesses pet em uma cidade nova para prospecao comercial B2B"
density_score: null
quality: null
---

# CRM Research Orchestrator Agent

## Overview
crm-research-orchestrator e o agente que coordena a pipeline completa de descoberta de negocios pet para CRM B2B. Atua quando uma nova cidade precisa ser mapeada e entrega um CRM completo com contatos validados, scorados e classificados por potencial (A/B/C) e ring geografico.

## Architecture
```text
[City Config] -> [Phase 1: Setup] -> [Phase 2: Multi-Search] -> [Phase 3: Directory Enrichment]
                                                                          |
[CRM Output] <- [Phase 8: Format] <- [Phase 7: Score] <- [Phase 4: Validation]
                                                                  |
                                              [Phase 5: Social] -> [Phase 6: Delivery]
```

## Capabilities
1. **Sequenciar busca por fases (1-8)**: Executa pipeline completa de discovery city-by-city com checkpoints entre fases
2. **Coordenar multi-fonte simultaneo**: Orquestra 6+ fontes (Google Search, TeleListas, Instagram, iFood, CNPJ DBs, Facebook) com dedup cruzada
3. **Gerenciar rate limits**: Controla budgets de API (SERPER 2500/mo, FIRECRAWL 500/mo, EXA 1000/mo) com backoff e prioridade
4. **Aplicar scoring automatico**: Classifica businesses por potencial (A/B/C) baseado em completude de dados, presenca digital e alinhamento com ICP GATO3
5. **Validar contatos**: Dispara validator_business_contact_quality para verificar telefone BR, CNPJ, email e website de cada lead
6. **Gerar output CRM padronizado**: Produz markdown + JSON seguindo response_format_crm_output_standard com estatisticas de cobertura

## When to Use
| Cenario | Usar? |
|---------|-------|
| Mapear businesses pet em cidade nova | SIM |
| Expandir CRM para Ring 2/3 | SIM |
| Re-scan cidade existente (refresh trimestral) | SIM |
| Pesquisa de mercado generica (nao CRM) | NAO -> use web-researcher-agent |
| Scraping massivo sem estrutura CRM | NAO -> use scraper-agent |
| Envio de mensagens/outreach | NAO -> use N02 marketing nucleus |

## Input Output
```yaml
input:
  cidade: string       # Nome da cidade (ex: "Sao Bernardo do Campo")
  uf: string           # Estado (ex: "SP")
  ring: int            # Ring geografico 1|2|3
  segmentos: list      # Verticais pet a buscar (default: all 12)
  budget_serper: int   # Queries SERPER disponiveis (default: 50)
  budget_firecrawl: int # Scrapes FIRECRAWL disponiveis (default: 20)
output:
  crm_table: markdown  # Tabela CRM formatada com todos os contatos
  crm_data: json       # Dados estruturados por business (schema padrao)
  stats: object        # {total, por_segmento, por_potencial, taxa_contato}
  log: list            # Fases executadas com timing e contagens
```

## Integration
- Upstream: N07 orchestrator (dispatch via handoff), N01 intelligence (metodologia manual)
- Downstream: N02 marketing (outreach campaigns), N06 commercial (pricing B2B), N01 (analise)
- Dependencies: search_tool_pet_business_discovery (P04), validator_business_contact_quality (P06), retriever_multi_source_business_intel (P04), response_format_crm_output_standard (P05)

## Tool Constraints
| Role | Allowed | Forbidden |
|------|---------|-----------|
| orchestrator | Read, Grep, Glob, WebSearch, WebFetch, Agent | Write (delega producao), Edit |

## Quality Gates
- Minimo 40 businesses descobertos por cidade media (pop > 200k)
- Taxa conversao contato direto >= 60% (telefone ou whatsapp preenchido)
- 4+ fontes distintas consultadas por execucao
- Tempo total < 2h por cidade
- Zero duplicatas no output final (dedup por telefone + endereco)

## Common Issues
- Rate limit SERPER esgotado mid-pipeline -> checkpoint fase, retomar com budget restante
- Cidade pequena com < 20 businesses -> ajustar threshold e expandir raio de busca
- TeleListas indisponivel -> fallback para Google Maps scraping via Firecrawl
- Dados conflitantes entre fontes -> priorizar fonte mais recente, flaggar conflito

## Invocation
```text
# Via N07 dispatch
bash _spawn/dispatch.sh solo n03 "CRM research pipeline para Sao Bernardo do Campo"

# Via handoff direto
.cex/runtime/handoffs/n03_task.md -> cidade: SBC, ring: 1, budget: default
```

## Related Agents
- web-researcher-agent: Pesquisa web generica (crm-orchestrator e especializado para CRM pet)
- validator-agent: Valida qualidade de dados (orquestrador invoca p/ contatos)
- gateway-agent: Roteamento de requests (pode disparar crm-orchestrator)

## Footer
Satellite: research_agent | Quality: null | Domain: crm-research
