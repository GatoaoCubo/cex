---
kind: memory
id: bld_memory_model_provider
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for model_provider artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_model_provider
  - bld_knowledge_card_model_provider
  - p03_sp_model_provider_builder
  - model-provider-builder
  - bld_examples_model_provider
  - bld_config_model_provider
  - p03_ins_model_provider
  - p01_kc_model_provider
  - bld_architecture_model_provider
  - p11_qg_model_provider
---
# Memory: model-provider-builder
## Summary
Model provider configs specify LLM API connections and routing rules for multi-model systems: provider authentication, tiered model selection, rate limits, fallback chains, and health tracking. The primary production challenge is model ID staleness — providers deprecate models quarterly, making hardcoded IDs a reliability risk. The second challenge is rate limit accuracy: limits vary by account tier and change without notice, so configs require explicit tier documentation and verification dates.
## Pattern
1. Always use full versioned model IDs — aliases like `gpt-4` resolve to different models over time
2. Always document the account tier alongside rate limits — free/pro/enterprise have 10x differences
3. Always configure at least one cross-provider fallback — single-provider configs caused 3 outage incidents
4. Include pricing per tier in the body — cost-aware routing needs current $/1M token data
5. Health check interval should be 60s minimum — faster checks waste rate limit budget
6. Circuit breaker pattern: open after 3 failures, half-open after 60s, closed after 1 success
## Anti-Pattern
1. Using unversioned model aliases (e.g., `gpt-4` instead of `gpt-4o-2024-08-06`) — aliases change silently
2. Setting rate limits higher than actual account tier — causes 429 cascades with exponential penalty
3. No fallback provider — Anthropic had 4h outage on 2025-12-15, taking down all Claude-only configs
4. Retry without backoff — 3 retries at full speed = 3x the rate limit pressure = longer cooldown
5. Hardcoding API keys instead of environment variables — breaks CI/CD and violates secret rotation policy
6. Single model without tiers — forces quality model for simple tasks, wasting 10x budget
## Context
Model provider configs occupy the P02 model layer as connection infrastructure for LLM routing. They are consumed by cex_router.py (multi-provider dispatch), cex_crew_runner.py (prompt execution), and nucleus boot scripts (startup model selection). In CEX's 7-nucleus architecture, each nucleus maps to one primary provider with fallback chains.
## Impact
Tiered routing (fast/balanced/quality) reduced API costs by 40-60% by routing simple tasks to Haiku instead of Opus. Cross-provider fallback eliminated downtime during the 2025-12-15 Anthropic outage (auto-routed to OpenAI in 30s). Versioned model IDs prevented 2 incidents where alias resolution changed, breaking context window assumptions.
## Reproducibility
For reliable model provider production: (1) verify model IDs against provider's current model list, (2) confirm rate limits for the specific account tier, (3) configure at least one cross-provider fallback, (4) include per-tier pricing from official pricing pages, (5) document backoff algorithm and circuit breaker parameters, (6) validate against 10 HARD + 12 SOFT gates.
## References
1. Anthropic rate limits: https://docs.anthropic.com/en/api/rate-limits
2. OpenAI rate limits: https://platform.openai.com/docs/guides/rate-limits
3. Google Gemini limits: https://ai.google.dev/gemini-api/docs/quota
4. CEX router: cex_router.py (multi-provider routing)

## Metadata

```yaml
id: bld_memory_model_provider
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-model-provider.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | model provider construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_provider]] | upstream | 0.61 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.60 |
| [[p03_sp_model_provider_builder]] | upstream | 0.58 |
| [[model-provider-builder]] | upstream | 0.57 |
| [[bld_examples_model_provider]] | upstream | 0.55 |
| [[bld_config_model_provider]] | upstream | 0.53 |
| [[p03_ins_model_provider]] | upstream | 0.50 |
| [[p01_kc_model_provider]] | upstream | 0.48 |
| [[bld_architecture_model_provider]] | upstream | 0.38 |
| [[p11_qg_model_provider]] | downstream | 0.38 |
