---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for instruction validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: instruction

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p03_ins_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "instruction" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 20 required fields present | Completeness |
| H07 | body has ## Steps section with numbered items | Steps are the essence |
| H08 | rollback defined if atomic: false | Partial execution needs undo path |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "instruction" | 0.5 | 10 |
| S03 | steps_count matches actual numbered steps in body | 1.0 | 10 |
| S04 | Each step has exactly one action (no compound) | 1.0 | 10 |
| S05 | Prerequisites are verifiable (not vague) | 1.0 | 10 |
| S06 | body has ## Prerequisites section | 0.5 | 10 |
| S07 | body has ## Validation section with checks | 0.5 | 10 |
| S08 | body has ## Rollback section | 0.5 | 10 |
| S09 | No identity/persona content (boundary check) | 1.0 | 10 |
| S10 | density_score >= 0.80 | 0.5 | 10 |
| S11 | No filler phrases ("this document", "in summary") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind instruction [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Task identified with clear scope
- [ ] No existing instruction for this task (brain_query checked)
- [ ] Prerequisites and dependencies enumerated
