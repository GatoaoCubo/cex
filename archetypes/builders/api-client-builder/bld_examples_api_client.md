---
kind: examples
id: bld_examples_client
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of client artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: api-client-builder
## Golden Example
INPUT: "Create client for a payment processing API with charges and refunds"
OUTPUT:
```yaml
id: p04_client_payment_gateway
kind: api_client
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
name: "Payment Gateway Client"
api: "Payment Gateway API"
base_url: "https://api.paygateway.com/v1"
auth: bearer
endpoints:
  - create_charge
  - get_charge
  - create_refund
  - list_transactions
quality: null
tags: [client, payment, api, P04]
tldr: "Payment gateway client: 4 endpoints, bearer auth, JSON, cursor pagination"
description: "Client consuming payment gateway API for charge creation, refunds, and transaction listing"
rate_limit: "100 req/min"
retry: "3 retries, exponential backoff (1s, 2s, 4s)"
timeout: "30s"
serialization: json
pagination: cursor
error_codes: ["400", "401", "402", "404", "429", "500"]
caching: "none (financial data)"
```
## Overview
Consumes payment gateway REST API for charge and refund operations.
Used by billing agents and transaction processing pipelines.
## Endpoints
### create_charge
POST /charges — Create a new payment charge.
Parameters:
- `amount` (integer, required): Amount in cents
- `currency` (string, required): ISO 4217 currency code
- `source` (string, required): Payment source token
Returns: {id, status, amount, currency, created} object
### get_charge
GET /charges/{id} — Retrieve charge by ID.
Parameters:
- `id` (string, required): Charge identifier
Returns: {id, status, amount, currency, refunded, metadata} object
### create_refund
POST /refunds — Refund a charge fully or partially.
Parameters:
- `charge_id` (string, required): Charge to refund
- `amount` (integer, optional): Partial amount; defaults to full
Returns: {id, charge_id, amount, status} object
### list_transactions
GET /transactions — List transactions with cursor pagination.
Parameters:
- `cursor` (string, optional): Pagination cursor
- `limit` (integer, optional): Max results; default 20, max 100
Returns: {data: [...], has_more, next_cursor} object
## Auth & Config
Base URL: https://api.paygateway.com/v1
Auth: Bearer token in `Authorization: Bearer {token}` header
Headers: `Content-Type: application/json`, `Idempotency-Key` on POST
## Error Handling
- 400: Bad request — validate params before retry
- 401: Auth failed — refresh token, retry once
- 402: Payment failed — surface to caller, no retry
- 429: Rate limited — backoff per Retry-After header
- 500: Server error — retry with exponential backoff
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_client_ pattern (H02 pass)
- kind: api_client (H04 pass)
- 19+ required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Endpoints, Auth & Config, Error Handling (H07 pass)
- endpoints list matches ## Endpoints names exactly (S03 pass)
- auth: bearer with base_url present (valid config) (S05 pass)
- tldr: 72 chars <= 160 (S01 pass)
- tags: 4 items, includes "client" (S02 pass)
- Each endpoint has method, path, parameters, return type (S06 pass)
## Anti-Example
INPUT: "Create client for weather API"
BAD OUTPUT:
```yaml
id: weather-client
kind: api_client
pillar: tools
name: Weather Client
endpoints: [weather, forecast]
auth: "yes"
quality: 8.5
tags: [weather]
```
Gets weather data from API.
## Endpoints
weather: gets current weather
forecast: gets forecast
FAILURES:
1. id: "weather-client" has hyphens and no `p04_client_` prefix -> H02 FAIL
2. kind: "api_client" not "client" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. Missing fields: api, base_url, version, created, updated, author, tldr -> H06 FAIL
6. auth: "yes" not a valid enum value -> S05 FAIL
7. tags: only 1 item, missing "client" -> S02 FAIL
8. Body missing ## Auth & Config, ## Error Handling sections -> H07 FAIL
