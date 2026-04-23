---
kind: schema
id: bld_schema_connector
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for connector
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Db Connector"
version: "1.0.0"
author: n03_builder
tags: [db_connector, builder, examples]
tldr: "Golden and anti-examples for db connector construction, demonstrating ideal structure and common pitfalls."
domain: "db connector construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_client
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
  - bld_schema_prompt_version
  - bld_schema_mcp_server
---

# Schema: connector

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_conn_{service_slug}) | YES | - | Namespace compliance |
| kind | literal "connector" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable connector name |
| service | string | YES | - | External service name |
| protocol | enum: rest, websocket, grpc, mqtt | YES | - | Transport protocol |
| auth | enum: none, api_key, oauth, bearer, hmac | YES | - | Auth strategy |
| endpoints | list[string], len >= 1 | YES | - | Endpoint names (inbound + outbound) |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "connector" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the connector does |
| health_check | string | REC | - | Health check endpoint or strategy |
| mapping | string | REC | - | Data mapping summary |
| transform | string | REC | - | Transform rules summary |
| retry | string | REC | - | Retry policy (max, backoff) |
| rate_limit | string | REC | - | Requests per unit time |
| logging | enum: structured, plaintext, none | REC | structured | Log format |
| versioning | string | REC | - | API version strategy |
## ID Pattern
Regex: `^p04_conn_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what service, integration pattern, who uses it
2. `## Endpoints` — each endpoint: direction, method/topic, path, data shape
3. `## Data Mapping` — field mapping rules, transform, inbound/outbound schemas
4. `## Health & Errors` — health_check, error codes, retry, circuit breaker
## Constraints
- max_bytes: 1024 (body only — compact connector spec)
- naming: p04_conn_{service_slug}.md + .yaml (dual file)
- machine_format: json (compiled artifact)
- id == filename stem
- endpoints list MUST include direction annotation in ## Endpoints section
- quality: null always
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_client]] | sibling | 0.71 |
| [[bld_schema_retriever_config]] | sibling | 0.68 |
| [[bld_schema_handoff_protocol]] | sibling | 0.67 |
| [[bld_schema_output_validator]] | sibling | 0.66 |
| [[bld_schema_memory_scope]] | sibling | 0.66 |
| [[bld_schema_constraint_spec]] | sibling | 0.65 |
| [[bld_schema_chunk_strategy]] | sibling | 0.65 |
| [[bld_schema_smoke_eval]] | sibling | 0.64 |
| [[bld_schema_prompt_version]] | sibling | 0.64 |
| [[bld_schema_mcp_server]] | sibling | 0.63 |
