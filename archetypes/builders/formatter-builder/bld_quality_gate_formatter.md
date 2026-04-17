---
id: p11_qg_formatter
kind: quality_gate
pillar: P11
title: "Gate: formatter"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "formatter — output transformation rules converting structured data to readable or consumable representations"
quality: 9.0
tags: [quality-gate, formatter, output-format, transformation, P11]
tldr: "Validates formatter artifacts: transform rule completeness, escaping strategy, null-field handling, and output example presence."
density_score: 0.91
llm_function: GOVERN
---
# Gate: formatter
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: formatter` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p05_fmt_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `formatter` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, target_format, input_type, rule_count, domain, quality, tags, tldr | Any missing field |
| H07 | `rule_count` matches number of rows in Formatting Rules table AND `rule_count` >= 1 | Mismatch or zero rules |
| H08 | `target_format` is one of: json, yaml, markdown, html, table, text, csv | Unlisted or absent value |
| H09 | `input_type` is documented (struct name, schema reference, or example type) | Input type unspecified |
| H10 | Escaping strategy declared (or explicitly marked N/A for plain text output) | Missing escape spec |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names input type and output format | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `formatter` and target format keyword | 0.05 | Both present=1.0, one=0.5 |
| S03 | Transform rules cover all declared input fields | 0.12 | All fields mapped=1.0, partial=0.5, none=0.0 |
| S04 | Input Specification section with structure and example | 0.10 | Present+example=1.0, spec only=0.5, absent=0.0 |
| S05 | Output Specification section with concrete formatted example | 0.12 | Present=1.0, absent=0.0 |
| S06 | Null/missing field behavior explicitly specified per rule | 0.10 | Explicit=1.0, implicit=0.3, absent=0.0 |
| S07 | Edge Cases section covers: null, empty string, special chars | 0.10 | All 3=1.0, 2=0.6, 1=0.3, 0=0.0 |
| S08 | Locale/i18n handling documented (dates, numbers, currency) or N/A stated | 0.08 | Documented=1.0, N/A stated=1.0, silent=0.0 |
| S09 | Truncation or overflow behavior specified | 0.08 | Specified=1.0, absent=0.0 |
| S10 | Boundary from `parser` and `response_format` stated | 0.07 | Both stated=1.0, one=0.5, absent=0.0 |
| S11 | `density_score` >= 0.80 | 0.05 | Met=1.0, below=0.0 |
| S12 | No filler phrases ("this formatter", "designed to", "various formats") | 0.03 | Clean=1.0, filler present=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for formatter calibration |
| >= 8.0 | PUBLISH — pool-eligible; transforms and escaping documented |
| >= 7.0 | REVIEW — usable but missing null-field handling or output example |
| < 7.0  | REJECT — redo; likely missing transform rules or escaping strategy |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Formatter is a thin wrapper; transform logic lives in an external library with public docs |
| approver | Engineer who owns the consuming pipeline |
| audit trail | Required: external library link, pipeline name, approver handle |
