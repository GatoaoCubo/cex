---
kind: schema
id: bld_schema_session_backend
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for session_backend
pattern: TEMPLATE derives from this. CONFIG restricts this.
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
