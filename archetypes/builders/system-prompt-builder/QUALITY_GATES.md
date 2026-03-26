---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for system_prompt validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: system_prompt

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p03_sp_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "system_prompt" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 19 required fields present | Completeness |
| H07 | body has ## Identity section | Core identity required |
| H08 | body has ## Rules section with numbered items | Rules are the essence |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "system_prompt" | 0.5 | 10 |
| S03 | rules_count matches actual numbered rules in body | 1.0 | 10 |
| S04 | Rules use ALWAYS/NEVER pattern | 1.0 | 10 |
| S05 | Identity defines domain expertise (not generic) | 1.0 | 10 |
| S06 | body has ## Output Format section | 0.5 | 10 |
| S07 | body has ## Constraints section with boundary | 0.5 | 10 |
| S08 | No task instructions in body (boundary check) | 1.0 | 10 |
| S09 | knowledge_boundary is specific (not "everything") | 0.5 | 10 |
| S10 | tone matches actual voice in Identity section | 0.5 | 10 |
| S11 | density_score >= 0.80 | 0.5 | 10 |
| S12 | No filler phrases ("this document", "in summary") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind system_prompt [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target agent identified with clear domain
- [ ] No existing system_prompt for this agent (brain_query checked)
- [ ] Domain expertise researched (not guessing)
