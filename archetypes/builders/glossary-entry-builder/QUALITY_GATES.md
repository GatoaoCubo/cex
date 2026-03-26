---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for glossary_entry validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: glossary_entry

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p01_gl_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "glossary_entry" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 10+ required fields present | Completeness |
| H07 | definition <= 3 lines | Conciseness constraint |
| H08 | synonyms is list, len >= 1 | Must have at least one synonym |
| H09 | term is non-empty string | Must define something |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "glossary" | 0.5 | 10 |
| S03 | Definition section present in body | 1.0 | 10 |
| S04 | Definition includes concrete example | 0.5 | 10 |
| S05 | term is lowercase (unless proper noun) | 0.5 | 10 |
| S06 | Disambiguation section present (if similar terms exist) | 0.5 | 10 |
| S07 | No filler phrases ("very important", "basically", "in summary") | 1.0 | 10 |
| S08 | Related Terms section with cross-references | 0.5 | 10 |

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
Primary: validate_artifact.py --kind glossary_entry [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Term identified and not already in glossary (brain_query checked)
- [ ] Domain context known (where is this term used?)
- [ ] At least one synonym identified
- [ ] Definition drafted at <= 3 lines
