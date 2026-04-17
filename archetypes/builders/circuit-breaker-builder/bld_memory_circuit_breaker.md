---
id: p10_lr_circuit_breaker_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Circuit breaker configs with failure_rate_threshold > 80% effectively never trip -- dependency is 80% failing before protection activates. Configs missing fallback_response caused NullPointerException in 3 of 5 reviewed integrations. Cooldown durations below 10 seconds led to rapid OPEN/HALF-OPEN oscillation without recovery."
pattern: "Set failure_rate_threshold at 50% for production services. Set cooldown_duration to match service restart time (typically 30-120s). Always declare fallback_response. Use COUNT_BASED window for low-traffic services, TIME_BASED for high-traffic."
evidence: "5 integrations: 3 missing fallback caused crashes; 2 with threshold 80+ never tripped; cooldown < 10s caused flapping in all observed cases."
confidence: 0.85
outcome: SUCCESS
domain: circuit_breaker
tags: [circuit-breaker, failure-threshold, cooldown, fallback, half-open, resilience4j]
tldr: "50% threshold + service-restart cooldown + explicit fallback = stable fault isolation. High threshold + missing fallback = production crashes."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [circuit breaker, failure rate, cooldown, half-open, fallback, probe, resilience, fault tolerance]
memory_scope: project
observation_types: [feedback, project]
quality: 7.5
title: "Memory Circuit Breaker"
density_score: 0.90
llm_function: INJECT
---
## Summary

Circuit breakers only protect when they actually trip. Too-high thresholds
(> 70%) allow severe degradation before activation. The sweet spot for most
LLM API dependencies is 40-60% -- enough to filter noise while catching real outages.

## Pattern
**50% threshold + service-restart cooldown + explicit fallback.**

Threshold discipline:
1. failure_rate_threshold: 50 for standard services; lower for payment APIs (30)
2. minimum_number_of_calls: set to at least 5 to prevent single-failure trips
3. sliding_window_size: 10 calls (COUNT_BASED) or 30 seconds (TIME_BASED) for LLM APIs

Cooldown discipline:
1. cooldown_duration: match the service's typical restart/recovery time
2. For LLM APIs: 60s (Anthropic resets 429 windows in ~60s)
3. For databases: 10-30s (connection pool recovery)
4. probe_count: 3 is safe default; higher for payment-critical paths

Fallback discipline:
1. Always declare fallback_response -- never leave it implicit
2. Include retry hint: "Retry after {cooldown_duration} seconds"
3. Log state transitions to monitor_config for observability

## Anti-Pattern
1. failure_rate_threshold: 90 -- breaker never trips in practice, offers no protection
2. No fallback_response -- callers receive unhandled exception during OPEN state
3. cooldown_duration: 1 -- half-open/open oscillation without real recovery
4. Monitoring exceptions by class name only -- misses wrapped/rethrown errors
5. Using circuit_breaker for rate limiting -- breakers isolate FAILURES, not throttle VOLUME
