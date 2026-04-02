---
id: p09_rate_limit_config_create_knowledge_card_about_api_rate_limiting_and_retry_patt
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "rate-limit-config-builder"
name: "API Rate Limiting and Retry Patterns"
provider: "anthropic"
rpm: 50
tpm: 80000
quality: 8.9
tags: [rate_limit_config, anthropic, retry-patterns, api-rate-limiting, build-tier, budget, 429]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD — token-bucket semantics, 60s retry-after, 80% budget alert"
description: "Reference config for Anthropic Build tier — RPM/TPM/RPD ceilings, retry guidance, and cost guardrails for production LLM integrations"
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
  claude-3-5-haiku-20241022:
    rpm: 50
    tpm: 100000
  claude-opus-4-6:
    rpm: 50
    tpm: 80000

---
## Overview
Rate quota config for Anthropic Build tier — default production tier after $5 cumulative API spend. Declares RPM, TPM, RPD, and concurrent ceilings with 429 retry guidance. Retry logic (exponential backoff, jitter, circuit break) belongs in `runtime_rule`; this artifact declares numeric limits and the recovery hint only.

## Limits
| Dimension | Limit | Semantics |
|-----------|-------|-----------|
| RPM | 50 | Rolling 60s window; token-bucket refill |
| TPM | 80,000 | Input + output tokens combined |
| RPD | 1,000 | Hard daily cap; resets UTC midnight |
| Concurrent | 10 | Max parallel in-flight requests |
| Retry-After | 60s | `Retry-After` header on 429 response |

## Tier
**build** — activated after $5 cumulative API spend. Includes all Claude 3/3.5/3.7/4.x models.
Upgrade to **Scale** (4K RPM, 400K TPM, 100K RPD) requires custom agreement with Anthropic sales.

## Budget
Monthly cap: $100.00
Alert threshold: 80% — trigger notification at $80 spend
Overage policy: requests blocked when `budget_usd` exceeded; resets at billing cycle start.