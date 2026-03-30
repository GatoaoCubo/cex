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
agent_node: edison
keywords: [connector, bidirectional, webhook, idempotency, health check, protocol, auth, data mapping, rate limit, transform]
---

## Summary
A client makes outbound calls only. A connector makes outbound calls and receives inbound calls (webhooks, callbacks, event streams). This creates two failure modes unique to connectors: duplicate processing from webhook retries, and silent failure when the inbound endpoint goes offline. Building a client when a connector is needed forces idempotency and health monitoring to be retrofitted — consistently more expensive than specifying them upfront.
## Pattern
**Use connector for bidirectional; client for outbound-only. Declare idempotency and health_check at spec time.**
Pattern selection: client = outbound HTTP calls + synchronous responses only. Connector = outbound calls AND inbound calls (webhooks, event subscriptions, callbacks).
Idempotency strategy for inbound paths:
- Extract unique event ID (most providers include event_id or X-Request-ID)
- Check against deduplication store before processing
- Acknowledge immediately (return 200); process asynchronously
- Retain event IDs for 24+ hours (covers all major provider retry windows)
Health check (required):
- Outbound: ping external health endpoint or make a minimal authenticated request
- Inbound: verify webhook endpoint reachable + returns expected challenge response
- Frequency: every 60s; alert after 3 consecutive failures
- Must be a named endpoint in the spec, not a comment
Direction annotation: every endpoint labeled inbound or outbound. Undirected endpoints make the data mapping section ambiguous.
## Anti-Pattern
- Missing `## Data Mapping` section (required; inbound field → internal schema, outbound internal → external schema).
- No idempotency on inbound endpoints (webhook retries create duplicates).
- No health_check (silent failure; detection falls to downstream data quality).
- protocol: rest for a streaming service (use websocket or grpc).
- Endpoints without direction annotation (S04 fail).
- No inbound endpoints but built as connector — build a client instead.
- Missing retry on outbound paths (exponential backoff, retryable 5xx only).
## Context
Bidirectional vs. unidirectional is the first design question. Common patterns:
- Request-Webhook (rest, outbound + inbound): Stripe, Shopify, Twilio
- Event Stream (websocket, full-duplex): Slack, Discord
- Two-Way Sync (rest, outbound + inbound): CRM to ERP
- Pub-Sub (mqtt/amqp): IoT devices, message brokers
