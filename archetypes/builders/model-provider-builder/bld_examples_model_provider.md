---
kind: examples
id: bld_examples_model_provider
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of model_provider artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: model-provider-builder
## Golden Example
INPUT: "Configure Anthropic provider for CEX with Max subscription"
OUTPUT:
```yaml
id: p02_mp_anthropic
kind: model_provider
pillar: P02
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
provider: "anthropic"
api_key_env: "ANTHROPIC_API_KEY"
api_base_url: null
auth_method: "api-key"
models:
  fast: "claude-haiku-3.5"
  balanced: "claude-sonnet-4-6"
  quality: "claude-opus-4-6"
rate_limit_rpm: 4000
rate_limit_tpm: 400000
max_retries: 3
timeout_seconds: 120
fallback: "openai"
health_check_interval: 60
cost_aware: true
nucleus_assignment: [N02, N03, N06, N07]
domain: llm_routing
quality: null
tags: [model-provider, anthropic, claude, multi-tier]
tldr: "Anthropic — claude-haiku/sonnet/opus tiers, 4K RPM (Max), fallback to OpenAI, cost-aware routing"
keywords: [anthropic, claude, llm-routing, fallback]
linked_artifacts:
  primary: null
  related: [p02_mp_openai, p02_mp_google]
data_source: "https://docs.anthropic.com/en/api/rate-limits"
## Boundary
model_provider IS: connection and routing config for Anthropic API (models, rate limits, fallback).
model_provider IS NOT: model_card, embedder_provider, agent, boot_config.
## Provider Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Provider | anthropic | https://docs.anthropic.com/en/api |
| API Base | https://api.anthropic.com | https://docs.anthropic.com/en/api |
| Auth Method | api-key (x-api-key header) | https://docs.anthropic.com/en/api/getting-started |
| RPM (Max tier) | 4000 | https://docs.anthropic.com/en/api/rate-limits |
| TPM (Max tier) | 400000 | https://docs.anthropic.com/en/api/rate-limits |
| Timeout | 120s | CEX convention |
## Model Tiers
| Tier | Model ID | Context | $/1M In | $/1M Out | Use Case |
|------|----------|---------|---------|----------|----------|
| fast | claude-haiku-3.5 | 200K | $0.80 | $4.00 | Classification, formatting, simple Q&A |
| balanced | claude-sonnet-4-6 | 200K | $3.00 | $15.00 | Research, analysis, general coding |
| quality | claude-opus-4-6 | 200K | $15.00 | $75.00 | Complex architecture, multi-file refactors |
## Fallback Chain
1. Primary: anthropic (claude-sonnet-4-6)
2. Fallback 1: openai (gpt-4o) — trigger: anthropic 429 or 5xx for > 30s
3. Fallback 2: google (gemini-2.5-pro) — trigger: both anthropic and openai unavailable
4. Circuit breaker: open after 3 consecutive failures, half-open after 60s
## Rate Limit Strategy
- Algorithm: exponential backoff with jitter (base=1s, max=60s)
- Retry: max 3 attempts, then fallback to next provider
- RPM tracking: sliding window per provider
- TPM tracking: token count per response, rolling 60s window
- 429 handling: immediate switch to fallback, mark provider degraded
## Anti-Patterns
1. Using `gpt-4` instead of `gpt-4o-2024-08-06` — unversioned aliases change without notice
2. Setting rate_limit_rpm to provider max without checking account tier — causes 429 cascades
3. No fallback configured — single provider outage takes down entire system
4. Retry without backoff — amplifies rate limit violations, accelerates account throttling
## References
- api: https://docs.anthropic.com/en/api
- rate-limits: https://docs.anthropic.com/en/api/rate-limits
- models: https://docs.anthropic.com/en/docs/about-claude/models
- pricing: https://docs.anthropic.com/en/docs/about-claude/pricing
```
WHY THIS IS GOLDEN:
- Every Provider Matrix row has Source URL (never `-`)
- Model IDs are current and versioned
- Rate limits match specific account tier (Max)
- Fallback chain has clear trigger conditions
- quality: null
- Anti-patterns are concrete with consequences
## Anti-Example
INPUT: "Configure OpenAI provider"
BAD OUTPUT:
```yaml
id: openai_config
kind: provider
provider: OpenAI
api_key: "sk-abc123..."
model: "gpt-4"
rate_limit: "high"
quality: 9.2
OpenAI is one of the leading AI providers. They offer powerful models
for various use cases. Contact sales for enterprise pricing.
```
FAILURES:
1. id: no `p02_mp_` prefix — H02 FAIL
2. kind: "provider" not "model_provider" — H04 FAIL
3. provider: uppercase — H07 FAIL
4. api_key: hardcoded secret — SECURITY VIOLATION
5. model: single unversioned model, no tiers — H08 FAIL
6. rate_limit: string not integer — H09 FAIL
7. quality: self-assigned 9.2 — H05 FAIL
8. No fallback configured — S03 FAIL
9. Body: marketing prose, no Provider Matrix — density FAIL
