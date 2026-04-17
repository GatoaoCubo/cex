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
quality: null
title: "Memory OpenAPI Spec"
density_score: 0.90
llm_function: INJECT
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
