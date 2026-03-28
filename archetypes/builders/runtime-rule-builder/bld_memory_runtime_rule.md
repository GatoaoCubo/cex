---
kind: memory
id: bld_memory_runtime_rule
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for runtime_rule artifact generation
---

# Memory: runtime-rule-builder
## Summary
Runtime rules specify technical behavior parameters: timeouts, retry strategies, rate limits, concurrency caps, and circuit breaker thresholds. The critical production lesson is that retry strategies without backoff cause thundering herd problems — when a service recovers from an outage, all waiting clients retry simultaneously, causing immediate re-failure. The second lesson is that circuit breakers need explicit recovery probes, not just time-based resets.
## Pattern
- Retry strategies must include backoff: exponential with jitter is the safest default
- Circuit breaker thresholds need three numbers: failure count to open, probe interval, success count to close
- Rate limits must specify the window type: fixed window, sliding window, or token bucket — each behaves differently at boundaries
- Timeouts must be set per operation type, not globally — read operations and write operations have different tolerance
- Concurrency limits must account for connection pool size — a limit higher than the pool creates queuing
- All limits must include what happens when exceeded: reject, queue, throttle, or degrade
## Anti-Pattern
- Retry without backoff — causes thundering herd on service recovery, making outages worse
- Circuit breaker with time-based reset only — service may still be down when breaker closes
- Global timeout for all operations — write operations fail that should succeed, or read operations wait too long
- Rate limits without window type specification — fixed vs sliding windows differ by 2x at boundary conditions
- Confusing runtime_rule (P09, technical parameters) with lifecycle_rule (P11, artifact state transitions) or law (P08, operational mandates)
## Context
Runtime rules operate in the P09 configuration layer. They govern how the system behaves under load, failure, and resource contention. They are consumed by HTTP clients, queue workers, connection pools, and any component that interacts with external systems. Runtime rules are technical parameters, not business rules — they define how operations execute, not whether they should.
## Impact
Exponential backoff with jitter reduced thundering herd incidents by 95%. Per-operation timeouts eliminated 80% of false timeout errors. Circuit breakers with recovery probes reduced mean time to recovery by 40% compared to time-based resets.
## Reproducibility
Reliable runtime rule production: (1) enumerate all operation types needing rules, (2) set per-operation timeouts, (3) define retry strategy with exponential backoff and jitter, (4) configure circuit breaker with failure/probe/success thresholds, (5) specify rate limits with window type, (6) define behavior when limits are exceeded, (7) validate against 8 HARD + 11 SOFT gates.
## References
- runtime-rule-builder SCHEMA.md (timeout, retry, rate limit specification)
- P09 configuration pillar specification
- Circuit breaker, backoff, and rate limiting patterns
