---
kind: architecture
id: bld_architecture_model_provider
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of model_provider — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - model-provider-builder
  - bld_collaboration_model_provider
  - p03_ins_model_provider
  - p03_sp_model_provider_builder
  - p01_kc_model_provider
  - bld_memory_model_provider
  - bld_knowledge_card_model_provider
  - bld_architecture_model_card
  - bld_config_model_provider
  - p11_qg_model_provider
---

# Architecture: model_provider in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 22+ field metadata header (id, kind, provider, models, rate limits, etc.) | model-provider-builder | active |
| provider_config | API endpoint, authentication method, base URL | author | active |
| model_tiers | Three-tier model selection: fast, balanced, quality | author | active |
| rate_limits | RPM and TPM constraints per account tier | author | active |
| fallback_chain | Ordered list of fallback providers with trigger conditions | author | active |
| retry_config | Max retries, backoff algorithm, timeout settings | author | active |
| health_tracking | Provider health check interval and circuit breaker state | author | active |
| cost_params | Per-model pricing for cost-aware routing decisions | author | active |
## Dependency Graph
```
provider_docs    --produces-->  model_provider  --consumed_by-->  cex_router.py
model_provider   --consumed_by-->  cex_crew_runner.py  --referenced_by-> nucleus_boot
model_provider   --signals-->      router_config.yaml
model_card       --informs-->      model_provider (model IDs, pricing)
```
| From | To | Type | Data |
|------|----|------|------|
| provider_docs (external) | model_provider | data_flow | official rate limits, model IDs, pricing |
| model_provider | cex_router.py | consumes | provider selection, model tiers, fallback chain |
| model_provider | cex_crew_runner.py | data_flow | model ID and API config for prompt execution |
| model_provider | router_config.yaml | produces | merged routing configuration for all providers |
| model_card (P02) | model_provider | dependency | model capabilities and pricing inform tier assignment |
| model_provider | nucleus_boot (boot/) | data_flow | provider and model selection for nucleus startup |
| model_provider | cex_token_budget.py | data_flow | token limits for budget calculation |
## Boundary Table
| model_provider IS | model_provider IS NOT |
|-------------------|------------------------|
| A connection and routing config for an LLM API | A technical LLM specification (model_card P02) |
| Tiered model selection (fast/balanced/quality) | An embedding model configuration (embedder_provider P01) |
| Rate limit and fallback chain definition | An agent identity or persona definition (agent P02) |
| Provider-specific with API key environment variable | A boot-time startup configuration (boot_config P02) |
| Updated when provider changes models or rate limits | A static document — must track provider deprecations |
| Scoped to one provider's API (may route to multiple models) | A cross-provider comparison table |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | provider_docs, model_card | Official documentation and model specs |
| Connection | provider_config, api_key_env | API endpoint and authentication |
| Selection | model_tiers, cost_params | Which model for which task quality level |
| Limits | rate_limits, retry_config | Operational constraints and error handling |
| Resilience | fallback_chain, health_tracking | Provider failure handling and recovery |
| Consumers | cex_router.py, cex_crew_runner.py, nucleus_boot | Systems that call LLM APIs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[model-provider-builder]] | upstream | 0.57 |
| [[bld_collaboration_model_provider]] | upstream | 0.56 |
| [[p03_ins_model_provider]] | upstream | 0.55 |
| [[p03_sp_model_provider_builder]] | upstream | 0.49 |
| [[p01_kc_model_provider]] | upstream | 0.48 |
| [[bld_memory_model_provider]] | downstream | 0.47 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.47 |
| [[bld_architecture_model_card]] | sibling | 0.44 |
| [[bld_config_model_provider]] | downstream | 0.42 |
| [[p11_qg_model_provider]] | downstream | 0.40 |
