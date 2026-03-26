---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for scoring_rubric artifacts
---

# Quality Gates: scoring_rubric

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p07_sr_ |
| H03 | id == filename stem |
| H04 | kind == scoring_rubric |
| H05 | pillar == P07 |
| H06 | quality == null |
| H07 | dimension weights sum to exactly 100% |
| H08 | dimensions_count >= 3 |
| H09 | automation_status in [manual, semi-automated, automated] |
| H10 | all 4 tiers defined (GOLDEN, PUBLISH, REVIEW, REJECT) |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | criteria are concrete per dimension (no subjective language) | 1.0 |
| S04 | Framework Overview section present | 1.0 |
| S05 | Calibration section has examples at >= 3 tiers | 1.0 |
| S06 | Automation section lists status per dimension | 1.0 |
| S07 | scale defined per dimension (0-10 or labeled) | 0.5 |
| S08 | no dimension overlap (each measures ONE thing) | 1.0 |
| S09 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
