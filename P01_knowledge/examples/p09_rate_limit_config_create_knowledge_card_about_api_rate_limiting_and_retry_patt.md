---
id: p09_rl_anthropic_build
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "rate-limit-config-builder"
name: "Anthropic Build Tier Rate Limits"
provider: "anthropic"
rpm: 50
tpm: 80000
quality: 8.7
tags: [rate_limit_config, anthropic, build-tier, api-patterns, retry-patterns]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD with retry patterns and budget controls"
description: "Rate limits for Anthropic API Build tier demonstrating standard API rate limiting and retry patterns"
budget_usd: 200.0
tier: "build"
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
density_score: 0.98
---
## Overview

Defines rate limits and retry patterns for the Anthropic API Build tier, demonstrating standard practices for API rate limiting configuration. This tier activates after $5 cumulative spend and provides production-ready quotas suitable for most applications requiring reliable Claude API access with predictable cost controls.

## Limits

| Dimension | Limit | Pattern |
|-----------|-------|---------|
| RPM | 50 | Token bucket: 50 requests/minute with burst tolerance |
| TPM | 80,000 | Token bucket: 80K tokens/minute across all models |
| RPD | 1,000 | Daily hard cap: 1K requests/day regardless of RPM |
| Concurrent | 10 | Max parallel in-flight requests at any instant |
| Retry After | 60s | Wait time after 429 response per Retry-After header |

## Tier

**Tier**: build  
Standard production tier requiring $5 cumulative API spend to activate. Includes access to all Claude models with production-grade rate limits. Upgrade path to Scale tier (4K RPM, 400K TPM) requires custom agreement. Typical retry pattern: exponential backoff with 60s base delay on 429 responses.

## Budget

Monthly cap: $200.00  
Alert threshold: 80% — notification triggered at $160 spend  
Overage policy: Hard stop at budget_usd with requests blocked until next billing cycle. Alert enables proactive scaling or usage optimization before hitting the cap.