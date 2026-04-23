---
id: bld_knowledge_card_retry_policy
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 8.8
title: "Retry Policy Builder -- Knowledge Card"
llm_function: INJECT
tags: [retry_policy, backoff, jitter, P09, resilience]
tldr: "retry_policy: backoff/jitter/budget config for retrying failed operations. NOT circuit_breaker (state machine) nor rate_limit_config (inbound throttle)."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
related:
  - bld_schema_client
  - p01_kc_api_rate_limiting_retry_patterns
  - bld_schema_bugloop
  - bld_examples_runtime_rule
  - bld_schema_model_provider
  - bld_schema_rate_limit_config
  - bld_schema_reranker_config
  - bld_schema_social_publisher
  - bld_schema_runtime_state
  - bld_schema_context_window_config
---

# Knowledge Card: retry_policy

## Definition

A `retry_policy` is a configuration artifact that specifies how failed operations are retried,
including backoff timing, jitter randomization, attempt limits, and error classification.
It implements the Retry pattern from distributed systems resilience -- configuring when and how
to re-attempt operations after transient failures like network timeouts, rate limit responses (429),
or temporary service unavailability. Grounded in AWS SDK Retry design and Microsoft Polly library.

## Origin

- **AWS Marc Brooker** (2015): "Exponential Backoff and Jitter" blog -- FULL/EQUAL/DECORRELATED jitter
- **Microsoft Polly** (2013): .NET resilience library -- WaitAndRetry, ExponentialBackoff
- **Netflix Ribbon** (2014): client-side retry with backoff for JVM microservices
- **CEX pillar**: P09 (Config) -- declarative resilience config consumed by runtime agents

## Key Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| max_attempts | integer | YES | Total attempts including initial (3 = 1 try + 2 retries) |
| initial_interval | integer (ms) | YES | Delay before first retry |
| backoff_strategy | enum | YES | exponential/linear/fixed/decorrelated |
| backoff_multiplier | float | conditional | Growth factor (2.0 = doubles each attempt) |
| max_interval | integer (ms) | YES | Cap on delay to prevent infinite growth |
| jitter | enum | REC | FULL/EQUAL/DECORRELATED/NONE |
| retry_budget | integer | REC | Max concurrent retries (prevents storm) |
| retryable_errors | list | YES | HTTP 429/503/504, ConnectionError, TimeoutError |
| non_retryable_errors | list | REC | HTTP 400/401/403 (client errors, no point retrying) |

## Backoff Delay Examples (exponential, multiplier=2.0, initial=100ms, jitter=FULL)

| Attempt | Base Delay | With FULL Jitter | Notes |
|---------|------------|-----------------|-------|
| 1 | 100ms | rand(0-100ms) | After first failure |
| 2 | 200ms | rand(0-200ms) | Doubles |
| 3 | 400ms | rand(0-400ms) | Doubles |
| 4 | 800ms | rand(0-800ms) | Doubles |
| 5+ | capped at max_interval | rand(0-max) | Ceiling hit |

## When to Use

| Scenario | Use retry_policy? |
|----------|-----------------|
| Transient network timeout or connection error | YES |
| HTTP 429 (rate limited) response | YES |
| HTTP 503/504 (service unavailable/gateway timeout) | YES |
| HTTP 400/401/403 (client error) | NO -- retrying won't fix it |
| Dependency permanently unavailable | NO -- use circuit_breaker |
| Choosing between backup providers | NO -- use fallback_chain |
| Inbound request throttle | NO -- use rate_limit_config |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No jitter (jitter: NONE) | All clients retry simultaneously -- thundering herd | Use FULL or DECORRELATED jitter |
| max_attempts too high (> 10) | Extended timeout cascade, user sees long delays | Use 3-5 attempts max |
| Retrying non-retryable errors (400/401) | Wastes resources, won't succeed | Classify errors; fail-fast on 4xx |
| No max_interval cap | Backoff grows unbounded (minutes, hours) | Cap at 30-60 seconds |
| Conflating with circuit_breaker | Circuit breaker disables dependency; retry just re-attempts | Separate configs for each |

## Decision Tree

```
Operation failed?
  Is it a transient error (network, 429, 503)?
    YES -> retry_policy
      Should we also disable dependency after too many failures?
        YES -> also circuit_breaker (separate config)
  Is it a client error (400, 401, 403)?
    YES -> fail immediately (no retry)
  Is it a permanent service outage?
    YES -> circuit_breaker (not retry)
  Need to switch to backup provider?
    YES -> fallback_chain (not retry)
```

## Cross-Framework Map

| Library | Language | Key Config |
|---------|----------|-----------|
| Polly WaitAndRetryAsync | .NET | RetryCount, SleepDurationProvider, ExceptionFilter |
| AWS SDK RetryConfig | Python/JS/Go | max_attempts, mode (adaptive/standard), retry_mode |
| Resilience4j Retry | Java | maxAttempts, waitDuration, retryExceptions |
| urllib3 Retry | Python | total, backoff_factor, status_forcelist |
| tenacity | Python | stop_after_attempt, wait_exponential, retry_if_exception |

## Integration Graph

```
retry_policy (P09)
  |
  |-- used by --> agent (P02) -- wraps API calls
  |-- used by --> api_client (P04) -- client-side retry
  |-- complemented by --> circuit_breaker (P09) -- disable after repeated failures
  |-- complemented by --> rate_limit_config (P09) -- inbound throttle
  |-- observed by --> monitor (P11) -- retry counts as metric
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_client]] | downstream | 0.33 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | sibling | 0.32 |
| [[bld_schema_bugloop]] | downstream | 0.32 |
| [[bld_examples_runtime_rule]] | downstream | 0.32 |
| [[bld_schema_model_provider]] | downstream | 0.31 |
| [[bld_schema_rate_limit_config]] | downstream | 0.30 |
| [[bld_schema_reranker_config]] | downstream | 0.29 |
| [[bld_schema_social_publisher]] | downstream | 0.29 |
| [[bld_schema_runtime_state]] | downstream | 0.29 |
| [[bld_schema_context_window_config]] | downstream | 0.28 |
