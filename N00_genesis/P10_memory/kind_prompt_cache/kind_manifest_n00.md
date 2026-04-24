---
id: n00_prompt_cache_manifest
kind: knowledge_card
8f: F3_inject
pillar: P10
nucleus: n00
title: "Prompt Cache -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, prompt_cache, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_prompt_cache
  - prompt-cache-builder
  - bld_collaboration_prompt_cache
  - p03_sp_prompt_cache_builder
  - p01_kc_prompt_cache
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_architecture_prompt_cache
  - bld_schema_usage_report
  - bld_schema_integration_guide
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prompt_cache configures TTL, eviction, and invalidation rules for cached LLM prompt/completion pairs. By defining when cached responses remain valid and when they must be refreshed, it enables significant token cost reduction (up to 90% cache hit savings on Anthropic API) while maintaining response freshness and accuracy.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prompt_cache` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| ttl_seconds | integer | yes | Time-to-live for cached entries (Anthropic default: 300) |
| eviction_policy | enum | yes | lru \| lfu \| ttl_only |
| max_entries | integer | yes | Maximum number of cached prompt/completion pairs |
| cache_scope | enum | yes | session \| nucleus \| global |
| invalidation_triggers | array | no | Events that force cache invalidation (e.g. model_update) |
| min_prompt_tokens | integer | no | Minimum prompt size eligible for caching |

## When to use
- When configuring Anthropic prompt caching for high-traffic builders (260 pre-compiled)
- When setting up the CEX prompt cache layer via `cex_prompt_cache.py`
- When tuning cache hit rates to reduce API token costs across nucleus boots

## Builder
`archetypes/builders/prompt_cache-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prompt_cache --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: pc_builders_global
kind: prompt_cache
pillar: P10
nucleus: n07
title: "Example Prompt Cache Config"
version: 1.0
quality: null
---
# Prompt Cache: Global Builder Cache
ttl_seconds: 300
eviction_policy: lru
max_entries: 260
cache_scope: global
min_prompt_tokens: 1024
```

## Related kinds
- `compression_config` (P10) -- compression reduces prompt size before cache lookup
- `context_window_config` (P03) -- context budget that cache helps preserve
- `model_registry` (P10) -- model version changes trigger cache invalidation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_prompt_cache]] | upstream | 0.52 |
| [[prompt-cache-builder]] | related | 0.50 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.44 |
| [[p03_sp_prompt_cache_builder]] | upstream | 0.43 |
| [[p01_kc_prompt_cache]] | sibling | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.38 |
| [[bld_architecture_prompt_cache]] | upstream | 0.38 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_integration_guide]] | upstream | 0.37 |
