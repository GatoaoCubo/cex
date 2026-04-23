---
id: p01_kc_csv_as_knowledge
kind: knowledge_card
pillar: P01
title: "CSV as Knowledge — Structured Data as Searchable Runtime Knowledge Base"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [csv, knowledge-base, bm25, structured-data, runtime-search]
tldr: "CSVs como knowledge base searchable via BM25 — sem banco, sem embeddings, sem servidor, ~50ms por query"
when_to_use: "Precisar de recomendacoes contextuais baseadas em dados estruturados sem infraestrutura externa"
keywords: [csv-knowledge, structured-search, data-driven-decisions, bm25-csv]
long_tails:
  - "Como usar CSVs como knowledge base para agentes LLM"
  - "Quando usar CSV com BM25 ao inves de banco de dados"
axioms:
  - "SEMPRE um CSV por dominio — nunca um CSV gigante multi-proposito"
  - "NUNCA hardcodar recomendacoes em codigo — usar CSV como fonte"
linked_artifacts:
  primary: null
  related: [p01_kc_bm25_search, p01_kc_agentskills_spec]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - p01_kc_bm25_search
  - p06_schema_export_format
  - p01_kc_multi_stack
  - bld_collaboration_agentic_rag
  - bld_collaboration_eval_metric
  - p01_kc_slide_generation
  - p02_agent_data_validator
  - p01_kc_brand_skill
  - p01_kc_brand_tokens_pipeline
  - bld_collaboration_ecommerce_vertical
---

## TL;DR

CSVs funcionam como knowledge bases consultaveis em runtime via BM25. Sem banco de dados, sem embeddings, sem servidor. Cada CSV e um dominio especializado (produtos, estilos, cores, tipografia) com busca em ~50ms. Pattern comprovado com 55+ CSVs em producao cobrindo design, UX e recomendacoes.

## Conceito Central

A premissa e que dados estruturados com keywords bem definidas nao precisam de embeddings para retrieval eficaz. Um CSV com colunas de busca (search_cols) e colunas de output (output_cols) separadas cria uma decision table consultavel: cada linha e uma regra codificada como dado, nao como codigo.

O pattern funciona porque CSVs sao: editaveis por humanos (Excel, Google Sheets), versionaveis (git diff legivel), portaveis (sem dependencia de runtime) e composiveis (multiplos CSVs consultados em paralelo). A busca BM25 no search_cols retorna as linhas mais relevantes, e o sistema extrai apenas os output_cols necessarios.

A separacao de dominios e critica: um CSV por tipo de conhecimento (produtos, estilos, guidelines) garante que BM25 opera num espaco lexico focado. CSVs grandes multi-proposito degradam precisao porque termos comuns a varios dominios diluem o ranking.

## Arquitetura/Patterns

| Componente | Arquivo | Conteudo |
|------------|---------|----------|
| Catalogo | products.csv | 161 tipos de produto + recomendacoes |
| Estilos | styles.csv | 67 estilos UI + CSS keywords |
| Cores | colors.csv | 161 paletas por tipo de produto |
| Tipografia | typography.csv | 57 font pairings + Google Fonts |
| Landing | landing.csv | 24 patterns + CTA strategies |
| UX Rules | ux-guidelines.csv | 99 regras + anti-patterns |

Schema padrao de cada CSV:
```
search_cols: colunas indexadas pelo BM25 (keywords, desc)
output_cols: colunas retornadas nos resultados (completas)
Linha 1: header com nomes das colunas
```

Multi-domain search (5 CSVs paralelos):
```
Request -> detect domain (regex)
  -> products.csv  (categoria?)
  -> styles.csv    (estilo UI?)
  -> colors.csv    (paleta?)
  -> landing.csv   (pattern?)
  -> typography.csv (fonts?)
-> merge resultados -> output unificado
```

Estrutura replicavel para qualquer dominio:
```
dominio/
  data/entities.csv    # catalogo de entidades
  data/rules.csv       # regras de recomendacao
  data/guidelines.csv  # anti-patterns + best practices
  scripts/core.py      # BM25 engine (reutilizavel)
```

## Exemplos Praticos

| Request | CSV consultado | Resultado |
|---------|---------------|-----------|
| Landing page para spa | products.csv | Estilo, paleta, pattern |
| Font para e-commerce | typography.csv | Pares com Google Fonts URL |
| Regra UX para forms | ux-guidelines.csv | Regras ARIA + anti-patterns |
| Grafico para dados | charts.csv | Tipo recomendado + quando nao usar |

Fluxo completo:
1. User request chega ao sistema
2. Regex detecta dominio automaticamente
3. BM25 busca nos search_cols do CSV do dominio
4. Top 3-5 resultados extraidos com output_cols
5. Resultado injetado como contexto para geracao LLM

CSV como decision table:
```csv
Product Type,Primary Style,Anti-Pattern
Banking,Trust & Authority,"AI purple gradients"
Gaming,3D & Hyperrealism,"Flat design"
Healthcare,Accessible & Ethical,"Low contrast"
```

## Anti-Patterns

- CSV gigante multi-dominio (degrada precisao BM25)
- Recomendacoes hardcoded em codigo ao inves de CSV
- Embeddings para dados estruturados simples (overkill)
- Dados duplicados entre CSVs de dominios diferentes
- Search_cols com textos longos (BM25 prefere keywords)
- Ausencia de output_cols separadas (retorna tudo)

## Referencias

- source: https://github.com/kepano/obsidian-skills
- source: https://en.wikipedia.org/wiki/Okapi_BM25
- related: p01_kc_bm25_search
- related: p01_kc_agentskills_spec

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bm25_search]] | sibling | 0.34 |
| [[p06_schema_export_format]] | downstream | 0.28 |
| [[p01_kc_multi_stack]] | sibling | 0.22 |
| [[bld_collaboration_agentic_rag]] | downstream | 0.19 |
| [[bld_collaboration_eval_metric]] | downstream | 0.18 |
| [[p01_kc_slide_generation]] | sibling | 0.17 |
| [[p02_agent_data_validator]] | downstream | 0.17 |
| [[p01_kc_brand_skill]] | sibling | 0.16 |
| [[p01_kc_brand_tokens_pipeline]] | sibling | 0.16 |
| [[bld_collaboration_ecommerce_vertical]] | downstream | 0.16 |
