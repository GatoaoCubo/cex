---
id: p11_qg_few_shot_example
kind: quality_gate
pillar: P11
title: "Gate: few_shot_example"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "few_shot_example — input/output pairs that teach format to LLMs via in-context prompt engineering"
quality: 9.0
tags: [quality-gate, few-shot-example, prompt-engineering, format-teaching, P11]
tldr: "Validates few_shot_example artifacts: input/output completeness, format demonstration clarity, and byte-size constraint."
density_score: 0.90
llm_function: GOVERN
---
# Gate: few_shot_example
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: few_shot_example` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p01_fse_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `few_shot_example` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | `input` field present and non-empty string | Missing or empty input |
| H07 | `output` field present and non-empty string | Missing or empty output |
| H08 | Artifact body size <= 1024 bytes | Exceeds byte limit (bloats prompt context) |
| H09 | No scoring rubric present anywhere in the artifact | Rubric found (conflates with golden_test) |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names the format being taught | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `few-shot` | 0.05 | Met=1.0, partial=0.5 |
| S03 | Output demonstrates FORMAT visibly (structure present, not just content) | 0.18 | Clear structure=1.0, content-only=0.2 |
| S04 | Input is a realistic task request (not abstract or contrived) | 0.14 | Realistic=1.0, contrived=0.3 |
| S05 | Explanation section present and explains why the output format is correct | 0.12 | Present+explains=1.0, missing=0.0 |
| S06 | Example is self-contained (no external reference required to understand it) | 0.10 | Self-contained=1.0, requires context=0.2 |
| S07 | Example covers a non-trivial pattern (edge case or formatting nuance) | 0.10 | Non-trivial=1.0, trivial happy-path=0.4 |
| S08 | `density_score` >= 0.80 | 0.08 | Met=1.0, below=0.0 |
| S09 | No filler in output ("as you can see", "this example shows") | 0.07 | Clean=1.0, filler present=0.0 |
| S10 | Difficulty level (`easy`/`medium`/`hard`) matches actual complexity | 0.06 | Accurate=1.0, mislabeled=0.2 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for few_shot_example calibration |
| >= 8.0 | PUBLISH — pool-eligible; format clearly demonstrated in output |
| >= 7.0 | REVIEW — usable but output may be content-heavy, not format-focused |
| < 7.0  | REJECT — redo; likely missing format structure or oversized body |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Domain so narrow that no realistic input exists; synthetic input approved in writing |
| approver | Prompt engineer who owns the target prompt template |
| audit trail | Required: target prompt ID, justification for synthetic input, approver name |
| expiry | Permanent until a realistic example is available to replace it |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality is invalid), H08 (byte limit protects prompt context budgets — non-negotiable) |
