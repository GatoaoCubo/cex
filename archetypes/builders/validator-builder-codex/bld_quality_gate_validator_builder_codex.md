---
kind: quality_gate
id: bld_quality_gate_validator_builder_codex
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for validator validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: validator

## HARD Gates

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | broken metadata breaks automation |
| H02 | id matches `^p06_val_[a-z][a-z0-9_]+$` | namespace compliance |
| H03 | id == filename stem | indexing relies on stable naming |
| H04 | kind == `validator` | type integrity |
| H05 | pillar == `P06` and `quality == null` | correct pillar and no self-score |
| H06 | all required fields from SCHEMA are present | completeness |
| H07 | `trigger` in `pre_commit|post_generate|pre_pool|on_signal` | valid runtime hook |
| H08 | `severity` in `block|warn|info` | valid enforcement level |
| H09 | body includes Rule, Checks, Error Messages, Pass Example, Fail Example | canonical structure |
| H10 | every rule/check expression is objective and machine-checkable | prevents rubric drift |

## SOFT Gates

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | `tldr` non-empty and <= 160 chars | 1.0 | 10 |
| S02 | tags list has at least 3 items | 0.5 | 10 |
| S03 | at least 3 checks are listed | 1.0 | 10 |
| S04 | error messages are specific and actionable | 1.0 | 10 |
| S05 | pass and fail examples are concrete, not placeholders | 1.0 | 10 |
| S06 | density >= 0.80 | 1.0 | 10 |
| S07 | no scoring, weights, or subjective quality language | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 10 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5
PUBLISH: >= 8.0
REVIEW:  >= 7.0
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: `python _tools/validate_artifact.py --kind validator <file>` [PLANNED]
Interim: validate manually against this file.

## Pre-Production Checklist
- [ ] Source constraint for the rule is identified
- [ ] Boundary against `quality_gate` and `scoring_rubric` is explicit
- [ ] At least one PASS and one FAIL example are concrete
