---
kind: quality_gate
id: p11_qg_session_backend
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of session_backend artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: session_backend"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, session-backend, persistence, state, P11]
tldr: "Gates for session_backend artifacts: validates backend type, TTL, serialization, encryption, scoping, and credential safety."
domain: "session_backend — session state persistence specifications with backend type, TTL, serialization, and encryption"
created: "2026-04-06"
updated: "2026-04-06"
density_score: 0.91
related:
  - bld_examples_session_backend
  - p03_sp_session_backend_builder
  - bld_output_template_session_backend
  - bld_architecture_session_backend
  - bld_schema_session_backend
  - session-backend-builder
  - bld_instruction_session_backend
  - bld_config_session_backend
  - p01_kc_session_backend
  - bld_collaboration_session_backend
---

## Quality Gate

# Gate: session_backend
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: session_backend` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p10_sb_[a-z][a-z0-9_]+$` | "ID fails session_backend namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"session_backend"` | "Kind is not 'session_backend'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, backend, ttl_hours, max_sessions, serialization, encryption, version, created, author, tags | "Missing required field(s)" |
| H07 | `backend` is one of: file, sqlite, redis, postgres | "Invalid backend type" |
| H08 | `path` present when backend is file or sqlite | "File/sqlite backend requires path field" |
| H09 | `connection_string` references env var (not embedded credential) when backend is redis or postgres | "Connection string must reference env var, never embed credentials" |
| H10 | `ttl_hours` is a positive number | "TTL must be a positive number" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Backend rationale | 1.0 | Why this backend fits the scale and infrastructure requirements |
| TTL policy justification | 1.0 | TTL hours explained relative to session length and storage constraints |
| Serialization trade-offs | 1.0 | Format choice justified with performance/readability/schema trade-offs |
| Encryption apownteness | 1.0 | Encryption level matches data sensitivity (PII = full, dev = none) |
| Scoping strategy | 1.0 | Namespace isolation prevents cross-nucleus contamination |
| Upgrade path clarity | 0.5 | Migration from current backend to next tier documented |
| Compaction strategy | 0.5 | Session cleanup and defragmentation defined |
| Concurrency handling | 1.0 | How concurrent read/write is handled (locks, WAL, atomic ops) |
| Credential safety | 1.0 | All connection details reference env vars, no embedded secrets |
| Max sessions rationale | 0.5 | max_sessions justified with resource calculation or capacity plan |
| Boundary clarity | 0.5 | Explicitly not compression_config, memory config, or cache |
| Documentation | 0.5 | tldr names the backend type and key limits (TTL, max_sessions) |
Weight sum: 1.0+1.0+1.0+1.0+1.0+0.5+0.5+1.0+1.0+0.5+0.5+0.5 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Prototype or spike where backend selection is exploratory and TTL is not yet calibrated |
| approver | Infra lead approval required (written); credential safety never bypassed |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
