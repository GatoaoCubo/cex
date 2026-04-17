---
id: p11_qg_reasoning_trace
kind: quality_gate
pillar: P11
title: "Gate: Reasoning Trace"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: builder
domain: reasoning_trace
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - reasoning_trace
  - cognition
  - p11
tldr: "Gates ensuring reasoning traces define complete step-evidence-confidence chains, record rejected alternatives, calibrate confidence scores, and contain no execution instructions."
llm_function: GOVERN
---
## Definition
A reasoning_trace is a structured decision record capturing WHY an agent chose a particular path. It passes this gate when every step has concrete evidence, confidence is calibrated to the 0.0-1.0 scale, at least one alternative is rejected with an evidence-based reason, the conclusion references the strongest evidence, and the trace contains no execution instructions or workflow logic.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches pattern `p03_rt_{agent}_{timestamp}` | Mismatched IDs cause routing failures |
| H03 | `kind` is exactly `reasoning_trace` (literal match) | Kind drives the loader; wrong literal silently misroutes |
| H04 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H05 | `agent` field is non-empty string | Traces without agent attribution cannot be audited |
| H06 | `intent` field is non-empty string | Traces without intent have no decision context |
| H07 | `steps` is a non-empty list with >= 2 entries | Single-step traces are assertions, not reasoning chains |
| H08 | Each step has non-empty `thought`, `evidence`, and `confidence` fields | Missing fields break the step-evidence-confidence contract |
| H09 | All `confidence` values are numeric in range 0.0-1.0 | Out-of-range values break geometric mean calculation |
| H10 | `conclusion` is non-empty string | Traces without conclusions are incomplete |
| H11 | `timestamp` is valid ISO 8601 datetime | Untimestamped traces cannot be ordered or deduplicated |
| H12 | Total YAML size <= 8192 bytes | Oversized traces exceed budget and slow consumers |
| H13 | Trace contains NO execution instructions or action items | Reasoning traces record WHY, not WHAT to do |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Evidence concreteness (references specific data, files, metrics vs vague claims) | 1.5 | Vague assertions ("it seemed better") | Some references ("benchmark showed improvement") | All steps cite specific metrics, files, or data points |
| 3 | Confidence calibration (scores match evidence strength, not over/under-confident) | 1.5 | All steps 0.9+ regardless of evidence | Most steps reasonably calibrated | Confidence clearly tracks evidence strength; low evidence = low confidence |
| 4 | Alternatives rejected with reasons (at least 1 rejected path with evidence-based reason) | 1.0 | No alternatives listed | Alternatives listed without reasons | Each alternative has specific evidence-based rejection reason |
| 5 | Conclusion references evidence (final decision cites strongest supporting data) | 1.0 | Conclusion is unsupported opinion | Conclusion mentions evidence vaguely | Conclusion directly references specific step evidence |
| 6 | Step ordering is logical (chronological or logical progression, no jumps) | 0.5 | Steps in random order | Mostly ordered | Clear logical/chronological progression |
| 7 | Tags include `reasoning_trace` | 0.5 | Missing | Present but misspelled | Exactly `reasoning_trace` in tags list |
| 8 | Duration_ms present when timing data available | 0.5 | Timing available but omitted | Present but approximate | Precise timing data included |
