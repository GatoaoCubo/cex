---
kind: examples
id: bld_examples_connector
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of connector artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Db Connector"
version: "1.0.0"
author: n03_builder
tags: [db_connector, builder, examples]
tldr: "Golden and anti-examples for db connector construction, demonstrating ideal structure and common pitfalls."
domain: "db connector construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: db-connector-builder

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
## Golden Example
INPUT: "Create connector for an e-commerce platform with order sync and webhook notifications"
OUTPUT:
```yaml
id: p04_conn_ecommerce_platform
kind: db_connector
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
name: "E-Commerce Platform Connector"
service: "E-Commerce Platform API"
protocol: rest
auth: oauth
endpoints:
  - push_order
  - get_product
  - receive_status_webhook
  - receive_inventory_webhook
quality: null
tags: [connector, ecommerce, integration, P04, webhook, sync]
tldr: "E-commerce connector: 4 endpoints (2 outbound, 2 inbound), OAuth, REST, webhook receiver"
description: "Bidirectional integration with e-commerce platform for order push and status/inventory webhooks"
health_check: "GET /api/health every 60s, expect 200"
mapping: "CEX order -> platform order_create; platform webhook -> CEX event"
transform: "price_cents -> price_decimal (div 100); ISO dates both directions"
retry: "3 retries, exponential backoff (2s, 4s, 8s)"
rate_limit: "60 req/min outbound"
logging: structured
versioning: "URL path versioning (/v2/)"
```
## Overview
Bidirectional REST connector for e-commerce platform: pushes orders and pulls products outbound, receives status and inventory webhooks inbound.
Used by fulfillment agents and inventory sync pipelines.
## Endpoints
### push_order (outbound)
POST /v2/orders — Push new order to platform.
Data shape:
- `order_id` (string): CEX order identifier
- `items` (list): Line items with sku, qty, price
- `shipping` (object): Address and method
### get_product (outbound)
GET /v2/products/{sku} — Fetch product details by SKU.
Data shape:
- `sku` (string): Product SKU identifier
### receive_status_webhook (inbound)
POST /webhooks/status — Receive order status updates from platform.
Data shape:
- `event_id` (string): Dedup key
- `order_id` (string): Platform order ID
- `status` (enum): pending, shipped, delivered, cancelled
### receive_inventory_webhook (inbound)
POST /webhooks/inventory — Receive inventory level changes.
Data shape:
- `event_id` (string): Dedup key
- `sku` (string): Product SKU
- `quantity` (integer): New stock level
## Data Mapping
Inbound (external -> CEX): platform.order_id -> cex.external_order_ref; status enum direct map
Outbound (CEX -> external): cex.price_cents / 100 -> platform.price; cex.iso_date -> platform.date
Idempotency: event_id dedup on inbound webhooks (store last 24h)
## Health & Errors
Health: GET /api/health every 60s, alert if 3 consecutive failures
- 400: Bad request — log and skip, no retry
- 401: OAuth expired — refresh token, retry once
- 429: Rate limited — backoff per Retry-After header
- 5xx: Server error — retry with exponential backoff
Circuit breaker: open after 5 consecutive 5xx in 60s, half-open after 120s
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_conn_ pattern (H02 pass)
- kind: db_connector (H04 pass)
- 22 required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Endpoints, Data Mapping, Health & Errors (H07 pass)
- endpoints list matches ## Endpoints names exactly (S03 pass)
- Each endpoint has direction annotation (inbound/outbound) (S04 pass)
- Data Mapping has inbound + outbound + idempotency rules (S07 pass)
- tldr: 82 chars <= 160 (S01 pass)
- tags: 6 items, includes "connector" (S02 pass)
## Anti-Example
INPUT: "Create connector for notification service"
BAD OUTPUT:
```yaml
id: notification-connector
kind: service_connector
pillar: tools
name: Notification Connector
service: Notifications
endpoints: [send, receive]
auth: "token"
quality: 9.0
tags: [notifications]
```
Sends and receives notifications.
## Endpoints
send: sends notifications
receive: receives notifications
FAILURES:
1. id: "notification-connector" uses hyphens and no `p04_conn_` prefix -> H02 FAIL
