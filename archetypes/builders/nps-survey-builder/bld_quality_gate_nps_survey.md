---
kind: quality_gate
id: p11_qg_nps_survey
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for nps_survey
quality: 9.1
title: "Quality Gate Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for nps_survey"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric                   | Threshold | Operator | Scope                        |
|--------------------------|-----------|----------|------------------------------|
| Bain NPS standard        | 100%      | equals   | All nps_survey artifacts     |
| Scale range              | 0-10      | equals   | All score fields             |

## HARD Gates
| ID  | Check                                              | Fail Condition                              |
|-----|----------------------------------------------------|---------------------------------------------|
| H01 | YAML frontmatter valid                             | Invalid YAML or missing required fields     |
| H02 | ID matches `^p11_nps_[a-z][a-z0-9_]+\.yaml$`      | Pattern mismatch                            |
| H03 | kind = `nps_survey`                               | Wrong or missing kind                       |
| H04 | scale.min=0 AND scale.max=10                       | Non-Bain scale                              |
| H05 | survey_type is `transactional` or `relational`     | Missing or invalid type                     |
| H06 | Routing rules cover promoter, passive, detractor   | Any score band unrouted                     |
| H07 | follow_up_question present and open-ended          | Missing or scored follow-up                 |

## SOFT Scoring
| Dim | Dimension                                        | Weight | Scoring Guide                                              |
|-----|--------------------------------------------------|--------|------------------------------------------------------------|
| D01 | NPS question phrasing (Bain standard)            | 0.30   | Exact likelihood-to-recommend phrasing = 1.0, paraphrase = 0.5, missing = 0 |
| D02 | Segmentation specificity                         | 0.20   | Measurable filters (tier, tenure, ARR) = 1.0, generic = 0.5, absent = 0 |
| D03 | Cadence completeness (frequency + cooldown)      | 0.20   | Both present = 1.0, frequency only = 0.5, neither = 0     |
| D04 | Routing destination specificity                  | 0.20   | Named system per band = 1.0, generic = 0.5, missing = 0   |
| D05 | Follow-up question quality                       | 0.10   | Band-specific + open-ended = 1.0, generic = 0.5, absent = 0|

## Actions
| Score   | Threshold | Action                              |
|---------|-----------|-------------------------------------|
| GOLDEN  | >=9.5     | Auto-publish, no review             |
| PUBLISH | >=8.0     | Auto-publish after validation       |
| REVIEW  | >=7.0     | Require manual review               |
| REJECT  | <7.0      | Reject and flag for rework          |

## Bypass
| Condition                  | Approver     | Audit Trail         |
|----------------------------|--------------|---------------------|
| Emergency churn spike      | CS Director  | Escalation log      |
