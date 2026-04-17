---
kind: knowledge_card
id: bld_knowledge_card_connector
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for connector production — bidirectional service integration
sources: Enterprise Integration Patterns (Hohpe 2003), Stripe webhooks, gRPC, MQTT
quality: 9.1
title: "Knowledge Card Db Connector"
version: "1.0.0"
author: n03_builder
tags: [db_connector, builder, examples]
tldr: "Golden and anti-examples for db connector construction, demonstrating ideal structure and common pitfalls."
domain: "db connector construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: connector

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
## Executive Summary
Connectors are bidirectional integration bridges that both send and receive data with external services via REST+webhooks, WebSocket, gRPC, or MQTT. Unlike clients (request/response only), connectors handle inbound events, two-way sync, and data transformation between systems. They define protocol, auth, endpoints, transforms, and health checks.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Direction | Bidirectional (send + receive) |
| Protocols | REST+webhook, WebSocket, gRPC, MQTT |
| Frontmatter fields | 20+ |
| Quality gates | 8 HARD + 12 SOFT |
| Key sections | endpoints, auth, transforms, health_check |
## Patterns
- **Protocol selection**: match the external service's integration model
| Protocol | Pattern | Use case |
|----------|---------|----------|
| REST+webhook | Outbound request + inbound callback | Stripe payments, SaaS notifications |
| WebSocket | Full-duplex persistent connection | Real-time chat, price feeds, events |
| gRPC | Bidirectional streaming | Microservice-to-microservice, high throughput |
| MQTT | Publish/subscribe topics | IoT devices, lightweight messaging |
- **Data transformation**: field renaming, type coercion, format conversion between systems — define per direction (inbound/outbound)
- **Idempotency**: deduplicate inbound events by event_id — prevents double-processing on webhook retries
- **Health checks**: periodic probes to verify external service connectivity and response time
- **Retry with backoff**: exponential backoff + jitter for transient failures; circuit breaker for persistent failures
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Using client for bidirectional needs | Client cannot receive webhooks or events |
| Forcing REST on streaming API | Polling wastes resources; use WebSocket/gRPC |
| No idempotency on inbound events | Webhook retries cause duplicate processing |
| Missing health check | Dead connection discovered only on failure |
| Untyped transforms | Data corruption when field types mismatch |
| No circuit breaker | Cascading failures when external service is down |
## Application
1. Identify service and protocol: REST+webhook, WebSocket, gRPC, or MQTT
2. Define auth strategy: API key, OAuth, mutual TLS, or token
3. Map endpoints: outbound (requests) and inbound (webhooks/events) with data types
4. Define transforms: field mapping per direction (inbound and outbound)
5. Configure resilience: health check, retry policy, circuit breaker, idempotency
6. Validate: test both directions — outbound request and inbound event handling
## References
- Hohpe & Woolf 2003: Enterprise Integration Patterns
- Stripe: webhook best forctices and event handling
- gRPC: bidirectional streaming documentation
- MQTT: pub/sub messaging protocol specification
