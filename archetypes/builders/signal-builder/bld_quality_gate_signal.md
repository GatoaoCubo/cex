---
id: p11_qg_signal
kind: quality_gate
pillar: P11
title: "Gate: Signal"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: signal
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - signal
  - inter-agent
  - p11
tldr: "Gates ensuring signal specs define an exhaustive status enum, emitter identity, timestamp, and minimal payload with no embedded business logic."
llm_function: GOVERN
---
## Definition
A signal is an atomic event emitted by one agent and consumed by another or a monitor. It carries a status, an emitter identity, a timestamp, and an optional minimal payload. A signal passes this gate when any consumer could parse and act on it without contacting the emitter, the status enum covers all terminal and non-terminal states, and the payload contains no business logic — only status data.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`signal-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `signal` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Status type** field with an explicit enum (e.g., `complete`, `error`, `progress`) and no open-ended string values | Open status strings make consumer logic fragile and non-exhaustive |
| H08 | Spec contains an **Emitter identity field** (the field name and type that identifies which agent emitted the signal) | Consumers and monitors need emitter identity to route, filter, and audit signals |
| H09 | Spec contains a **Timestamp field** (field name, type, and format, e.g., ISO 8601 UTC) | Without timestamps, ordering and deduplication are impossible |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Payload is minimal JSON (only fields required for consumers to act; no verbose metadata) | 1.0 | Large nested payload | Moderate size | Flat structure, <= 10 fields, no nested objects except optional extension |
| 3 | Status enum is exhaustive (covers all reachable states including error sub-types) | 1.0 | Only happy-path statuses | Happy path + generic error | All terminal states + progress states + known error variants |
| 4 | Consumer expectations documented (who reads this signal and what they do per status) | 1.0 | No consumers listed | Consumers named | Consumers named + action per status per consumer |
| 5 | Idempotency considered (spec states whether duplicate signals are safe or must be deduplicated) | 1.0 | No mention | Noted as a concern | Explicit idempotency ruling with dedup key if required |
| 6 | Tags include `signal` | 0.5 | Missing | Present but misspelled | Exactly `signal` in tags list |
| 7 | Extension fields optional not required (future payload fields are opt-in; consumers ignore unknown keys) | 0.5 | Extension fields are required | Marked optional but schema enforces them | Schema allows unknown fields; consumers ignore unknown keys |
| 8 | Backward compatibility policy stated (additive-only field additions, versioning strategy) | 1.0 | No compatibility policy | Semver bump required for any change | Additive-only policy: new optional fields never break consumers |
