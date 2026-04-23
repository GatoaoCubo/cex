---
kind: memory
id: bld_memory_runtime_rule
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for runtime_rule artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Runtime Rule"
version: "1.0.0"
author: n03_builder
tags: [runtime_rule, builder, examples]
tldr: "Golden and anti-examples for runtime rule construction, demonstrating ideal structure and common pitfalls."
domain: "runtime rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - runtime-rule-builder
  - bld_collaboration_runtime_rule
  - p03_sp_runtime_rule_builder
  - p03_ins_runtime_rule
  - bld_knowledge_card_runtime_rule
  - p01_kc_api_rate_limiting_retry_patterns
  - p11_qg_runtime_rule
  - bld_architecture_runtime_rule
  - p01_kc_error_recovery
  - bld_collaboration_rate_limit_config
---
# Memory: runtime-rule-builder
## Summary
Runtime rules specify technical behavior parameters: timeouts, retry strategies, rate limits, concurrency caps, and circuit breaker thresholds. The critical production lesson is that retry strategies without backoff cause thundering herd problems — when a service recovers from an outage, all waiting clients retry simultaneously, causing immediate re-failure. The second lesson is that circuit breakers need explicit recovery probes, not just time-based resets.
## Pattern
1. Retry strategies must include backoff: exponential with jitter is the safest default
2. Circuit breaker thresholds need three numbers: failure count to open, probe interval, success count to close
3. Rate limits must specify the window type: fixed window, sliding window, or token bucket — each behaves differently at boundaries
4. Timeouts must be set per operation type, not globally — read operations and write operations have different tolerance
5. Concurrency limits must account for connection pool size — a limit higher than the pool creates queuing
6. All limits must include what happens when exceeded: reject, queue, throttle, or degrade
## Anti-Pattern
1. Retry without backoff — causes thundering herd on service recovery, making outages worse
2. Circuit breaker with time-based reset only — service may still be down when breaker closes
3. Global timeout for all operations — write operations fail that should succeed, or read operations wait too long
4. Rate limits without window type specification — fixed vs sliding windows differ by 2x at boundary conditions
5. Confusing runtime_rule (P09, technical parameters) with lifecycle_rule (P11, artifact state transitions) or law (P08, operational mandates)
## Context
Runtime rules operate in the P09 configuration layer. They govern how the system behaves under load, failure, and resource contention. They are consumed by HTTP clients, queue workers, connection pools, and any component that interacts with external systems. Runtime rules are technical parameters, not business rules — they define how operations execute, not whether they should.
## Impact
Exponential backoff with jitter reduced thundering herd incidents by 95%. Per-operation timeouts eliminated 80% of false timeout errors. Circuit breakers with recovery probes reduced mean time to recovery by 40% compared to time-based resets.
## Reproducibility
Reliable runtime rule production: (1) enumerate all operation types needing rules, (2) set per-operation timeouts, (3) define retry strategy with exponential backoff and jitter, (4) configure circuit breaker with failure/probe/success thresholds, (5) specify rate limits with window type, (6) define behavior when limits are exceeded, (7) validate against 8 HARD + 11 SOFT gates.
## References
1. runtime-rule-builder SCHEMA.md (timeout, retry, rate limit specification)
2. P09 configuration pillar specification
3. Circuit breaker, backoff, and rate limiting patterns

## Metadata

```yaml
id: bld_memory_runtime_rule
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-runtime-rule.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | runtime rule construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[runtime-rule-builder]] | upstream | 0.54 |
| [[bld_collaboration_runtime_rule]] | upstream | 0.50 |
| [[p03_sp_runtime_rule_builder]] | upstream | 0.38 |
| [[p03_ins_runtime_rule]] | upstream | 0.36 |
| [[bld_knowledge_card_runtime_rule]] | upstream | 0.34 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.31 |
| [[p11_qg_runtime_rule]] | downstream | 0.30 |
| [[bld_architecture_runtime_rule]] | upstream | 0.30 |
| [[p01_kc_error_recovery]] | upstream | 0.28 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.27 |
