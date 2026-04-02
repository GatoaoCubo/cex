---
id: p09_rate_limit_config_create_knowledge_card_about_api_rate_limiting_and_retry_patt
kind: rate_limit_config
pillar: P09
version: "1.1.0"
created: "2026-04-02"
updated: "2026-04-02"
author: rate-limit-config-builder
name: "API Rate Limiting and Retry Patterns — Anthropic Build Tier Reference"
provider: anthropic
rpm: 50
tpm: 80000
quality: 8.9
tags: [rate_limit_config, anthropic, build-tier, retry-patterns, api-rate-limiting, 429-handling]
tldr: "Anthropic Build: 50 RPM, 80K TPM, 1K RPD, 10 concurrent; retry after 60s on 429; alert at 80% of $100/mo budget cap."
description: "Rate limits for Anthropic API Build tier with 429 retry guidance — quotas, budget cap, and per-model overrides."
budget_usd: 100.0
tier: build
rpd: 1000
concurrent: 10
retry_after: 60
alert_threshold: 0.8
density_score: 1.0
model_overrides:
  claude-3-5-sonnet-20241022:
    rpm: 50
    tpm: 80000
  claude-3-5-haiku-20241022:
    rpm: 50
    tpm: 100000
  claude-3-opus-20240229:
    rpm: 50
    tpm: 40000
---
## Overview
Declares quota boundaries for Anthropic API Build tier — the default production tier after $5 cumulative spend. All limits are account-level and shared across API keys. Retry logic (backoff, jitter, circuit break) belongs in `runtime_rule`; this artifact declares only the numeric ceilings and the `retry_after` hint from provider 429 headers.

## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 50 | All models combined, rolling 60s window |
| TPM | 80,000 | Tokens per minute, input + output |
| RPD | 1,000 | Daily hard cap; resets at UTC midnight |
| Concurrent | 10 | Max parallel in-flight requests |
| Retry After | 60s | Value from `Retry-After` header on 429 |

## Tier
**Tier**: build — activated after $5 cumulative API spend. Includes all Claude 3/3.5 models. Opus has reduced TPM (40K) at this tier. Upgrade to Scale (4,000 RPM / 400K TPM / 100K RPD) requires custom agreement with Anthropic sales — open a support ticket when Build is consistently saturated above 70% RPM.

## Budget
Monthly cap: $100.00. Alert threshold: 80% — trigger notification at $80 spend; circuit-break new requests at $100. Overage policy: requests blocked when `budget_usd` exceeded; budget resets at billing cycle start. Callers must read `Retry-After` header on every 429 — do not use fixed-interval retry; Anthropic may vary this value. Exponential backoff with jitter is the correct pattern in `runtime_rule`, starting at this `retry_after` value.