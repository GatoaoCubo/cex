---
quality: 8.2
id: kc_api_rate_limiting
kind: knowledge_card
pillar: P01
nucleus: n04
title: "API Rate Limiting Best Practices"
version: "1.0.0"
tags: [api, rate-limiting, backend, resilience]
created: 2026-04-19
related:
  - p09_rate_limit_config
  - bld_tools_usage_quota
  - kc_integration_guide
  - p01_kc_api_rate_limiting_retry_patterns
  - bld_collaboration_rate_limit_config
  - bld_knowledge_card_rate_limit_config
  - rate-limit-config-builder
  - bld_memory_runtime_rule
  - p06_schema_api_response_contract
  - p03_sp_model_provider_builder
density_score: 1.0
updated: "2026-04-22"
---

# API Rate Limiting Best Practices

## Summary

Rate limiting protects APIs from abuse and ensures fair resource distribution
across consumers. This KC covers token bucket, sliding window, and fixed window
algorithms, with implementation guidance for production systems.

## Core Concepts

| Concept | Definition | When to use |
|---------|-----------|-------------|
| Token bucket | Tokens refill at fixed rate; requests consume tokens | Bursty traffic with sustained average |
| Sliding window | Counts requests in a rolling time window | Smooth rate enforcement |
| Fixed window | Counts requests in discrete time intervals | Simple implementation, allows edge bursts |
| Leaky bucket | Requests queue and drain at fixed rate | Strict output rate control |

## Implementation

### Headers (RFC 6585 + draft-ietf-httpapi-ratelimit-headers)

```
RateLimit-Limit: 100
RateLimit-Remaining: 42
RateLimit-Reset: 1620000000
Retry-After: 30
```

### Response codes

- **429 Too Many Requests** -- client exceeded rate limit
- **503 Service Unavailable** -- server-side throttling (backpressure)

### Storage backends

| Backend | Latency | Distributed? | Notes |
|---------|---------|-------------|-------|
| Redis | <1ms | Yes | INCR + EXPIRE atomic; industry standard |
| In-memory | <0.1ms | No | Single-instance only; loses state on restart |
| Database | 5-20ms | Yes | Last resort; high write amplification |

## Best Practices

1. **Return headers always** -- clients need visibility even when not throttled
2. **Tier by authentication** -- anonymous < authenticated < premium
3. **Separate read/write limits** -- writes are more expensive
4. **Use exponential backoff on 429** -- with jitter to avoid thundering herd
5. **Log rate limit events** -- essential for capacity planning

## References

- RFC 6585: Additional HTTP Status Codes (429)
- IETF draft-ietf-httpapi-ratelimit-headers-07
- Stripe API rate limiting documentation
- Google Cloud API design guide: rate limiting section

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_rate_limit_config]] | downstream | 0.37 |
| [[bld_tools_usage_quota]] | downstream | 0.28 |
| [[kc_integration_guide]] | sibling | 0.27 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | sibling | 0.27 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.26 |
| [[bld_knowledge_card_rate_limit_config]] | sibling | 0.25 |
| [[rate-limit-config-builder]] | downstream | 0.25 |
| [[bld_memory_runtime_rule]] | downstream | 0.25 |
| [[p06_schema_api_response_contract]] | downstream | 0.23 |
| [[p03_sp_model_provider_builder]] | downstream | 0.23 |
