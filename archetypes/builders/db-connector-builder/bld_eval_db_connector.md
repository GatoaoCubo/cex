---
kind: quality_gate
id: p11_qg_connector
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of connector artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: connector"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, connector, P04, bidirectional, integration, data-transform]
tldr: "Pass/fail gate for connector artifacts: bidirectional flow coverage, transform rules, health check, and protocol selection rationale."
domain: "bidirectional service integration — connectors exchanging data with external services via REST, WebSocket, gRPC, or MQTT"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.92
related:
  - p11_qg_client
  - bld_instruction_connector
  - db-connector-builder
  - bld_collaboration_connector
  - p03_sp_connector_builder
  - p10_lr_connector_builder
  - bld_examples_connector
  - bld_architecture_connector
  - bld_schema_connector
  - bld_knowledge_card_connector
---

## Quality Gate

# Gate: connector

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
## Definition
| Field | Value |
|---|---|
| metric | connector artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: db_connector` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_connector` but file is `other_connector.md` |
| H04 | Kind equals literal `connector` | `kind: client` or `kind: integration` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `service`, `protocol`, or `auth_strategy` |
| H07 | Both inbound and outbound directions represented | Only inbound or only outbound endpoints defined — that is a client, not a connector |
| H08 | Protocol is one of: rest, websocket, grpc, mqtt | `protocol: costm` without documented justification |
| H09 | Health check strategy defined | `health_check` field absent; connector must document liveness verification |
| H10 | Transform rules defined for at least one endpoint | Connector passes raw data without any mapping — transforms must be explicit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Inbound endpoint completeness | 1.0 | All data the system receives from the external service is documented |
| Outbound endpoint completeness | 1.0 | All data the system sends to the external service is documented |
| Transform rule precision | 1.0 | Field mappings specify source field, target field, and transformation logic |
| Auth strategy depth | 1.0 | Auth scheme covers token lifecycle, rotation, and failure handling |
| Health check actionability | 0.5 | Health check endpoint and expected response documented; failure action defined |
| Retry policy | 1.0 | Retry conditions, max attempts, backoff strategy defined per endpoint direction |
| Rate limit compliance | 0.5 | External service rate limits documented; throttling strategy described |
| Logging strategy | 0.5 | Which events are logged (connection errors, transform failures, auth events) stated |
| Protocol justification | 1.0 | Protocol choice justified against alternatives for the declared use case |
| Failure isolation | 1.0 | Inbound failure does not cascade to outbound; isolation mechanism documented |
| Boundary clarity | 1.0 | Explicitly not a client (unidirectional) or MCP server — bidirectionality contract stated |
| Domain specificity | 1.0 | Endpoints, transforms, and protocols specific to the declared external service |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Connector for a third-party service whose webhook schema changes without versioning — inbound schema unstable |
| approver | Integration owner with written acknowledgment of unstable upstream schema |
| audit_trail | Bypass reason, external service name, and schema instability report link in frontmatter comment |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
