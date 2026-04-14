---
id: p11_qg_client
kind: quality_gate
pillar: P11
title: "Gate: client"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "API consumer definition — unidirectional clients for REST, GraphQL, or gRPC external services"
quality: 9.0
tags: [quality-gate, client, P04, api-consumer, auth-strategy, endpoint-mapping]
tldr: "Pass/fail gate for client artifacts: endpoint coverage, auth strategy declaration, retry/rate-limit policy, and unidirectional boundary."
density_score: 0.91
llm_function: GOVERN
---
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
