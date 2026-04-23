---
kind: architecture
id: bld_architecture_session_backend
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of session_backend — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - session-backend-builder
  - p03_sp_session_backend_builder
  - p01_kc_session_backend
  - bld_collaboration_session_backend
  - bld_examples_session_backend
  - bld_output_template_session_backend
  - bld_tools_session_backend
  - p11_qg_session_backend
  - p10_sb_redis
  - bld_schema_session_backend
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| backend | Storage engine type: file, sqlite, redis, postgres | session-backend-builder | required |
| path | Filesystem path for file/sqlite backends | session-backend-builder | conditional |
| connection_string | Connection URI for redis/postgres backends (env var reference only) | session-backend-builder | conditional |
| ttl_hours | Hours before inactive session is eligible for cleanup | session-backend-builder | required |
| max_sessions | Maximum concurrent sessions per scope before eviction | session-backend-builder | required |
| serialization | Data format: json, msgpack, protobuf | session-backend-builder | required |
| encryption | At-rest encryption: none, basic (AES-256), full (AES-256 + TLS) | session-backend-builder | required |
| scoping | Namespace strategy: per-nucleus, per-agent, global | session-backend-builder | required |
| compaction | Whether to compact/defragment session data on load | session-backend-builder | recommended |
| metadata | config id, version, pillar, scope, author, created date | session-backend-builder | required |
## Dependency Graph
```
env_config (P09) --feeds--> session_backend (provides connection_string env vars)
session_backend --consumed_by--> cex_memory_update.py (reads/writes session state)
session_backend --consumed_by--> cex_coordinator.py (manages cross-nucleus session handoffs)
session_backend --consumed_by--> cex_sdk/memory/stores.py (implements storage interface)
session_backend --consumed_by--> .cex/runtime/ (default file backend location)
compression_config (P10) --independent-- session_backend (compression reduces state; session persists it)
memory_config (P10) --independent-- session_backend (memory defines what to keep; session defines where to store)
guardrail (P11) --constrains--> session_backend (security rules for encryption and access)
```
| From | To | Type | Data |
|------|----|------|------|
| env_config | session_backend | feeds | connection_string, encryption keys via env vars |
| session_backend | cex_memory_update.py | consumed_by | read/write session state on each turn |
| session_backend | cex_coordinator.py | consumed_by | cross-nucleus session handoff data |
| session_backend | cex_sdk/memory/stores.py | consumed_by | storage interface implementation |
| guardrail | session_backend | constrains | encryption requirements, access control rules |
## Boundary Table
| session_backend IS | session_backend IS NOT |
|-------------------|------------------------|
| A specification of WHERE session state is persisted between turns | A compression_config (P10) — compression reduces context; session stores it |
| Covers backend type, connection, TTL, serialization, encryption | A memory config (P10) — memory defines what to remember; session defines where |
| Follows file-first principle: simplest backend until scale demands upgrade | A cache config — cache is ephemeral key-value; session is durable state |
| Declares session scoping for nucleus isolation | An env_config (P09) — env_config catalogs variables; session_backend consumes them |
| Specifies upgrade path from file to postgres | A runtime_rule (P09) — runtime_rule governs timeouts; session has TTL |
| Defines compaction strategy for efficient storage | A boot_config (P02) — boot_config is provider startup; session is state persistence |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Storage | backend, path, connection_string | Physical persistence layer |
| Lifecycle | ttl_hours, max_sessions, compaction | Session creation, expiration, cleanup |
| Format | serialization, encryption | Data encoding and protection |
| Isolation | scoping | Namespace separation between nuclei |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[session-backend-builder]] | downstream | 0.68 |
| [[p03_sp_session_backend_builder]] | upstream | 0.64 |
| [[p01_kc_session_backend]] | downstream | 0.64 |
| [[bld_collaboration_session_backend]] | downstream | 0.59 |
| [[bld_examples_session_backend]] | upstream | 0.55 |
| [[bld_output_template_session_backend]] | upstream | 0.55 |
| [[bld_tools_session_backend]] | upstream | 0.52 |
| [[p11_qg_session_backend]] | downstream | 0.49 |
| [[p10_sb_redis]] | downstream | 0.46 |
| [[bld_schema_session_backend]] | upstream | 0.45 |
