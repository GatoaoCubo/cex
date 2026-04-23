---
quality: 8.4
quality: 8.0
kind: config
id: bld_config_openapi_spec
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 30
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
title: "Config OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, config]
tldr: "Naming: p06_oas_{slug}.md. OAS version: 3.1.0. Max 8192 bytes. Use $ref for schemas used 2+ times."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - kc_api_reference
  - bld_config_mcp_server
  - bld_config_client
  - bld_schema_rbac_policy
  - bld_instruction_api_reference
  - p03_ins_mcp_server
  - bld_schema_client
  - p10_lr_api_reference_builder
  - p03_sp_mcp_server_builder
  - bld_schema_mcp_server
---

# Config: openapi_spec Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_oas_{api_slug}.md` | `p06_oas_user_management_api.md` |
| Builder directory | kebab-case | `openapi-spec-builder/` |
| Frontmatter fields | snake_case | `api_name`, `oas_version` |
| API slug | snake_case, lowercase, no hyphens | `user_management_api`, `payment_gateway` |
| operationId | camelCase | `getUser`, `createOrder`, `listProducts` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths

- Output: `N0X_{domain}/P06_schema/p06_oas_{api_slug}.md`
- Compiled: `N0X_{domain}/P06_schema/compiled/p06_oas_{api_slug}.yaml`

## Size Limits

- Body: max 8192 bytes (larger than most kinds -- OAS docs are inherently verbose)
- Total (frontmatter + body): ~10000 bytes
- Density: >= 0.78 (structured YAML, not prose)

## OAS Version Policy

| Version | Status | When to Use |
|---------|--------|-------------|
| 3.1.0 | PREFERRED | New specs (full JSON Schema, webhooks) |
| 3.0.3 | ALLOWED | When tooling requires 3.0.x compatibility |
| 2.0 (Swagger) | DEPRECATED | Migrate to 3.x; do not create new Swagger 2 specs |

## Schema Reuse Policy

| Condition | Action |
|-----------|--------|
| Schema used in 2+ places | Move to components.schemas, use $ref |
| Response shape identical in 3+ operations | Move to components.responses |
| Parameter appears in 3+ paths | Move to components.parameters |
| Single-use inline schema | Inline is acceptable |

## Operation Conventions

| Field | Convention | Example |
|-------|-----------|---------|
| operationId | camelCase, verb+noun | listUsers, getUser, createUser, updateUser, deleteUser |
| summary | Short imperative phrase | "List all users", "Get user by ID" |
| tags | PascalCase noun | ["Users", "Orders", "Products"] |
| Error codes | Always declare 400/401/404/500 | Even if unlikely -- tooling needs them |

## HTTP Method Assignment

| Action | HTTP Method | Has Body? |
|--------|-------------|-----------|
| List collection | GET /resources | No |
| Get single | GET /resources/{id} | No |
| Create | POST /resources | YES |
| Full replace | PUT /resources/{id} | YES |
| Partial update | PATCH /resources/{id} | YES |
| Delete | DELETE /resources/{id} | No |

## Response Code Policy

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST (new resource) |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation failure |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | Authenticated but no permission |
| 404 | Not Found | Resource does not exist |
| 409 | Conflict | Duplicate resource |
| 500 | Internal Error | Server-side failure |

## Security Scheme Reference

| Scheme | OAS Type | When to Use |
|--------|----------|-------------|
| JWT Bearer | http bearer | Standard REST API authentication |
| API Key header | apiKey in header | Simple service-to-service auth |
| OAuth2 code flow | oauth2 authorizationCode | User-delegated access |
| OAuth2 client credentials | oauth2 clientCredentials | Machine-to-machine |
| No auth | (none) | Public read-only endpoints only |
| mTLS | mutual TLS | Service mesh internal auth |
| No auth declared | Tooling skips security tests | Always declare scheme in components.securitySchemes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_api_reference]] | upstream | 0.28 |
| [[bld_config_mcp_server]] | sibling | 0.27 |
| [[bld_config_client]] | sibling | 0.26 |
| [[bld_schema_rbac_policy]] | upstream | 0.24 |
| [[bld_instruction_api_reference]] | upstream | 0.24 |
| [[p03_ins_mcp_server]] | upstream | 0.24 |
| [[bld_schema_client]] | upstream | 0.23 |
| [[p10_lr_api_reference_builder]] | downstream | 0.22 |
| [[p03_sp_mcp_server_builder]] | upstream | 0.22 |
| [[bld_schema_mcp_server]] | upstream | 0.22 |
