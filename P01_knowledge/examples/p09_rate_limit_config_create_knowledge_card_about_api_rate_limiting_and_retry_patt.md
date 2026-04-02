---
id: p09_rl_anthropic_build
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: builder_agent
name: "Anthropic Build Tier — Rate Limits & Retry Patterns"
provider: anthropic
rpm: 50
tpm: 80000
rpd: 1000
concurrent: 10
retry_after: 60
tier: build
budget_usd: 100.0
alert_threshold: 0.8
quality: 8.9
tags: [rate_limit_config, anthropic, build-tier, retry-patterns, api-limits]
tldr: "Anthropic Build: 50 RPM, 80K TPM, 1K RPD, 10 concurrent — exponential backoff on 429, $100/mo cap at 80% alert"
description: "Rate limits and retry patterns for Anthropic API Build tier — standard production tier after $5 cumulative spend"
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
Declares quota ceilings for the Anthropic API Build tier — activated after $5 cumulative spend. Covers RPM, TPM, RPD, concurrent slots, per-model overrides, budget cap, and 429 retry patterns for all Claude models.

## Limits
| Dimension | Limit | Algorithm |
|-----------|-------|-----------|
| RPM | 50 | sliding window (60s) |
| TPM | 80,000 | token bucket, refills per second |
| RPD | 1,000 | daily hard cap, resets UTC midnight |
| Concurrent | 10 | max parallel in-flight requests |

## Tier
**Tier**: build — requires $5 cumulative API spend to activate.
Includes all Claude models. Per-model overrides apply: Opus caps at 40K TPM; Haiku allows 100K TPM.
Upgrade path: Scale tier via custom Anthropic sales agreement (4K RPM, 400K TPM, 100K RPD).

## Budget
Monthly cap: $100.00 USD
Alert threshold: 80% — notify at $80 spend.
Overage policy: requests blocked when budget_usd exceeded; reset at billing cycle start.
Retry policy: on 429, read `Retry-After` header (Anthropic default: 60s); apply exponential backoff with jitter for concurrent callers. Backoff logic and circuit-break strategy belong in `runtime_rule`, not here.