---
id: p02_mp_anthropic
kind: model_provider
pillar: P02
title: "Example — Anthropic Claude Model Provider"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
provider: anthropic
api_key_env: ANTHROPIC_API_KEY
models:
  fast: claude-haiku-4-5-20251001
  balanced: claude-sonnet-4-6
  quality: claude-opus-4-6
rate_limit_rpm: 60
rate_limit_tpm: 100000
fallback: google
max_retries: 3
domain: model_provider
quality: 9.1
tags: [model-provider, anthropic, claude, routing, llm]
tldr: "Anthropic provider config — 3 tiers (haiku/sonnet/opus), 60 RPM, fallback to Google, $0.25-$75 per 1M tokens."
when_to_use: "Primary LLM provider for CEX nuclei when Anthropic API access is available"
keywords: [anthropic, claude, provider, routing, tier, fallback]
density_score: null
related:
  - bld_examples_model_provider
  - p01_kc_model_provider
  - p03_sp_model_provider_builder
  - bld_collaboration_model_provider
  - bld_knowledge_card_model_provider
  - model-provider-builder
  - bld_memory_model_provider
  - p03_ins_model_provider
  - bld_examples_model_card
  - bld_config_model_provider
---

# Model Provider: Anthropic Claude

## Tier Configuration
| Tier | Model | Context | Input $/1M | Output $/1M | Use Case |
|------|-------|---------|-----------|------------|----------|
| fast | claude-haiku-4-5 | 200K | $0.25 | $1.25 | Classification, formatting, simple tasks |
| balanced | claude-sonnet-4-6 | 200K | $3.00 | $15.00 | Research, analysis, code review |
| quality | claude-opus-4-6 | 200K | $15.00 | $75.00 | Architecture, multi-file refactor, orchestration |

## Rate Limits
| Limit | Value | Scope |
|-------|-------|-------|
| Requests per minute | 60 | Per API key |
| Tokens per minute | 100,000 | Per API key |
| Max concurrent | 10 | Per organization |
| Batch API discount | 50% | Async, 24h SLA |

## Nucleus-to-Tier Routing
| Nucleus | Default Tier | Rationale |
|---------|-------------|-----------|
| N01 (Research) | quality | Large document analysis needs max capability |
| N02 (Marketing) | balanced | Copy quality matters but doesn't need opus |
| N03 (Builder) | quality | Artifact construction needs precision |
| N04 (Knowledge) | balanced | KC generation is structured, not creative |
| N05 (Operations) | balanced | Code review/testing is systematic |
| N06 (Commercial) | balanced | Pricing/funnel work is template-driven |
| N07 (Orchestrator) | quality | Mission planning needs best reasoning |

## Fallback Chain
```
anthropic (primary) → google (secondary) → openai (tertiary)
```
Trigger: 3 consecutive 429/500 errors within 60 seconds.
Recovery: health check every 30s, restore when 3 consecutive successes.

## API Configuration
```yaml
provider: anthropic
api_key_env: ANTHROPIC_API_KEY
base_url: https://api.anthropic.com
api_version: "2023-06-01"
max_retries: 3
retry_delay_ms: 1000
timeout_ms: 120000
```

## Boundary
model_provider IS: connection and routing config for an LLM API with tiers, limits, and fallbacks.
model_provider IS NOT: a model card (technical spec), a boot config (agent startup), or a router (dispatch logic).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_model_provider]] | downstream | 0.47 |
| [[p01_kc_model_provider]] | related | 0.42 |
| [[p03_sp_model_provider_builder]] | downstream | 0.35 |
| [[bld_collaboration_model_provider]] | related | 0.35 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.35 |
| [[model-provider-builder]] | related | 0.34 |
| [[bld_memory_model_provider]] | downstream | 0.33 |
| [[p03_ins_model_provider]] | downstream | 0.32 |
| [[bld_examples_model_card]] | downstream | 0.30 |
| [[bld_config_model_provider]] | downstream | 0.29 |
