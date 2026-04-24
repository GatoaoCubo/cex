---
quality: 8.0
quality: 7.7
id: kc_event_stream
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, event_stream, kafka, kinesis, P04]
density_score: 0.97
updated: "2026-04-17"
related:
  - p01_kc_webhook
  - bld_collaboration_webhook
  - bld_memory_webhook
  - p03_sp_webhook_builder
  - webhook-builder
  - p01_kc_signal
  - bld_architecture_webhook
  - bld_instruction_webhook
  - bld_knowledge_card_connector
  - p03_sp_signal_builder
---
# Knowledge Card: event_stream

## Definition
An `event_stream` is a configuration artifact for a real-time, ordered, durable sequence
of domain events consumed by one or more independent subscribers. Industry implementations:
Kafka topic, AWS Kinesis stream, Azure Event Hub, Apache Pulsar topic. Events are written
by a producer and read by consumer groups, each tracking their own offset independently.

## When to Use
- Multiple independent consumers need the same domain events
- Events must be replayable (for audit, reprocessing, or onboarding new consumers)
- Order of events within an entity's lifecycle matters (per-partition ordering)
- Throughput exceeds what synchronous HTTP can handle reliably (> ~100 events/sec)
- Temporal decoupling required: producer and consumers don't need to be alive simultaneously

## When NOT to Use
- Single outbound HTTP call to one endpoint: use `webhook`
- Internal CEX nucleus coordination signal: use `signal` (not a user-facing kind)
- One-time notification to one recipient: use `webhook`
- Time-triggered batch: use `schedule`
- Request-response pattern: use `api_client`

## Structure
Every `event_stream` configures:
1. **Event types**: which domain events flow through this stream
2. **Producer**: which service or aggregate writes to the stream
3. **Consumer groups**: each group has independent offset + lag tolerance
4. **Partitioning**: partition key (for ordering) + partition count (for parallelism)
5. **Retention**: time (hours) + bytes (GB) -- determines replay window
6. **Delivery semantics**: at_most_once, at_least_once, or exactly_once
7. **Schema**: format (Avro/Protobuf/JSON) + registry + compatibility mode
8. **Operations**: lag thresholds, alerts, producer error rate

## Consumer Groups Explained
Each consumer group reads the stream independently:
- Group A (fulfillment): reads from latest, processes in real time
- Group B (analytics): reads from earliest, processes historical data
- Group C (audit): reads everything, slow lag tolerance acceptable
All three groups read the same events without interfering with each other.

## Partition Design
Partition key determines both parallelism and ordering scope:
- `orderId` as key: all events for one order go to the same partition (ordered per order)
- `userId` as key: all events for one user go to the same partition
- No key: round-robin (no per-entity ordering guarantee)

## Delivery Semantics Trade-offs
| Semantic | Data loss risk | Duplication risk | Cost |
|----------|---------------|-----------------|------|
| at_most_once | possible | none | low |
| at_least_once | none | possible | medium |
| exactly_once | none | none | high |

Default: at_least_once. Use exactly_once only for financial or idempotency-critical flows.

## Use Cases
1. **Order events stream**: OrderPlaced, OrderPaid, OrderShipped consumed by fulfillment, analytics, and notification services independently
2. **User activity stream**: PageViewed, ItemAddedToCart consumed by personalization and fraud detection
3. **IoT sensor stream**: device telemetry consumed by real-time alerting and historical archiving

## Relationships to Other Kinds
| Kind | Relationship |
|------|-------------|
| `webhook` | single outbound HTTP push to one endpoint (no ordering, no replay, 1 consumer) |
| `process_manager` | subscribes to event streams to drive process state transitions |
| `domain_event` | schema of individual events flowing through the stream |
| `api_client` | may consume events via HTTP SSE or WebSocket (pull-based alternative) |

## Anti-Patterns
- **No partition key**: loses per-entity ordering; always specify a partition key
- **One consumer group for all**: each independent consumer needs its own group
- **Missing schema registry**: without a registry, schema evolution causes breaking changes
- **Retention too short**: if a consumer goes offline for 48h and retention is 24h, events are lost
- **Confusing with webhook**: webhook is push to one; event_stream is pull by many

## CEX Metadata
| Property | Value |
|----------|-------|
| Pillar | P04 (Tools) |
| ID pattern | `p04_es_{slug}` |
| max_bytes | 3072 |
| llm_function | CALL |
| Builder | event-stream-builder (13 ISOs) |
| Nucleus | N05 (Operations) or N03 (Engineering) |
| Pattern source | Kafka docs, AWS Kinesis, Kleppmann DDIA (2017) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_webhook]] | sibling | 0.23 |
| [[bld_collaboration_webhook]] | downstream | 0.22 |
| [[bld_memory_webhook]] | downstream | 0.21 |
| [[p03_sp_webhook_builder]] | downstream | 0.21 |
| [[webhook-builder]] | downstream | 0.20 |
| [[p01_kc_signal]] | sibling | 0.19 |
| [[bld_architecture_webhook]] | downstream | 0.18 |
| [[bld_instruction_webhook]] | downstream | 0.17 |
| [[bld_knowledge_card_connector]] | sibling | 0.16 |
| [[p03_sp_signal_builder]] | downstream | 0.16 |
