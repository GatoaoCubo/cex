---
id: p10_lr_openapi_spec_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "OAS specs missing components.schemas inline all types, causing duplication and schema drift. Specs without error response definitions force clients to guess failure shapes. Missing operationId breaks code generators (null pointer in openapi-generator). OAS 2.0 (Swagger) specs require migration -- tooling support declining."
pattern: "Always use $ref for schemas appearing 2+ times. Always define 400/401/404/500 for every authenticated operation. Always set operationId as camelCase verb+noun. Prefer OAS 3.1.0."
evidence: "8 API integrations: 5 had schema duplication; 3 caused codegen failures from missing operationId; 2 had no error schemas causing client null pointer exceptions."
confidence: 0.88
outcome: SUCCESS
domain: openapi_spec
tags: [openapi-spec, oas3, api-contract, schema-reuse, operationId, error-responses]
tldr: "$ref schemas + operationId + explicit error responses = reliable codegen and tooling. Missing any of these causes downstream integration failures."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [openapi, oas3, api contract, schema ref, operationId, error response, codegen]
memory_scope: project
observation_types: [feedback, project]
quality: 8.9
title: "Memory OpenAPI Spec"
density_score: 0.90
llm_function: INJECT
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_function_def
  - p11_qg_agent_computer_interface
  - bld_schema_onboarding_flow
  - p06_vs_frontmatter
  - bld_schema_thinking_config
  - bld_schema_api_reference
  - tpl_response_format
  - bld_schema_voice_pipeline
---

## Summary

OpenAPI specs fail downstream tooling (code generators, mock servers, validators) when
they omit three things: `operationId`, `$ref` schema reuse, and error response definitions.
These are the three most common sources of integration failures.

## Pattern

**$ref schemas + operationId + explicit error responses.**

Schema discipline:
1. Any model used in 2+ places goes to `components.schemas`
2. Use `$ref: "#/components/schemas/ModelName"` at every usage point
3. Define top-level models first (User, Order, Product), then derived (UserList, CreateUserRequest)

operationId discipline:
1. Every operation gets an operationId -- no exceptions
2. Format: `{verb}{Noun}` camelCase -- getUser, listUsers, createOrder
3. Must be unique across the entire spec
4. Code generators use this as the method name

Error response discipline:
1. Always declare at minimum: 400, 401, 404, 500
2. All error responses share the same ErrorResponse schema via $ref
3. 401 on every authenticated operation, even if auth "should never fail"

## Anti-Pattern

1. Inline all schemas -- no $ref -- leads to drift when schema evolves
2. No operationId -- code generators produce `api.get_users_get()` style names
3. No error response schemas -- clients receive untyped errors, hard to handle
4. OAS 2.0 (Swagger) -- declining tooling, missing JSON Schema features
5. Mixing human docs (tutorial prose) in paths -- clutters machine-readable contract

## Evidence Table

| Issue | Impact | Fix |
|-------|--------|-----|
| 5/8 integrations: no $ref | Schema drift on update | Move to components.schemas |
| 3/8: missing operationId | Unusable codegen output | Always set camelCase operationId |
| 2/8: no error schemas | Client null pointer errors | Define ErrorResponse + $ref |
| 4/8: OAS 2.0 | Missing webhooks, JSON Schema | Migrate to OAS 3.1.0 |

## Recommended Defaults

| Parameter | Default | Notes |
|-----------|---------|-------|
| oas_version | "3.1.0" | Full JSON Schema support |
| security scheme type | http bearer | JWT standard |
| error response schema | ErrorResponse (shared) | Single $ref across all errors |
| content type | application/json | Standard REST |
| operationId format | camelCase verb+noun | Code generator compatibility |

## Application Checklist

| Check | Question | Pass Condition |
|-------|----------|----------------|
| Schema reuse | Any schema in 2+ places? | Move to components.schemas |
| operationId | Every operation named? | Yes, camelCase verb+noun |
| Error responses | 400/401/404/500 on all ops? | Yes, shared ErrorResponse $ref |
| Security | Global security set? | Yes, scheme declared in components |
| OAS version | Using 3.1.0? | Yes, unless tooling forces 3.0.x |
| OAS version | Using 3.1.0 or 3.0.3? | Yes, never Swagger 2.0 |
| Webhook | Webhooks declared in spec? | Yes, in webhooks section if event-driven |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.21 |
| [[bld_schema_integration_guide]] | upstream | 0.21 |
| [[bld_schema_function_def]] | upstream | 0.20 |
| [[p11_qg_agent_computer_interface]] | downstream | 0.19 |
| [[bld_schema_onboarding_flow]] | upstream | 0.19 |
| [[p06_vs_frontmatter]] | upstream | 0.19 |
| [[bld_schema_thinking_config]] | upstream | 0.19 |
| [[bld_schema_api_reference]] | upstream | 0.19 |
| [[tpl_response_format]] | upstream | 0.19 |
| [[bld_schema_voice_pipeline]] | upstream | 0.19 |
