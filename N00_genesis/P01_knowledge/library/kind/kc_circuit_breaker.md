---
id: p01_kc_circuit_breaker
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P09
title: "Circuit Breaker -- Deep Knowledge for circuit_breaker"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: circuit_breaker
quality: 8.8
tags: [circuit_breaker, P09, GOVERN, kind-kc, resilience, fault-tolerance]
tldr: "circuit_breaker auto-disables failing dependencies via state machine (closed/open/half-open) and allows recovery after cooldown. NOT rate_limit_config or fallback_chain."
when_to_use: "Building, reviewing, or reasoning about circuit_breaker artifacts"
keywords: [circuit_breaker, resilience, fault-tolerance, hystrix, resilience4j, cooldown, half-open]
feeds_kinds: [circuit_breaker]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_error_recovery
  - bld_memory_runtime_rule
  - bld_memory_action_paradigm
  - bld_architecture_runtime_rule
  - p01_kc_routing_resilience
  - bld_knowledge_card_runtime_rule
  - p11_qg_runtime_rule
  - p03_sp_runtime_rule_builder
  - p03_sp_rate_limit_config_builder
  - p11_qg_fallback_chain
---

# Circuit Breaker

## Spec
```yaml
kind: circuit_breaker
pillar: P09
llm_function: GOVERN
max_bytes: 3072
naming: p09_cb_{service}.md
core: true
```

## What It Is
A circuit_breaker declares the resilience configuration for a single downstream dependency.
It implements the circuit breaker design pattern: when failure rate exceeds a threshold,
calls are auto-disabled (OPEN) for a cooldown period, then recovery is probed (HALF-OPEN)
before returning to normal (CLOSED). This prevents cascade failure in distributed systems.

NOT rate_limit_config (inbound throttle). NOT fallback_chain (ordered provider substitution).
NOT runtime_rule (retry and backoff logic).

## Cross-Framework Map
| Framework/Library | Equivalent | Notes |
|-------------------|-----------|-------|
| Hystrix (Netflix) | @HystrixCommand | circuitBreaker.requestVolumeThreshold, sleepWindowInMilliseconds |
| Resilience4j | CircuitBreakerConfig | failureRateThreshold, waitDurationInOpenState, permittedNumberOfCallsInHalfOpenState |
| Polly (.NET) | CircuitBreakerPolicy | handledEventsAllowedBeforeBreaking, durationOfBreak |
| pybreaker (Python) | CircuitBreaker | fail_max, reset_timeout |
| opossum (Node.js) | CircuitBreaker | timeout, errorThresholdPercentage, resetTimeout |

## State Machine
| State | Entry Condition | Exit Condition |
|-------|----------------|----------------|
| CLOSED | Initial / after recovery | failure_rate >= threshold over window |
| OPEN | failure_rate exceeded | after cooldown_duration seconds |
| HALF-OPEN | After cooldown | probe_count successes -> CLOSED; any failure -> OPEN |

## Key Parameters
| Parameter | Type | Typical | Notes |
|-----------|------|---------|-------|
| failure_rate_threshold | int [1,100] | 50 | % failures to trip; 50% is safe default |
| cooldown_duration | int (seconds) | 60 | Match service restart time |
| probe_count | int | 3 | Half-open test calls; higher for critical paths |
| sliding_window_type | enum | COUNT_BASED | TIME_BASED for high-traffic services |
| sliding_window_size | int | 10 | Calls or seconds in observation window |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Conservative threshold | Payment/audit APIs | failure_rate_threshold: 20, cooldown: 120s |
| Standard threshold | LLM APIs, microservices | failure_rate_threshold: 50, cooldown: 60s |
| Lenient threshold | Metrics/non-critical | failure_rate_threshold: 70, cooldown: 30s |
| Slow call detection | Latency-sensitive | slow_call_threshold_ms: 5000, slow_call_rate_threshold: 50 |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| threshold: 90 | Never trips in practice; offers no protection | Lower to 40-60% |
| No fallback_response | Callers receive unhandled exception during OPEN | Always declare fallback |
| cooldown: 1 | OPEN/HALF-OPEN oscillation without recovery | Match service restart time (>= 30s) |
| Conflating with rate_limit_config | Different problem: failure vs volume | rate_limit_config is inbound throttle |

## Integration Graph
```
monitored_exceptions --> [circuit_breaker] --> agent, tool_config
                               |
                     runtime_rule (retry after failure)
                     rate_limit_config (parallel: inbound throttle)
                     monitor (state transition events)
```

## Decision Tree
- IF dependency has failure rate > 30% at peak -> failure_rate_threshold: 40
- IF dependency restart time > 60s -> cooldown_duration: 120
- IF payment/audit critical path -> probe_count: 5-10
- IF latency as important as errors -> add slow_call_threshold_ms

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_error_recovery]] | sibling | 0.36 |
| [[bld_memory_runtime_rule]] | downstream | 0.21 |
| [[bld_memory_action_paradigm]] | downstream | 0.19 |
| [[bld_architecture_runtime_rule]] | upstream | 0.19 |
| [[p01_kc_routing_resilience]] | sibling | 0.19 |
| [[bld_knowledge_card_runtime_rule]] | sibling | 0.19 |
| [[p11_qg_runtime_rule]] | downstream | 0.19 |
| [[p03_sp_runtime_rule_builder]] | upstream | 0.18 |
| [[p03_sp_rate_limit_config_builder]] | related | 0.17 |
| [[p11_qg_fallback_chain]] | downstream | 0.17 |
