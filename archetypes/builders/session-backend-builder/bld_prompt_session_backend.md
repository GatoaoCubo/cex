---
kind: instruction
id: bld_instruction_session_backend
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for session_backend
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_trace_config
  - bld_instruction_retriever_config
  - bld_instruction_context_doc
  - bld_instruction_output_validator
  - p03_sp_session_backend_builder
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
  - bld_instruction_prompt_version
  - bld_instruction_constraint_spec
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

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify session
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | session backend construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.52 |
| [[bld_instruction_trace_config]] | sibling | 0.46 |
| [[bld_instruction_retriever_config]] | sibling | 0.44 |
| [[bld_instruction_context_doc]] | sibling | 0.44 |
| [[bld_instruction_output_validator]] | sibling | 0.43 |
| [[p03_sp_session_backend_builder]] | related | 0.42 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.42 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.42 |
| [[bld_instruction_prompt_version]] | sibling | 0.41 |
| [[bld_instruction_constraint_spec]] | sibling | 0.40 |
