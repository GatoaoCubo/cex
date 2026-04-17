---
kind: examples
id: bld_examples_circuit_breaker
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of circuit_breaker artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: null
title: "Examples Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, examples]
tldr: "Golden and anti-examples for circuit_breaker construction: state machine, thresholds, cooldown, fallback."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: circuit-breaker-builder

## Golden Example
INPUT: "Create circuit breaker for Anthropic API calls"
OUTPUT:
```yaml
id: p09_cb_anthropic_api
kind: circuit_breaker
pillar: P09
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
service: "anthropic_api"
failure_rate_threshold: 50
cooldown_duration: 60
probe_count: 3
sliding_window_type: "COUNT_BASED"
sliding_window_size: 10
minimum_number_of_calls: 5
slow_call_threshold_ms: 30000
fallback_response: "Service temporarily unavailable. Retry after 60 seconds."
monitored_exceptions: [ConnectionError, TimeoutError, HTTP_5xx, HTTP_529]
quality: null
tags: [circuit_breaker, anthropic_api, llm_resilience]
tldr: "Anthropic API circuit breaker: 50% failure rate trips 60s cooldown; 3 probes to recover"
```

## Overview
Protects callers from cascading failure when the Anthropic API is degraded or unavailable.
Trips when 5 of the last 10 calls fail (50%), disabling the integration for 60 seconds.

## State Machine
| State | Condition | Transitions To |
|-------|-----------|---------------|
| CLOSED | Normal operation | OPEN when failure_rate >= 50% over last 10 calls |
| OPEN | API disabled | HALF-OPEN after 60s cooldown |
| HALF-OPEN | Recovery probe | CLOSED if 3 probes succeed; OPEN if any probe fails |

## Cooldown
- Duration: 60 seconds
- Probe calls: 3 requests allowed in HALF-OPEN
- Recovery criteria: 3 consecutive probe successes
- Reset trigger: 3 consecutive successes from half-open state

## Fallback
Response during OPEN state: "Service temporarily unavailable. Retry after 60 seconds."
Error code: 503
SLA impact: Callers receive 503 immediately instead of waiting for timeout

WHY THIS IS GOLDEN:
- failure_rate_threshold: 50 (positive integer, range [1,100]) -- H07 pass
- cooldown_duration: 60 (positive integer seconds) -- H08 pass
- probe_count: 3 (positive integer) -- H09 pass
- All 4 body sections present -- H10 pass
- quality: null -- H05 pass
- id matches ^p09_cb_ pattern -- H02 pass
- monitored_exceptions lists real error types including HTTP_529 (Anthropic overload)

## Anti-Example
INPUT: "Create circuit breaker for my API"
BAD OUTPUT:
```yaml
id: my-api-breaker
kind: breaker
failure_rate_threshold: "high"
cooldown_duration: -30
quality: 9.5
tags: [api]
```
FAILURES:
1. id: "my-api-breaker" has hyphens, no p09_cb_ prefix -> H02 FAIL
2. kind: "breaker" not "circuit_breaker" -> H04 FAIL
3. failure_rate_threshold: "high" is not integer in [1,100] -> H07 FAIL
4. cooldown_duration: -30 is negative -> H08 FAIL
5. quality: 9.5 (not null) -> H05 FAIL
6. Missing service, probe_count, pillar, version -> H06 FAIL
7. Missing all 4 body sections -> H10 FAIL
8. tags: only 1 item, missing "circuit_breaker" -> H09 FAIL
