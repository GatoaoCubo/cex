---
id: p09_rl_openai_tier1
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "rate-limit-config-builder"
name: "OpenAI Tier 1 Rate Limits"
provider: "openai"
rpm: 500
tpm: 200000
quality: 8.6
tags: [rate_limit_config, openai, tier1, production]
tldr: "OpenAI Tier 1: 500 RPM, 200K TPM, $100/mo cap at 80% alert"
description: "Rate limits for OpenAI API Tier 1 — production tier activated after $5 cumulative spend"
budget_usd: 100.0
tier: "tier1"
concurrent: 10
retry_after: 20
alert_threshold: 0.8
model_overrides:
  gpt-4o:
    rpm: 500
    tpm: 30000
  gpt-4o-mini:
    rpm: 500
    tpm: 200000
  gpt-3.5-turbo:
    rpm: 500
    tpm: 200000
density_score: 1.0
---
## Overview
Declares rate limits for OpenAI API Tier 1 — the standard production tier activated after $5 cumulative spend. Supports all GPT models with tier-wide limits and per-model token quotas.

## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 500 | Requests per minute, all models |
| TPM | 200,000 | Tokens per minute, varies by model |
| Concurrent | 10 | Max parallel in-flight requests |
| Retry After | 20 | Seconds to wait after 429 response |

## Tier
**Tier**: tier1  
Production tier requiring $5 cumulative API spend to activate. Includes access to GPT-4o, GPT-4o-mini, and GPT-3.5-turbo. Upgrade to Tier 2 requires $50 cumulative spend for higher limits.

## Budget
Monthly cap: $100.00  
Alert threshold: 80% — trigger notification at $80 spend  
Overage policy: Requests continue but billing alerts fire; set hard stops via OpenAI dashboard if needed.