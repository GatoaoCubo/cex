---
id: p09_rl_anthropic_scale
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
name: "Anthropic Scale Tier Rate Limits and Retry Patterns"
provider: "anthropic"
rpm: 4000
tpm: 400000
quality: 8.8
tags: [rate_limit_config, anthropic, scale-tier, retry-patterns, 429]
tldr: "Anthropic Scale: 4K RPM, 400K TPM, 100K RPD, 50 concurrent — 60s retry-after, $500/mo cap at 80% alert"
description: "Rate limits and retry patterns for Anthropic API Scale tier — custom agreement, high-volume production"
budget_usd: 500.0
tier: "scale"
rpd: 100000
concurrent: 50
retry_after: 60
alert_threshold: 0.8
model_overrides:
  claude-3-5-sonnet-20241022:
    rpm: 4000
    tpm: 400000
  claude-3-5-haiku-20241022:
    rpm: 4000
    tpm: 400000
density_score: 1.0
---
## Overview

Scale tier rate limits for Anthropic API — 80× Build throughput via custom sales agreement. Designed for parallel agent workloads and batch pipelines exceeding Build tier capacity. Callers must read `Retry-After` header on all 429 responses and implement exponential backoff with jitter.

## Limits

| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 4,000 | All models combined |
| TPM | 400,000 | All models combined |
| RPD | 100,000 | Daily hard cap |
| Concurrent | 50 | Max parallel in-flight |
| Retry After | 60s | Per 429 `Retry-After` header |

## Tier

**Tier**: scale — requires custom agreement with Anthropic sales. Activates when Build tier (50 RPM) is consistently saturated. Next: Enterprise tier via negotiated SLA and dedicated capacity allocation.

## Budget

Cap: $500/mo. Alert at 80% ($400 spend triggers notification). Blocked at 100%; resets at billing cycle start.
Retry policy: HTTP 429 → honor `Retry-After: 60` → exponential backoff with jitter; max 3 retries before circuit open. Retry logic lives in `runtime_rule`, not here.