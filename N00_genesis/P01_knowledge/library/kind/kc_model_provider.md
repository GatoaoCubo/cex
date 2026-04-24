---
id: p01_kc_model_provider
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P02
title: "Model Provider -- Deep Knowledge for model_provider"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: model_provider
quality: 9.1
tags: [model_provider, p02, BECOME, kind-kc, routing, llm]
tldr: "Configuration for LLM provider connections -- credentials, models, rate limits, and fallback chains"
when_to_use: "Configuring multi-provider LLM routing, adding new model providers, or setting up fallback chains"
keywords: [model, provider, llm, routing, anthropic, openai, google, fallback]
feeds_kinds: [model_provider]
density_score: null
related:
  - model-provider-builder
  - bld_collaboration_model_provider
  - bld_knowledge_card_model_provider
  - bld_memory_model_provider
  - p03_sp_model_provider_builder
  - p03_ins_model_provider
  - bld_examples_model_provider
  - bld_config_model_provider
  - p11_qg_model_provider
  - p02_mp_anthropic
---

# Model Provider

## Spec
```yaml
kind: model_provider
pillar: P02
llm_function: BECOME
max_bytes: 3072
naming: p02_mp_{{provider}}.yaml
core: false
```

## Purpose

A model provider config defines how CEX connects to an LLM API. Each provider has models, tiers (fast/balanced/quality), rate limits, and API key configuration. The `cex_router.py` reads these configs to make per-request routing decisions.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| provider | Service identifier | `anthropic`, `openai`, `google`, `local` |
| api_key_env | Env var name | `ANTHROPIC_API_KEY` |
| models.fast | Low-latency model | `claude-3-5-haiku-20241022` |
| models.balanced | Default model | `claude-sonnet-4-6` |
| models.quality | Best quality model | `claude-opus-4-6` |
| rate_limit_rpm | Requests per minute | `60` |
| rate_limit_tpm | Tokens per minute | `100000` |
| fallback | Next provider if this fails | `openai` |
| max_retries | Retry count on transient errors | `3` |

## Key Patterns

1. **Tiered routing**: nucleus type determines tier (N01 research -> quality, N02 marketing -> balanced)
2. **Fallback chains**: anthropic -> google -> openai (if primary is down or rate-limited)
3. **Cost-aware**: route batch/low-priority work to cheaper models automatically
4. **Health tracking**: `cex_router.py` records error rates per provider, degrades unhealthy ones

## Anti-Patterns

- Hardcoding model IDs in tool code (breaks when models are deprecated)
- Single provider without fallback (single point of failure)
- No rate limit config (429 storms on batch operations)
- Using quality tier for everything (10x cost with marginal quality gain for routine tasks)

## CEX Integration

- `router_config.yaml` maps 4 providers x 7 nuclei with fallback chains
- `cex_router.py` reads model_provider configs at runtime
- `cex_crew_runner._resolve_model()` (T02) delegates to Router
- Provider health metrics stored in router state for adaptive routing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[model-provider-builder]] | related | 0.55 |
| [[bld_collaboration_model_provider]] | related | 0.53 |
| [[bld_knowledge_card_model_provider]] | sibling | 0.52 |
| [[bld_memory_model_provider]] | downstream | 0.51 |
| [[p03_sp_model_provider_builder]] | downstream | 0.51 |
| [[p03_ins_model_provider]] | downstream | 0.51 |
| [[bld_examples_model_provider]] | downstream | 0.49 |
| [[bld_config_model_provider]] | downstream | 0.46 |
| [[p11_qg_model_provider]] | downstream | 0.45 |
| [[p02_mp_anthropic]] | related | 0.45 |
