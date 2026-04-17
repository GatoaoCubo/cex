---
id: p09_rate_limit_config
kind: rate_limit_config
pillar: P09
version: 1.0.0
title: "Template — Rate Limit Config"
tags: [template, rate-limit, throttle, quota, api]
tldr: "Configures request rate limiting for APIs and LLM calls. Defines limits per window, burst allowance, quota tracking, and backpressure behavior."
quality: 9.0
updated: "2026-04-07"
domain: "configuration management"
author: n03_builder
created: "2026-04-07"
density_score: 0.98
---

# Rate Limit Config: [SERVICE_NAME]

## Purpose
[WHAT service this protects — API endpoints, LLM calls, external provider]

## Limits

| Tier | Requests/min | Requests/hour | Daily Quota | Burst |
|------|-------------|---------------|-------------|-------|
| free | 10 | 100 | 1,000 | 20 |
| standard | 60 | 1,000 | 10,000 | 100 |
| premium | 300 | 10,000 | 100,000 | 500 |

## Algorithm
- **Type**: [token_bucket | sliding_window | fixed_window]
- **Window**: [1min | 5min | 1hour]
- **Key**: [api_key | ip_address | user_id | nucleus]
- **Storage**: [redis | in-memory | database]

## Backpressure Behavior
| Situation | Response | HTTP Code |
|-----------|----------|-----------|
| At limit | Queue request, wait up to [5s] | 200 (delayed) |
| Over limit | Reject immediately | 429 Too Many Requests |
| Burst exceeded | Throttle to base rate | 429 + Retry-After header |
| Quota exhausted | Block until reset | 429 + reset_at timestamp |

## Response Headers
```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1711891200
Retry-After: 30
```

## LLM-Specific Limits
| Provider | RPM | TPM | Daily $ |
|----------|-----|-----|---------|
| Anthropic | 50 | 100K | $50 |
| OpenAI | 60 | 150K | $30 |
| Local (Ollama) | unlimited | unlimited | $0 |

## Quality Gate
- [ ] Limits defined per tier
- [ ] Backpressure behavior specified (queue vs reject)
- [ ] Response headers include remaining + reset
- [ ] Daily cost budget defined for LLM providers
