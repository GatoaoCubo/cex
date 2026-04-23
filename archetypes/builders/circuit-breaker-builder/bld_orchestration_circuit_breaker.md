---
quality: 8.8
quality: 8.2
kind: collaboration
id: bld_collaboration_circuit_breaker
pillar: P12
llm_function: COLLABORATE
purpose: How circuit-breaker-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
title: "Collaboration Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, collaboration]
tldr: "Dependency fault isolation specialist. Upstream of runtime_rule and monitor. Downstream of agent and tool configs."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_runtime_rule
  - bld_collaboration_rate_limit_config
  - bld_collaboration_builder
  - bld_collaboration_model_provider
  - bld_collaboration_fallback_chain
  - bld_collaboration_boot_config
  - bld_collaboration_quality_gate
  - bld_collaboration_cost_budget
  - bld_architecture_kind
  - bld_collaboration_memory_scope
---

# Collaboration: circuit-breaker-builder

## My Role in Crews
I am a RESILIENCE SPECIALIST. I answer ONE question:
"how should this dependency be isolated when it fails, and how should recovery be probed?"
I do not define retry logic. I do not define inbound rate limits. I do not choose between providers.
I declare the fault isolation boundary for a single downstream dependency.

## Crew Compositions

### Crew: "Resilient API Integration"
```
  1. rate-limit-config-builder  -> "quota declaration (RPM, TPM, budget)"
  2. circuit-breaker-builder    -> "fault isolation (failure threshold, cooldown)"
  3. runtime-rule-builder       -> "retry and backoff policy for 429 and transient failures"
  4. env-config-builder         -> "API key, base URL, model selection"
```

### Crew: "Production Hardening"
```
  1. circuit-breaker-builder    -> "per-service fault isolation configs"
  2. backpressure-policy-builder -> "upstream flow control during degradation"
  3. guardrail-builder          -> "execution constraints and safety limits"
  4. monitor-builder            -> "state transition observability"
```

### Crew: "Multi-Provider Resilience"
```
  1. fallback-chain-builder     -> "ordered provider substitution list"
  2. circuit-breaker-builder    -> "breaker per provider in the chain"
  3. rate-limit-config-builder  -> "quotas per provider"
```

## Handoff Protocol

### I Receive
- seeds: service name, traffic volume, acceptable failure tolerance
- failure patterns: what types of errors occur (5xx, timeout, DNS)
- recovery SLA: how long is an outage before recovery should be attempted

### I Produce
- circuit_breaker artifact (.md with YAML frontmatter)
- committed to: `N0X_{domain}/P09_config/p09_cb_{service_slug}.md`

### I Signal
- signal: complete (with quality score)
- if quality < 8.0: signal retry with gate failures listed

## Builders I Depend On
None -- independent builder (layer 0). Circuit breakers can be defined standalone.

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents wrap calls through circuit breaker at execution time |
| runtime-rule-builder | Retry policy may consult circuit state before retrying |
| monitor-builder | Monitors track CLOSED/OPEN/HALF-OPEN state transition events |
| backpressure-policy-builder | Backpressure may read circuit state to decide shedding policy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_runtime_rule]] | sibling | 0.49 |
| [[bld_collaboration_rate_limit_config]] | sibling | 0.46 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_collaboration_model_provider]] | sibling | 0.38 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.38 |
| [[bld_collaboration_boot_config]] | sibling | 0.36 |
| [[bld_collaboration_quality_gate]] | sibling | 0.34 |
| [[bld_collaboration_cost_budget]] | sibling | 0.34 |
| [[bld_architecture_kind]] | upstream | 0.33 |
| [[bld_collaboration_memory_scope]] | sibling | 0.33 |
