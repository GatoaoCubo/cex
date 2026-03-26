---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for pattern validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: pattern

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p08_pat_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "pattern" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 14 required fields present | Completeness |
| H07 | tags is list, len >= 3 | Searchability minimum |
| H08 | name is non-empty, 2-5 words | Pattern must be clearly named |
| H09 | problem describes recurring situation | One-off fixes are not patterns |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | forces present, len >= 2 | 1.0 | 10 |
| S03 | consequences include >= 1 cost (not benefits-only) | 1.0 | 10 |
| S04 | Examples section has >= 2 concrete applications | 1.0 | 10 |
| S05 | Anti-Patterns section has >= 1 wrong approach | 1.0 | 10 |
| S06 | Related Patterns section present with refs | 1.0 | 10 |
| S07 | Body has all 9 required sections | 1.0 | 10 |
| S08 | density >= 0.80 (no filler phrases) | 1.0 | 10 |
| S09 | Solution section is concrete (not abstract advice) | 1.0 | 10 |
| S10 | keywords present, len >= 2 | 0.5 | 10 |
| S11 | applicability describes both when-to-use and when-not | 0.5 | 10 |

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
Primary: validate_artifact.py --kind pattern [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Problem confirmed as recurring (not one-off)
- [ ] No existing pattern covers same solution (brain_query checked)
- [ ] At least 2 concrete examples of the pattern in practice
- [ ] Forces and consequences identifiable (not just benefits)
