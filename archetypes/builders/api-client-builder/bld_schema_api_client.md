---
kind: schema
id: bld_schema_client
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for client
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Api Client"
version: "1.0.0"
author: n03_builder
tags: [api_client, builder, examples]
tldr: "Golden and anti-examples for api client construction, demonstrating ideal structure and common pitfalls."
domain: "api client construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_chunk_strategy
  - bld_schema_connector
  - bld_schema_mcp_server
  - bld_schema_constraint_spec
  - bld_schema_smoke_eval
  - bld_schema_prompt_version
---

# Schema: client
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_client_{api_slug}) | YES | - | Namespace compliance |
| kind | literal "client" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable client name |
| api | string | YES | - | Target API name |
| base_url | string (URL) | YES | - | API base URL |
| auth | enum: none, api_key, oauth, bearer | YES | - | Auth strategy |
| endpoints | list[string], len >= 1 | YES | - | Exact endpoint names consumed |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "client" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the client does |
| rate_limit | string | REC | - | Requests per unit time |
| retry | string | REC | - | Retry policy (max, backoff) |
| timeout | string | REC | - | Request timeout |
| serialization | enum: json, xml, protobuf | REC | json | Wire format |
| pagetion | enum: cursor, offset, none | REC | none | Pagination strategy |
| error_codes | list[string] | REC | - | Key error codes handled |
| caching | string | REC | - | Cache strategy |
## ID Pattern
Regex: `^p04_client_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what API, use case, who consumes it
2. `## Endpoints` — each endpoint: method, path, parameters, return type
3. `## Auth & Config` — base_url, auth method, required headers
4. `## Error Handling` — error codes, retry strategy, timeout behavior
## Constraints
- max_bytes: 1024 (body only — compact client spec)
- naming: p04_client_{api_slug}.md + .yaml (dual file)
- machine_format: json (compiled artifact)
- id == filename stem
- endpoints list MUST match endpoint names defined in ## Endpoints section
- quality: null always
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.68 |
| [[bld_schema_handoff_protocol]] | sibling | 0.68 |
| [[bld_schema_output_validator]] | sibling | 0.66 |
| [[bld_schema_memory_scope]] | sibling | 0.66 |
| [[bld_schema_chunk_strategy]] | sibling | 0.66 |
| [[bld_schema_connector]] | sibling | 0.66 |
| [[bld_schema_mcp_server]] | sibling | 0.65 |
| [[bld_schema_constraint_spec]] | sibling | 0.65 |
| [[bld_schema_smoke_eval]] | sibling | 0.64 |
| [[bld_schema_prompt_version]] | sibling | 0.64 |
