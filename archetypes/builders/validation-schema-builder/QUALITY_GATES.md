---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for validation_schema validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: validation_schema

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p06_vs_ |
| H03 | id == filename stem |
| H04 | kind == validation_schema |
| H05 | pillar == P06 |
| H06 | quality == null |
| H07 | all 17 required fields present |
| H08 | fields_count >= 1 |
| H09 | on_failure in [reject, warn, auto_fix] |
| H10 | format in [json, yaml] |
| H11 | target_kind is non-empty string |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "validation-schema" | 0.5 |
| S03 | Fields table present with name, type, required, constraints | 1.0 |
| S04 | Failure Handling section with remediation | 1.0 |
| S05 | Integration section with pipeline position | 1.0 |
| S06 | Schema Overview explains what is validated | 1.0 |
| S07 | No filler prose (no "looks correct", "should be good") | 1.0 |
| S08 | Field types are JSON-compatible (string, integer, number, boolean, array, object) | 0.5 |
| S09 | density >= 0.80 | 1.0 |

## Scoring
```text
hard_pass = all 11 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind validation_schema [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target kind identified with its _schema.yaml read
- [ ] Field list derived from target kind's required fields
- [ ] on_failure strategy decided (reject/warn/auto_fix)
- [ ] No confusion with response_format (P05)
