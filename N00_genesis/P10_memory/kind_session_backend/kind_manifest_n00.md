---
id: n00_session_backend_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Session Backend -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, session_backend, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A session_backend defines the per-user session state persistence configuration, specifying the storage technology, serialization format, TTL, and isolation guarantees for user sessions in multi-user or multi-tenant deployments. It is the infrastructure contract that ensures session_state artifacts are reliably stored and retrieved.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `session_backend` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| backend_type | enum | yes | redis \| sqlite \| filesystem \| dynamodb \| postgres |
| connection_string_ref | string | yes | Reference to secret_config holding the connection string |
| ttl_seconds | integer | yes | Session expiry in seconds |
| isolation_level | enum | yes | user \| nucleus \| global |
| serialization | enum | yes | json \| msgpack \| pickle |
| max_session_bytes | integer | no | Maximum bytes per session entry |

## When to use
- When deploying a nucleus to production with multiple concurrent users
- When configuring Redis or SQLite as the session persistence layer
- When auditing session isolation guarantees for SOC2 compliance

## Builder
`archetypes/builders/session_backend-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind session_backend --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sb_redis_production
kind: session_backend
pillar: P10
nucleus: n05
title: "Example Session Backend"
version: 1.0
quality: null
---
# Session Backend: Redis Production
backend_type: redis
connection_string_ref: secret_redis_prod
ttl_seconds: 3600
isolation_level: user
serialization: json
```

## Related kinds
- `session_state` (P10) -- the data this backend stores and retrieves
- `secret_config` (P09) -- holds the connection string referenced by this backend
- `memory_architecture` (P10) -- system architecture that specifies this backend choice
