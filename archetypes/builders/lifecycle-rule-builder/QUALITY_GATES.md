```yaml
---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for lifecycle_rule artifacts
---
```

# Quality Gates: lifecycle_rule

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p11_lc_ |
| H03 | id == filename stem |
| H04 | kind == lifecycle_rule |
| H05 | pillar == P11 |
| H06 | quality == null |
| H07 | freshness_days is positive integer |
| H08 | review_cycle in [weekly, monthly, quarterly, yearly] |
| H09 | scope, ownership are non-empty strings |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | States table has >= 3 states | 1.0 |
| S04 | Transitions table has >= 3 transitions | 1.0 |
| S05 | Automation section lists concrete methods | 1.0 |
| S06 | Review Protocol section present with reviewer and cycle | 1.0 |
| S07 | No subjective triggers ("feels outdated", "when needed") | 0.5 |
| S08 | density >= 0.80 | 1.0 |

## Scoring
```text
hard_pass = all 9 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind lifecycle_rule [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Artifact kind to govern is identified
- [ ] No existing lifecycle_rule for same scope (check P11_feedback/examples/)
- [ ] Freshness period researched (domain volatility known)
