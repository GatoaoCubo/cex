---
kind: architecture
id: bld_architecture_backpressure_policy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of backpressure_policy -- inventory, dependencies, and architectural position
quality: 8.8
title: "Architecture Backpressure Policy"
version: "1.0.0"
author: n03_builder
tags: [backpressure_policy, builder, architecture]
tldr: "Component map: overflow_strategy, buffer, watermarks, request_batch. External: circuit_breaker, rate_limit_config."
domain: "backpressure policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| overflow_strategy | Policy when consumer cannot keep up | backpressure_policy | required |
| buffer_size | Max items queued before overflow activates | backpressure_policy | required |
| shed_threshold | Fraction of buffer capacity to begin shedding | backpressure_policy | required |
| high_watermark | Absolute depth triggering active backpressure | backpressure_policy | recommended |
| low_watermark | Depth at which normal flow resumes | backpressure_policy | recommended |
| request_batch_size | Items requested per demand signal (Reactive Streams) | backpressure_policy | recommended |
| monitored_queue | Queue/channel this policy governs | backpressure_policy | recommended |
| circuit_breaker | Dependency failure isolation (separate concern) | P09 (separate kind) | external |
| rate_limit_config | Inbound request throttle (RPM/TPM) | P09 (separate kind) | external |
| runtime_rule | Retry and backoff strategy | P09 (separate kind) | external |
| producer | Upstream data source | P04 (tool/agent) | producer |
| consumer | Downstream processor | P02 (agent) | consumer |

## Flow Model

```
PRODUCER                    BUFFER                    CONSUMER
  |                           |                           |
  |--emit(item)-->            |                           |
  |                     buffer_size                       |
  |               shed_threshold (e.g. 80%)               |
  |               high_watermark (absolute)               |
  |                           |                           |
  |                  If buffer >= shed_threshold:         |
  |                  apply overflow_strategy:             |
  |                    DROP_LATEST: discard new           |
  |                    DROP_OLDEST: discard old           |
  |                    THROTTLE: slow producer            |
  |                    ERROR: raise to caller             |
  |                           |                           |
  |                           |--request(batch_size)-->   |
  |                           |<--process(items)----------
  |                    if depth <= low_watermark:         |
  |                    resume normal emission             |
```

## Dependency Graph
```
overflow_strategy  --governs-->   buffer overflow behavior
buffer_size        --limits-->    queue depth
shed_threshold     --triggers-->  overflow_strategy activation
high_watermark     --triggers-->  active backpressure signal
low_watermark      --releases-->  backpressure (resume normal)
request_batch_size --controls-->  consumer demand rate
circuit_breaker    --parallel-->  handles FAILURES (not lag)
rate_limit_config  --parallel-->  handles INBOUND RATE (not consumer lag)
```

## Boundary Table
| backpressure_policy IS | backpressure_policy IS NOT |
|------------------------|---------------------------|
| Consumer lag management | Dependency failure isolation (that is circuit_breaker) |
| Buffer + overflow strategy declaration | Inbound request throttle RPM/TPM (that is rate_limit_config) |
| Reactive Streams demand signaling config | Retry/backoff strategy (that is runtime_rule) |
| Producer-consumer flow contract | Observability (that is trace_config/monitor) |
| Queue/channel overflow policy | Authentication/authorization (that is env_config) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| detection | shed_threshold, high_watermark | Detect consumer lag early |
| control | overflow_strategy | Define response to overflow |
| buffering | buffer_size, monitored_queue | Absorb bursts within limit |
| signaling | request_batch_size, low_watermark | Control demand and resume |
| external | circuit_breaker, rate_limit_config | Adjacent, non-overlapping concerns |
