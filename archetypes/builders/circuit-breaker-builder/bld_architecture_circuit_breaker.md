---
kind: architecture
id: bld_architecture_circuit_breaker
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of circuit_breaker -- inventory, dependencies, and architectural position
quality: null
title: "Architecture Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, architecture]
tldr: "Component map: state machine (closed/open/half-open), failure window, cooldown, probe. External: rate_limit_config, fallback_chain."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| failure_rate_threshold | % of failures that trips the breaker from CLOSED to OPEN | circuit_breaker | required |
| cooldown_duration | Seconds circuit stays OPEN before moving to HALF-OPEN | circuit_breaker | required |
| probe_count | Number of test calls in HALF-OPEN before closing | circuit_breaker | required |
| sliding_window_type | COUNT_BASED or TIME_BASED failure tracking | circuit_breaker | required |
| sliding_window_size | Number of calls or seconds in the observation window | circuit_breaker | required |
| minimum_number_of_calls | Min calls before failure rate is meaningful | circuit_breaker | recommended |
| slow_call_threshold_ms | Call duration above which it counts as slow failure | circuit_breaker | recommended |
| fallback_response | Response returned while circuit is OPEN | circuit_breaker | recommended |
| monitored_exceptions | Error types that increment failure counter | circuit_breaker | recommended |
| rate_limit_config | Inbound throttle (RPM/TPM quotas) | P09 (separate kind) | external |
| fallback_chain | Ordered provider substitution list | P02 (separate kind) | external |
| runtime_rule | Retry logic and backoff strategy | P09 (separate kind) | external |
| agent | Orchestrator that wraps calls through circuit breaker | P02 | consumer |
| monitor | Observability layer that tracks circuit state transitions | P11 | consumer |

## State Machine

```
            failure_rate >= threshold
CLOSED  ---------------------------------> OPEN
  ^                                          |
  |                                          | after cooldown_duration
  |        probe_count calls succeed         |
HALF-OPEN <-------------------------------- HALF-OPEN
  |
  | any probe call fails
  |
  v
OPEN (reset cooldown)
```

## Dependency Graph
```
failure_rate_threshold  --trips-->       state: OPEN
cooldown_duration       --transitions--> state: HALF-OPEN
probe_count             --closes-->      state: CLOSED
sliding_window          --tracks-->      failure_rate
monitored_exceptions    --filter-->      failure_counter
fallback_response       --returns-->     caller (when OPEN)
rate_limit_config       --independent--> (parallel concern)
runtime_rule            --parallel-->   (retry after failure, not circuit)
```

## Boundary Table
| circuit_breaker IS | circuit_breaker IS NOT |
|---------------------|------------------------|
| Dependency failure isolation via state machine | Inbound request throttle (that is rate_limit_config) |
| Auto-disable + auto-recovery pattern | Ordered provider substitution (that is fallback_chain) |
| Slow call detection and failure counting | Retry with backoff strategy (that is runtime_rule) |
| Service-level fault tolerance config | Generic environment variables (that is env_config) |
| Per-dependency resilience declaration | System-wide observability (that is trace_config) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| detection | sliding_window, failure_rate_threshold, monitored_exceptions | Track and evaluate failure signal |
| state | CLOSED/OPEN/HALF-OPEN state machine | Control whether calls are allowed |
| recovery | cooldown_duration, probe_count | Govern return to healthy state |
| response | fallback_response | Serve callers during OPEN state |
| external | rate_limit_config, fallback_chain, runtime_rule | Adjacent concerns |
