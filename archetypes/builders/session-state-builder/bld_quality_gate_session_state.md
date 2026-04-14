---
id: p11_qg_session-state
kind: quality_gate
pillar: P11
title: "Gate: Session State"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: session_state
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - session-state
  - ephemeral
  - p11
tldr: "Gates ensuring session state specs define minimal checkpoint fields, realistic TTL, and a recovery protocol for partial or expired state."
llm_function: GOVERN
---
## Definition
A session state spec describes an ephemeral snapshot of an in-progress interaction: which fields to capture, how long the snapshot lives, and how to restore a session from it. A spec passes this gate when the captured fields are the minimum necessary to resume work (not a full database dump), the TTL reflects the realistic session length, and partial or expired state has a defined recovery path rather than a hard failure.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`session-state-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `session_state` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains **Checkpoint fields** defined (named list of fields captured at each checkpoint, with type per field) | Without a field list, the snapshot schema is undefined and serialization is non-deterministic |
| H08 | Spec contains an **Expiry / TTL** value (numeric duration + unit, e.g., `ttl: 3600s`) | Without TTL, expired state accumulates and privacy risks cannot be bounded |
| H09 | Spec contains a **Recovery protocol** (what to do when state is absent, partial, or expired at resume time) | Missing recovery causes hard failures instead of graceful degradation |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Fields capture minimal necessary state (no redundant or derivable fields) | 1.0 | Many redundant fields | Some redundancy | Only fields that cannot be recomputed from stable data |
| 3 | TTL realistic for session length (not too short causing premature expiry, not too long accumulating stale state) | 1.0 | TTL not justified | Round-number guess | TTL derived from measured or estimated session duration |
| 4 | Recovery handles partial state (spec addresses incomplete snapshots, not just absent ones) | 1.0 | Only absent state handled | Partial noted, no procedure | Explicit partial-state recovery logic per missing field |
| 5 | No persistent data (all captured data is ephemeral; storage backend is volatile) | 1.0 | Persistent writes present or unclear | Noted as ephemeral | Explicit confirmation + storage backend is volatile (memory or cache) |
| 6 | Tags include `session-state` | 0.5 | Missing | Present but misspelled | Exactly `session-state` in tags list |
| 7 | Token budget tracking noted (LLM context budget included or explicitly excluded with reason) | 0.5 | No mention | Noted as not applicable | Explicitly included or explicitly excluded with reason |
| 8 | Serialization format defined (JSON, msgpack, etc.) with example serialized snapshot | 1.0 | No format stated | Format named only | Format + example snapshot + size estimate |
