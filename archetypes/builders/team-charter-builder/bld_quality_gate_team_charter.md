---
kind: quality_gate
id: p12_qg_team_charter
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for team_charter
quality: 9.0
title: "Quality Gate Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, quality_gate, governance]
tldr: "Quality gate with HARD and SOFT scoring for team_charter"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Charter governance completeness | 100% required fields | equals | All team_charter artifacts |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p12_tc_[a-z][a-z0-9_]+_v[0-9]+\\.md$ | ID format mismatch |
| H03 | kind field equals "team_charter" | Kind field incorrect or missing |
| H04 | charter_id present and unique | Missing or duplicate charter_id |
| H05 | crew_template_ref resolves to existing file | Dangling reference or missing |
| H06 | mission_statement includes deadline | No temporal anchor in mission statement |
| H07 | budget.tokens, budget.time_hours, budget.cost_usd all present | Any budget sub-field missing |
| H08 | termination_criteria covers SUCCESS, FAILURE, TIMEOUT | Any termination condition missing |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Mission statement quality (action + object + deadline + outcome) | 0.25 | All 4 elements present = 1.0, 3 = 0.75, 2 = 0.5, < 2 = 0 |
| D02 | OKR completeness (1 Objective + >= 2 numeric Key Results) | 0.25 | Full OKR with numeric thresholds = 1.0, prose only = 0.5, absent = 0 |
| D03 | Budget specificity (all 3 sub-fields + ceiling ratio >= 1.5x) | 0.20 | All fields + ratio = 1.0, all fields no ratio = 0.7, partial = 0.3 |
| D04 | Stakeholder RACI completeness (all 4 roles assigned) | 0.15 | All 4 RACI roles = 1.0, 3 = 0.75, < 3 = 0 |
| D05 | Escalation protocol coverage (>= 3 IF-THEN rules) | 0.15 | >= 3 rules = 1.0, 2 = 0.75, 1 = 0.5, 0 = 0 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN | >= 9.5 | Archive as gold example + auto-authorize for dispatch |
| PUBLISH | >= 8.0 | Authorize for N07 dispatch |
| REVIEW | >= 7.0 | Require N07 manual review before dispatch |
| REJECT | < 7.0 | Reject; rebuild from output_template |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|----------|-------------|
| Emergency GDP override (time-critical mission) | User explicit approval | Charter v1 flagged as emergency; review post-mission |
