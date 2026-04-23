---
kind: schema
id: bld_schema_embedder_provider
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for embedder_provider — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_model_provider
  - bld_schema_model_card
  - bld_schema_embedding_config
  - bld_schema_vector_store
  - bld_schema_integration_guide
  - bld_schema_search_tool
  - bld_schema_boot_config
  - bld_schema_constraint_spec
  - bld_schema_reranker_config
  - bld_schema_retriever_config
---

# Schema: embedder_provider
## Frontmatter Fields
| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p01_emb_{provider}_{slug}) | YES | — | CEX naming |
| kind | literal "embedder_provider" | YES | — | CEX |
| pillar | literal "P01" | YES | — | CEX |
| version | semver string | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | — | CEX |
| updated | date YYYY-MM-DD | YES | — | CEX |
| author | string | YES | — | CEX |
| provider | enum (see below) | YES | — | CEX |
| model | string | YES | — | Provider API |
| dimensions | integer > 0 | YES | — | Provider docs |
| dimensions_override | integer > 0 or null | REC | null | Matryoshka |
| max_tokens | integer > 0 | YES | — | Provider API |
| batch_size | integer > 0 | YES | — | Provider API |
| normalize | boolean | YES | — | Provider docs |
| truncate | boolean or string | REC | true | Provider API |
| distance_metric | enum (cosine/dot_product/euclidean) | YES | cosine | Math |
| matryoshka | boolean | REC | false | Provider docs |
| sparse_support | boolean | REC | false | Provider docs |
| api_key_env | string or null | YES | — | CEX convention |
| api_base_url | string or null | REC | null | Provider API |
| pricing | object (see Pricing Policy) | REC | — | Provider docs |
| mteb_score | float or null | REC | null | MTEB leaderboard |
| domain | literal "embedding" | YES | — | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string], len >= 3 | YES | — | CEX |
| tldr | string < 160ch | YES | — | CEX |
| keywords | list[string] | REC | — | CEX |
| linked_artifacts | object | REC | — | CEX |
| data_source | URL string | YES | — | CEX |
## Provider Enum
Valid: openai, cohere, voyage, jina, nomic, local, huggingface, other
## Pricing Policy
Frontmatter uses standard API pricing (not enterprise or volume discounts).
```yaml
pricing:
  per_1m_tokens: float  # USD per 1M tokens. null if local/free.
  per_request: float or null  # if provider charges per request instead
  currency: USD
```
Rule: local models = null (not 0). Free API tier = 0.00 (not null).
## Dimension Spec
```yaml
dimensions: 1536           # native output dimensions
dimensions_override: 512   # reduced via matryoshka (if supported)
matryoshka: true            # supports MRL dimension reduction
```
Rule: dimensions_override MUST be <= dimensions. Only valid if matryoshka: true.
## Body Structure (required sections)
1. `## Boundary` — embedder_provider IS / IS NOT
2. `## Configuration Matrix` — table with Parameter + Value + Source columns
3. `## Dimension Tradeoffs` — native vs reduced dimension comparison
4. `## Integration Pattern` — SDK initialization code snippet
5. `## Anti-Patterns` — >= 4 common mistakes
6. `## References` — >= 1 official URL
## Constraints
- max_bytes: 4096 (body only, excl frontmatter)
- naming: p01_emb_{provider}_{model_slug}.yaml
- id == filename stem
- every Configuration row MUST have Source URL (never `-`)
- dimensions and max_tokens MUST be positive integers
- normalize MUST be boolean (never string)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_provider]] | sibling | 0.71 |
| [[bld_schema_model_card]] | sibling | 0.57 |
| [[bld_schema_embedding_config]] | sibling | 0.56 |
| [[bld_schema_vector_store]] | sibling | 0.55 |
| [[bld_schema_integration_guide]] | sibling | 0.53 |
| [[bld_schema_search_tool]] | sibling | 0.53 |
| [[bld_schema_boot_config]] | sibling | 0.52 |
| [[bld_schema_constraint_spec]] | sibling | 0.52 |
| [[bld_schema_reranker_config]] | sibling | 0.51 |
| [[bld_schema_retriever_config]] | sibling | 0.50 |
