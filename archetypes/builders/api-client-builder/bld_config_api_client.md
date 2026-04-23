---
kind: config
id: bld_config_client
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Api Client"
version: "1.0.0"
author: n03_builder
tags: [api_client, builder, examples]
tldr: "Golden and anti-examples for api client construction, demonstrating ideal structure and common pitfalls."
domain: "api client construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_connector
  - bld_knowledge_card_client
  - bld_config_mcp_server
  - bld_schema_client
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
---
# Config: client Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_client_{api_slug}.md` + `.yaml` | `p04_client_stripe.md` |
| Builder directory | kebab-case | `api-client-builder/` |
| Frontmatter fields | snake_case | `base_url`, `rate_limit` |
| API slug | snake_case, lowercase, no hyphens | `stripe`, `openai`, `railway` |
| Endpoint names | snake_case, verb_noun pattern | `create_charge`, `list_users` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_client_{api_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_client_{api_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Auth Enum
| Value | When to use |
|-------|-------------|
| none | Internal APIs with network-level trust only |
| api_key | Static key in header (most common for SaaS APIs) |
| oauth | OAuth 2.0 flow for user-delegated access |
| bearer | JWT or token in Authorization: Bearer header |
## Serialization Enum
| Value | When to use |
|-------|-------------|
| json | REST APIs (default, most common) |
| xml | Legacy SOAP or XML-based APIs |
| protobuf | gRPC services |
## Pagination Enum
| Value | When to use |
|-------|-------------|
| cursor | Token-based pagetion (Stripe, Shopify style) |
| offset | Numeric offset/limit (SQL-style) |
| none | API returns all results or no list endpoints |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_connector]] | sibling | 0.41 |
| [[bld_knowledge_card_client]] | upstream | 0.40 |
| [[bld_config_mcp_server]] | sibling | 0.34 |
| [[bld_schema_client]] | upstream | 0.32 |
| [[bld_config_memory_scope]] | sibling | 0.31 |
| [[bld_config_retriever_config]] | sibling | 0.30 |
| [[bld_config_prompt_version]] | sibling | 0.30 |
| [[bld_config_output_validator]] | sibling | 0.29 |
| [[bld_config_handoff_protocol]] | sibling | 0.28 |
| [[bld_config_constraint_spec]] | sibling | 0.28 |
