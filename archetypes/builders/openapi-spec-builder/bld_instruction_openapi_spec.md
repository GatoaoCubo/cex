---
kind: instruction
id: bld_instruction_openapi_spec
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for openapi_spec
pattern: 3-phase pipeline (define -> compose -> validate)
quality: null
title: "Instruction OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, instruction]
tldr: "3-phase: define API surface and security, compose OAS 3.x document with paths and components, validate compliance."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce an openapi_spec

## Phase 1: DEFINE

1. Identify the API name and base URL (production + staging servers)
2. Enumerate all endpoints: path + HTTP method + brief purpose
3. For each operation: identify path params, query params, request body shape
4. For each operation: identify success response schema and error codes
5. Determine authentication mechanism: JWT bearer, API key, OAuth2, or none
6. List all unique data models that will be shared across operations
7. Identify which operations require auth and which are public
8. Determine OAS version: 3.1.0 preferred (3.0.3 if tooling requires)

## Phase 2: COMPOSE

1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p06_oas_{api_slug}` -- verify pattern `^p06_oas_[a-z][a-z0-9_]+$`
4. Write OpenAPI document:
   a. Set openapi version and info block
   b. Define servers array (at least production)
   c. For each path: write path item with operations
   d. For each operation: write operationId (camelCase), summary, tags
   e. For each operation: write parameters array (path/query params)
   f. For each operation: write requestBody if POST/PUT/PATCH
   g. For each operation: write responses (success + error codes)
   h. Move all schemas to components.schemas, use $ref
   i. Move reusable responses to components.responses
   j. Define security schemes in components.securitySchemes
   k. Set global security requirement
5. Write Security section: auth method summary
6. Write Error Responses table: code, meaning, schema
7. Verify body <= 8192 bytes

## Phase 3: VALIDATE

1. Confirm id matches `^p06_oas_[a-z][a-z0-9_]+$`
2. Confirm kind == openapi_spec
3. Confirm oas_version present and valid ("3.1.0" or "3.0.3")
4. Confirm servers array non-empty
5. Confirm paths non-empty with at least one operation
6. Confirm all 3 body sections present: OpenAPI Document, Security, Error Responses
7. Cross-check: not api_reference (no prose tutorial), not api_client (no code)
8. Confirm quality: null
9. Revise if score < 8.0
