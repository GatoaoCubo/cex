---
kind: schema
id: bld_schema_model_provider
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for model_provider — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_embedder_provider
  - bld_schema_model_card
  - bld_schema_vector_store
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_boot_config
  - bld_schema_agent_card
  - bld_schema_constraint_spec
  - bld_schema_benchmark_suite
  - bld_schema_embedding_config
---

# Schema: model_provider
## Frontmatter Fields
| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p02_mp_{provider}) | YES | — | CEX naming |
| kind | literal "model_provider" | YES | — | CEX |
| pillar | literal "P02" | YES | — | CEX |
| version | semver string | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | — | CEX |
| updated | date YYYY-MM-DD | YES | — | CEX |
| author | string | YES | — | CEX |
| provider | enum (see below) | YES | — | CEX |
| api_key_env | string or null | YES | — | CEX convention |
| api_base_url | string or null | REC | null | Provider API |
| auth_method | enum (bearer/api-key/oauth/none) | YES | bearer | Provider API |
| models | object (see Model Tiers) | YES | — | Provider docs |
| rate_limit_rpm | integer > 0 or null | YES | — | Provider docs |
| rate_limit_tpm | integer > 0 or null | YES | — | Provider docs |
| max_retries | integer >= 0 | YES | 3 | CEX convention |
| timeout_seconds | integer > 0 | REC | 120 | CEX convention |
| fallback | string or null | YES | — | CEX routing |
| health_check_interval | integer > 0 or null | REC | 60 | CEX convention |
| cost_aware | boolean | REC | true | CEX routing |
| nucleus_assignment | list[string] or null | REC | null | CEX nucleus |
| domain | literal "llm_routing" | YES | — | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string], len >= 3 | YES | — | CEX |
| tldr | string < 160ch | YES | — | CEX |
| keywords | list[string] | REC | — | CEX |
| linked_artifacts | object | REC | — | CEX |
| data_source | URL string | YES | — | CEX |
## Provider Enum
Valid: anthropic, openai, google, ollama, groq, mistral, together, fireworks, deepseek, other
## Model Tiers
```yaml
models:
  fast: "claude-haiku-3.5"        # cheapest, fastest, simple tasks
  balanced: "claude-sonnet-4-6"    # mid-tier, most tasks
  quality: "claude-opus-4-6"       # most capable, complex tasks
```
Rule: each model ID must be currently active (not deprecated). Use full versioned identifiers.
## Rate Limits
```yaml
rate_limit_rpm: 1000    # requests per minute (account tier)
rate_limit_tpm: 80000   # tokens per minute (account tier)
max_retries: 3          # with exponential backoff + jitter
timeout_seconds: 120    # per-request timeout
```
Rule: limits must match the user's actual account tier. Free tier is default.
## Fallback Configuration
```yaml
fallback: "openai"                  # primary fallback provider
health_check_interval: 60           # seconds between health checks
cost_aware: true                    # route to cheapest capable model
```
## Body Structure (required sections)
1. `## Boundary` — model_provider IS / IS NOT
2. `## Provider Matrix` — table with Parameter + Value + Source columns
3. `## Model Tiers` — table with Tier, Model ID, Context, Pricing, Use Case
4. `## Fallback Chain` — ordered fallback list with conditions
5. `## Rate Limit Strategy` — backoff, retry, circuit breaker details
6. `## Anti-Patterns` — >= 4 common mistakes
7. `## References` — >= 1 official URL
## Constraints
- max_bytes: 4096 (body only, excl frontmatter)
- naming: p02_mp_{provider}.yaml
- id == filename stem
- every Provider Matrix row MUST have Source URL (never `-`)
- model IDs MUST be currently active
- rate limits MUST be positive integers or null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_embedder_provider]] | sibling | 0.65 |
| [[bld_schema_model_card]] | sibling | 0.54 |
| [[bld_schema_vector_store]] | sibling | 0.51 |
| [[bld_schema_integration_guide]] | sibling | 0.50 |
| [[bld_schema_reranker_config]] | sibling | 0.49 |
| [[bld_schema_boot_config]] | sibling | 0.48 |
| [[bld_schema_agent_card]] | sibling | 0.48 |
| [[bld_schema_constraint_spec]] | sibling | 0.48 |
| [[bld_schema_benchmark_suite]] | sibling | 0.47 |
| [[bld_schema_embedding_config]] | sibling | 0.47 |
