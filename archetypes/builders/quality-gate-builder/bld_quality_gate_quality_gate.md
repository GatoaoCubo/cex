---
id: p11_qg_quality_gate
kind: quality_gate
pillar: P11
title: "Gate: Quality Gate"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: quality_gate
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - p11
  - scoring
  - governance
  - recursive
tldr: "Recursive quality gate for quality_gate artifacts: verifies HARD/SOFT structure, weight math, and bypass rules."
llm_function: GOVERN
---
## Definition
A quality gate artifact defines the acceptance criteria for one artifact kind. It contains blocking HARD gates (binary pass/fail), a weighted SOFT scoring table, a four-tier action map, and a bypass policy. This gate is self-applicable: it evaluates other quality gate files, including itself.
Scope: files with `kind: quality_gate`. Does not apply to scoring rubrics (P08), validators (P07), or benchmark suites (P13).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p11_qg_*` | `id.startswith("p11_qg_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `quality_gate` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | HARD gates section present with >= 6 gates | count rows in HARD Gates table >= 6 |
| H08 | SOFT scoring table present with weights that sum to 100% when normalized | sum(weight_i / total_weight) == 1.0 within float tolerance |
| H09 | Actions section present with all four tiers: GOLDEN, PUBLISH, REVIEW, REJECT | all four tier names present in Actions table |
| H10 | Bypass section present with condition, approver, audit_log, and expiry fields | all four fields non-empty in Bypass table |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Universal HARD gates H01-H06 (YAML, id namespace, id=filename, kind, quality null, required fields) are all present | 1.0 |
| 3  | SOFT weights use only values 0.5 or 1.0 (no fractional intermediates) | 0.5 |
| 4  | Scoring formula is documented inline (not just assumed) | 1.0 |
| 5  | Bypass section explicitly states H01 and H05 cannot be bypassed | 1.0 |
| 6  | Tags list includes `quality-gate` | 0.5 |
| 7  | Tier thresholds match standard: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0 | 1.0 |
| 8  | Every gate predicate is testsble (binary outcome, no subjective language) | 1.0 |
| 9  | Gate set is domain-adapted, not a copy-paste of a generic template | 1.0 |
| 10 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for new gate authors |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Gate covers an experimental artifact kind in active design (schema not yet stable) |
| approver | Pillar owner must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 14 days from bypass grant; gate must reach full compliance before expiry |
