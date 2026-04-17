---
id: p11_qg_connector
kind: quality_gate
pillar: P11
title: "Gate: connector"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "bidirectional service integration — connectors exchanging data with external services via REST, WebSocket, gRPC, or MQTT"
quality: 9.0
tags: [quality-gate, connector, P04, bidirectional, integration, data-transform]
tldr: "Pass/fail gate for connector artifacts: bidirectional flow coverage, transform rules, health check, and protocol selection rationale."
density_score: 0.92
llm_function: GOVERN
---
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
