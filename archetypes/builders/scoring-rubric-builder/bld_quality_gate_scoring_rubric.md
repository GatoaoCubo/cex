---
id: p11_qg_scoring-rubric
kind: quality_gate
pillar: P11
title: "Gate: Scoring Rubric"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: scoring_rubric
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - scoring-rubric
  - evaluation
  - p11
tldr: "Gates ensuring scoring rubric files define measurable dimensions, justified weights summing to 100%, and calibrated tier thresholds."
llm_function: GOVERN
---
## Definition
A scoring rubric is an evaluation framework that rates a target artifact on multipland weighted dimensions and maps the aggregate score to an action tier. A rubric passes this gate when a reviewer with no prior context could apply it consistently, two independent reviewers would reach scores within 1.0 point of each other on the same input, and the tier thresholds match established system standards.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`scoring-rubric-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `scoring_rubric` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Dimensions list** with >= 3 named dimensions, each with a description | Fewer than 3 dimensions cannot capture meaningful variation in artifact quality |
| H08 | Spec contains **Weights** for all dimensions, and weights sum to exactly 100% (or normalize to 100%) | Unbalanced weights produce scores that cannot be compared across rubric versions |
| H09 | Spec contains **Tier thresholds** for >= 3 distinct tiers (e.g., GOLDEN / PUBLISH / REVIEW / REJECT) with numeric boundaries | Without tiers, a score is a number with no actionable meaning |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Each dimension has concrete scale descriptors (what 1, 5, 10 look like) | 1.0 | No descriptors | Endpoint anchors only (1 and 10) | Full anchors at 1, 5, and 10 with examples |
| 3 | Weights justified by utility impact (rationale provided per weight) | 1.0 | No justification | One-sentence generic rationale | Per-dimension rationale tied to artifact utility |
| 4 | Tiers align with standard thresholds (>= 9.5 golden, >= 8.0 publish, >= 7.0 review, < 7.0 reject) | 1.0 | Custom non-standard thresholds | Partially aligned | Exact alignment with system standards |
| 5 | Calibration via golden tests referenced (pointer to 1+ example with known scores) | 0.5 | No calibration reference | Reference named but not accessible | Accessible example with expected score documented |
| 6 | Tags include `scoring-rubric` | 0.5 | Missing | Present but misspelled | Exactly `scoring-rubric` in tags list |
| 7 | Automation status per dimension (manual / semi-auto / fully automated) | 0.5 | No automation noted | Some dimensions labeled | All dimensions labeled with tool or check reference |
| 8 | Inter-rater guidance (instructions for resolving disagreements between reviewers) | 1.0 | No guidance | General tiebreaker rule | Specific procedure with escalation path |
