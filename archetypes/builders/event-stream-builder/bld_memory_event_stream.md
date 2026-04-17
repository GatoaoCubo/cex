---
id: bld_memory_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Memory"
version: 1.0.0
quality: 5.8
tags: [builder, event_stream, memory]
llm_function: INJECT
density_score: 0.97
updated: "2026-04-17"
---
# Memory: event_stream
## Session Patterns
- Partition key selection: ask "what entity needs ordered processing?" -- that field is the partition key.
- Retention sizing: retention_hours should cover at least the slowest consumer's replay window. 7 days (168h) is a safe default.
- Consumer groups: every consumer that needs independent offset tracking needs its own group.
- Delivery semantics: at_least_once is the default. exactly_once only when financial or idempotency is provably impossible.
## Common Mistakes
- No partition key: loses per-entity ordering. Always specify partition_key.
- Only one consumer group: if analytics and processing read the same stream, they need separate groups.
- Missing schema registry: without a registry, schema evolution becomes breaking changes.
- Confusing retention with backup: retention is for consumer replay, not disaster recovery.
## Vocabulary
- "Topic" = Kafka term for event_stream
- "Stream" = Kinesis/Flink/Pulsar term for event_stream
- "Consumer group" = set of consumers that share an offset (load balanced within the group)
- "Offset" = position in the stream (each consumer group tracks its own)
- "Lag" = how far behind the consumer is from the latest event
## Throughput Sizing Guide
| Events/sec | Partitions | Notes |
|-----------|-----------|-------|
| < 1000 | 3-6 | Single service |
| 1k-10k | 6-12 | Multi-service |
| 10k-100k | 12-24 | High traffic |
| > 100k | 24+ | Platform-scale |
