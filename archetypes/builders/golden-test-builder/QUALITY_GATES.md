---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for golden_test artifacts
---

# Quality Gates: golden_test

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p07_gt_ |
| H03 | id == filename stem |
| H04 | kind == golden_test |
| H05 | pillar == P07 |
| H06 | quality == null |
| H07 | quality_threshold >= 9.5 |
| H08 | target_kind is non-empty string |
| H09 | Golden Output section present and non-empty |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | rationale references gate IDs (H/S pattern) | 1.0 |
| S04 | Input Scenario section present | 1.0 |
| S05 | Evaluation Criteria section present | 1.0 |
| S06 | reviewer is non-empty | 0.5 |
| S07 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
