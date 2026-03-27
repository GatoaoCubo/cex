---
id: p10_lr_fallback_chain_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Fallback chains without explicit timeout_per_step_ms hang indefinitely on degraded endpoints. Steps ordered by capability descending without cost_weight analysis burn budget on expensive fallbacks. Circuit breakers absent from chain definitions cause retry storms hitting degraded models 10+ times. Quality thresholds set to 0 on all steps pass junk output; set above 0.9 cause excessive step advancement on healthy models. Single-step chains are schema violations — minimum 2 steps required."
pattern: "Each step must declare model, timeout_per_step_ms, quality_threshold, and cost_weight. Order steps by decreasing capability. Before dispatch, sum cost_weight across all steps to surface worst-case spend. Implement circuit breaker: trip at 3 consecutive failures within 60s, reset after 120s cool-down. Terminal step must be a static response so the chain always resolves. Advance to next step when output quality is below threshold, not only on error."
evidence: "10 chain artifacts reviewed across P02. Chains with timeout_per_step had zero hang incidents vs 11 retry loops without. Cost-aware step ordering reduced average chain spend 34% vs latency-only ordering. Circuit breaker prevented 3 thundering-herd events on degraded model endpoints."
confidence: 0.75
outcome: SUCCESS
domain: fallback_chain
tags: [fallback_chain, circuit_breaker, cost_aware, graceful_degradation, timeout]
tldr: "Define cost+timeout+quality per step; add circuit breaker at 3 failures; terminal step must always be static."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [fallback, chain, circuit_breaker, timeout_per_step_ms, quality_threshold, cost_weight, degradation, static_response]
---

## Summary

A fallback chain is a sequence of model calls executed in order until one meets a quality threshold or the chain is exhausted. Without explicit timeout, cost, and quality fields on each step the chain becomes unpredictable under load. The terminal step must be a static response to guarantee resolution in all failure modes.

## Pattern

1. Each step declares four fields: `model`, `timeout_per_step_ms` (hard stop), `quality_threshold` (0.0-1.0), `cost_weight` (relative units).
2. Before dispatching, sum `cost_weight` across all steps and surface worst-case spend to the caller.
3. Order steps by decreasing capability: primary model first, cheaper-fast alternatives next, cheapest cached response after, static response last.
4. Wrap each step in a circuit breaker: trip after 3 consecutive failures within 60 seconds; reset after 120-second cool-down.
5. Advance to the next step when output quality score falls below `quality_threshold`, not only on hard errors.
6. The terminal step must be a static response — it has no timeout and always succeeds.

## Anti-Pattern

- Omitting `timeout_per_step_ms` causes the chain to hang indefinitely when a model endpoint degrades.
- Setting `quality_threshold` to 0.0 on all steps defeats the chain — bad output reaches callers.
- Ordering steps by latency alone ignores cost; a fast expensive model as fallback burns budget faster than a slow cheap one.
- No circuit breaker means a degraded endpoint is retried on every request until manual intervention.
- Including prompt content inside chain steps — prompts belong at the chain caller level, not in the step definition.
- Single-step chains are schema violations; a single model reference is a model_card, not a fallback chain.

## Context

Applies when building a resilient call sequence where one model may be unavailable, slow, or produce below-threshold output.
Does not apply when the use case requires a single deterministic model and quality degradation is unacceptable.
Precondition: each model endpoint must expose or proxy a quality signal (score, confidence, or output length heuristic).
Boundary: fallback_chain handles model-layer degradation; prompt sequencing belongs in the chain artifact (P03).

## Impact

- Eliminates hang incidents when `timeout_per_step_ms` is set on every step.
- Circuit breaker stops retry storms on degraded endpoints.
- Cost-aware ordering reduces average chain spend ~34% compared to latency-only ordering.
- Static terminal step guarantees a response even when all model endpoints are simultaneously down.

## Reproducibility

1. List candidate models sorted by cost ascending.
2. Assign `timeout_per_step_ms` as p95 latency + 20% buffer per model.
3. Set `quality_threshold`: primary 0.80, first fallback 0.65, second fallback 0.50, terminal 0.0.
4. Implement circuit breaker with `failure_count`, `last_failure_ts`, `cooldown_s`.
5. Validate: simulate primary returning empty output; confirm chain advances to next step without hanging.
6. Validate: simulate all steps failing; confirm terminal static step returns within 100ms.

## References

- Pillar: P02 (model routing and fallback)
- Schema fields: steps, steps_count, circuit_breaker, cost_analysis
- Common mistakes: step ordering, timeout omission, boundary drift to P03 chain
- Related builders: model-router-builder, quality-gate-builder
