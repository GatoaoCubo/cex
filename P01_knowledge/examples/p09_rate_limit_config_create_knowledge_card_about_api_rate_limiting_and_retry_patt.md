---
id: p09_rl_api_rate_limiting_and_retry
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-03-29"
updated: "2026-04-02"
author: builder_agent
name: "API Rate Limiting and Retry Patterns"
title: "API Rate Limiting and Retry Patterns"
provider: anthropic
rpm: 50
tpm: 80000
quality: 8.8
tags: [rate_limit_config, anthropic, retry-patterns, api-rate-limiting, 429]
tldr: "Anthropic Build: 50 RPM / 80K TPM / 1K RPD — 60s retry-after, 0.8 alert threshold, $100/mo budget cap"
description: "Rate limits for Anthropic Build tier with 429 retry guidance and budget controls"
budget_usd: 100.0
tier: "build"
rpd: 1000
concurrent: 10
retry_after: 60
alert_threshold: 0.8
density_score: 1.0
model_overrides:
  claude-3-5-sonnet-20241022:
    rpm: 50
    tpm: 80000
  claude-3-haiku-20240307:
    rpm: 50
    tpm: 100000
  claude-3-7-sonnet-20250219:
    rpm: 50
    tpm: 80000
---
## Overview
Rate quota boundaries for Anthropic Build tier — activated after $5 cumulative API spend. Declares RPM, TPM, RPD, and concurrent ceilings with 429 recovery hint. Retry backoff logic (exponential, jitter, circuit break) belongs in `runtime_rule`; this artifact declares numeric limits and the retry seed value only.

## Limits
| Dimension | Limit | Semantics |
|-----------|-------|-----------|
| RPM | 50 | Rolling 60s token-bucket; burst up to bucket size |
| TPM | 80,000 | Input + output tokens combined, sliding window |
| RPD | 1,000 | Hard daily cap; resets UTC midnight |
| Concurrent | 10 | Max parallel in-flight requests at any instant |
| Retry-After | 60s | `Retry-After` header value on 429 response |

## Tier
**build** — activated after $5 cumulative API spend. All Claude 3/3.5/3.7/4.x models included.
Upgrade: Scale tier (4K RPM / 400K TPM) requires Anthropic sales agreement.
Per-model exception: claude-3-haiku allows 100K TPM vs 80K tier default.

## Budget
Cap: $100.00/mo · Alert: 80% ($80.00) · Overage: requests blocked until billing cycle reset.