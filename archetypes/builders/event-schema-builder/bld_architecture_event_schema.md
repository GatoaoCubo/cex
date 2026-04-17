---
kind: architecture
id: bld_architecture_event_schema
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of event_schema -- inventory, dependencies, and architectural position
quality: null
title: "Architecture Event Schema"
version: "1.0.0"
author: n03_builder
tags: [event_schema, builder, architecture]
tldr: "Component map: event_type, specversion, source, subject, payload (JSON Schema), versioning, routing. External: data_contract, event_stream."
domain: "event schema construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| event_type | CloudEvents type attribute (reverse-DNS naming) | event_schema | required |
| specversion | CloudEvents spec version (always "1.0") | event_schema | required |
| source | URI identifying the event producer | event_schema | required |
| subject | Event subject (entity identifier) | event_schema | recommended |
| datacontenttype | MIME type of data payload (application/json) | event_schema | required |
| payload_schema | JSON Schema defining the event data structure | event_schema | required |
| schema_version | Semantic version of this schema | event_schema | required |
| evolution_strategy | How breaking changes are managed | event_schema | recommended |
| routing_metadata | Additional headers/attributes for message routing | event_schema | optional |
| data_contract | Producer-consumer SLA (separate kind) | P06 (separate kind) | external |
| event_stream | Kafka/Kinesis infrastructure config (separate kind) | P09 (separate kind) | external |
| openapi_spec | REST API contract (separate kind) | P06 (separate kind) | external |

## CloudEvents Envelope Structure

```
CloudEvent {
  specversion: "1.0"           -- always 1.0 (CloudEvents standard)
  id: uuid                     -- unique event identifier
  type: "com.example.order.created.v1"  -- reverse-DNS naming
  source: "/orders-service"    -- producer URI
  subject: "order-123"         -- entity identifier
  time: "2026-04-17T10:00:00Z" -- RFC3339 timestamp
  datacontenttype: "application/json"
  data: {                      -- the payload (event_schema defines this)
    order_id: "order-123",
    customer_id: "cust-456",
    total_amount: 99.99
  }
}
```

## Versioning Strategy

| Strategy | When | Trade-off |
|----------|------|-----------|
| version in type (recommended) | New major version | Clean separation; old consumers unaffected |
| schema_version field | Minor evolution | Consumers check version field |
| Schemaless evolution | Never | Breaking changes are invisible |

Type versioning example:
- v1: `com.example.order.created.v1`
- v2: `com.example.order.created.v2` (consumers opt-in to new version)

## Boundary Table

| event_schema IS | event_schema IS NOT |
|-----------------|---------------------|
| Event payload schema definition | Producer-consumer SLA and obligations (that is data_contract) |
| CloudEvents/AsyncAPI format | Message broker infrastructure (that is event_stream) |
| Event type naming and versioning | REST API contract (that is openapi_spec) |
| Payload structure (data field) | Topic partitioning and throughput (that is event_stream) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| envelope | specversion, id, source, type, time | CloudEvents standard attributes |
| routing | subject, routing_metadata | Message routing and entity targeting |
| payload | payload_schema (JSON Schema) | Actual event data structure |
| versioning | schema_version, evolution_strategy | Schema lifecycle management |
