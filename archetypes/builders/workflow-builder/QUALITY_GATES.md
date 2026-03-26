---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for workflow validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: workflow

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p12_wf_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "workflow" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 20 required fields present | Completeness |
| H07 | body has ## Steps section with numbered steps | Core content |
| H08 | steps_count matches actual steps in body | Integrity check |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "workflow" | 0.5 | 10 |
| S03 | Each step has Agent/Action/Input/Output | 1.0 | 10 |
| S04 | execution field matches step arrangement | 0.5 | 10 |
| S05 | Dependencies section present and specific | 0.5 | 10 |
| S06 | Signals section references signal-builder conventions | 1.0 | 10 |
| S07 | Steps with dependencies list them explicitly | 1.0 | 10 |
| S08 | No prompt chaining in body (boundary check) | 1.0 | 10 |
| S09 | spawn_configs referenced if satellites are used | 0.5 | 10 |
| S10 | No filler phrases ("this document", "in summary") | 1.0 | 10 |
| S11 | density_score >= 0.80 | 0.5 | 10 |
| S12 | Purpose section explains mission outcome (not generic) | 0.5 | 10 |

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
Primary: validate_artifact.py --kind workflow [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Mission decomposed into agent-level steps
- [ ] No existing workflow for this mission (brain_query checked)
- [ ] Dependencies mapped (step order, prerequisites)
- [ ] Signals defined per step (reference signal-builder)
