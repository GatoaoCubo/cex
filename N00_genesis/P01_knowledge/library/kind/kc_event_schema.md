---
id: kc_event_schema
kind: knowledge_card
pillar: P01
title: "Knowledge Card -- Event Schema"
version: 1.0.0
quality: null
tags: [knowledge, event_schema, cloudevents, asyncapi, event-driven]
---

# Event Schema

## Definition

An `event_schema` is a formal schema for event payloads in event-driven architectures, following the CloudEvents 1.0 specification (CNCF standard for event envelopes) and AsyncAPI 3.0 (the event-driven equivalent of OpenAPI). It defines the event type (reverse-DNS naming with version), payload structure (JSON Schema), versioning strategy, and routing metadata. Consumed by event producers, consumers, schema registries, and message routing infrastructure.

Not data_contract (producer-consumer SLA with obligations). Not event_stream (Kafka/Kinesis infrastructure configuration). Not openapi_spec (REST API contract).

## When to Use

| Scenario | Use event_schema? |
|----------|-----------------|
| Kafka message payload structure definition | YES |
| Webhook payload definition | YES |
| Domain event definition (OrderCreated, UserRegistered) | YES |
| EventBridge/SNS/PubSub event format | YES |
| Producer-consumer SLA with data quality obligations | NO -- use data_contract |
| Kafka topic config (partitions, retention) | NO -- use event_stream |
| REST API contract | NO -- use openapi_spec |

## Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| event_type | string | YES | Reverse-DNS + version: com.acme.order.created.v1 |
| schema_version | semver | YES | Schema version for consumer compatibility |
| source | URI string | YES | Producing service identifier |
| datacontenttype | "application/json" | YES | Payload MIME type |
| payload_schema | JSON Schema | YES | Structure of the data field |
| evolution_strategy | enum | REC | ADDITIVE_ONLY or VERSIONED_TYPE |

## CloudEvents Envelope

| Attribute | Description | Required |
|-----------|-------------|----------|
| specversion | "1.0" (always) | YES |
| id | UUID -- unique per event | YES |
| type | event_type (reverse-DNS + version) | YES |
| source | Producing service URI | YES |
| subject | Entity identifier (order-123) | REC |
| time | RFC3339 timestamp | REC |
| datacontenttype | "application/json" | YES |
| data | Payload matching payload_schema | YES |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No version in event_type | Consumer breaks on schema change | Always suffix .v{major} |
| Field list instead of JSON Schema | Not machine-validatable | Use proper JSON Schema |
| No required fields | Silent null handling bugs | Declare `required: [...]` |
| Conflating with data_contract | Schema is structure, not obligation | Separate artifacts |
| Deleting old event_type version | Breaks consumers mid-migration | Deprecate, never delete |

## Event Type Naming

| Pattern | Example |
|---------|---------|
| Correct: reverse-DNS + version | `com.acme.order.created.v1` |
| Acceptable: domain + version | `orders.created.v1` |
| Anti-pattern: no namespace | `OrderCreated` |
| Anti-pattern: no version | `com.acme.order.created` |

## Cross-Framework Map

| Standard/Tool | Equivalent | Notes |
|---------------|-----------|-------|
| CloudEvents 1.0 | event_schema | event_schema follows CloudEvents envelope |
| AsyncAPI 3.0 messages | event_schema | AsyncAPI .message = event_schema |
| Apache Avro | event_schema (data only) | Avro = payload schema only |
| Confluent Schema Registry | event_schema storage | Registry stores versioned schemas |

## Decision Tree

```
Need event payload schema?
  YES -> event_schema
    Include version in type?
      YES -> com.example.aggregate.event.v1
    Use JSON Schema for payload?
      YES -> define required fields, types, formats
    Breaking change needed?
      YES -> new event_type version (v2)
      NO  -> additive change, same type, bump schema_version
```

## Integration

- Produced by: state_machine (P12) -- state transition events
- Consumed by: agent (P02) -- agents react to events
- Stored in: event_stream (P09) -- Kafka/Kinesis topics
- Governed by: data_contract (P06) -- SLA on top of schema
- Pillar: P06 (Schema) -- machine-readable event contract
