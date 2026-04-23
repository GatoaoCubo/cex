---
kind: collaboration
id: bld_collaboration_runtime_rule
pillar: P09
llm_function: COLLABORATE
purpose: How runtime-rule-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Runtime Rule"
version: "1.0.0"
author: n03_builder
tags: [runtime_rule, builder, examples]
tldr: "Golden and anti-examples for runtime rule construction, demonstrating ideal structure and common pitfalls."
domain: "runtime rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_fallback_chain
  - bld_collaboration_env_config
  - bld_collaboration_rate_limit_config
  - runtime-rule-builder
  - bld_collaboration_path_config
  - bld_collaboration_boot_config
  - bld_memory_runtime_rule
  - bld_collaboration_builder
  - bld_collaboration_trace_config
  - bld_collaboration_retriever_config
---

# Collaboration: runtime-rule-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what timeouts, retries, and limits govern this operation at runtime?"
I produce technical operational parameters — timeouts, retry strategies, rate limits, circuit breakers. I do not handle lifecycle rules, inviolable laws, safety guardrails, or generic env config.
## Crew Compositions
### Crew: "Resilient API Integration"
```
  1. connector-builder        -> "external API connector definition and auth config"
  2. runtime-rule-builder     -> "timeout, retry backoff, and circuit breaker for the connector"
  3. fallback-chain-builder   -> "ordered fallback when circuit breaker trips"
```
### Crew: "Agent Operational Config"
```
  1. env-config-builder       -> "environment variables and infrastructure settings"
  2. runtime-rule-builder     -> "operational limits: rate limits, concurrency, timeouts"
  3. feature-flag-builder     -> "on/off toggles for runtime behaviors"
  4. spawn-config-builder     -> "spawn parameters informed by the runtime limits"
```
### Crew: "Governance Stack"
```
  1. invariant-builder              -> "inviolable rules that cannot be overridden"
  2. guardrail-builder        -> "safety boundaries on agent behavior"
  3. runtime-rule-builder     -> "technical operational limits (timeouts, retries, throttle)"
  4. lifecycle-rule-builder   -> "artifact lifecycle transition rules"
```
## Handoff Protocol
### I Receive
- seeds: operation type, SLA requirements, external service characteristics, failure tolerance level
- optional: existing runtime config to extend, observed failure rates, peak load estimates, vendor rate limit docs
### I Produce
- runtime_rule artifact (YAML frontmatter + rule specification with timeout/retry/rate-limit/circuit-breaker sections, max 4096 bytes)
- committed to: `cex/P09/examples/p09_rr_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- connector-builder: provides external service latency profile and known rate limits that set my thresholds
- env-config-builder: provides environment-level settings that bound my runtime parameters
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| feature-flag-builder | Feature flags may need timeout and fallback rules during rollout |
| env-config-builder | Env config may reference runtime rule values for service limits |
| spawn-config-builder | Uses my concurrency and timeout limits to configure agent_group spawn parameters |
| fallback-chain-builder | Triggers fallback chain when I define circuit breaker trip conditions |
| daemon-builder | Applies my retry and rate limit rules to long-running daemon operations |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_fallback_chain]] | sibling | 0.40 |
| [[bld_collaboration_env_config]] | sibling | 0.40 |
| [[bld_collaboration_rate_limit_config]] | sibling | 0.40 |
| [[runtime-rule-builder]] | related | 0.39 |
| [[bld_collaboration_path_config]] | sibling | 0.37 |
| [[bld_collaboration_boot_config]] | sibling | 0.36 |
| [[bld_memory_runtime_rule]] | downstream | 0.36 |
| [[bld_collaboration_builder]] | sibling | 0.34 |
| [[bld_collaboration_trace_config]] | sibling | 0.33 |
| [[bld_collaboration_retriever_config]] | sibling | 0.33 |
