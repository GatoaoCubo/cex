---
id: p04_retr_multi_source_business_intel
kind: retriever
pillar: P04
title: Multi-Source Business Intelligence Retriever
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: builder_agent
domain: crm-research
store_type: multi_backend
embedding_model: null
similarity_metric: null
search_type: hybrid
top_k: 50
score_threshold: null
reranker: null
llm_function: INJECT
tags: [retriever, multi-source, crm, business-intel, aggregation, GATO3]
tldr: "Agregador multi-fonte que orquestra coleta de dados business pet de 6 backends simultaneos — SERPER, FIRECRAWL, EXA, FETCH, social, delivery."
quality: 9.0
density_score: null
---

# Multi-Source Business Intelligence Retriever

## Overview
Retriever multi-backend para pipeline CRM pet. Nao usa embedding store tradicional — agrega resultados de 6 fontes externas em formato unificado. Cada fonte tem adapter proprio com dedup cruzada por telefone+endereco. Resultados consolidados alimentam o validator e response_format downstream.

## Sources & Adapters
```yaml
sources:
  serper:
    type: api
    tool: mcp__google-search__search_web
    output: [title, url, snippet]
    rate: 2500/mo
    priority: 1
    use_for: [pet_shop, veterinario, banho_tosa, distribuidor]

  firecrawl_directories:
    type: scraper
    tool: mcp__firecrawl__firecrawl_scrape
    targets: ["telelistas.net/{cidade}/pet", "guiamais.com.br"]
    output: [nome, telefone, endereco, segmento]
    rate: 500/mo
    priority: 2

  firecrawl_social:
    type: scraper
    tool: mcp__firecrawl__firecrawl_scrape
    targets: ["instagram.com/explore/tags/{cidade}pet", "facebook.com/search"]
    output: [nome, url_perfil, telefone_bio]
    rate: shared_with_directories
    priority: 4

  exa_semantic:
    type: api
    tool: exa_search
    output: [title, url, snippet, score]
    rate: 1000/mo
    priority: 3
    use_for: [long_tail, nichos_especificos]

  fetch_delivery:
    type: http
    tool: mcp__fetch__fetch
    targets: ["ifood.com.br/delivery/{cidade}/pet", "rappi.com.br"]
    output: [nome, endereco, categoria, rating]
    rate: unlimited
    priority: 5

  fetch_cnpj:
    type: http
    tool: mcp__fetch__fetch
    targets: ["receitaws.com.br/v1/cnpj/{cnpj}"]
    output: [razao_social, cnpj, situacao, endereco_fiscal]
    rate: unlimited
    priority: 6
```

## Dedup Strategy
```yaml
dedup:
  primary_key: telefone
  secondary_key: endereco_normalizado
  merge_policy: "Manter registro mais completo, agregar fontes_cruzadas"
  conflict_resolution: "Dado mais recente prevalece, flaggar conflito"
```

## Orchestration Flow
```text
[City Config] -> [Parallel: SERPER + FIRECRAWL + EXA]
                      |
              [Merge + Dedup Round 1]
                      |
              [Sequential: Social + Delivery]
                      |
              [Merge + Dedup Round 2]
                      |
              [Optional: CNPJ enrichment for potencial A]
                      |
              [Unified Business List]
```

## Integration
- Upstream: agent_crm_research_orchestrator (dispatch)
- Downstream: validator_business_contact_quality, response_format_crm_output_standard
- Dependencies: search_tool_pet_business_discovery (query terms)

## Footer
Store: multi_backend (6 sources) | Quality: null | Domain: crm-research
