---
id: p11_qg_session_backend
kind: quality_gate
pillar: P11
title: "Gate: session_backend"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
domain: "session_backend — session state persistence specifications with backend type, TTL, serialization, and encryption"
quality: 9.0
tags: [quality-gate, session-backend, persistence, state, P11]
tldr: "Gates for session_backend artifacts: validates backend type, TTL, serialization, encryption, scoping, and credential safety."
density_score: 0.91
llm_function: GOVERN
---
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
