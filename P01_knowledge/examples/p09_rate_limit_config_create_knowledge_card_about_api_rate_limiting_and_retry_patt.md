---
id: p09_rl_anthropic_build
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-03-29"
updated: "2026-04-02"
author: builder_agent
title: "Anthropic Build Tier — Rate Limits & Retry Patterns"
name: "Anthropic Build Tier Rate Limits"
provider: anthropic
rpm: 50
tpm: 80000
quality: 8.8
tags: [rate_limit_config, anthropic, build-tier, retry, 429]
tldr: "Anthropic Build: 50 RPM, 80K TPM, 1K RPD, 10 concurrent; retry_after 60s; $100/mo cap, 80% alert"
description: "Rate limits for Anthropic API Build tier — activated after $5 spend. Documents quota ceilings and 429 retry hint."
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
    tpm: 80000
density_score: 1.0
---
## Overview
Rate quota config for Anthropic Build tier — default production tier after $5 cumulative API spend. Declares RPM, TPM, RPD, and concurrent ceilings. Retry logic (backoff, jitter, circuit break) belongs in `runtime_rule`; this artifact declares only numeric limits and the 429 recovery hint.

## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 50 | All models, rolling 60s window |
| TPM | 80,000 | Input + output tokens combined |
| RPD | 1,000 | Hard daily cap; resets UTC midnight |
| Concurrent | 10 | Max parallel in-flight requests |
| Retry-After | 60s | `Retry-After` header on 429 response |

## Tier
**build** — activated after $5 API spend. Includes all Claude 3/3.5/3.7 models.
Upgrade to **Scale** (4K RPM, 400K TPM, 100K RPD) requires custom agreement with Anthropic sales.
claude-3-haiku-20240307 carries a higher TPM allowance (100K) vs the 80K tier default.

## Budget
Monthly cap: **$100.00**
Alert threshold: **80%** — notify at $80 spend.
Overage policy: requests blocked at limit; budget resets at billing cycle start.