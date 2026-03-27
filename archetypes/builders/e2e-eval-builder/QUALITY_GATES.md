---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for e2e_eval artifacts
---

# Quality Gates: e2e_eval

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses without error |
| H02 | id starts with p07_e2e_ |
| H03 | id == filename stem |
| H04 | kind == e2e_eval |
| H05 | pillar == P07 |
| H06 | quality == null |
| H07 | pipeline is non-empty string |
| H08 | stages is non-empty list |
| H09 | input is non-empty string |
| H10 | timeout is positive integer |
| H11 | environment is non-empty string |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | each stage has agent + assertion | 1.0 |
| S04 | expected_output is concrete (not vague) | 1.0 |
| S05 | data_fixtures present | 0.5 |
| S06 | cleanup procedure defined | 0.5 |
| S07 | density_score >= 0.80 | 1.0 |
| S08 | Pipeline Overview section present | 0.5 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
