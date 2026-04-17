---
id: bld_knowledge_card_event_schema
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: null
title: "Event Schema Builder -- Knowledge Card"
llm_function: INJECT
tags: [event_schema, cloudevents, asyncapi, P06, event-driven]
tldr: "event_schema: CloudEvents/AsyncAPI payload schema with structure, versioning, and routing. NOT data_contract (SLA) nor event_stream (infrastructure)."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
---

# Knowledge Card: event_schema

## Definition

An `event_schema` is a formal schema for event payloads in event-driven architectures,
following the CloudEvents 1.0 specification (CNCF standard for event envelopes) and
AsyncAPI 3.0 (the event-driven equivalent of OpenAPI). It defines the event type,
payload data structure (JSON Schema), versioning strategy, and routing metadata.
Consumed by event producers, consumers, schema registries, and message routing infrastructure.

## Origin

- **CloudEvents 1.0** (CNCF, 2020): standardized event envelope format
- **AsyncAPI 3.0** (2023): machine-readable spec for event-driven APIs
- **Apache Avro / Confluent Schema Registry**: schema evolution and compatibility
- **Domain Events** (Evans DDD 2003): events as first-class domain artifacts
- **CEX pillar**: P06 (Schema) -- machine-readable contracts

## Key Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| event_type | string | YES | CloudEvents type: reverse-DNS + version |
| schema_version | semver | YES | Schema version for consumer compatibility |
| source | URI string | YES | Producing service identifier |
| specversion | "1.0" | YES | CloudEvents spec version |
| datacontenttype | "application/json" | YES | Payload MIME type |
| payload_schema | JSON Schema | YES | Structure of the data field |
| evolution_strategy | enum | REC | ADDITIVE_ONLY/VERSIONED_TYPE/FULL_COMPATIBILITY |

## When to Use

| Scenario | Use event_schema? |
|----------|-----------------|
| Defining Kafka message payload structure | YES |
| Webhook payload definition | YES |
| Domain event definition (OrderCreated, UserRegistered) | YES |
| EventBridge / SNS / PubSub event format | YES |
| Producer-consumer SLA with data quality obligations | NO -- use data_contract |
| Kafka topic configuration (partitions, retention) | NO -- use event_stream |
| REST API contract | NO -- use openapi_spec |

## CloudEvents Type Naming

| Pattern | Example | Notes |
|---------|---------|-------|
| Reverse DNS + aggregate + event + version | com.acme.order.created.v1 | Recommended standard |
| Domain + event + version | orders.created.v1 | Acceptable for internal systems |
| Simple name | OrderCreated | Anti-pattern -- no namespace or version |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No version in event_type | Consumers break on schema change | Always suffix .v{major} |
| Additive + breaking changes | Consumer code breaks silently | Use VERSIONED_TYPE for breaking changes |
| Embedding SLA in event_schema | Conflates schema with contract | Separate data_contract for obligations |
| No datacontenttype | Consumers guess payload format | Always declare application/json |
| Generic payload (object {}) | No structure enforcement | Define full JSON Schema |

## Decision Tree

```
Need to define event payload structure?
  YES -> event_schema
    Is it CloudEvents compatible?
      YES -> use CloudEvents envelope fields
      NO -> declare specversion anyway (future compatibility)
    Is it breaking change?
      YES -> new event_type version (com.ex.order.created.v2)
      NO -> additive schema change (same event_type, update schema_version)
```

## Cross-Framework Map

| Framework/Standard | Equivalent | Notes |
|-------------------|-----------|-------|
| CloudEvents 1.0 | event_schema | event_schema follows CloudEvents envelope |
| AsyncAPI 3.0 messages | event_schema | AsyncAPI .message = event_schema |
| Avro Schema | event_schema (data only) | Avro = payload; event_schema = envelope + payload |
| Confluent Schema Registry | event_schema storage | Registry stores event_schema artifacts |
| EventBridge schema | event_schema | AWS EventBridge uses CloudEvents-like format |

## CloudEvents Example

```json
{
  "specversion": "1.0",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "type": "com.example.order.created.v1",
  "source": "/orders-service",
  "subject": "order-123",
  "time": "2026-04-17T10:00:00Z",
  "datacontenttype": "application/json",
  "data": {
    "order_id": "order-123",
    "customer_id": "cust-456",
    "items": [{"sku": "PROD-1", "qty": 2}],
    "total_amount": 99.99,
    "currency": "USD"
  }
}
```

## Integration Graph

```
event_schema (P06)
  |
  |-- produced by --> state_machine (P12) -- state transition events
  |-- consumed by --> agent (P02) -- agents react to events
  |-- stored in --> event_stream (P09) -- Kafka/Kinesis topics
  |-- governed by --> data_contract (P06) -- SLA on top of schema
  |-- documented by --> api_reference (P01) -- event catalog docs
```
