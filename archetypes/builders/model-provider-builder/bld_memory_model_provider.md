---
kind: memory
id: bld_memory_model_provider
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for model_provider artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: model-provider-builder
## Summary
Model provider configs specify LLM API connections and routing rules for multi-model systems: provider authentication, tiered model selection, rate limits, fallback chains, and health tracking. The primary production challenge is model ID staleness — providers deprecate models quarterly, making hardcoded IDs a reliability risk. The second challenge is rate limit accuracy: limits vary by account tier and change without notice, so configs require explicit tier documentation and verification dates.
## Pattern
- Always use full versioned model IDs — aliases like `gpt-4` resolve to different models over time
- Always document the account tier alongside rate limits — free/pro/enterprise have 10x differences
- Always configure at least one cross-provider fallback — single-provider configs caused 3 outage incidents
- Include pricing per tier in the body — cost-aware routing needs current $/1M token data
- Health check interval should be 60s minimum — faster checks waste rate limit budget
- Circuit breaker pattern: open after 3 failures, half-open after 60s, closed after 1 success
## Anti-Pattern
- Using unversioned model aliases (e.g., `gpt-4` instead of `gpt-4o-2024-08-06`) — aliases change silently
- Setting rate limits higher than actual account tier — causes 429 cascades with exponential penalty
- No fallback provider — Anthropic had 4h outage on 2025-12-15, taking down all Claude-only configs
- Retry without backoff — 3 retries at full speed = 3x the rate limit pressure = longer cooldown
- Hardcoding API keys instead of environment variables — breaks CI/CD and violates secret rotation policy
- Single model without tiers — forces quality model for simple tasks, wasting 10x budget
## Context
Model provider configs occupy the P02 model layer as connection infrastructure for LLM routing. They are consumed by cex_router.py (multi-provider dispatch), cex_crew_runner.py (prompt execution), and nucleus boot scripts (startup model selection). In CEX's 7-nucleus architecture, each nucleus maps to one primary provider with fallback chains.
## Impact
Tiered routing (fast/balanced/quality) reduced API costs by 40-60% by routing simple tasks to Haiku instead of Opus. Cross-provider fallback eliminated downtime during the 2025-12-15 Anthropic outage (auto-routed to OpenAI in 30s). Versioned model IDs prevented 2 incidents where alias resolution changed, breaking context window assumptions.
## Reproducibility
For reliable model provider production: (1) verify model IDs against provider's current model list, (2) confirm rate limits for the specific account tier, (3) configure at least one cross-provider fallback, (4) include per-tier pricing from official pricing pages, (5) document backoff algorithm and circuit breaker parameters, (6) validate against 10 HARD + 12 SOFT gates.
## References
- Anthropic rate limits: https://docs.anthropic.com/en/api/rate-limits
- OpenAI rate limits: https://platform.openai.com/docs/guides/rate-limits
- Google Gemini limits: https://ai.google.dev/gemini-api/docs/quota
- CEX router: cex_router.py (multi-provider routing)
