---
id: p01_kc_api_rate_limiting_retry_patterns
kind: knowledge_card
type: infrastructure
pillar: P01
title: "API Rate Limiting and Retry Patterns"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: rate-limit-config-builder
domain: rate_limit_config
quality: 9.1
tags: [rate-limiting, retry-patterns, rpm, tpm, exponential-backoff, 429, anthropic, openai, litellm]
tldr: "API rate limits enforce RPM/TPM/RPD ceilings via token bucket or sliding window; 429s require exponential backoff with jitter — declare limits in rate_limit_config, handle retries in runtime_rule."
when_to_use: "When integrating LLM provider APIs, configuring retry logic for 429 responses, or building multi-provider rate-aware clients"
keywords: [rate limit, rpm, tpm, rpd, concurrent, token bucket, sliding window, 429, exponential backoff, jitter, retry, anthropic, openai, litellm]
density_score: 1.0
---
# API Rate Limiting and Retry Patterns

## Core Concept

Rate limits are provider-enforced ceilings on API consumption: **RPM** (requests per minute), **TPM** (tokens per minute), **RPD** (requests per day), **concurrent** (parallel in-flight). Two algorithms enforce them independently: **token bucket** (TPM — continuous refill, burst to bucket cap) and **sliding window** (RPM — rolling 60s count). Both can bind simultaneously — 10 RPM ≠ 10 concurrent; each constrains through a different axis.

`rate_limit_config` **declares** these ceilings as a static artifact. Enforcement logic belongs in `runtime_rule`. Spend caps live in `budget_usd`. Keeping these three concerns in separate artifacts prevents config changes from breaking retry logic.

## Provider Limits by Tier

| Provider | Tier | RPM | TPM | RPD | Concurrent | retry_after |
|----------|------|-----|-----|-----|------------|-------------|
| Anthropic | Free | 5 | 20,000 | 50 | 5 | 60s |
| Anthropic | Build | 50 | 80,000 | 1,000 | 10 | 60s |
| Anthropic | Scale | 4,000 | 400,000 | 100,000 | 50 | 60s |
| OpenAI | Free | 3 | 40,000 | — | 3 | varies |
| OpenAI | Tier 1 | 500 | 200,000 | — | 50 | varies |
| OpenAI | Tier 2 | 5,000 | 2,000,000 | — | 100 | varies |
| OpenAI | Tier 5 | 10,000 | 10,000,000 | — | 500 | varies |
| LiteLLM | Proxy | configurable | configurable | configurable | configurable | pass-through |

RPD: Anthropic enforces daily caps; OpenAI Tier 1+ does not. Verify against provider dashboard per model.

## Enforcement Algorithms

**Token bucket (TPM):** Each token consumed removes from a bucket that refills at `tpm/60` per second. Burst allowed up to bucket cap. When bucket empties → 429.

**Sliding window (RPM):** Counts requests in the trailing 60 seconds. Exceeding RPM → 429 immediately, regardless of token state.

Both run independently. A workflow can be RPM-compliant but TPM-blocked (large prompts per request) or TPM-compliant but RPM-blocked (many small requests). Profiling both axes is mandatory before production.

## Retry Patterns for 429

**Exponential backoff with full jitter** (recommended):
```
wait = min(cap, base * 2^attempt) * random(0, 1)
```
- `base`: 1s · `cap`: 60s (or provider `Retry-After` header) · `attempt`: 0-indexed · `random(0,1)`: uniform jitter

**Anthropic:** Returns `Retry-After: 60` on 429. Retrying sooner amplifies backoff — always honor the header.

**OpenAI:** Returns `x-ratelimit-reset-requests` and `x-ratelimit-reset-tokens` with exact Unix timestamps. Use these for precision scheduling instead of blind backoff.

| Strategy | Use When | Risk |
|----------|----------|------|
| Exponential + full jitter | Default | None — best practice |
| Retry-After header | Header present | Must parse correctly |
| Circuit breaker | Sustained limits in prod | Prevents cascade failure |
| Fixed delay (no jitter) | Never | Thundering herd on shared instances |

## Artifact Boundaries

| Concern | CEX Kind | Contains |
|---------|----------|----------|
| Quota declaration | `rate_limit_config` | RPM, TPM, RPD, concurrent, budget_usd |
| Retry/backoff logic | `runtime_rule` | Exponential backoff, circuit breaker, timeout |
| Connection config | `env_config` | API keys, base URL, model selection |

Mixing these causes drift: a `rate_limit_config` change must never force a `runtime_rule` redeploy.

## Anti-Patterns

| Anti-Pattern | Consequence |
|-------------|-------------|
| Fictional RPM/TPM values | 429 floods; false capacity ceiling — 5/8 prod integrations failed this way |
| No `budget_usd` cap | Runaway agent exhausts monthly spend with no ceiling |
| `alert_threshold: 1.0` | Alert fires at 100% — already over budget when triggered |
| Fixed retry, no jitter | Thundering herd; 429 cascades amplify under load |
| Ignoring `Retry-After` header | Repeated hammer → exponential provider penalty |
| One config for all providers | Each provider has independent limit pools; sharing causes cross-contamination |
| Retry logic inside `rate_limit_config` | Couples declaration and enforcement; breaks on config-only change |

## CEX Integration

- **Declare quotas:** `rate_limit_config` → `P09_config/examples/p09_ratelimit_{provider}.md`
- **Declare retries:** `runtime_rule` → `P09_config/examples/p09_rr_{provider}_retry.md`
- **Runtime flow:** `agent` reads `rate_limit_config` at task start → `client` throttles against RPM/TPM → `guardrail` enforces `budget_usd` circuit breaker → `runtime_rule` handles 429 backoff

Budget discipline: set `budget_usd` from actual monthly target, `alert_threshold: 0.8` (alert at 80%, hard stop at 100%), document overage policy (block vs. queue).

## References
- Anthropic rate limits: docs.anthropic.com/en/api/rate-limits
- OpenAI rate limits: platform.openai.com/docs/guides/rate-limits
- LiteLLM proxy: docs.litellm.ai/docs/proxy/rate_limit
- Backoff strategy: AWS Architecture Blog — Exponential Backoff and Jitter