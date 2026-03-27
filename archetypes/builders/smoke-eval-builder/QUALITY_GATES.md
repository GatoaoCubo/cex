---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for smoke_eval artifacts
---

# Quality Gates: smoke_eval

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p07_se_ |
| H03 | id == filename stem |
| H04 | kind == smoke_eval |
| H05 | pillar == P07 |
| H06 | quality == null |
| H07 | timeout <= 30 seconds |
| H08 | fast_fail == true |
| H09 | critical_path is non-empty list |
| H10 | assertions is non-empty list |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | scope is descriptive (not generic) | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | tldr < 160 chars | 1.0 |
| S04 | each assertion has timeout_ms | 0.5 |
| S05 | prerequisites listed | 0.5 |
| S06 | On Failure section present | 1.0 |
| S07 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
