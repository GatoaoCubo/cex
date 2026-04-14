---
id: p11_qg_parser
kind: quality_gate
pillar: P11
title: "Gate: parser"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: parser
quality: 9.0
tags: [quality-gate, parser, P11, P05, governance, data-extraction]
tldr: "Gates for parser artifacts — input format defined, extraction rules tested, output schema matched to consumer."
density_score: 0.85
llm_function: GOVERN
---
# Gate: parser
## Definition
| Field     | Value                                               |
|-----------|-----------------------------------------------------|
| metric    | extraction rule coverage + output schema fidelity   |
| threshold | 8.0                                                 |
| operator  | >=                                                  |
| scope     | all parser artifacts (P05)                          |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = parser silently skipped |
| H02 | id matches `^p05_parser_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "parser" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | input_format field names the raw source format (json, html, csv, plain_text, yaml, xml, or other) | Unknown input = undefined extraction behavior |
| H08 | extraction_rules list has >= 1 entry, each with field, method, and expression | Rules without expressions cannot be automated |
| H09 | output_schema block defines >= 1 field with name and type | Consumers need a contract before wiring |
| H10 | At least one extraction rule has required: true | A parser extracting only optional fields has no guaranteed output |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "parser" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | Each extraction rule expression tested with a passing sample input in examples block | 1.0 |
| S05 | error_handling block describes strategy for malformed input (skip, default, raise, or partial) | 1.0 |
| S06 | normalization_steps list documents transforms applied after extraction (trim, lowercase, cast, etc.) | 0.5 |
| S07 | fallback_rule defined for when primary extraction finds no match | 1.0 |
| S08 | edge_cases block lists >= 2 known malformed or ambiguous input variants | 1.0 |
| S09 | output_schema consumer field names the downstream artifact or service that receives output | 0.5 |
| S10 | extraction is idempotent — same input always produces same output (documented or trivially true) | 1.0 |
| S11 | performance_note states whether parser is line-by-line or document-level and expected throughput | 0.5 |
| S12 | No filler phrases ("this parser", "designed to extract", "various fields") | 1.0 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference parser for this input format |
| >= 8.0 | PUBLISH — wire to ingestion pipeline |
| >= 7.0 | REVIEW — add edge cases, fallback rule, or error handling |
| < 7.0  | REJECT — rework extraction rules and output schema |
## Bypass
| Field | Value |
|-------|-------|
| conditions | One-time migration requiring parser before full validation when input format is stable and small volume |
| approver | p05-chief |
| audit_trail | Log in records/audits/ with input sample, output produced, and timestamp |
| expiry | 48h — parser must pass all gates before production ingestion begins |
| never_bypass | H01 (YAML), H05 (quality null) |
