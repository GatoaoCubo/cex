---
kind: config
id: bld_config_session_backend
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
title: "Config Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: session_backend Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_sb_{{backend}}.yaml` | `p10_sb_file_default.yaml` |
| Builder directory | kebab-case | `session-backend-builder/` |
| Frontmatter fields | snake_case | `ttl_hours`, `max_sessions` |
| Backend names | lowercase, single word or snake_case | `file`, `sqlite`, `redis`, `postgres` |
| Session key prefix | `{nucleus}:{scope}:{session_id}` | `n03:builder:sess_abc123` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P10_memory/examples/p10_sb_{{backend}}.yaml`
- Compiled: `cex/P10_memory/compiled/p10_sb_{{backend}}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80 (no filler)
## Backend Enum
| Value | When to use | Dependencies |
|-------|-------------|-------------|
| file | Single-agent, local, zero external deps | Filesystem only |
| sqlite | Multi-agent, local, need concurrent reads | sqlite3 stdlib |
| redis | Distributed, need TTL enforcement, pub/sub | redis-py + Redis server |
| postgres | Production, need transactions, full SQL, audit trail | psycopg2 + PostgreSQL |
## Serialization Enum
| Value | Trade-offs |
|-------|-----------|
| json | Human-readable, schema-flexible, slower, larger |
| msgpack | Binary, fast, compact, not human-readable |
| protobuf | Typed schema, fastest, smallest, requires .proto definition |
## Security Levels
| Level | Encryption | Access | When |
|-------|-----------|--------|------|
| none | No encryption | Filesystem permissions | Dev/local, no sensitive data |
| basic | AES-256 at rest | Filesystem + app-level auth | Staging, some sensitive data |
| full | AES-256 at rest + TLS in transit | IAM + row-level access | Production, PII/secrets in session |
