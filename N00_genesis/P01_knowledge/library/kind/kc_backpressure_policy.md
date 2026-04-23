---
id: p01_kc_backpressure_policy
kind: knowledge_card
type: kind
pillar: P09
title: "Backpressure Policy -- Deep Knowledge for backpressure_policy"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: backpressure_policy
quality: 8.8
tags: [backpressure_policy, P09, GOVERN, kind-kc, reactive-streams, flow-control]
tldr: "backpressure_policy defines how a pipeline responds when consumers lag behind producers: overflow strategy, buffer, watermarks. NOT circuit_breaker or rate_limit_config."
when_to_use: "Building, reviewing, or reasoning about backpressure_policy artifacts"
keywords: [backpressure, reactive-streams, overflow, buffer, watermark, producer-consumer, flow-control]
feeds_kinds: [backpressure_policy]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
related:
  - p11_qg_context_window_config
  - p01_kc_context_window_config
  - bld_schema_context_window_config
  - bld_schema_streaming_config
  - bld_instruction_streaming_config
  - bld_knowledge_card_streaming_config
  - kc_streaming_config
---

# Backpressure Policy

## Spec
```yaml
kind: backpressure_policy
pillar: P09
llm_function: GOVERN
max_bytes: 2048
naming: p09_bp_{scope}.md
core: true
```

## What It Is
A backpressure_policy defines the flow control contract for an async producer-consumer pipeline.
When the consumer processes slower than the producer emits, the policy specifies the overflow
strategy (drop/buffer/throttle/error), buffer limits, and watermarks for adaptive flow control.

Based on Reactive Streams specification (2014) and the broader back-pressure mechanism
from TCP/IP (RFC 793 window scaling). NOT circuit_breaker (dependency failure isolation).
NOT rate_limit_config (inbound request throttle). NOT runtime_rule (retry logic).

## Cross-Framework Map
| Library | Language | Overflow Config |
|---------|----------|----------------|
| Project Reactor | Java | FluxSink.OverflowStrategy: DROP/BUFFER/LATEST/ERROR |
| RxJava | Java | BackpressureStrategy: DROP/BUFFER/LATEST/ERROR/MISSING |
| Akka Streams | Scala/Java | OverflowStrategy: dropHead/dropTail/dropBuffer/fail |
| Node.js streams | JavaScript | highWaterMark option; readable.pause()/resume() |
| Kafka consumer | Java | max.poll.records, fetch.max.bytes |

## Overflow Strategies
| Strategy | Semantics | Data Loss | Use When |
|----------|-----------|-----------|---------|
| DROP_LATEST | Reject newest incoming items | Yes -- new | Freshness less important than stability |
| DROP_OLDEST | Evict oldest buffered items | Yes -- old | Recency more important than in-flight |
| BUFFER | Accumulate up to buffer_size | No (until full) | Bursty traffic, recoverable lag |
| THROTTLE | Signal producer to slow down | No | Producer rate is controllable |
| ERROR | Raise exception to caller | Caller decides | Caller must explicitly handle overflow |

## Key Parameters
| Parameter | Type | Typical | Notes |
|-----------|------|---------|-------|
| overflow_strategy | enum | DROP_LATEST | See strategy table above |
| buffer_size | int | 100-1000 | Max items; consider memory budget |
| shed_threshold | float [0,1] | 0.7-0.8 | Start shedding at 70-80% capacity |
| high_watermark | int | shed_threshold * buffer_size | Activate backpressure signal |
| low_watermark | int | 40-60% of buffer_size | Resume normal flow |
| request_batch_size | int | 5-20 | Items per demand signal |

## Patterns
| Pattern | When to Use | Config |
|---------|-------------|--------|
| Early shedding | Latency-sensitive pipeline | shed_threshold: 0.5, overflow: THROTTLE |
| Standard protection | LLM job queue | shed_threshold: 0.8, overflow: DROP_LATEST |
| No-loss pipeline | Audit, financial | shed_threshold: 0.6, overflow: ERROR or THROTTLE |
| High-volume stream | Metrics, telemetry | shed_threshold: 0.9, buffer_size: 10000, overflow: DROP_LATEST |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| shed_threshold: 0.99 | Buffer already overflowing before action | Lower to 0.7-0.8 |
| No low_watermark | System oscillates between states | Set low_watermark at 40-60% of buffer_size |
| DROP without documentation | Engineers assume no data loss | Always document data_loss_risk |
| buffer_size: 100000 | OOM with large objects | Calculate memory: buffer_size * avg_item_bytes |

## Integration Graph
```
producer (agent, tool) --> [backpressure_policy] --> consumer (agent, database)
                                  |
                         monitor (queue depth tracking)
                         circuit_breaker (parallel: failure handling)
                         rate_limit_config (parallel: inbound throttle)
```

## Decision Tree
- IF data loss unacceptable -> overflow: THROTTLE or ERROR
- IF producer rate uncontrollable -> overflow: DROP_LATEST or DROP_OLDEST
- IF memory constrained -> lower buffer_size, raise shed_threshold penalty
- IF oscillation observed -> increase hysteresis gap (high - low watermark)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_context_window_config]] | downstream | 0.21 |
| [[p01_kc_context_window_config]] | sibling | 0.19 |
| [[bld_schema_context_window_config]] | upstream | 0.18 |
| [[bld_schema_streaming_config]] | upstream | 0.17 |
| [[bld_instruction_streaming_config]] | upstream | 0.17 |
| [[bld_knowledge_card_streaming_config]] | sibling | 0.16 |
| [[kc_streaming_config]] | sibling | 0.16 |
