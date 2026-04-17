---
id: bld_knowledge_card_circuit_breaker
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 8.8
title: "Circuit Breaker Builder -- Knowledge Card"
llm_function: INJECT
tags: [circuit_breaker, resilience, fault-tolerance, hystrix, resilience4j, P09]
tldr: "circuit_breaker: resilience config that auto-disables failing dependencies via state machine (closed/open/half-open) and recovers after cooldown."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
---

# Knowledge Card: circuit_breaker

## Definition
A `circuit_breaker` is a resilience configuration artifact that auto-disables a failing
downstream dependency and allows controlled recovery after a cooldown period. It implements
the classic circuit breaker design pattern from distributed systems -- named after the
electrical circuit breaker that cuts power when current exceeds safe limits.

## Origin
- **Michael Nygard** -- "Release It!" (2007): first formal description of circuit breaker in software
- **Netflix Hystrix** (2012): popularized in microservices; open-sourced for JVM
- **Resilience4j** (2017): modern JVM implementation; influenced Spring Cloud, Quarkus
- **Reactive Streams** (2014): extended pattern with backpressure integration
- **CEX pillar**: P09 (Config) -- declarative config consumed by runtime agents

## State Machine
Circuit breakers operate as a 3-state machine:

| State | Meaning | Behavior |
|-------|---------|---------|
| CLOSED | Normal operation | All calls pass through; failures tracked |
| OPEN | Dependency disabled | All calls fail-fast with fallback_response |
| HALF-OPEN | Recovery probing | Limited test calls; close on success, reopen on failure |

Transitions:
- CLOSED -> OPEN: when failure_rate >= failure_rate_threshold over the sliding window
- OPEN -> HALF-OPEN: after cooldown_duration seconds
- HALF-OPEN -> CLOSED: if probe_count consecutive probes succeed
- HALF-OPEN -> OPEN: if any probe fails (reset cooldown)

## Key Fields
| Field | Role | Example |
|-------|------|---------|
| failure_rate_threshold | % failures to trip | 50 (50% of last 10 calls) |
| cooldown_duration | Seconds OPEN | 60 |
| probe_count | HALF-OPEN test calls | 3 |
| sliding_window_type | COUNT_BASED or TIME_BASED | COUNT_BASED |
| sliding_window_size | Window size | 10 (calls) or 30 (seconds) |
| fallback_response | Response while OPEN | "Service unavailable. Retry in 60s." |
| monitored_exceptions | Failure types | [ConnectionError, HTTP_5xx] |

## ID Convention
Pattern: `p09_cb_{service_slug}` where slug is lowercase snake_case.
Examples: `p09_cb_anthropic_api`, `p09_cb_postgres_primary`, `p09_cb_stripe_payments`

## Boundary
| circuit_breaker IS | circuit_breaker IS NOT |
|--------------------|------------------------|
| Dependency failure isolation | Inbound request throttle -- that is rate_limit_config |
| State machine with cooldown recovery | Ordered provider substitution -- that is fallback_chain |
| Per-service resilience config | Retry / backoff logic -- that is runtime_rule |
| Fault isolation + fast-fail | Generic environment config -- that is env_config |

## When to Use
- Downstream service has intermittent failures (5xx, timeout, network)
- Cascading failure risk: one dependency failing causes caller chain to fail
- Need fast-fail behavior to preserve caller resources during outage
- Want automatic recovery detection without manual intervention

## When NOT to Use
- Rate limiting inbound requests (use rate_limit_config)
- Choosing between equivalent providers (use fallback_chain)
- Configuring retry delays (use runtime_rule)
- Service-to-service load balancing (use load_balancer_config)

## Industry Implementations
| Library | Language | Key Config |
|---------|----------|-----------|
| Hystrix | Java | circuitBreaker.requestVolumeThreshold, sleepWindowInMilliseconds |
| Resilience4j | Java | failureRateThreshold, waitDurationInOpenState, permittedNumberOfCallsInHalfOpenState |
| Polly | .NET | handledEventsAllowedBeforeBreaking, durationOfBreak |
| pybreaker | Python | fail_max, reset_timeout |
| opossum | Node.js | timeout, errorThresholdPercentage, resetTimeout |

## CEX Usage Pattern
```yaml
# In agent boot config or tool config:
circuit_breaker_ref: p09_cb_anthropic_api
# Agent reads this and wraps all API calls through the state machine
```

Circuit breakers are consumed by agents (P02) and tools (P04).
State changes should emit signals to monitor (P11) for observability.
