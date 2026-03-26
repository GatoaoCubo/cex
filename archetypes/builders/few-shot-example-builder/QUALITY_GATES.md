---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for few_shot_example validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: few_shot_example

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id matches `^p01_fse_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on exact match |
| H04 | kind == "few_shot_example" | Type integrity |
| H05 | quality == null | Never self-score — evaluation is external |
| H06 | input field present and non-empty string | Incomplete pair has zero learning value |
| H07 | output field present and non-empty string | Incomplete pair has zero learning value |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "few-shot" | 0.5 | 10 |
| S03 | Explanation section present and non-empty | 1.0 | 10 |
| S04 | input is realistic task request (not abstract) | 1.0 | 10 |
| S05 | output demonstrates format clearly (not describes) | 1.0 | 10 |
| S06 | body <= 1024 bytes | 1.0 | 10 |
| S07 | no scoring rubric present (not golden_test) | 1.0 | 10 |

## Scoring Formula

```text
hard_pass = all 7 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind few_shot_example [PLANNED]
Interim: validate manually against this file, checking each gate in order.

## Pre-Production Checklist
- [ ] Domain identified (what artifact kind or format is being exemplified?)
- [ ] No existing few_shot_example for same domain+difficulty (brain_query checked)
- [ ] input is a specific, realistic task request
- [ ] output is a complete format demonstration (not a description)
- [ ] quality: null in frontmatter
- [ ] id matches p01_fse_ pattern and equals filename stem
- [ ] No scoring rubric anywhere in the artifact
