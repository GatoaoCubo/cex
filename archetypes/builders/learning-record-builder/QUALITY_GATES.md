---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for learning_record validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: learning_record

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p10_lr_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "learning_record" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 15 required fields present | Completeness |
| H07 | tags is list, len >= 3 | Searchability minimum |
| H08 | topic is non-empty string | Learning must have subject |
| H09 | outcome in [SUCCESS, PARTIAL, FAILURE] | Enum strict |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | score is float 0.0-10.0 | 1.0 | 10 |
| S03 | Pattern section has >= 2 concrete steps | 1.0 | 10 |
| S04 | Anti-Pattern section has >= 1 specific failure | 1.0 | 10 |
| S05 | Context section names environment + timing | 1.0 | 10 |
| S06 | Impact section has measurable outcomes | 1.0 | 10 |
| S07 | Reproducibility section present with confidence | 1.0 | 10 |
| S08 | Body has all 7 required sections | 1.0 | 10 |
| S09 | density >= 0.80 (no filler phrases) | 1.0 | 10 |
| S10 | satellite field present | 0.5 | 10 |
| S11 | keywords present, len >= 2 | 0.5 | 10 |
| S12 | timestamp in ISO 8601 format | 0.5 | 10 |

## Scoring Formula
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
Primary: validate_artifact.py --kind learning_record [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Experience identified with clear outcome (SUCCESS/PARTIAL/FAILURE)
- [ ] No existing learning_record covers same experience (brain_query checked)
- [ ] Both pattern and anti-pattern identifiable
- [ ] Impact can be quantified (time, errors, quality delta)
