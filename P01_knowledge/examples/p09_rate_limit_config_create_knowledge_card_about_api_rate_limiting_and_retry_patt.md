---
id: p09_rl_anthropic_build
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: rate-limit-config-builder
name: "Anthropic Claude API — Build Tier Rate Limits"
provider: anthropic
rpm: 50
tpm: 80000
quality: 8.9
tags: [rate_limit_config, anthropic, build-tier, retry-patterns, 429]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD, 10 concurrent — 429 retry-after 60s, $100/mo cap at 80% alert"
description: "Authoritative quota boundaries for Anthropic Claude API Build tier — numeric ceilings plus 429 retry seed for runtime_rule handoff"
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
  claude-opus-4-6:
    rpm: 50
    tpm: 80000
density_score: 1.0
---
## Overview
Declares numeric quota ceilings for Anthropic Claude API Build tier — the standard production tier activated after $5 cumulative API spend. Covers RPM, TPM, RPD, and concurrent limits with the 429 `Retry-After` seed value. Retry backoff logic (exponential, jitter, circuit breaker) belongs in `runtime_rule`; this artifact declares quota boundaries and the retry seed only.

## Limits
| Dimension | Limit | Semantics |
|-----------|-------|-----------|
| RPM | 50 | Rolling 60s token-bucket; burst up to bucket size |
| TPM | 80,000 | Input + output tokens combined, sliding window |
| RPD | 1,000 | Hard daily cap; resets UTC midnight |
| Concurrent | 10 | Max parallel in-flight requests at any instant |
| Retry-After | 60s | `Retry-After` header value returned on 429 response |

## Tier
**build** — Activated after $5 cumulative API spend. Includes all Claude models. Upgrade to **scale** (4,000 RPM / 400K TPM / 100K RPD) requires a custom agreement with Anthropic sales.

| Tier | RPM | TPM | RPD | Activation |
|------|-----|-----|-----|------------|
| free | 5 | 20,000 | 50 | Default (claude.ai accounts) |
| build | 50 | 80,000 | 1,000 | $5 cumulative spend |
| scale | 4,000 | 400,000 | 100,000 | Sales agreement |

## Budget
Monthly cap: **$100.00 USD**
Alert threshold: **80%** — trigger notification at $80 spend.
Overage policy: Requests blocked when `budget_usd` exhausted; resets at billing cycle start.
Retry seed: Pass `retry_after: 60` to `runtime_rule` for exponential backoff with jitter — do not implement retry logic in this artifact. RPD cap is independent of RPM; both can bind simultaneously on high-volume bursts.