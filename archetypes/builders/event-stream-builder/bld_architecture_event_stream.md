---
id: bld_architecture_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Architecture"
version: 1.0.0
quality: 7.2
tags: [builder, event_stream, architecture]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
---
# Architecture: event_stream
## Core Model
An event_stream is a durable, ordered, append-only log of domain events.
Multiple consumers read from it independently (each tracks its own offset).
Industry implementations: Kafka topic, AWS Kinesis stream, Azure Event Hub, Pulsar topic.
## Structural Topology
```
Producer(s) --> [event_stream: ordered, partitioned, retained]
                       |
          [Consumer Group A: offset=latest]
          [Consumer Group B: offset=earliest (reprocessing)]
          [Consumer Group C: offset=checkpoint]
```
## Key Properties
1. Ordered: within a partition, events are ordered by arrival time
2. Durable: retained for configurable time/bytes (survives consumer restart)
3. Replayable: consumers can seek to any offset (replay window = retention)
4. Multi-consumer: many consumer groups, each with independent offset
5. Partitioned: parallel consumption via partition key (e.g., orderId)
## Relationship to Other Kinds
| Kind | Relationship |
|------|-------------|
| webhook | single outbound HTTP push (not ordered, not replayable, 1 consumer) |
| signal | internal CEX nucleus completion signal (not domain events, not persisted as stream) |
| process_manager | subscribes to event streams to drive process transitions |
| domain_event | schema definition for events flowing through the stream |
## Delivery Semantics
| Semantic | When | Tradeoff |
|----------|------|----------|
| at_most_once | fire-and-forget, low latency OK | may lose events |
| at_least_once | retries on failure | may duplicate; consumers must be idempotent |
| exactly_once | Kafka transactions / idempotent producer | highest cost, use for financial data |
## Partition Design
- High cardinality key (userId, orderId): balanced load, high parallelism
- Low cardinality key (region, type): easy global ordering, less parallelism
- No key: round-robin, no ordering guarantee per entity
