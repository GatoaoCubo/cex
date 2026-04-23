---
id: bld_knowledge_card_openapi_spec
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 8.8
title: "OpenAPI Spec Builder -- Knowledge Card"
llm_function: INJECT
tags: [openapi_spec, api-contract, oas3, P06, openapi-initiative]
tldr: "openapi_spec: machine-readable OAS 3.x API contract defining paths, schemas, and security. NOT api_reference (human docs) nor api_client (SDK)."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
related:
  - bld_schema_api_reference
  - bld_schema_client
  - bld_schema_integration_guide
  - bld_schema_tts_provider
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_bugloop
  - bld_schema_sandbox_spec
  - bld_schema_quickstart_guide
---

# Knowledge Card: openapi_spec

## Definition
An `openapi_spec` is a machine-readable API contract following the OpenAPI Specification 3.x
(OAS 3.x) standard, published by the OpenAPI Initiative (Linux Foundation). It defines the
surface of a REST API: paths, HTTP operations, request/response schemas, and security schemes.
Consumed by code generators, mock servers, validation middleware, and API documentation tools.

## Origin
- **Swagger 2.0** (2014): SmartBear, later donated to OpenAPI Initiative
- **OAS 3.0** (2017): OpenAPI Initiative, major restructure from Swagger 2
- **OAS 3.1** (2021): Full JSON Schema alignment, webhooks support
- **CEX pillar**: P06 (Schema) -- machine-readable contracts consumed by tooling

## Key Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| openapi | string | YES | OAS version: "3.1.0" |
| info.title | string | YES | API name |
| info.version | string | YES | API version (semver or date-based) |
| servers | array | YES | Base URL(s) for the API |
| paths | object | YES | API endpoints and their operations |
| components.schemas | object | REC | Reusable JSON Schema definitions |
| components.securitySchemes | object | REC | Auth method definitions |
| security | array | OPT | Global security requirement |
| tags | array | OPT | Operation grouping |

## When to Use

| Scenario | Use openapi_spec? |
|----------|-------------------|
| Define REST API surface for code generation | YES |
| Create API mocking / stub server | YES |
| Configure API gateway routing rules | YES |
| Generate SDK client libraries (Python, JS, Go) | YES |
| Document event-driven / async API | NO -- use event_schema + AsyncAPI |
| Define producer-consumer data SLA | NO -- use data_contract |
| Write human-readable API guide | NO -- use api_reference |

## Cross-Framework Map

| Tool/Standard | Equivalent | Notes |
|---------------|-----------|-------|
| Swagger 2.0 | openapi_spec (legacy) | Superseded by OAS 3.x |
| RAML 1.0 | openapi_spec (competitor) | Less tooling support |
| API Blueprint | openapi_spec (competitor) | Markdown-based, discontinued |
| GraphQL SDL | openapi_spec (different paradigm) | For graph APIs, not REST |
| gRPC .proto | openapi_spec (different transport) | For gRPC APIs |
| JSON:API | openapi_spec (constraint layer) | Can be described via OAS |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Inline all schemas, no $ref | Duplication, drift, hard to maintain | Use components.schemas + $ref |
| Missing error responses | Clients cannot handle failures | Define 400/401/404/500 for every operation |
| No security scheme | API appears unauthenticated to tools | Declare securitySchemes + global security |
| Using OAS 2 (Swagger) format | Missing $ref features, less JSON Schema support | Migrate to OAS 3.1 |
| Mixing documentation prose in spec | Clutters machine-readable contract | Move prose to api_reference |

## Decision Tree

```
Need to describe a REST API?
  |-- YES: openapi_spec
  |       Is it event-driven (Kafka, WebSocket)?
  |         YES -> event_schema (AsyncAPI format)
  |         NO  -> openapi_spec (OAS 3.x)
  |-- NO:
       Is it a data exchange SLA?
         YES -> data_contract
         Is it for code gen only?
           YES -> api_client (SDK)
```

## Integration Graph

```
openapi_spec (P06)
  |
  |-- consumed by --> api_client (P04) -- code generation
  |-- consumed by --> api_reference (P01) -- human docs
  |-- consumed by --> api_gateway config (P09) -- routing rules
  |-- consumed by --> mock_server (P05) -- testing stubs
  |-- references --> data_contract (P06) -- schema definitions
  |-- secured by --> security scheme (inline) -- OAuth2/apiKey
```

## OAS 3.x Structure Summary

```yaml
openapi: "3.1.0"
info:
  title: "My API"
  version: "1.0.0"
servers:
  - url: "https://api.example.com/v1"
paths:
  /users/{id}:
    get:
      operationId: getUser
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: User found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/User"
components:
  schemas:
    User:
      type: object
      properties:
        id: {type: string}
        name: {type: string}
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
security:
  - bearerAuth: []
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_api_reference]] | downstream | 0.44 |
| [[bld_schema_client]] | downstream | 0.34 |
| [[bld_schema_integration_guide]] | downstream | 0.33 |
| [[bld_schema_tts_provider]] | downstream | 0.33 |
| [[bld_schema_reranker_config]] | downstream | 0.31 |
| [[bld_schema_dataset_card]] | downstream | 0.30 |
| [[bld_schema_usage_report]] | downstream | 0.30 |
| [[bld_schema_bugloop]] | downstream | 0.30 |
| [[bld_schema_sandbox_spec]] | downstream | 0.29 |
| [[bld_schema_quickstart_guide]] | downstream | 0.29 |
