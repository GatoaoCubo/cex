---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for guardrail artifacts
---

# Quality Gates: guardrail

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p11_gr_ |
| H03 | id == filename stem |
| H04 | kind == guardrail |
| H05 | pillar == P11 |
| H06 | quality == null |
| H07 | severity in [critical, high, medium, low] |
| H08 | scope is non-empty string |
| H09 | enforcement in [block, warn, log] |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | Rules section has >= 3 concrete, measurable restrictions | 1.0 |
| S04 | Violations section has >= 2 specific examples | 1.0 |
| S05 | Enforcement section lists detection methods | 1.0 |
| S06 | Bypass section has approver and audit trail | 1.0 |
| S07 | No subjective language in rules ("be careful", "appropriate") | 0.5 |
| S08 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
