---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for skill validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: skill

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id matches `^p04_skill_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "skill" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 15 required fields present | Completeness |
| H07 | body has ## Purpose section | Core purpose required |
| H08 | body has ## Workflow Phases with >= 2 subsections | Phases are the essence of skill |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | description <= 120 chars, non-empty | 1.0 | 10 |
| S02 | phases list in frontmatter matches body ### subsections exactly | 1.0 | 10 |
| S03 | user_invocable: true iff trigger starts with `/` | 1.0 | 10 |
| S04 | when_to_use and when_not_to_use parallel (same abstraction level) | 0.5 | 10 |
| S05 | No identity language in body ("You are", "I will", "my role") | 1.0 | 10 |
| S06 | body has ## Anti-Patterns with >= 3 named failures | 1.0 | 10 |
| S07 | body has ## Metrics with >= 2 measurable targets | 0.5 | 10 |
| S08 | Each phase has Input / Action / Output defined | 1.0 | 10 |
| S09 | examples list has >= 2 concrete invocations | 0.5 | 10 |
| S10 | density >= 0.80 (no filler phrases) | 0.5 | 10 |

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
Primary: validate_artifact.py --kind skill [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Capability name and domain identified
- [ ] No existing skill for this capability (brain_query checked)
- [ ] Phase decomposition reviewed (no overlapping phases)
- [ ] Trigger type determined (slash vs keyword vs event)
