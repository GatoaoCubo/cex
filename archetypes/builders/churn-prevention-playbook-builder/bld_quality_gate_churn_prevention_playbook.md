---
kind: quality_gate
id: p03_qg_churn_prevention_playbook
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for churn_prevention_playbook
quality: 9.1
title: "Quality Gate Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for churn_prevention_playbook"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric                        | Threshold | Operator | Scope                              |
|-------------------------------|-----------|----------|------------------------------------|
| Gainsight/ChurnZero alignment | 100%      | equals   | All playbook artifacts             |
| Save script completeness      | 4 sections| min      | opening + discovery + objections + close |

## HARD Gates
| ID  | Check                                                       | Fail Condition                         |
|-----|-------------------------------------------------------------|----------------------------------------|
| H01 | YAML frontmatter valid                                      | Invalid YAML or missing required fields|
| H02 | ID matches `^p03_cpp_[a-z][a-z0-9_]+\.md$`                 | Pattern mismatch                       |
| H03 | kind = `churn_prevention_playbook`                         | Wrong or missing kind                  |
| H04 | health_score_model present with >= 3 components             | Incomplete health model                |
| H05 | intervention_triggers covers red-zone AND pre-renewal       | Missing trigger coverage               |
| H06 | Save script has opening, discovery, objections, close       | Incomplete script structure            |
| H07 | Win-back sequence has >= 3 touchpoints                      | Insufficient win-back coverage         |

## SOFT Scoring
| Dim | Dimension                                           | Weight | Scoring Guide                                                  |
|-----|-----------------------------------------------------|--------|----------------------------------------------------------------|
| D01 | Health score model completeness                     | 0.25   | 5 components (usage, NPS, support, engagement, contract) = 1.0, 3-4 = 0.7, <3 = 0.3 |
| D02 | Churn reason taxonomy coverage                      | 0.20   | All 4 reasons (product, budget, competitor, champion) = 1.0, 2-3 = 0.6, <2 = 0.2 |
| D03 | Objection handler specificity                       | 0.20   | Named objections with scripts = 1.0, generic = 0.5, absent = 0|
| D04 | Escalation path completeness                        | 0.15   | CSM -> VP CS -> exec = 1.0, CSM -> mgr only = 0.6, single hop = 0.2 |
| D05 | Win-back sequence quality                           | 0.20   | 3+ touchpoints + personalization hooks = 1.0, generic = 0.5, absent = 0 |

## Actions
| Score   | Threshold | Action                              |
|---------|-----------|-------------------------------------|
| GOLDEN  | >=9.5     | Auto-publish, no review             |
| PUBLISH | >=8.0     | Auto-publish after validation       |
| REVIEW  | >=7.0     | Require CS Director review          |
| REJECT  | <7.0      | Reject -- rebuild with save script  |

## Bypass
| Condition                  | Approver     | Audit Trail              |
|----------------------------|--------------|--------------------------|
| Emergency churn spike      | VP CS        | Incident log             |
