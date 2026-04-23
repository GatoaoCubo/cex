---
kind: schema
id: bld_schema_prompt_cache
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for prompt_cache
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_context_window_config
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_memory_scope
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_bugloop
  - bld_schema_integration_guide
---

# Schema: prompt_cache
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_pc_{slug}) | YES | — | Namespace compliance |
| kind | literal "prompt_cache" | YES | — | Type integrity |
| pillar | literal "P10" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| title | string | YES | — | Human-readable config name |
| ttl_seconds | int | YES | 300 | Time-to-live for cached entries |
| eviction_strategy | enum (lru/lfu/fifo) | YES | lru | Which entries are removed first |
| max_entries | int | YES | 10000 | Max cached entries |
| cache_key_method | enum (hash_full/hash_prefix/semantic) | YES | hash_full | How cache keys are computed |
| invalidation_trigger | enum (ttl_expire/content_change/manual) | YES | ttl_expire | What triggers cache eviction |
| storage_backend | enum (memory/redis/sqlite) | YES | memory | Where cache lives |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "prompt_cache" |
| tldr | string <= 160ch | YES | — | Dense summary |
## ID Pattern
Regex: `^p10_pc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Cache Strategy` — TTL, eviction, max_entries rationale
2. `## Key Method` — how cache keys are computed and matched
3. `## Invalidation Rules` — what triggers cache eviction
4. `## Storage Backend` — where cache lives, scaling considerations
5. `## Integration` — how this connects to prompt assembly and model providers
## Constraints
- max_bytes: 2048
- naming: p10_pc_{name}.yaml
- eviction_strategy: lru, lfu, or fifo
- cache_key_method: hash_full, hash_prefix, or semantic
- storage_backend: memory, redis, or sqlite

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_context_window_config]] | sibling | 0.61 |
| [[bld_schema_usage_report]] | sibling | 0.61 |
| [[bld_schema_search_strategy]] | sibling | 0.60 |
| [[bld_schema_reranker_config]] | sibling | 0.60 |
| [[bld_schema_quickstart_guide]] | sibling | 0.59 |
| [[bld_schema_memory_scope]] | sibling | 0.59 |
| [[bld_schema_sandbox_config]] | sibling | 0.59 |
| [[bld_schema_dataset_card]] | sibling | 0.59 |
| [[bld_schema_bugloop]] | sibling | 0.58 |
| [[bld_schema_integration_guide]] | sibling | 0.58 |
