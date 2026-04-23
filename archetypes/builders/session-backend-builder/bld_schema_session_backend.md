---
kind: schema
id: bld_schema_session_backend
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for session_backend
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_memory_scope
  - bld_schema_retriever_config
  - bld_schema_golden_test
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_usage_report
  - bld_schema_constraint_spec
  - bld_schema_unit_eval
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
---

# Schema: session_backend
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_sb_{backend}) | YES | - | Namespace compliance |
| kind | literal "session_backend" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| backend | enum: file, sqlite, redis, postgres | YES | - | Storage engine type |
| path | string | COND | - | Required for file/sqlite; filesystem path |
| connection_string | string | COND | - | Required for redis/postgres; env var reference |
| ttl_hours | number > 0 | YES | - | Session expiration in hours |
| max_sessions | integer > 0 | YES | - | Max concurrent sessions per scope |
| serialization | enum: json, msgpack, protobuf | YES | - | Data format |
| encryption | enum: none, basic, full | YES | - | At-rest encryption level |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "session_backend" |
| tldr | string <= 160ch | YES | - | Dense summary |
| scoping | enum: per_nucleus, per_agent, global | REC | per_nucleus | Namespace strategy |
| description | string <= 200ch | REC | - | What this config covers |
| compaction | boolean | REC | false | Compact on load |
| upgrade_path | string | REC | - | Next backend tier |
## ID Pattern
Regex: `^p10_sb_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Backend Specification` — engine type, connection, rationale
2. `## Session Lifecycle` — creation, TTL, expiration, cleanup, compaction
3. `## Serialization` — format, trade-offs, schema evolution
4. `## Security` — encryption, access control, credential references
## Constraints
- max_bytes: 4096 (body only)
- naming: p10_sb_{backend}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- backend MUST be one of: file, sqlite, redis, postgres
- path required when backend is file or sqlite
- connection_string required when backend is redis or postgres
- connection_string MUST reference env var, never embed actual credentials
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_memory_scope]] | sibling | 0.65 |
| [[bld_schema_retriever_config]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.59 |
| [[bld_schema_output_validator]] | sibling | 0.58 |
| [[bld_schema_handoff_protocol]] | sibling | 0.58 |
| [[bld_schema_usage_report]] | sibling | 0.57 |
| [[bld_schema_constraint_spec]] | sibling | 0.57 |
| [[bld_schema_unit_eval]] | sibling | 0.57 |
| [[bld_schema_chunk_strategy]] | sibling | 0.57 |
| [[bld_schema_smoke_eval]] | sibling | 0.56 |
