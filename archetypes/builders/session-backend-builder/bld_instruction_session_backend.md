---
kind: instruction
id: bld_instruction_session_backend
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for session_backend
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a session_backend
## Phase 1: RESEARCH
1. Identify the target: which agent, nucleus, or system scope needs session persistence?
2. Determine scale requirements: single-agent (file), multi-agent (sqlite), distributed (redis/postgres)
3. Catalog what state needs persistence: conversation history, tool results, handoff context, decision manifests
4. Classify data sensitivity: does the session contain secrets, PII, or sensitive business logic?
5. Determine TTL requirements: how long should inactive sessions persist before cleanup?
6. Assess concurrency: will multiple processes read/write the same session simultaneously?
7. Evaluate existing infrastructure: is redis/postgres already deployed, or is file-based the only option?
8. Check existing session_backends via brain_query [IF MCP] for the same scope — do not duplicate
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Backend Specification** section: backend type, path/connection, rationale for selection
5. Write **Session Lifecycle** section: creation, TTL, expiration, cleanup, compaction on load
6. Write **Serialization** section: format choice (json/msgpack/protobuf), trade-offs, schema evolution
7. Write **Security** section: encryption at rest, access control, credential references (env vars only)
8. Write **Scoping** section: namespace strategy, per-nucleus isolation, key prefix conventions
9. Write **Upgrade Path** section: how to migrate from current backend to the next tier (file→sqlite→redis→postgres)
10. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p10_sb_[a-z][a-z0-9_]+$`
4. Confirm backend is one of: file, sqlite, redis, postgres
5. Confirm ttl_hours is a positive number
6. Confirm max_sessions is a positive integer
7. Confirm serialization is one of: json, msgpack, protobuf
8. Confirm no actual credentials or connection passwords appear in the artifact
9. Confirm `quality` is null
10. Confirm body <= 4096 bytes
11. Cross-check: is this a persistence backend? If this is token reduction it belongs in `compression_config`. If this is long-term memory it belongs in memory config. If this is ephemeral caching it belongs in cache config. This artifact specifies WHERE to persist state, not HOW to reduce it or WHAT to remember.
12. If score < 8.0: revise in the same pass before outputting
