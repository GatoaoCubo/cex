---
quality: 8.6
quality: 8.0
kind: collaboration
id: bld_collaboration_backpressure_policy
pillar: P12
llm_function: COLLABORATE
purpose: How backpressure-policy-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
title: "Collaboration Backpressure Policy"
version: "1.0.0"
author: n03_builder
tags: [backpressure_policy, builder, collaboration]
tldr: "Consumer lag specialist. Works with circuit-breaker, rate-limit-config, and monitor in resilience crews."
domain: "backpressure policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_rate_limit_config
  - bld_collaboration_builder
  - bld_collaboration_runtime_rule
  - bld_collaboration_memory_scope
  - bld_architecture_kind
  - bld_collaboration_boot_config
  - bld_collaboration_quality_gate
  - bld_collaboration_retriever_config
  - bld_collaboration_agent
  - bld_collaboration_streaming_config
---

# Collaboration: backpressure-policy-builder

## My Role in Crews
I am a FLOW CONTROL SPECIALIST. I answer ONE question:
"how should this pipeline respond when consumers cannot keep up with producers?"
I do not handle dependency failures (circuit breakers). I do not throttle inbound requests (rate limits).
I declare the overflow policy and buffer contract for producer-consumer imbalance.

## Crew Compositions

### Crew: "Pipeline Resilience"
```
  1. circuit-breaker-builder      -> "dependency fault isolation per service"
  2. backpressure-policy-builder  -> "consumer lag management per queue"
  3. rate-limit-config-builder    -> "inbound request throttling"
  4. runtime-rule-builder         -> "retry and backoff strategy"
```

### Crew: "Event Streaming Setup"
```
  1. backpressure-policy-builder  -> "Kafka consumer overflow policy"
  2. env-config-builder           -> "Kafka connection and topic config"
  3. monitor-builder              -> "consumer lag observability"
```

### Crew: "LLM Inference Pipeline"
```
  1. rate-limit-config-builder    -> "provider RPM/TPM quotas"
  2. circuit-breaker-builder      -> "provider failure isolation"
  3. backpressure-policy-builder  -> "job queue overflow policy"
  4. agent-builder                -> "inference agent with all policies wired"
```

## Handoff Protocol

### I Receive
- seeds: queue/channel name, producer throughput, consumer throughput
- acceptable data loss: can items be dropped? which end?
- buffer memory budget: max items to hold

### I Produce
- backpressure_policy artifact (.md with YAML frontmatter)
- committed to: `N0X_{domain}/P09_config/p09_bp_{scope_slug}.md`

### I Signal
- signal: complete (with quality score)
- if quality < 8.0: signal retry with gate failures listed

## Builders I Depend On
None -- independent builder (layer 0). Backpressure policies can be defined standalone.

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents configure job queues using backpressure_policy at runtime |
| monitor-builder | Monitors track queue depth and shed events against policy thresholds |
| circuit-breaker-builder | Circuit breakers may consult backpressure state during half-open probing |
| workflow-builder | Workflows reference backpressure_policy for async step queues |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_rate_limit_config]] | sibling | 0.41 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_collaboration_runtime_rule]] | sibling | 0.39 |
| [[bld_collaboration_memory_scope]] | sibling | 0.35 |
| [[bld_architecture_kind]] | upstream | 0.34 |
| [[bld_collaboration_boot_config]] | sibling | 0.34 |
| [[bld_collaboration_quality_gate]] | sibling | 0.34 |
| [[bld_collaboration_retriever_config]] | sibling | 0.34 |
| [[bld_collaboration_agent]] | sibling | 0.33 |
| [[bld_collaboration_streaming_config]] | sibling | 0.33 |
