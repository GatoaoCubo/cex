---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for axiom validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: axiom

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p10_ax_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "axiom" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 13 required fields present | Completeness |
| H07 | tags is list, len >= 3 | Searchability minimum |
| H08 | rule field is ONE sentence (no period-separated compounds) | Atomicity |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | rationale present with >= 2 reasons | 1.0 | 10 |
| S03 | scope names concrete domain boundary | 1.0 | 10 |
| S04 | enforcement describes detection mechanism | 1.0 | 10 |
| S05 | immutable == true present | 0.5 | 10 |
| S06 | Body has all 7 required sections | 1.0 | 10 |
| S07 | Examples section has >= 2 cases | 1.0 | 10 |
| S08 | Violations section has >= 1 breach scenario | 1.0 | 10 |
| S09 | density >= 0.80 (no filler phrases) | 1.0 | 10 |
| S10 | keywords present, len >= 2 | 0.5 | 10 |

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
Primary: validate_artifact.py --kind axiom [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Candidate rule identified as truly immutable
- [ ] No existing axiom covers same truth (brain_query checked)
- [ ] Scope boundary clearly defined
- [ ] Can articulate at least one violation scenario
