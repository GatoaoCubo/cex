---
kind: examples
id: bld_examples_rate_limit_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of rate_limit_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: rate-limit-config-builder

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Golden Example
INPUT: "Create rate limit config for Anthropic Build tier"
OUTPUT:
```yaml
id: p09_rl_anthropic_build
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Anthropic Build Tier Rate Limits"
provider: "anthropic"
rpm: 50
tpm: 80000
quality: null
tags: [rate_limit_config, anthropic, build-tier]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD, $100/mo cap at 80% alert"
description: "Rate limits for Anthropic API Build tier — standard production tier after $5 spend"
budget_usd: 100.0
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
```
## Overview
Declares rate limits for the Anthropic API Build tier — the default production tier
activated after $5 cumulative spend. Used by all Claude API integrations at this tier.
## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 50 | Requests per minute, all models |
| TPM | 80,000 | Tokens per minute, all models |
| RPD | 1,000 | Requests per day hard cap |
| Concurrent | 10 | Max parallel in-flight requests |
## Tier
**Tier**: build
Standard production tier. Requires $5 cumulative API spend to activate.
Includes all Claude models. Upgrade to Scale tier requires costm agreement with Anthropic sales.
## Budget
Monthly cap: $100.00
Alert threshold: 80% — trigger notification at $80 spend
Overage policy: Requests blocked when budget_usd exceeded; reset at billing cycle start.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p09_rl_ pattern (H02 pass)
- kind: rate_limit_config (H04 pass)
- rpm: 50 and tpm: 80000 are positive integers (H07+H08 pass)
- all 4 body sections present (H10 pass)
- tags: 3 items, includes "rate_limit_config" (H09 pass)
- model_overrides with real Anthropic model IDs (SOFT bonus)
- budget_usd + alert_threshold + overage policy (Budget gate pass)
- tldr: 67 chars <= 160 (tldr gate pass)
- retry_after: 60 matches Anthropic 429 Retry-After header value
## Anti-Example
INPUT: "Create rate limit config for OpenAI"
BAD OUTPUT:
```yaml
id: openai-limits
kind: config
provider: openai
rpm: unlimited
tpm: lots
quality: 9.5
tags: [openai]
```
Rate limits for OpenAI. Use when calling GPT.
FAILURES:
1. id: "openai-limits" has hyphens and no `p09_rl_` prefix -> H02 FAIL
2. kind: "config" not "rate_limit_config" -> H04 FAIL
3. quality: 9.5 (not null) -> H05 FAIL
4. rpm: "unlimited" is not a positive integer -> H07 FAIL
5. tpm: "lots" is not a positive integer -> H08 FAIL
6. tags: only 1 item, missing "rate_limit_config" -> H09 FAIL
7. Missing required fields: pillar, version, created, updated, author, name, tier, tldr -> H06 FAIL
8. Body missing ## Overview, ## Limits, ## Tier, ## Budget sections -> H10 FAIL
9. No tier specified — cannot verify limits against provider docs -> SOFT FAIL
10. No budget_usd or alert_threshold — cost unbounded -> SOFT FAIL
