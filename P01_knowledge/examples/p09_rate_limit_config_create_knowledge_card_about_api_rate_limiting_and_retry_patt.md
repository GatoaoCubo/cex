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
tags: [rate-limit-config, rpm, tpm, retry, 429, backoff, budget, api, anthropic, openai]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD with retry patterns and budget controls"
when_to_use: "When integrating LLM APIs and need to declare rate limits, handle 429 errors, or govern monthly spend"
keywords: [rate limit, rpm, tpm, rpd, concurrent, 429, retry, backoff, budget, token bucket, sliding window, anthropic, openai, litellm]
density_score: 0.93
---
# API Rate Limiting and Retry Patterns

## Core Concept

Rate limits are provider-enforced ceilings on API consumption: **RPM** (requests per minute), **TPM** (tokens per minute), **RPD** (requests per day), **concurrent** (parallel in-flight). Two algorithms enforce them independently: **token bucket** (TPM — continuous refill, burst to bucket cap) and **sliding window** (RPM — rolling 60s count). Both can bind simultaneously — 10 RPM ≠ 10 concurrent; each constrains through a different axis.

`rate_limit_config` **declares** these ceilings as a static artifact. Enforcement logic belongs in `runtime_rule`. Spend caps live in `budget_usd`. Separating these three concerns prevents config changes from silently breaking retry logic.

## Provider Limits by Tier

| Provider | Tier | RPM | TPM | RPD | Concurrent | retry_after |
|----------|------|-----|-----|-----|------------|-------------|
| Anthropic | Free | 5 | 20,000 | 50 | 5 | 60s |
| Anthropic | Build | 50 | 80,000 | 1,000 | 10 | 60s |
| Anthropic | Scale | 4,000 | 400,000 | 100,000 | 50 | 60s |
| OpenAI | Free | 3 | 40,000 | — | 5 | 20s |
| OpenAI | Tier 1 | 500 | 200,000 | — | 10 | 20s |
| OpenAI | Tier 2 | 5,000 | 2,000,000 | — | 50 | 20s |
| LiteLLM | proxy | configurable | configurable | — | configurable | passthrough |

## Retry Pattern: Exponential Backoff with Jitter

```
429 received
  ↓
read Retry-After header (use if present; Anthropic returns 60s)
  ↓
wait = max(retry_after, base_delay * 2^attempt + random(0, base_delay))
  ↓
retry (max 3 attempts before circuit break)
  ↓
if 3 consecutive 429s → open circuit, alert, wait full window
```

| Strategy | Formula | When to apply |
|----------|---------|---------------|
| Fixed | `wait = retry_after` | Provider specifies exact header value |
| Exponential | `wait = base × 2^n` | Unknown backoff ceiling, single caller |
| Jittered | `wait = base × 2^n + rand(0, base)` | Multiple callers — prevents thundering herd |
| Linear | `wait = base × n` | Lightweight retry, low concurrency |

## When to Use / When NOT

**Use** `rate_limit_config` when: declaring provider quotas for Anthropic, OpenAI, or LiteLLM; defining monthly USD spend caps; configuring per-model RPM/TPM overrides in mixed-model workflows; feeding limit values into `runtime_rule` for backoff sizing.

**Do NOT use** for: retry/backoff logic (→ `runtime_rule`), API keys and base URLs (→ `env_config`), execution timeouts or circuit breakers (→ `guardrail`).

## Anti-Patterns

| Anti-Pattern | Consequence |
|-------------|-------------|
| Fictional RPM/TPM ("unlimited", 9999999) | 429 floods; false capacity ceiling reached unexpectedly |
| No `budget_usd` cap | Runaway agent exhausts monthly spend with no ceiling |
| `alert_threshold: 1.0` | Alert fires at 100% — overspend already occurred |
| Fixed 1s retry after 429 | Retry storm amplifies cascade; exponential backoff required |
| Retry logic inside rate_limit_config | Config change silently breaks retry behavior |
| One config spanning multiple providers | Each provider has independent limit pools; must be separate artifacts |
| No `rpd` when Anthropic enforces daily cap | Build tier hits 1K RPD before RPM ceiling — invisible bottleneck |

## CEX Integration

- **Kind**: `rate_limit_config` (P09) — declarative, consumed by `client`, `agent`, `guardrail`
- **Budget control**: `budget_usd` + `alert_threshold: 0.8` → notify at 80%, hard-block at 100%
- **Model overrides**: `model_overrides` map overrides tier defaults per model ID (e.g. `claude-3-5-sonnet-20241022`)
- **Boundary contract**: `rate_limit_config` (WHAT limits exist) → `runtime_rule` (HOW to handle violations) → `env_config` (WHERE to connect)
- **ID pattern**: `p09_rl_{provider}_{tier}` — one artifact per provider-tier combination
- **Accuracy rule**: copy RPM/TPM from provider API console for the exact tier — never estimate