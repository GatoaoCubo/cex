---
id: p01_kc_session_backend
kind: knowledge_card
type: kind
pillar: P10
title: "Session Backend -- Deep Knowledge for session_backend"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: session_backend
quality: 9.1
tags: [session_backend, p10, INJECT, kind-kc, memory, session, persistence]
tldr: "Configuration for agent session state persistence -- where and how conversation/context state is stored between turns"
when_to_use: "Configuring session persistence, choosing between file/redis/postgres backends, or building stateful agents"
keywords: [session, backend, persistence, state, redis, sqlite, file, conversation]
feeds_kinds: [session_backend]
density_score: null
related:
  - p10_sb_redis
  - bld_architecture_session_backend
  - session-backend-builder
  - p03_sp_session_backend_builder
  - bld_examples_session_backend
  - bld_collaboration_session_backend
  - bld_knowledge_card_session_backend
  - bld_instruction_session_backend
  - bld_memory_session_state
  - p01_kc_session_state
---

# Session Backend

## Spec
```yaml
kind: session_backend
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_sb_{{backend}}.yaml
core: false
```

## Purpose

A session backend config tells CEX where to persist agent state between turns/runs. This includes conversation history, accumulated context, memory observations, and runtime state (locks, signals, counters).

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| backend | Storage technology | `file`, `sqlite`, `redis`, `postgres`, `memory` |
| path | Storage location (file/sqlite) | `.cex/runtime/sessions/` |
| connection_string | DB connection (redis/postgres) | `redis://localhost:6379/0` |
| ttl_hours | Session expiry | `24` (auto-cleanup after 24h) |
| max_sessions | Concurrent session limit | `100` |
| serialization | Format for state blobs | `json`, `msgpack`, `pickle` |
| encryption | Encrypt stored state | `false` |

## Key Patterns

1. **File-first**: Default to filesystem (`.cex/runtime/`) -- zero deps, git-trackable, debuggable
2. **Upgrade path**: file -> sqlite (single-file DB, concurrent reads) -> redis (multi-process) -> postgres (production)
3. **Session scoping**: Each nucleus gets its own session namespace to prevent cross-contamination
4. **Compaction on load**: When restoring a session, compress old turns before injecting into context

## Anti-Patterns

- In-memory only without persistence (state lost on crash)
- Global session namespace (nucleus A reads nucleus B's state)
- No TTL (sessions accumulate forever, disk fills)
- Pickle serialization (security risk from untrusted data)
- Storing full LLM responses in session (bloat -- store summaries)

## CEX Integration

- `.cex/runtime/` is the default file-based session backend
- Subdirs: `handoffs/`, `signals/`, `pids/`, `archive/` each serve as specialized session stores
- `cex_memory_update.py` writes observations to builder memory files (long-term session)
- `cex_coordinator.py` tracks cross-wave state (mission-level session)
- `cex_sdk/memory/stores.py` provides pluggable backend abstraction

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_sb_redis]] | related | 0.58 |
| [[bld_architecture_session_backend]] | upstream | 0.55 |
| [[session-backend-builder]] | upstream | 0.53 |
| [[p03_sp_session_backend_builder]] | upstream | 0.53 |
| [[bld_examples_session_backend]] | upstream | 0.52 |
| [[bld_collaboration_session_backend]] | downstream | 0.49 |
| [[bld_knowledge_card_session_backend]] | sibling | 0.49 |
| [[bld_instruction_session_backend]] | upstream | 0.44 |
| [[bld_memory_session_state]] | related | 0.43 |
| [[p01_kc_session_state]] | sibling | 0.42 |
