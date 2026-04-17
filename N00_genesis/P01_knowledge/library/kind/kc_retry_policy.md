---
id: kc_retry_policy
kind: knowledge_card
pillar: P01
title: "Knowledge Card -- Retry Policy"
version: 1.0.0
quality: null
tags: [knowledge, retry_policy, backoff, jitter, resilience, polly]
---

# Retry Policy

## Definition

A `retry_policy` is a configuration artifact specifying how failed operations are retried with backoff timing, jitter randomization, attempt limits, and error classification. It implements the Retry pattern from distributed systems resilience -- configuring when and how to re-attempt operations after transient failures (network timeouts, rate limit responses, temporary service unavailability). Grounded in AWS SDK Retry design (Marc Brooker 2015) and Microsoft Polly library.

Not circuit_breaker (open/closed state machine that disables a dependency). Not rate_limit_config (inbound request throttle for your own API).

## When to Use

| Scenario | Use retry_policy? |
|----------|-----------------|
| Transient network timeout or connection error | YES |
| HTTP 429 (rate limited) response | YES |
| HTTP 503/504 (service unavailable/gateway timeout) | YES |
| HTTP 400/401/403 (client error -- won't succeed on retry) | NO -- fail immediately |
| Dependency permanently unavailable | NO -- use circuit_breaker |
| Choosing between backup providers | NO -- use fallback_chain |

## Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| operation | string | YES | Operation being retried |
| max_attempts | integer | YES | Total attempts (initial + retries) |
| initial_interval | integer (ms) | YES | Delay before first retry |
| backoff_strategy | enum | YES | exponential/linear/fixed/decorrelated |
| max_interval | integer (ms) | YES | Cap on delay growth |
| jitter | enum | REC | FULL/EQUAL/DECORRELATED/NONE |
| retry_budget | integer | REC | Max concurrent retries |
| retryable_errors | list | YES | Error types that trigger retry |
| non_retryable_errors | list | REC | Error types to fail immediately |

## Jitter Types (AWS Marc Brooker 2015)

| Jitter | Effect | Use When |
|--------|--------|----------|
| NONE | All clients retry simultaneously | Never -- thundering herd |
| FULL | rand(0, base_delay) | Medium-high concurrency |
| EQUAL | base/2 + rand(0, base/2) | Some predictability needed |
| DECORRELATED | min(max, rand(initial, prev*3)) | High concurrency -- AWS recommended |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| jitter: NONE | Thundering herd on recovery | Use FULL or DECORRELATED |
| max_attempts > 10 | Cascade timeout from user's perspective | Keep 3-5 for user-facing |
| Retrying 400/401/403 | Client errors won't succeed | Classify in non_retryable_errors |
| No max_interval | Backoff grows unbounded | Cap at 30-60 seconds |

## Cross-Framework Map

| Library | Language | Key Config |
|---------|----------|-----------|
| Polly WaitAndRetryAsync | .NET | RetryCount, SleepDurationProvider |
| AWS SDK RetryConfig | Python/JS/Go | max_attempts, mode |
| Resilience4j Retry | Java | maxAttempts, waitDuration |
| tenacity | Python | stop_after_attempt, wait_exponential |

## Decision Tree

```
Operation failed?
  Transient error (429/503/504/network)?
    YES -> retry_policy
      Persistent failures after retries?
        YES -> also circuit_breaker
  Client error (400/401/403)?
    YES -> fail immediately (no retry_policy)
  Need backup provider?
    YES -> fallback_chain
```

## Integration

- Used by: agent (P02) wrapping API calls
- Used by: api_client (P04) -- client-side retry
- Complemented by: circuit_breaker (P09) -- disable after repeated failures
- Observed by: monitor (P11) -- retry counts as health metric
- Pillar: P09 (Config) -- declarative resilience config
