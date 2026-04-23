---
quality: 8.0
quality: 7.7
id: kc_openapi_spec
kind: knowledge_card
pillar: P01
title: "Knowledge Card -- OpenAPI Spec"
version: 1.0.0
tags: [knowledge, openapi_spec, oas3, api-contract, openapi-initiative]
related:
  - bld_schema_api_reference
  - bld_schema_client
  - bld_schema_integration_guide
  - bld_schema_tts_provider
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_bugloop
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_sandbox_spec
density_score: 1.0
updated: "2026-04-22"
---

# OpenAPI Spec

## Definition

An `openapi_spec` is a machine-readable API contract following the OpenAPI Specification 3.x (OAS 3.x), published by the OpenAPI Initiative (Linux Foundation). It formally defines a REST API surface: paths, HTTP operations, request/response schemas, security schemes, and server configurations. Consumed by code generators, mock servers, API gateways, validation middleware, and documentation tools.

Not api_reference (human-readable docs). Not api_client (SDK implementation). Not event_schema (async/event-driven APIs).

## When to Use

| Scenario | Use openapi_spec? |
|----------|-----------------|
| Define REST API surface for code generation | YES |
| Create API mocking and stub server | YES |
| Configure API gateway routing | YES |
| Generate SDK client libraries | YES |
| Document event-driven or async API | NO -- use event_schema |
| Write human-readable API guide | NO -- use api_reference |
| Define data exchange SLA | NO -- use data_contract |

## Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| openapi | string | YES | OAS version: "3.1.0" or "3.0.3" |
| info.title | string | YES | API human-readable name |
| info.version | string | YES | API version string |
| servers | array | YES | Base URL(s) for the API |
| paths | object | YES | Endpoints and their HTTP operations |
| components.schemas | object | REC | Reusable JSON Schema definitions |
| components.securitySchemes | object | REC | Auth method definitions |
| security | array | REC | Global security requirement |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Inline all schemas, no $ref | Duplication; schema drift on change | Use components.schemas + $ref |
| Missing error responses | Clients cannot handle failure cases | Define 400/401/404/500 minimum |
| No security scheme | API appears unauthenticated to tooling | Declare securitySchemes |
| Missing operationId | Code generators produce unusable method names | Always set camelCase operationId |
| OAS 2.0 (Swagger) format | Declining tooling support | Migrate to OAS 3.1.0 |

## Cross-Framework Map

| Tool/Standard | Equivalent | Notes |
|---------------|-----------|-------|
| Swagger 2.0 | openapi_spec (legacy) | Superseded by OAS 3.x |
| RAML 1.0 | openapi_spec (competitor) | Less tooling support |
| AsyncAPI 3.0 | event_schema | For event-driven APIs |
| GraphQL SDL | openapi_spec (different paradigm) | For graph APIs |
| gRPC .proto | openapi_spec (different transport) | For gRPC APIs |

## Decision Tree

```
REST API contract needed?
  YES -> openapi_spec
    Is it event-driven (WebSocket, Kafka)?
      YES -> event_schema (AsyncAPI format)
      NO  -> openapi_spec (OAS 3.x)
  NO:
    Human-readable API docs?
      YES -> api_reference
    SDK implementation?
      YES -> api_client
```

## Integration

- Consumed by: api_client (P04), api_reference (P01), api_gateway config (P09)
- References: data_contract (P06) for shared schema definitions
- Secured by: security schemes inline (OAuth2, apiKey, http bearer)
- Pillar: P06 (Schema) -- machine-readable contract for tooling consumption

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_api_reference]] | downstream | 0.48 |
| [[bld_schema_client]] | downstream | 0.38 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_tts_provider]] | downstream | 0.37 |
| [[bld_schema_reranker_config]] | downstream | 0.36 |
| [[bld_schema_benchmark_suite]] | downstream | 0.35 |
| [[bld_schema_bugloop]] | downstream | 0.35 |
| [[bld_schema_sandbox_config]] | downstream | 0.34 |
| [[bld_schema_usage_report]] | downstream | 0.34 |
| [[bld_schema_sandbox_spec]] | downstream | 0.34 |
