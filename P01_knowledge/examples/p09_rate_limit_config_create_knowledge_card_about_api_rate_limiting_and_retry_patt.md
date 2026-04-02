---
id: p09_rl_anthropic_build_retry
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: rate-limit-config-builder
name: "API Rate Limiting and Retry Patterns — Anthropic Build Tier"
provider: anthropic
rpm: 50
tpm: 80000
quality: 8.9
tags: [rate_limit_config, anthropic, build-tier, retry-patterns, 429, token-bucket]
tldr: "Anthropic Build: 50 RPM, 80K TPM, 1K RPD, concurrent 10 — exponential backoff 60s on 429, $100/mo cap at 80% alert"
description: "Rate limits for Anthropic Build tier with retry pattern guidance: token-bucket TPM, sliding-window RPM, exponential backoff on 429 using Retry-After header"
budget_usd: 100.0
tier: build
rpd: 1000
concurrent: 10
retry_after: 60
alert_threshold: 0.8
model_overrides:
  claude-3-5-sonnet-20241022:
    rpm: 50
    tpm: 80000
  claude-3-haiku-20240307:
    rpm: 50
    tpm: 100000
  claude-3-opus-20240229:
    rpm: 50
    tpm: 40000
density_score: 1.0
---
## Overview
Declares quota boundaries for Anthropic API Build tier — the default production tier
activated after $5 cumulative spend. Covers RPM (sliding window), TPM (token bucket),
and daily RPD caps. Retry pattern: honour `Retry-After: 60` header on 429; use
exponential backoff (base 2s, max 64s) when header absent.

## Limits
| Dimension | Limit | Algorithm | Notes |
|-----------|-------|-----------|-------|
| RPM | 50 | Sliding window (60s) | All models; resets per rolling minute |
| TPM | 80,000 | Token bucket | Refills ~1,333 tokens/s; burst to bucket cap |
| RPD | 1,000 | Fixed daily window | Hard cap; resets at UTC midnight |
| Concurrent | 10 | In-flight counter | Independent of RPM — both can bind |

**Retry pattern on 429**: read `Retry-After` header (Anthropic returns 60s); if absent,
backoff = min(2^attempt, 64)s with ±10% jitter. Max 5 retries before circuit open.

## Tier
**Tier**: build — requires $5 cumulative API spend to activate.
Includes all Claude 3/3.5/3.7 models. Per-model overrides above apply.
Upgrade to Scale (4,000 RPM / 400K TPM) requires custom agreement with Anthropic sales.

## Budget
Monthly cap: $100.00
Alert threshold: 80% — trigger notification at $80 spend.
Overage policy: requests blocked when `budget_usd` exceeded; resets at billing cycle start.
Retry logic and backoff strategy belong in `runtime_rule`, not here.