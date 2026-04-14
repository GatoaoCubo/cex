---
id: p11_qg_golden_test
kind: quality_gate
pillar: P11
title: "Gate: golden_test"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "golden_test — reference quality calibration cases scoring 9.5+ with rationale mapped to evaluation gates"
quality: 9.0
tags: [quality-gate, golden-test, calibration, evaluation, quality-baseline, P11]
tldr: "Validates golden_test artifacts: verified 9.5+ source quality, rationale-to-gate mapping, and non-self-referential target kind."
density_score: 0.93
llm_function: GOVERN
---
# Gate: golden_test
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden (the golden_test itself must also reach 9.5) |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: golden_test` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p07_gt_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `golden_test` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, target_kind, quality_threshold, reviewer, domain, quality, tags, tldr | Any missing field |
| H07 | `quality_threshold` >= 9.5 | Threshold below the golden standard |
| H08 | `target_kind` is non-empty and NOT `golden_test` | Self-referential calibration |
| H09 | `Golden Output` section present and non-empty | No reference output to calibrate against |
| H10 | `Input Scenario` section present and non-empty | No input; test is unverifiable |
| H11 | `rationale` references at least one gate ID (pattern: H\d+ or S\d+) | No gate mapping; rationale is unstructured |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names `target_kind` and what makes this golden | 0.10 | Named=1.0, vague=0.3 |
| S02 | Tags list len >= 3, includes `target_kind` as keyword | 0.06 | Present=1.0, absent=0.0 |
| S03 | Rationale maps to >= 3 distinct gate IDs of `target_kind` | 0.15 | 3+=1.0, 2=0.6, 1=0.3, 0=0.0 |
| S04 | Golden Output is complete and copy-pasteable as a real artifact | 0.14 | Complete=1.0, skeleton=0.4, absent=0.0 |
| S05 | Input Scenario is non-trivial (edge case or high-complexity scenario) | 0.12 | Edge/complex=1.0, trivial=0.3 |
| S06 | Boundary from `few_shot_example` stated (teaches format vs. evaluates quality) | 0.09 | Explicit=1.0, implied=0.4, absent=0.0 |
| S07 | Boundary from `unit_eval` stated | 0.07 | Explicit=1.0, implied=0.4, absent=0.0 |
| S08 | Verification source cited for 9.5+ quality claim (reviewer name or process) | 0.10 | Cited=1.0, absent=0.0 |
| S09 | Evaluation Criteria section present with pass/fail conditions | 0.10 | Present=1.0, absent=0.0 |
| S10 | `density_score` >= 0.85 (golden tests must be information-dense) | 0.07 | Met=1.0, below=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — accepted into calibration set; informs all future scoring for `target_kind` |
| >= 8.0 | PUBLISH — pool-eligible reference; not yet calibration-authoritative |
| >= 7.0 | REVIEW — rationale incomplete or verification source missing |
| < 7.0  | REJECT — redo; likely unverified source quality or missing gate mapping |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Bootstrap only: first golden_test for a brand-new kind where no prior calibration set exists |
| approver | Two independent reviewers must sign off in lieu of automated verification |
| audit trail | Required: both reviewer names, review date, written agreement on quality assessment |
