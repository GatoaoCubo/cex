---
id: p11_qg_workflow_primitive
kind: quality_gate
pillar: P11
title: "Gate: Workflow Primitive"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: builder
domain: workflow_primitive
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - workflow_primitive
  - orchestration
  - p11
tldr: "Gates ensuring workflow primitives define typed I/O, enforce composition rules (parallel-merge, loop max_iter, gate threshold), and contain no full workflow graphs or DAG edges."
llm_function: GOVERN
---
## Definition
A workflow_primitive is an atomic orchestration building block — one of seven types (step, condition, loop, parallel, router, gate, merge) with typed inputs and outputs. It passes this gate when its type is valid, inputs and outputs are typed, type-specific guards are present (max_iter for loops, threshold for gates, merge_ref for parallel), and the primitive contains no full workflow graphs or DAG edges.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches pattern `p12_wp_{type}` or `p12_wp_{type}_{name}` | Mismatched IDs cause routing failures |
| H03 | `kind` is exactly `workflow_primitive` (literal match) | Kind drives the loader; wrong literal silently misroutes |
| H04 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H05 | `type` is one of: step, condition, loop, parallel, router, gate, merge | Unknown types break primitive resolution |
| H06 | `inputs` is a non-empty list with typed entries (name + type + required) | Untyped inputs break composition |
| H07 | `outputs` is a non-empty list with typed entries (name + type) | Untyped outputs break downstream consumption |
| H08 | Loop primitives have `max_iter` in range 1-100 | Unbounded loops are system killers |
| H09 | Parallel primitives have `merge_ref` pointing to a merge primitive | Fan-out without fan-in loses data |
| H10 | Gate primitives have numeric `threshold` | Thresholdless gates always pass — useless |
| H11 | Router primitives have `default_route` | Unmatched routes silently drop work |
| H12 | Total YAML size <= 4096 bytes | Oversized primitives exceed token budget |
| H13 | Primitive is atomic: one type, one operation, no workflow graphs | Compound primitives defeat the purpose of composition |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler | Mostly substantive | No filler; every line carries information |
| 2 | I/O typing precision (types match domain expectations, descriptions present) | 1.5 | Types are all "string" | Most types correct | Every type precisely matches the data it carries |
| 3 | Guard clause completeness (type-specific guards present and reasonable) | 1.5 | Missing required guards | Guards present but values questionable | Guards present with well-justified values |
| 4 | Composition metadata (composable_after/before lists match type semantics) | 1.0 | No composition metadata | Partial metadata | Complete composition rules for this type |
| 5 | Description clarity (one-line, actionable, matches what the primitive does) | 0.5 | Vague or missing | Present but generic | Precise one-line description of the operation |
| 6 | Error handling (on_error or retry_count defined where apownte) | 0.5 | No error handling | retry_count set | on_error with fallback primitive reference |
| 7 | Tags include `workflow_primitive` | 0.5 | Missing | Present but misspelled | Exactly `workflow_primitive` in tags list |
| 8 | Cross-primitive type compatibility (output types match expected input types of successor) | 1.0 | Types incompatible | Most compatible | All outputs type-match expected downstream inputs |
