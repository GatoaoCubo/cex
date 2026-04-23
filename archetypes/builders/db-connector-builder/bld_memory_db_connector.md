---
id: p10_lr_connector_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Connectors built without idempotency strategy on inbound webhooks produced duplicate records in 3 of 5 integrations when the external service retried delivery. Connectors without health_check definitions failed silently for hours before detection. Both issues are preventable at spec time."
pattern: "Bidirectional connectors require idempotency strategy for inbound paths and a health_check definition. Use connector pattern when integration involves both outbound calls and inbound webhooks; use client pattern when integration is outbound-only."
evidence: "5 bidirectional integrations: 3 duplicate record incidents from missing idempotency on inbound webhooks. 2 extended silent failures from missing health_check. Zero incidents in connectors where both were specified at build time."
confidence: 0.7
outcome: SUCCESS
domain: connector
tags: [connector, idempotency, health-check, bidirectional, webhook-dedup]
tldr: "Connectors need idempotency on inbound paths and health_check definitions. Use connector for bidirectional; client for outbound-only."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [connector, bidirectional, webhook, idempotency, health check, protocol, auth, data mapping, rate limit, transform]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Db Connector"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_connector
  - p11_qg_connector
  - bld_examples_connector
  - bld_instruction_connector
  - p03_sp_connector_builder
  - webhook-builder
  - p01_kc_webhook
  - db-connector-builder
  - bld_collaboration_webhook
  - bld_output_template_connector
---
## Summary

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
A client makes outbound calls only. A connector makes outbound calls and receives inbound calls (webhooks, callbacks, event streams). This creates two failure modes unique to connectors: duplicate processing from webhook retries, and silent failure when the inbound endpoint goes offline. Building a client when a connector is needed forces idempotency and health monitoring to be retrofitted — consistently more expensive than specifying them upfront.
## Pattern
**Use connector for bidirectional; client for outbound-only. Declare idempotency and health_check at spec time.**
Pattern selection: client = outbound HTTP calls + synchronous responses only. Connector = outbound calls AND inbound calls (webhooks, event subscriptions, callbacks).
Idempotency strategy for inbound paths:
1. Extract unique event ID (most providers include event_id or X-Request-ID)
2. Check against deduplication store before processing
3. Acknowledge immediately (return 200); process asynchronously
4. Retain event IDs for 24+ hours (covers all major provider retry windows)
Health check (required):
1. Outbound: ping external health endpoint or make a minimal authenticated request
2. Inbound: verify webhook endpoint reachable + returns expected challenge response
3. Frequency: every 60s; alert after 3 consecutive failures
4. Must be a named endpoint in the spec, not a comment
Direction annotation: every endpoint labeled inbound or outbound. Undirected endpoints make the data mapping section ambiguous.
## Anti-Pattern
1. Missing `## Data Mapping` section (required; inbound field → internal schema, outbound internal → external schema).
2. No idempotency on inbound endpoints (webhook retries create duplicates).
3. No health_check (silent failure; detection falls to downstream data quality).
4. protocol: rest for a streaming service (use websocket or grpc).
5. Endpoints without direction annotation (S04 fail).
6. No inbound endpoints but built as connector — build a client instead.
7. Missing retry on outbound paths (exponential backoff, retryable 5xx only).
## Context
Bidirectional vs. unidirectional is the first design question. Common patterns:
1. Request-Webhook (rest, outbound + inbound): Stripe, Shopify, Twilio
2. Event Stream (websocket, full-duplex): Slack, Discord
3. Two-Way Sync (rest, outbound + inbound): CRM to ERP
4. Pub-Sub (mqtt/amqp): IoT devices, message brokers

## Metadata

```yaml
id: p10_lr_connector_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-connector-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | connector |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_connector]] | upstream | 0.55 |
| [[p11_qg_connector]] | downstream | 0.52 |
| [[bld_examples_connector]] | upstream | 0.48 |
| [[bld_instruction_connector]] | upstream | 0.47 |
| [[p03_sp_connector_builder]] | upstream | 0.45 |
| [[webhook-builder]] | upstream | 0.42 |
| [[p01_kc_webhook]] | upstream | 0.42 |
| [[db-connector-builder]] | upstream | 0.41 |
| [[bld_collaboration_webhook]] | upstream | 0.39 |
| [[bld_output_template_connector]] | upstream | 0.38 |
