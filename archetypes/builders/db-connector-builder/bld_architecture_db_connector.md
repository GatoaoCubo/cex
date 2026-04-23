---
kind: architecture
id: bld_architecture_connector
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of connector — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Db Connector"
version: "1.0.0"
author: n03_builder
tags: [db_connector, builder, examples]
tldr: "Golden and anti-examples for db connector construction, demonstrating ideal structure and common pitfalls."
domain: "db connector construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - db-connector-builder
  - p11_qg_connector
  - bld_architecture_client
  - bld_collaboration_connector
  - p03_sp_connector_builder
  - bld_instruction_connector
  - p04_db_postgres
  - bld_examples_connector
  - p10_lr_connector_builder
  - bld_knowledge_card_connector
---

## Component Inventory

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
| Name | Role | Owner | Status |
|------|------|-------|--------|
| outbound_endpoint | Sends data to external service — method, path, payload schema | connector | required |
| inbound_endpoint | Receives data from external service — webhook path, event schema | connector | required |
| protocol | Wire protocol for the integration (REST, WebSocket, gRPC, MQTT) | connector | required |
| auth_strategy | Authentication for both directions (API key, OAuth2, mTLS, HMAC) | connector | required |
| data_mapping | Transform rules converting internal schema to external format and back | connector | required |
| health_check | Periodic probe confirming the external service is reachable | connector | required |
| retry_policy | Backoff + max_attempts for failed outbound requests | connector | required |
| rate_limit | Throttle policy applied to outbound calls | connector | optional |
| env_config | Secrets, service URLs, and credentials from environment | P09 | external |
| guardrail | Auth and rate enforcement constraints | P11 | external |
| agent | Caller that triggers outbound operations or handles inbound events | P02 | consumer |
| workflow | Orchestrator that sequences connector calls in a pipeline | P12 | consumer |
## Dependency Graph
```
env_config         --produces-->  auth_strategy
env_config         --produces-->  outbound_endpoint
guardrail          --produces-->  rate_limit
outbound_endpoint  --depends-->   protocol
outbound_endpoint  --depends-->   auth_strategy
outbound_endpoint  --depends-->   data_mapping
inbound_endpoint   --depends-->   protocol
inbound_endpoint   --depends-->   auth_strategy
inbound_endpoint   --depends-->   data_mapping
health_check       --depends-->   outbound_endpoint
retry_policy       --depends-->   outbound_endpoint
outbound_endpoint  <-->           inbound_endpoint
agent              --depends-->   outbound_endpoint
agent              --depends-->   inbound_endpoint
workflow           --depends-->   outbound_endpoint
```
| From | To | Type | Data |
|------|----|------|------|
| env_config | auth_strategy | produces | credentials injected at runtime |
| guardrail | rate_limit | produces | throttle policy |
| outbound_endpoint | protocol, auth, mapping | depends | wire+auth+transform |
| inbound_endpoint | protocol, auth, mapping | depends | wire+auth+transform |
| health_check | outbound_endpoint | depends | liveness probe |
| retry_policy | outbound_endpoint | depends | retry on failure |
| agent/workflow | endpoints | depends | runtime callers |
## Boundary Table
| connector IS | connector IS NOT |
|-------------|-----------------|
| Bidirectional integration (send+receive) | Unidirectional API consumer (api_client) |
| Data mapping between schemas | HTML/DOM extractor (scraper) |
| Webhooks, streams, pub/sub | MCP protocol server (mcp_server) |
| Health check and liveness | Phased capability (skill) |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Search data in database | db_connector | retriever | retriever=vector/keyword; db_connector=structured SQL |
| Call external REST API | db_connector | api_client | api_client=unidirectional; db_connector=data store access |
| Receive event from service | db_connector | webhook | webhook=HTTP event; db_connector=query/execute |
## Decision Tree
- Structured data query (SQL)? → db_connector
- Vector/keyword search? → retriever
- External API call? → api_client
- Receive inbound events? → webhook
## Neighbor Comparison
| Dim | db_connector | retriever | Diff |
|---|---|---|---|
| Query | SQL/GraphQL | Vector similarity | Different query language |
| Data | Structured rows | Unstructured chunks | Different data model |
| Index | B-tree/hash | HNSW/IVF | Different index types |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[db-connector-builder]] | upstream | 0.44 |
| [[p11_qg_connector]] | downstream | 0.43 |
| [[bld_architecture_client]] | sibling | 0.41 |
| [[bld_collaboration_connector]] | downstream | 0.41 |
| [[p03_sp_connector_builder]] | upstream | 0.40 |
| [[bld_instruction_connector]] | upstream | 0.35 |
| [[p04_db_postgres]] | upstream | 0.33 |
| [[bld_examples_connector]] | upstream | 0.33 |
| [[p10_lr_connector_builder]] | downstream | 0.31 |
| [[bld_knowledge_card_connector]] | upstream | 0.31 |
