---
id: p11_qg_smoke-eval
kind: quality_gate
pillar: P11
title: "Gate: Smoke Eval"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: EDISON
domain: smoke_eval
quality: null
density_score: 0.85
tags:
  - quality-gate
  - smoke-eval
  - sanity-test
  - p11
tldr: "Gates ensuring smoke eval files define a critical path, binary pass/fail assertions, a timeout under 30s, and no deep correctness testing."
---

## Definition

A smoke eval is a fast sanity check (under 30 seconds) that confirms the most critical path of a system is alive and reachable. It does not verify correctness, edge cases, or performance — those belong to deeper eval types. A smoke eval passes this gate when every assertion is binary (pass or fail, no partial credit), the critical path covers the highest-impact flow, and the eval fails fast on the first hard error rather than accumulating multiple failures.

---

## HARD Gates

Failure on any HARD gate = immediate REJECT regardless of score.

| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`smoke-eval-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `smoke_eval` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Critical path** definition (the single most important user or system flow being verified) | Without a named critical path, the eval may check low-value flows while missing failures in high-value ones |
| H08 | Spec contains an **Assertions list** (each assertion is a named binary check: pass or fail, no partial states) | Non-binary assertions introduce ambiguity into CI pass/fail decisions |
| H09 | Spec contains a **Timeout** value that is <= 30 seconds | Evals exceeding 30s are no longer smoke evals; they block CI pipelines and defeat the purpose |

---

## SOFT Scoring

Dimensions are weighted; total normalized weight = 100%.

| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Assertions are binary pass/fail (no graded or scored assertions) | 1.0 | Assertions use scores or ranges | Mixed binary and graded | Every assertion is strictly pass or fail with no ambiguous middle state |
| 3 | Critical path covers the most important flow (not a secondary or convenience flow) | 1.0 | Covers peripheral feature | Covers important but not highest-impact flow | Covers the flow whose failure would cause the most user or system impact |
| 4 | Fast-fail on first hard error (eval halts and reports on first assertion failure) | 1.0 | Runs all assertions regardless | Partial fast-fail | Explicitly configured to halt on first failure with clear fail message |
| 5 | Health check components listed (services, endpoints, or dependencies checked before assertions begin) | 1.0 | No health checks | One component listed | All external dependencies checked before assertions begin |
| 6 | Tags include `smoke-eval` | 0.5 | Missing | Present but misspelled | Exactly `smoke-eval` in tags list |
| 7 | CI integration notes (invocation command, required env vars, expected output on pass) | 1.0 | No CI notes | Invocation command only | Invocation command + required env vars + expected output on pass |
| 8 | No deep correctness testing (strictly surface-level: existence, reachability, basic response shape) | 1.0 | Includes deep tests | Minor scope creep | Strictly surface-level checks only; no algorithm or data integrity assertions |
| 9 | Baseline expected results documented (status codes, response shape, acceptable latency range) | 1.0 | No baseline | Status codes only | Status codes + response shape + acceptable latency range |
| 10 | Environment requirements noted (OS, runtime, network access, credentials needed) | 0.5 | No environment stated | Runtime named | Full list: OS, runtime version, network requirements, secrets needed |

Score = sum(rating * weight) / sum(weights) normalized to 0-10.

---

## Actions

| Threshold | Action |
|-----------|--------|
| >= 9.5 | GOLDEN — archive to pool, tag as reference implementation |
| >= 8.0 | PUBLISH — merge to main, available for CI integration |
| >= 7.0 | REVIEW — return to author with dimension-level feedback |
| < 7.0 | REJECT — do not merge; author must revise from scratch or substantially rewrite |

---

## Bypass

| Field | Value |
|-------|-------|
| condition | System under test is a local development stub with no external dependencies; eval is used for developer inner loop only and never runs in CI |
| approver | Domain lead with written sign-off confirming the eval will not be added to CI |
| audit_log | Entry required in `records/audits/gate_bypasses.md` with date, eval name, approver, and expiry |
| expiry | 14 days; eval must pass full gate before CI integration |

H01 (parseable frontmatter) and H05 (quality=null) are NEVER bypassable under any condition.
