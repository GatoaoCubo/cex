---
id: p11_qg_satellite-spec
kind: quality_gate
pillar: P11
title: "Gate: Satellite Spec"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: EDISON
domain: satellite_spec
quality: null
density_score: 0.85
tags:
  - quality-gate
  - satellite-spec
  - autonomous-agent
  - p11
tldr: "Gates ensuring satellite spec files define a fully autonomous agent with role, model, tools, boot sequence, and dispatch rules."
---

## Definition

A satellite spec describes a fully autonomous agent: its identity, the LLM it runs on, the external tools it can call, how it starts up, how it receives work, and how it shuts down. A spec passes this gate when any operator could launch and operate the satellite from the document alone, without consulting the author.

---

## HARD Gates

Failure on any HARD gate = immediate REJECT regardless of score.

| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`satellite-spec-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `satellite_spec` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Role** definition (one-paragraph description of what the satellite does and does not do) | Without role boundary, operators cannot determine if a task is in scope |
| H08 | Spec contains a **Model** assignment: LLM provider and model name (e.g., `provider: anthropic`, `model: claude-opus-4-6`) | Satellite cannot be launched without knowing which model to request |
| H09 | Spec contains an **MCP server list** (may be empty list `[]`, but must be explicitly declared) | Tool availability determines what the satellite can execute |
| H10 | Spec contains a **Boot sequence**: ordered steps to bring the satellite from cold to ready state | Without boot sequence, launch is non-reproducible |

---

## SOFT Scoring

Dimensions are weighted; total normalized weight = 100%.

| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Constraints documented (what the satellite must never do) | 1.0 | No constraints listed | Partial list, vague | Explicit NEVER list with rationale per constraint |
| 3 | Dispatch rules present (how the satellite receives and accepts tasks) | 1.0 | No dispatch described | Dispatch channel named, no detail | Full dispatch protocol: channel, format, acceptance criteria |
| 4 | Scaling rules defined (concurrency limits, queue behavior, overflow handling) | 0.5 | No mention | Single-instance only documented | Concurrency limits, queue behavior, and overflow all defined |
| 5 | Monitoring configuration (signals emitted, health check, alerting thresholds) | 1.0 | No monitoring | Logs only | Structured signals + health check + alerting thresholds |
| 6 | Tags include `satellite-spec` | 0.5 | Missing | Present but misspelled | Exactly `satellite-spec` in tags list |
| 7 | Domain boundaries explicit (data and systems the satellite may and may not access) | 1.0 | No boundaries | Implicit in examples | Explicit allowed-access list and forbidden-access list |
| 8 | Tool availability listed with version or source per MCP server | 1.0 | None listed | Names only | Names + source/version + fallback if unavailable |
| 9 | Dependency map complete (upstream inputs and downstream consumers with data flow types) | 1.0 | No dependencies mapped | One direction only | Full upstream + downstream map with data flow types |
| 10 | Shutdown protocol documented (graceful stop, signal handling, state flush) | 1.0 | No shutdown described | Kill signal only | Graceful drain + state flush + confirmation signal |

Score = sum(rating * weight) / sum(weights) normalized to 0-10.

---

## Actions

| Threshold | Action |
|-----------|--------|
| >= 9.5 | GOLDEN — archive to pool, tag as reference implementation |
| >= 8.0 | PUBLISH — merge to main, available for operator use |
| >= 7.0 | REVIEW — return to author with dimension-level feedback |
| < 7.0 | REJECT — do not merge; author must revise from scratch or substantially rewrite |

---

## Bypass

| Field | Value |
|-------|-------|
| condition | Satellite is a short-lived experiment (TTL < 48h) and will not be shared beyond the originating team |
| approver | Domain lead with written sign-off |
| audit_log | Entry required in `records/audits/gate_bypasses.md` with date, satellite name, approver, and expiry |
| expiry | 48 hours from bypass grant; spec must pass or be deleted |

H01 (parseable frontmatter) and H05 (quality=null) are NEVER bypassable under any condition.
