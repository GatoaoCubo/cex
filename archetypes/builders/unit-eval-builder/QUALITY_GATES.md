---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for unit_eval artifacts
---

# Quality Gates: unit_eval

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p07_ue_ |
| H03 | id == filename stem |
| H04 | kind == unit_eval |
| H05 | pillar == P07 |
| H06 | quality == null |
| H07 | target is non-empty string |
| H08 | target_kind is non-empty string |
| H09 | assertions is non-empty list |
| H10 | timeout is positive integer |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | each assertion has gate_ref | 1.0 |
| S04 | expected_output is concrete (not vague) | 1.0 |
| S05 | setup and teardown present | 0.5 |
| S06 | coverage_scope defined | 0.5 |
| S07 | density >= 0.80 | 1.0 |
| S08 | edge_case explicitly set | 0.5 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
