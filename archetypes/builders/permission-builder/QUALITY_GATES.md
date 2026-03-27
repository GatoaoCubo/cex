---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for permission artifacts
---

# Quality Gates: permission

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p09_perm_ |
| H03 | id == filename stem |
| H04 | kind == permission |
| H05 | pillar == P09 |
| H06 | quality == null |
| H07 | read, write, execute each in [allow, deny, conditional] |
| H08 | scope is non-empty string |
| H09 | roles is non-empty list |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | Access Matrix has >= 2 roles with read/write/execute columns | 1.0 |
| S04 | Allow List has >= 2 explicit entries with justification | 1.0 |
| S05 | Deny List has >= 1 entry (deny overrides allow documented) | 1.0 |
| S06 | Audit section lists logged events with retention | 1.0 |
| S07 | Escalation section has approver and duration | 0.5 |
| S08 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
