---
kind: architecture
id: bld_architecture_openapi_spec
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of openapi_spec -- inventory, dependencies, and architectural position
quality: 8.8
title: "Architecture OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, architecture]
tldr: "Component map: info, servers, paths, components (schemas/securitySchemes), tags. External: api_client, api_reference."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p03_sp_api_reference_builder
  - bld_output_template_api_reference
  - bld_instruction_api_reference
  - bld_examples_api_reference
  - kc_api_reference
  - api-reference-builder
  - bld_knowledge_card_api_reference
  - bld_instruction_component_map
  - api-client-builder
  - p01_kc_api_client
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| info | API metadata (title, version, description, contact) | openapi_spec | required |
| servers | Base URL(s) and server variables | openapi_spec | required |
| paths | Path items and HTTP operations | openapi_spec | required |
| components.schemas | Reusable JSON Schema definitions | openapi_spec | recommended |
| components.securitySchemes | Auth method definitions (OAuth2, apiKey, http) | openapi_spec | recommended |
| components.parameters | Reusable parameter definitions | openapi_spec | optional |
| components.responses | Reusable response definitions | openapi_spec | optional |
| components.examples | Reusable example payloads | openapi_spec | optional |
| security | Global security requirement | openapi_spec | recommended |
| tags | Operation grouping/documentation | openapi_spec | optional |
| externalDocs | Link to external documentation | openapi_spec | optional |
| api_reference | Human-readable documentation (Redoc, Swagger UI) | P01 (separate kind) | consumer |
| api_client | SDK implementation from this spec | P04 (separate kind) | consumer |
| data_contract | Producer-consumer SLA (separate concern) | P06 (separate kind) | external |

## Structure Diagram

```
openapi: "3.1.0"
  |-- info           (title, version, description)
  |-- servers        (base URLs)
  |-- paths          (endpoints)
  |     |-- {path}
  |           |-- {method}: get | post | put | patch | delete
  |                 |-- operationId, summary, description
  |                 |-- parameters (path, query, header, cookie)
  |                 |-- requestBody (content, schema ref)
  |                 |-- responses (200, 400, 401, 404, 500)
  |                 |-- security (per-operation override)
  |                 |-- tags
  |-- components
  |     |-- schemas          (reusable JSON Schema)
  |     |-- securitySchemes  (OAuth2, apiKey, http)
  |     |-- parameters       (reusable params)
  |     |-- responses        (reusable responses)
  |-- security (global requirement)
  |-- tags (grouping)
```

## Boundary Table

| openapi_spec IS | openapi_spec IS NOT |
|-----------------|---------------------|
| Machine-readable OAS 3.x contract | Human-readable API docs (that is api_reference) |
| Path/operation/schema definition | SDK or client code generation target only (that is api_client) |
| Security scheme declaration | Producer-consumer data SLA (that is data_contract) |
| REST API surface description | Event-driven payload schema (that is event_schema) |
| Tooling input (codegen, mocking, validation) | Implementation code (that is api_client) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| metadata | info, servers, tags | Identify and locate the API |
| surface | paths, operations | Define what the API does |
| data | components.schemas | Define what the API accepts and returns |
| security | components.securitySchemes, security | Define how the API is protected |
| reuse | components.parameters, responses, examples | DRY -- share definitions across operations |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_api_reference_builder]] | upstream | 0.25 |
| [[bld_output_template_api_reference]] | upstream | 0.24 |
| [[bld_instruction_api_reference]] | upstream | 0.23 |
| [[bld_examples_api_reference]] | upstream | 0.22 |
| [[kc_api_reference]] | upstream | 0.22 |
| [[api-reference-builder]] | upstream | 0.20 |
| [[bld_knowledge_card_api_reference]] | upstream | 0.19 |
| [[bld_instruction_component_map]] | upstream | 0.19 |
| [[api-client-builder]] | upstream | 0.18 |
| [[p01_kc_api_client]] | upstream | 0.18 |
