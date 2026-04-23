---
kind: quality_gate
id: p11_qg_client
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of client artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: client"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, client, P04, api-consumer, auth-strategy, endpoint-mapping]
tldr: "Pass/fail gate for client artifacts: endpoint coverage, auth strategy declaration, retry/rate-limit policy, and unidirectional boundary."
domain: "API consumer definition — unidirectional clients for REST, GraphQL, or gRPC external services"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - api-client-builder
  - bld_instruction_client
  - p11_qg_connector
  - bld_collaboration_client
  - bld_examples_client
  - p03_sp_client_builder
  - bld_schema_client
  - bld_architecture_client
  - bld_knowledge_card_client
  - bld_tools_client
---

## Quality Gate

# Gate: client
## Definition
| Field | Value |
|---|---|
| metric | client artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: api_client` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_client` but file is `other_client.md` |
| H04 | Kind equals literal `client` | `kind: connector` or `kind: integration` or any other value |
| H05 | Quality field is null | `quality: 9.0` or any non-null value |
| H06 | All required fields present | Missing `base_url`, `auth_strategy`, or `endpoints` |
| H07 | At least one endpoint defined | `endpoints: []` or endpoints field absent |
| H08 | Auth strategy is one of: api_key, bearer, oauth2, basic, none | `auth_strategy: costm` without documented scheme |
| H09 | Each endpoint has HTTP method and path | Endpoint missing `method` or `path` field |
| H10 | Client is unidirectional (consume-only) | Client defines push, webhook receipt, or server-side event emission |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Endpoint completeness | 1.0 | All endpoints needed for the declared use case are listed |
| Return type documentation | 1.0 | Each endpoint declares return type or response schema reference |
| Parameter documentation | 1.0 | Path params, query params, and request body documented per endpoint |
| Rate limit handling | 1.0 | Rate limit (requests/sec or requests/day) declared and retry-after strategy described |
| Retry policy | 1.0 | Retry conditions (which HTTP codes trigger retry), max retries, and backoff defined |
| Timeout configuration | 0.5 | Connection timeout and read timeout values documented |
| Pagination pattern | 0.5 | Pagination strategy (cursor, offset, page) documented for list endpoints |
| Serialization format | 0.5 | Request/response serialization format declared (json, xml, protobuf) |
| Error response mapping | 1.0 | HTTP error codes mapped to client exception types or error structs |
| Auth token lifecycle | 0.5 | Token expiry, refresh, and storage strategy documented |
| Boundary clarity | 1.0 | Explicitly not a connector or MCP server — consume-only contract stated |
| Domain specificity | 1.0 | Endpoints and parameters specific to the external service being consumed |
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
| conditions | Client targeting an unstable third-party API under active change — endpoint schema not yet finalized |
| approver | Tech lead acknowledgment that API contract is pending stabilization |
| audit_trail | Bypass reason with target API version and expected stabilization date in frontmatter comment |
| expiry | 30d — client must reach >= 7.0 once upstream API stabilizes |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |

## Examples

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
quality: 8.8
tags: [client, payment, api, P04]
tldr: "Payment gateway client: 4 endpoints, bearer auth, JSON, cursor pagetion"
description: "Client consuming payment gateway API for charge creation, refunds, and transaction listing"
rate_limit: "100 req/min"
retry: "3 retries, exponential backoff (1s, 2s, 4s)"
timeout: "30s"
serialization: json
pagetion: cursor
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
GET /transactions — List transactions with cursor pagetion.
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
