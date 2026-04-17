---
id: bld_knowledge_card_backpressure_policy
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: null
title: "Backpressure Policy Builder -- Knowledge Card"
llm_function: INJECT
tags: [backpressure_policy, reactive-streams, flow-control, producer-consumer, P09]
tldr: "backpressure_policy: flow control config defining how a system responds when consumers lag behind producers (Reactive Streams)."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
---

# Knowledge Card: backpressure_policy

## Definition
A `backpressure_policy` is a flow control configuration artifact that defines how a system
responds when downstream consumers cannot keep up with upstream producers. It specifies the
overflow strategy, buffer sizing, shedding thresholds, and demand signaling to prevent
queue exhaustion, out-of-memory errors, and cascade failure in async pipelines.

## Origin
- **Reactive Streams specification** (2014): formal protocol for non-blocking async streams with backpressure
- **TCP/IP flow control** (RFC 793, 1981): window scaling as original backpressure mechanism
- **Project Reactor / Spring WebFlux** (2016): popularized reactive backpressure in JVM ecosystem
- **RxJava** (2013+): original reactive extension with MISSING and ERROR backpressure strategies
- **Akka Streams** (2015): demand-driven pull model based on Reactive Streams
- **CEX pillar**: P09 (Config) -- declarative policy consumed by queue managers and pipeline orchestrators

## The Producer-Consumer Problem

```
PRODUCER (fast)  -->  [BUFFER]  -->  CONSUMER (slow)
     |                  |                 |
     |                  |                 |
  10 req/s           100 items          3 req/s
                    capacity
```

Without backpressure: buffer fills, producer blocks or crashes, data lost.
With backpressure_policy: defined overflow_strategy activates at shed_threshold.

## Overflow Strategies

| Strategy | Semantics | Use When | Data Loss |
|----------|-----------|---------|-----------|
| DROP_LATEST | Reject newest incoming items | Freshness > completeness (sensor data, metrics) | Yes -- new items |
| DROP_OLDEST | Evict oldest buffered items | Recency > in-flight work | Yes -- old items |
| BUFFER | Accumulate up to buffer_size | Bursty traffic, recoverable lag | No (until full) |
| THROTTLE | Signal producer to slow down | Producer rate is controllable | No |
| ERROR | Raise exception to caller | Caller must handle overflow | Caller decides |

## Key Fields
| Field | Role | Example |
|-------|------|---------|
| overflow_strategy | What happens on consumer lag | DROP_LATEST |
| buffer_size | Max items buffered | 100 |
| shed_threshold | Fraction to start shedding | 0.8 (80%) |
| high_watermark | Depth for active backpressure | 80 |
| low_watermark | Depth to resume normal flow | 40 |
| request_batch_size | Items per demand signal | 5 |
| monitored_queue | Named queue this governs | "llm_job_queue" |

## ID Convention
Pattern: `p09_bp_{scope_slug}` where slug is lowercase snake_case.
Examples: `p09_bp_llm_job_queue`, `p09_bp_event_ingest`, `p09_bp_stream_processor`

## Boundary
| backpressure_policy IS | backpressure_policy IS NOT |
|------------------------|---------------------------|
| Consumer lag management | Dependency failure isolation -- that is circuit_breaker |
| Overflow strategy for producer-consumer imbalance | Inbound request throttle RPM/TPM -- that is rate_limit_config |
| Buffer sizing and shedding policy | Retry / backoff after failure -- that is runtime_rule |
| Reactive Streams demand signaling config | Service mesh load balancing -- that is load_balancer_config |

## When to Use
- Async job queue where consumers process slower than producers enqueue
- Event streaming pipeline with variable throughput (Kafka consumer lag)
- LLM inference pipeline: token generation slower than request arrival
- Real-time data ingestion: sensor stream faster than database writer

## When NOT to Use
- Dependency is failing (not just slow) -- use circuit_breaker
- Limiting total inbound requests per minute -- use rate_limit_config
- Choosing between equivalent providers -- use fallback_chain
- Managing retry delays after failures -- use runtime_rule

## Watermark Hysteresis
```
Normal flow:        buffer depth < low_watermark
Backpressure:       buffer depth >= high_watermark
Recovery:           buffer depth drops back below low_watermark
Invalid:            low_watermark >= high_watermark (never configure this)
```
Hysteresis gap (high - low) prevents rapid oscillation between states.
Typical gap: 30-50% of buffer_size.

## Industry Implementations
| Library | Language | Key Config |
|---------|----------|-----------|
| Project Reactor | Java | FluxSink.OverflowStrategy, onBackpressureDrop/Buffer/Error |
| RxJava | Java | BackpressureStrategy.DROP/BUFFER/LATEST/ERROR/MISSING |
| Akka Streams | Scala/Java | OverflowStrategy.dropHead/dropTail/dropBuffer/fail |
| Node.js streams | JavaScript | readable.pause()/resume(), highWaterMark option |
| Kafka consumer | Java | max.poll.records, fetch.max.bytes, session.timeout.ms |
