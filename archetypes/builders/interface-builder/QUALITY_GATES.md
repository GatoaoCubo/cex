---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for interface validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: interface

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p06_iface_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "interface" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 13+ required fields present | Completeness |
| H07 | methods is list, len >= 1, each has name/input/output | Method structure |
| H08 | backward_compatible is boolean | Type correctness |
| H09 | provider and consumer both present and non-empty | Bilateral requirement |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "interface" | 0.5 | 10 |
| S03 | Contract Definition section present and non-empty | 1.0 | 10 |
| S04 | Methods table present with all columns | 1.0 | 10 |
| S05 | Each method has description field | 0.5 | 10 |
| S06 | Versioning section present with backward_compatible note | 0.5 | 10 |
| S07 | No filler phrases ("this document", "in summary", "basically") | 1.0 | 10 |
| S08 | Mock Specification section present with example payload | 0.5 | 10 |
| S09 | deprecation section present (even if null) | 0.5 | 10 |
| S10 | density_score >= 0.80 (if provided) | 0.5 | 10 |

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
Primary: validate_artifact.py --kind interface [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Integration point identified (which two agents/systems?)
- [ ] No existing interface for same contract (brain_query checked)
- [ ] Methods defined with typed input/output
- [ ] Provider and consumer clearly identified
