---
kind: examples
id: bld_examples_session_backend
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of session_backend artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: session-backend-builder
## Golden Example
INPUT: "Define a file-based session backend for CEX development environment"
OUTPUT:
```yaml
id: p10_sb_file_default
kind: session_backend
pillar: P10
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
backend: file
path: ".cex/runtime/sessions/"
ttl_hours: 72
max_sessions: 50
serialization: json
encryption: none
scoping: per_nucleus
quality: 8.8
tags: [session_backend, file, development, P10, zero-deps]
tldr: "File-based sessions at .cex/runtime/sessions/, JSON, 72h TTL, 50 max, per-nucleus scoping"
description: "Zero-dependency file backend for local development with per-nucleus session isolation"
compaction: true
upgrade_path: "file -> sqlite (when concurrent access needed) -> redis (when distributed)"
```
## Backend Specification
File-based session storage using JSON files in `.cex/runtime/sessions/`. Each session is a
single JSON file named `{nucleus}_{session_id}.json`. Zero external dependencies — requires
only filesystem access. Chosen for development because it is inspectable (human-readable JSON),
debuggable (files can be manually edited), and needs no server processes.
## Session Lifecycle
- **Create**: new file written on first turn of a conversation
- **Read**: loaded and parsed at start of each turn; compacted if stale entries detected
- **TTL**: sessions older than 72 hours are eligible for cleanup on next load
- **Cleanup**: expired sessions deleted by cex_memory_update.py on startup scan
- **Compaction**: on load, remove superseded entries (e.g., old handoff data that has been archived)
- **Max sessions**: when 50 sessions exist, oldest inactive session is evicted before creating new
## Serialization
JSON format selected for development:
- Human-readable: developers can inspect session files directly
- Schema-flexible: no .proto or schema migration needed
- Trade-off: ~2x larger than msgpack, ~5x slower parse — acceptable for dev volume
- Schema evolution: new fields added with null defaults; old sessions remain readable
## Security
- Encryption: none (development environment, no sensitive data in sessions)
- Access: filesystem permissions (user-only read/write on session directory)
- No credentials needed — file backend uses local filesystem
- Upgrade to `basic` encryption when sessions contain user PII or API responses
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p10_sb_ pattern (H02 pass)
- kind: session_backend (H04 pass)
- All 6 core fields present: backend, path, ttl_hours, max_sessions, serialization, encryption (H06 pass)
- backend "file" is valid enum (H07 pass)
- path present for file backend (H08 pass)
- ttl_hours: 72 is positive (H10 pass)
- Body has all 4 sections: Backend Specification, Session Lifecycle, Serialization, Security
- Upgrade path documented
- Compaction strategy defined
## Anti-Example
INPUT: "Create session config for redis"
BAD OUTPUT:
```yaml
id: redis-sessions
kind: session
pillar: storage
backend: redis
connection_string: "redis://admin:s3cret@redis.prod.internal:6379/0"
quality: 7.0
tags: [redis]
```
Connect to Redis for sessions.
FAILURES:
1. id: "redis-sessions" uses hyphens and no `p10_sb_` prefix -> H02 FAIL
2. kind: "session" not "session_backend" -> H04 FAIL
3. pillar: "storage" not "P10" -> H06 FAIL
4. quality: 7.0 (not null) -> H05 FAIL
5. connection_string embeds actual password "s3cret" -> H09 FAIL (must reference env var)
6. Missing fields: ttl_hours, max_sessions, serialization, encryption, version, created, author -> H06 FAIL
7. tags: only 1 item, missing "session_backend" -> S02 FAIL
8. Body missing Backend Specification, Session Lifecycle, Serialization, Security sections -> structural FAIL
9. No TTL defined — sessions accumulate forever -> S03 FAIL
10. No scoping defined — global namespace collision risk -> S05 FAIL
