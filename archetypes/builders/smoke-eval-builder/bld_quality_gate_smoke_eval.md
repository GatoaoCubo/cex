---
id: p11_qg_smoke-eval
kind: quality_gate
pillar: P11
title: "Gate: Smoke Eval"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: smoke_eval
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - smoke-eval
  - sanity-test
  - p11
tldr: "Gates ensuring smoke eval files define a critical path, binary pass/fail assertions, a timeout under 30s, and no deep correctness testing."
llm_function: GOVERN
---
## Definition
A smoke eval is a fast sanity check (under 30 seconds) that confirms the most critical path of a system is alive and reachable. It does not verify correctness, edge cases, or performance — those belong to deeper eval types. A smoke eval passes this gate when every assertion is binary (pass or fail, no partial credit), the critical path covers the highest-impact flow, and the eval fails fast on the first hard error rather than accumulating multiple failures.
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
