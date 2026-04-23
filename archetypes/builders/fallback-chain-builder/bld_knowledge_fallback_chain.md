---
kind: knowledge_card
id: bld_knowledge_card_fallback_chain
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for fallback_chain production — graceful model degradation
sources: Nygard 2007 "Release It!", Netflix Hystrix, LiteLLM fallbacks, AWS Route 53
quality: 9.1
title: "Knowledge Card Fallback Chain"
version: "1.0.0"
author: n03_builder
tags: [fallback_chain, builder, examples]
tldr: "Golden and anti-examples for fallback chain construction, demonstrating ideal structure and common pitfalls."
domain: "fallback chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_fallback_chain
  - p10_lr_fallback_chain_builder
  - fallback-chain-builder
  - bld_collaboration_fallback_chain
  - p03_sp_fallback_chain_builder
  - p11_qg_fallback_chain
  - p01_kc_fallback_chain
  - bld_examples_fallback_chain
  - bld_schema_fallback_chain
  - p02_fb_CHAIN_SLUG
---

# Domain Knowledge: fallback_chain
## Executive Summary
Fallback chains implement graceful degradation for LLM systems — when the primary model fails or produces below-threshold quality, the system automatically falls to the next model in a ranked sequence. Derived from circuit breaker design (Nygard 2007), adapted for multi-model architectures where models vary in capability, cost, and latency. Fallback chains differ from prompt chains (text sequencing), workflows (agent orchestration), and routers (task routing).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (identity/model) |
| Frontmatter fields | 15 required |
| Quality gates | 8 HARD + 10 SOFT |
| Degradation order | Most capable → least capable (opus → sonnet → haiku) |
| Trigger types | timeout, error, rate_limit, quality_below_threshold |
| Circuit breaker | N consecutive failures trips breaker |
| Key fields | steps, timeout_per_step, quality_threshold, cost_ceiling |
## Patterns
- **Ordered degradation**: steps rank from most capable/expensive to least capable/cheapest
- **Dual gating**: timeout gating (max time per step) AND quality gating (output score threshold)
- **Circuit breaker**: N consecutive failures trip breaker, halting all attempts — prevents resource waste
- **Cost ceiling**: total chain cost has a maximum; reaching ceiling triggers alert
- **Retry before fallback**: retry_count attempts per step before moving to next model
| Source | Concept | Application |
|--------|---------|-------------|
| Nygard "Release It!" | Circuit breaker pattern | circuit_breaker_threshold |
| Netflix Hystrix | Cascading failure prevention | timeout + retry per step |
| LiteLLM | Model-level fallback alternatives | Chain step sequence |
| AWS Route 53 | Health-based failover | quality_threshold triggers next |
- **Final step alert**: reaching the last step means system is at minimum capability — trigger operational alert
- **Stateless per-request**: chain state resets for each new request; no carry-over between calls
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Ascending order (cheap → expensive) | Wastes time on weak models before trying capable ones |
| No quality threshold | Low-quality output from fast model accepted silently |
| No circuit breaker | Infinite retries waste tokens and time |
| No cost ceiling | Expensive model retries accumulate unbounded cost |
| Single step chain | Not a chain; just a model selection |
| Quality threshold = 0 | Every output accepted; fallback never triggers |
## Application
1. Rank models: most capable first (opus → sonnet → haiku)
2. Set timeout per step: based on expected response time + buffer
3. Define quality threshold: minimum acceptable output score (0-10)
4. Configure circuit breaker: N failures before stopping
5. Set cost ceiling: maximum total spend across all steps
6. Validate: degradation order is descending, thresholds are meaningful
## References
- Nygard 2007: "Release It!" — circuit breaker pattern
- LiteLLM: model fallback configuration documentation
- Netflix Hystrix: cascading failure prevention patterns
- AWS Route 53: health check-based DNS failover

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_fallback_chain]] | downstream | 0.52 |
| [[p10_lr_fallback_chain_builder]] | downstream | 0.49 |
| [[fallback-chain-builder]] | downstream | 0.42 |
| [[bld_collaboration_fallback_chain]] | downstream | 0.40 |
| [[p03_sp_fallback_chain_builder]] | downstream | 0.40 |
| [[p11_qg_fallback_chain]] | downstream | 0.37 |
| [[p01_kc_fallback_chain]] | sibling | 0.35 |
| [[bld_examples_fallback_chain]] | downstream | 0.34 |
| [[bld_schema_fallback_chain]] | downstream | 0.33 |
| [[p02_fb_CHAIN_SLUG]] | downstream | 0.32 |
