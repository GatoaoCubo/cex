---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for lens validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: lens

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p02_lens_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "lens" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 12+ required fields present | Completeness |
| H07 | perspective is non-empty string | Must define a viewpoint |
| H08 | applies_to is list, len >= 1 | Must target at least one kind |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "lens" | 0.5 | 10 |
| S03 | Perspective section present in body | 1.0 | 10 |
| S04 | Filters section with concrete attributes | 1.0 | 10 |
| S05 | Application section with steps | 0.5 | 10 |
| S06 | Limitations section present | 0.5 | 10 |
| S07 | No filler phrases ("very important", "comprehensive", "in summary") | 1.0 | 10 |
| S08 | focus field is concrete, not abstract | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 8 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind lens [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Perspective identified and not duplicate (brain_query checked)
- [ ] Target artifact kinds known (applies_to scoped)
- [ ] Concrete filters listed (not abstract categories)
- [ ] Bias declared (null if neutral)
