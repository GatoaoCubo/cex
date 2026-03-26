---
lp: P11
llm_function: GOVERN
purpose: Quality gates for quality_gate artifacts (recursive)
note: this file IS an instance of what the builder produces
---

# Quality Gates: quality_gate

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p11_qg_ |
| H03 | id == filename stem |
| H04 | type == quality_gate |
| H05 | lp == P11 |
| H06 | quality == null |
| H07 | title is non-empty |
| H08 | Definition table has numeric threshold |
| H09 | Scoring table present |
| H10 | scoring weights sum to 100% |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | Checklist >= 3 items | 1.0 |
| S04 | Actions table present | 1.0 |
| S05 | Bypass section present | 1.0 |
| S06 | No subjective language | 0.5 |
| S07 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
