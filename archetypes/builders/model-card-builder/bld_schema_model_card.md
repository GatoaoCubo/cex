---
kind: schema
id: bld_schema_model_card
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for model_card — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Model Card"
version: "1.0.0"
author: n03_builder
tags: [model_card, builder, examples]
tldr: "Golden and anti-examples for model card construction, demonstrating ideal structure and common pitfalls."
domain: "model card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_model_provider
  - bld_schema_embedder_provider
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_sandbox_spec
  - bld_schema_optimizer
  - bld_schema_multimodal_prompt
  - bld_schema_benchmark_suite
  - bld_schema_pricing_page
  - bld_schema_vector_store
---

# Schema: model_card
## Frontmatter Fields
| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p02_mc_{provider}_{slug}) | YES | — | CEX naming |
| kind | literal "model_card" | YES | — | CEX |
| pillar | literal "P02" | YES | — | CEX |
| version | semver string | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | — | CEX |
| updated | date YYYY-MM-DD | YES | — | CEX |
| author | string | YES | — | CEX |
| model_name | string | YES | — | Mitchell 2019 |
| provider | enum (see below) | YES | — | LiteLLM |
| model_type | enum (text-generation/embedding/multimodal) | YES | — | HF pipeline_tag |
| status | enum (active/deprecated/sunset) | YES | active | CEX-ext |
| release_date | date or null | REC | null | HF, Meta |
| knowledge_cutoff | YYYY-MM or null | REC | null | Mitchell |
| context_window | integer > 0 | YES | — | Universal |
| max_output | integer > 0 | YES | — | Anthropic SDK |
| modalities | object (5 bools) | YES | — | LangChain |
| features | object (8 bools) | YES | — | LiteLLM |
| pricing | object (see Pricing Policy) | YES | — | LiteLLM |
| domain | literal "model_selection" | YES | — | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string], len >= 3 | YES | — | CEX |
| tldr | string < 160ch | YES | — | CEX |
| when_to_use | string | YES | — | CEX |
| keywords | list[string] | REC | — | CEX |
| linked_artifacts | object | REC | — | CEX |
| data_source | URL string | YES | — | CEX |
## Provider Enum
Valid: anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other
## Pricing Policy
Frontmatter uses BASE TIER (lowest published price for standard API access).
If provider has tiered pricing (e.g., Google <=200K / >200K), use lowest tier.
Document higher tiers in body Specifications table.
```yaml
pricing:
  input: float    # base tier, per 1M tokens, USD. null if open-weight.
  output: float   # base tier, per 1M tokens, USD. null if open-weight.
  cache_read: float or null   # null if provider has no caching
  cache_write: float or null  # null if provider has no symmetric cache write
  unit: per_1M_tokens         # ALWAYS this value
```
Rule: open-weight = null (not 0). Free commercial tier = 0.00 (not null).
## Modalities Object
```yaml
modalities:
  text_input: bool
  text_output: bool
  image_input: bool
  audio_input: bool
  pdf_input: bool
```
## Features Object
```yaml
features:
  tool_calling: bool
  structured_output: bool
  reasoning: bool
  prompt_caching: bool
  code_execution: bool
  web_search: bool
  fine_tunable: bool
  batch_api: bool
```
## Body Structure (required sections)
1. `## Boundary` -- model_card IS / IS NOT
2. `## Specifications` — table with Value + Source columns
3. `## Capabilities` — boolean table matching features object
4. `## When to Use` — decision table >= 5 rows with alternatives
5. `## References` — >= 1 official URL
## Constraints
- max_bytes: 4096 (body only, excl frontmatter)
- naming: p02_mc_{provider}_{model_slug}.md
- id == filename stem
- every Specifications row MUST have Source URL (never `-`)
- all modalities/features values MUST be boolean

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_provider]] | sibling | 0.63 |
| [[bld_schema_embedder_provider]] | sibling | 0.61 |
| [[bld_schema_integration_guide]] | sibling | 0.53 |
| [[bld_schema_reranker_config]] | sibling | 0.52 |
| [[bld_schema_sandbox_spec]] | sibling | 0.51 |
| [[bld_schema_optimizer]] | sibling | 0.51 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.51 |
| [[bld_schema_benchmark_suite]] | sibling | 0.50 |
| [[bld_schema_pricing_page]] | sibling | 0.49 |
| [[bld_schema_vector_store]] | sibling | 0.49 |
