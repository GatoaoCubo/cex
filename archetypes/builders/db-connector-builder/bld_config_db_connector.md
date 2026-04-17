---
kind: config
id: bld_config_connector
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
title: "Config Db Connector"
version: "1.0.0"
author: n03_builder
tags: [db_connector, builder, examples]
tldr: "Golden and anti-examples for db connector construction, demonstrating ideal structure and common pitfalls."
domain: "db connector construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: connector Production Rules

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_conn_{service_slug}.md` + `.yaml` | `p04_conn_stripe.md` |
| Builder directory | kebab-case | `db-connector-builder/` |
| Frontmatter fields | snake_case | `health_check`, `rate_limit` |
| Service slug | snake_case, lowercase, no hyphens | `stripe`, `slack`, `bling_erp` |
| Endpoint names | snake_case, verb_noun or receive_noun | `push_order`, `receive_webhook` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_conn_{service_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_conn_{service_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2500 bytes
- Density: >= 0.80 (no filler)
## Protocol Enum
| Value | When to use |
|-------|-------------|
| rest | HTTP request/response + webhook callbacks (most common) |
| websocket | Full-duplex real-time data exchange |
| grpc | High-throughput bidirectional streaming between services |
| mqtt | Lightweight pub/sub (IoT, event-driven) |
## Auth Enum
| Value | When to use |
|-------|-------------|
| none | Internal services with network-level trust only |
| api_key | Static key in header (most common for SaaS) |
| oauth | OAuth 2.0 flow for user-delegated access |
| bearer | JWT or static token in Authorization header |
| hmac | Webhook signature verification (inbound auth) |
## Logging Enum
| Value | When to use |
|-------|-------------|
| structured | JSON logs with fields (default, recommended) |
| plaintext | Simple text logs (legacy systems) |
| none | No logging (sensitive data, minimal footprint) |
