---
id: n00_fallback_chain_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Fallback Chain -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, fallback_chain, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_collaboration_model_provider
  - bld_schema_model_provider
  - model-provider-builder
  - bld_schema_embedder_provider
  - bld_schema_stt_provider
  - bld_schema_boot_config
  - bld_schema_fallback_chain
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Fallback Chain defines an ordered sequence of LLM providers to attempt when the primary provider fails (quota, rate limit, outage). It governs the routing logic: try provider A, if it fails try B, then C. The fallback_chain is the resilience backbone of CEX multi-runtime deployments, ensuring nucleus availability even when individual providers are down.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `fallback_chain` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Chain name and nucleus |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Target nucleus this chain governs |
| chain | list | yes | Ordered list of provider entries |
| retry_budget | int | yes | Maximum retries per provider before fallback |
| timeout_seconds | int | yes | Provider response timeout before fallback |
| health_check | bool | yes | Whether to probe providers before dispatch |

## When to use
- When configuring multi-provider resilience for a nucleus
- When adding a new provider to an existing nucleus's fallback order
- When defining budget-optimized routing (expensive primary, cheap fallback)

## Builder
`archetypes/builders/fallback_chain-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind fallback_chain --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- operators managing multi-runtime deployments
- `{{DOMAIN_CONTEXT}}` -- provider availability and cost constraints

## Example (minimal)
```yaml
---
id: fallback_chain_n01_multi_provider
kind: fallback_chain
pillar: P02
nucleus: n01
title: "N01 Multi-Provider Fallback"
version: 1.0
quality: null
---
nucleus: n01
chain:
  - provider: claude
    model: claude-sonnet-4-6
    priority: 1
  - provider: ollama
    model: llama3.1:8b
    priority: 2
retry_budget: 3
timeout_seconds: 120
health_check: true
```

## Related kinds
- `model_provider` (P02) -- individual providers in the chain
- `boot_config` (P02) -- boot parameters for each provider
- `router` (P02) -- higher-level routing that uses fallback chains

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_provider]] | related | 0.48 |
| [[bld_schema_model_provider]] | downstream | 0.46 |
| [[model-provider-builder]] | related | 0.39 |
| [[bld_schema_embedder_provider]] | downstream | 0.37 |
| [[bld_schema_stt_provider]] | downstream | 0.37 |
| [[bld_schema_boot_config]] | downstream | 0.37 |
| [[bld_schema_fallback_chain]] | downstream | 0.37 |
| [[bld_schema_reranker_config]] | downstream | 0.37 |
| [[bld_schema_integration_guide]] | downstream | 0.36 |
| [[bld_schema_quickstart_guide]] | downstream | 0.36 |
