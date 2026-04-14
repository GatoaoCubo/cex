---
id: p11_qg_feature_flag
kind: quality_gate
pillar: P11
title: "Gate: feature_flag"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "feature_flag — on/off toggles with rollout percentage, cohort targeting, and kill switch behavior"
quality: 9.0
tags: [quality-gate, feature-flag, toggle, rollout, P11]
tldr: "Validates feature_flag artifacts: toggle semantics, rollout strategy completeness, and kill switch safety."
density_score: 0.91
llm_function: GOVERN
---
# Gate: feature_flag
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: feature_flag` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p09_ff_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `feature_flag` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, flag_name, default_state, category, rollout_percentage, quality, tags, tldr | Any missing field |
| H07 | Body has sections: `## Flag Specification`, `## Rollout Strategy`, `## Lifecycle` | Any required section absent |
| H08 | `default_state` is one of: `on`, `off` | Any other value |
| H09 | `rollout_percentage` is integer 0–100 | Out of range or non-integer |
| H10 | `category` is one of: `release`, `experiment`, `ops`, `permission` | Any unlisted value |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names flag and toggle behavior | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `feature_flag` | 0.05 | Met=1.0, partial=0.5 |
| S03 | `flag_name` is snake_case and descriptive | 0.07 | Snake_case+descriptive=1.0, generic=0.3 |
| S04 | Rollout strategy has stages with explicit percentages | 0.12 | All stages=1.0, partial=0.5, absent=0.0 |
| S05 | Kill switch behavior documented | 0.10 | Explicit=1.0, implied=0.4, absent=0.0 |
| S06 | Cohort targeting rules defined when `rollout_percentage` < 100 | 0.10 | Defined=1.0, missing when needed=0.0, N/A=1.0 |
| S07 | Lifecycle section includes retire or sunset date | 0.08 | Present=1.0, absent=0.0 |
| S08 | Rollback procedure described step-by-step | 0.10 | Step-by-step=1.0, brief=0.5, absent=0.0 |
| S09 | Observability hook defined (metric or log emitted on toggle change) | 0.10 | Present=1.0, absent=0.0 |
| S10 | Boundary from `env_config` and `permission` stated | 0.08 | Both stated=1.0, one=0.5, absent=0.0 |
| S11 | `density_score` >= 0.80 | 0.07 | Met=1.0, below=0.0 |
| S12 | No filler phrases ("designed to enable", "various use cases") | 0.03 | Clean=1.0, filler present=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for feature_flag calibration |
| >= 8.0 | PUBLISH — pool-eligible; rollout strategy and kill switch documented |
| >= 7.0 | REVIEW — usable but missing sunset date or observability hook |
| < 7.0  | REJECT — redo; likely missing rollback procedure or cohort rules |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Hotfix rollout only; flag controls an active incident mitigation with no time to complete all gates |
| approver | Product owner or on-call engineer |
| audit trail | Required: incident ticket, timestamp, approver handle |
| expiry | 24 hours; must be replaced with compliant artifact |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality is invalid), H08 (boolean semantics must be exact for runtime evaluation) |
