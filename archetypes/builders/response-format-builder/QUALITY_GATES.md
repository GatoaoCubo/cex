---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for response_format validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: response_format

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p05_rf_ |
| H03 | id == filename stem |
| H04 | kind == response_format |
| H05 | pillar == P05 |
| H06 | quality == null |
| H07 | all 17 required fields present |
| H08 | sections_count >= 1 |
| H09 | format_type in [json, yaml, markdown, csv, plaintext] |
| H10 | injection_point in [system_prompt, user_message] |
| H11 | target_kind is non-empty string |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "response-format" | 0.5 |
| S03 | Sections table present with ordered entries | 1.0 |
| S04 | Example Output section with complete concrete example | 1.0 |
| S05 | Injection Instructions with point and template | 1.0 |
| S06 | Format Overview explains purpose and target | 1.0 |
| S07 | No filler prose (no "looks good", "appropriate", "well-structured") | 1.0 |
| S08 | sections list matches sections table entries | 0.5 |
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
Primary: validate_artifact.py --kind response_format [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target kind identified with output requirements understood
- [ ] Format type chosen based on consumption pattern (json for machines, markdown for humans)
- [ ] Injection point decided (system_prompt for persistent, user_message for per-request)
- [ ] No confusion with validation_schema (P06)
