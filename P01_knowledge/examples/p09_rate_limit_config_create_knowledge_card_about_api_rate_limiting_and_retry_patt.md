---
id: p01_kc_api_rate_limiting_retry_patterns
kind: knowledge_card
type: infrastructure
pillar: P01
title: "API Rate Limiting and Retry Patterns"
version: 1.0.0
created: 2026-03-29
updated: 2026-04-02
author: builder_agent
domain: rate_limit_config
quality: 9.1
tags: [knowledge_card, rate-limit-config, api, rpm, tpm, retry, 429, backoff, budget, provider]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD with retry patterns and budget controls"
when_to_use: "When integrating LLM provider APIs and configuring rate limits, retry logic, and cost controls"
keywords: [rate limit, rpm, tpm, rpd, concurrent, retry, 429, backoff, exponential, token bucket, sliding window, budget, alert_threshold, anthropic, openai, litellm]
density_score: 1.0
---
# API Rate Limiting and Retry Patterns

## Core Concept

Rate limits are provider-enforced ceilings on API consumption: **RPM** (requests per minute), **TPM** (tokens per minute), **RPD** (requests per day), **concurrent** (parallel in-flight). Two algorithms enforce them independently: **token bucket** (TPM — continuous refill, burst to bucket cap) and **sliding window** (RPM — rolling 60s count). Both can bind simultaneously — 10 RPM ≠ 10 concurrent; each constrains through a different axis.

`rate_limit_config` **declares** these ceilings as a static artifact. Enforcement logic belongs in `runtime_rule`. Spend caps live in `budget_usd`. Keeping these three concerns in separate artifacts prevents config changes from breaking retry logic.

## Provider Limits by Tier

| Provider | Tier | RPM | TPM | RPD | Concurrent | Notes |
|----------|------|-----|-----|-----|------------|-------|
| Anthropic | Free | 5 | 20,000 | 50 | — | claude.ai accounts |
| Anthropic | Build | 50 | 80,000 | 1,000 | 10 | After $5 cumulative spend |
| Anthropic | Scale | 4,000 | 400,000 | 100,000 | 50 | Custom agreement required |
| OpenAI | Free | 3 | 40,000 | — | — | Trial accounts |
| OpenAI | Tier 1 | 500 | 200,000 | — | — | $5 spent |
| OpenAI | Tier 2 | 5,000 | 2,000,000 | — | — | $50 spent |
| OpenAI | Tier 5 | 10,000 | 10,000,000 | — | — | $1,000 spent |
| LiteLLM | Proxy | configurable | configurable | configurable | configurable | Aggregates providers; passes through 429s |

## Retry Pattern: Exponential Backoff with Jitter

```python
import time, random

def call_with_retry(fn, max_retries=5, base_delay=1.0):
    for attempt in range(max_retries):
        try:
            return fn()
        except RateLimitError as e:
            retry_after = int(e.headers.get("Retry-After", base_delay * (2 ** attempt)))
            jitter = random.uniform(0, retry_after * 0.1)
            time.sleep(retry_after + jitter)
    raise MaxRetriesExceeded()
```

**Rules:**
- Always read `Retry-After` header — Anthropic returns 60s; use it, do not guess
- Add ±10% jitter to prevent thundering herd when many clients hit 429 simultaneously
- Exponential backoff only when `Retry-After` absent: `base × 2^attempt`, capped at 60s
- Track retry budget per request (max 5 attempts) — infinite retry loops amplify 429 cascades

## Budget Controls

| Field | Value | Purpose |
|-------|-------|---------|
| `budget_usd` | e.g. 100.0 | Monthly hard stop — blocks requests when exceeded |
| `alert_threshold` | 0.8 | Alert at 80% of budget before hitting ceiling |
| `overage_policy` | blocked \| queued | Behavior when `budget_usd` exceeded |

Set `alert_threshold: 0.8` — alerting at 100% is too late to react. Missing `budget_usd` means one runaway agent exhausts monthly spend silently.

## When to Use / When NOT

**Use** when:
- Integrating any paid LLM provider API
- Running parallel agents that share a provider quota pool
- Setting up cost-controlled production deployments
- Configuring multi-provider load balancing via LiteLLM proxy

**Do NOT use** for:
- Retry/backoff logic implementation → `runtime_rule`
- API keys, base URLs, model selection → `env_config`
- Execution timeouts, circuit breakers → `guardrail`
- One config spanning multiple providers — each has independent limit pools

## Anti-Patterns

| Anti-Pattern | Consequence |
|-------------|-------------|
| `rpm: 9999999` (fictional) | Runtime enforces wrong ceiling; real 429s arrive unexpectedly |
| No `budget_usd` | Runaway agent exhausts monthly spend; first signal is the invoice |
| `alert_threshold: 1.0` | Alert fires at 100% — no time to react before hard stop |
| No `retry_after` | Callers default to 1s fixed retry, creating storms on 429 |
| Retry logic inside `rate_limit_config` | Config changes break retry behavior; violates separation of concerns |
| Single config for all providers | Provider A's 429 triggers Provider B's backoff — misdiagnosis |

## CEX Integration

- `rate_limit_config` (P09) → declares RPM/TPM/budget ceilings (this KC's domain)
- `runtime_rule` (P09) → implements retry/backoff logic against those ceilings
- `env_config` (P09) → holds API keys and endpoint URLs
- `guardrail` (P11) → enforces cost circuit breakers referencing `budget_usd`
- `agent` (P02) → reads `rate_limit_config` to throttle parallel task execution

## References

- Anthropic rate limits: docs.anthropic.com/en/api/rate-limits
- OpenAI rate limits: platform.openai.com/docs/guides/rate-limits
- LiteLLM proxy config: docs.litellm.ai/docs/proxy/rate_limit
- Related artifact: `p09_rl_anthropic_build` — Anthropic Build tier rate_limit_config
- Related artifact: `p09_rl_openai_tier2` — OpenAI Tier 2 rate_limit_config