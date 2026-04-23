---
kind: schema
id: bld_schema_research_pipeline
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for research_pipeline config
pattern: CONFIG derives from this. TEMPLATE renders this.
quality: 9.2
title: "Schema Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_social_publisher
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_thinking_config
  - bld_schema_input_schema
---

# Schema: research_pipeline

## Config Schema (the YAML every company fills)

### identity (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| empresa | string | YES | "CODEXA" |
| nicho | string | YES | "pet_ecommerce" |
| idioma | enum(pt-BR,en,es,fr,de) | YES | "pt-BR" |
| pais | enum(BR,US,EU,UK,LATAM,APAC,costm) | YES | "BR" |

### sources (required — at least 2 categories)
| Category | Type | Required | Example |
|----------|------|----------|---------|
| inbound | list[string] | YES | [mercadolivre, shopee, amazon_br] |
| outbound | list[string] | NO | [youtube, reddit, reclameaqui] |
| search | list[string] | YES | [serper, exa, gemini_search] |
| trends | list[string] | NO | [pytrends, keepa] |
| rag | list[string] | NO | [local_docs, supabase_embeddings] |

### storm_perspectives (required, min 3)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| role | string | YES | "buyer" |
| focus | string | YES | "preco frete reviews confianca" |

### multi_model (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| extraction | string (model ID) | YES | "gemini-2.5-flash" |
| reasoning | string (model ID) | YES | "gpt-5-mini" |
| social | string (model ID) | NO | same as extraction |
| critic | string (model ID) | YES | "o4-mini" |

### budget (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| firecrawl_monthly | int | NO | 3000 |
| firecrawl_per_research | int | NO | 10 |
| serper_daily | int | NO | 100 |

### output (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| formats | list[enum(html,pptx,json,md)] | YES | [html, json] |
| idioma | string | YES | same as identity.idioma |
| template | enum(consulting,academic,brief,raw) | NO | "consulting" |

### quality (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| crag_min_score | float(0.0-1.0) | YES | 0.7 |
| critic_max_iterations | int(1-5) | YES | 3 |
| final_min_score | float(1.0-10.0) | YES | 8.0 |

### marketplace_schemas (optional — for inbound sources)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| {source_name} | object | NO | {fields: [title, price, rating, sold_qty]} |
| {source}.fields | list[string] | YES | extracted data fields per marketplace |

## Validation Rules
1. sources must have at least 2 categories populated (min: inbound + search)
2. storm_perspectives must have at least 3 entries
3. All *_env API key fields MUST be SCREAMING_SNAKE_CASE
4. No plaintext secrets anywhere in config
5. budget values must be positive integers
6. crag_min_score must be between 0.0 and 1.0
7. critic_max_iterations must be between 1 and 5
8. multi_model.critic must be a thinking/reasoning model

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.58 |
| [[bld_schema_reranker_config]] | sibling | 0.58 |
| [[bld_schema_social_publisher]] | sibling | 0.58 |
| [[bld_schema_quickstart_guide]] | sibling | 0.57 |
| [[bld_schema_pitch_deck]] | sibling | 0.57 |
| [[bld_schema_sandbox_config]] | sibling | 0.55 |
| [[bld_schema_dataset_card]] | sibling | 0.55 |
| [[bld_schema_benchmark_suite]] | sibling | 0.54 |
| [[bld_schema_thinking_config]] | sibling | 0.53 |
| [[bld_schema_input_schema]] | sibling | 0.53 |
