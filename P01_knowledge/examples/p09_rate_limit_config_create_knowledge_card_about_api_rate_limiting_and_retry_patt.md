---
id: p09_rl_api_rate_limiting_retry
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: rate-limit-config-builder
title: "API Rate Limiting and Retry Patterns for LLM Providers"
name: "API Rate Limiting and Retry Patterns"
provider: anthropic
rpm: 50
tpm: 80000
quality: 9.0
tags: [rate_limit_config, anthropic, retry-patterns, api-rate-limiting, backoff]
tldr: "Anthropic Build: 50 RPM / 80K TPM / 1K RPD — exponential backoff on 429, 0.8 alert threshold, $100/mo cap"
description: "Rate quota boundaries for Anthropic Build tier with retry pattern reference for 429 handling"
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
density_score: 1.0
---
## Overview
Rate quota config for Anthropic Build tier — default production tier after $5 cumulative spend. Documents quota ceilings and the 429 retry hint. Retry logic (backoff algorithm, jitter, circuit break) belongs in `runtime_rule`; this artifact declares only numeric limits.

## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 50 | All models, rolling 60s window |
| TPM | 80,000 | Input + output tokens combined |
| RPD | 1,000 | Hard daily cap, resets UTC midnight |
| Concurrent | 10 | Max parallel in-flight requests |
| Retry-After | 60s | `Retry-After` header value on 429 |

## Tier
**build** — activated after $5 API spend. Includes all Claude 3/3.5/3.7 models.
Upgrade to Scale (4K RPM, 400K TPM) requires custom agreement with Anthropic sales.

### Retry Patterns (reference)
| Pattern | Formula | Use When |
|---------|---------|----------|
| Exponential backoff | `min(60 * 2^n, 3600)` | Standard 429 |
| Jitter | `backoff * (0.8 + random(0, 0.4))` | High concurrency |
| Circuit break | Stop after 5 consecutive 429s | Sustained overload |

## Budget
Monthly cap: $100.00 · Alert at 80% ($80) · Hard stop at 100%.
Overage policy: requests blocked until billing cycle reset; no queuing.