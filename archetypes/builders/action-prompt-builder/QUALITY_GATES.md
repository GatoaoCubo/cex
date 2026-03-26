---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for action_prompt validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: action_prompt

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p03_ap_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "action_prompt" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 21 required fields present | Completeness |
| H07 | edge_cases has >= 2 entries | Robustness requirement |
| H08 | body has all 5 required sections | Structure compliance |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "action_prompt" | 0.5 | 10 |
| S03 | action is verb phrase (starts with verb) | 1.0 | 10 |
| S04 | input_required lists specific data items with types | 1.0 | 10 |
| S05 | output_expected describes verifiable structure | 1.0 | 10 |
| S06 | purpose explains WHY (not just WHAT) | 0.5 | 10 |
| S07 | No identity/persona content (boundary check) | 1.0 | 10 |
| S08 | No detailed recipe with prerequisites (instruction territory) | 1.0 | 10 |
| S09 | Validation section has verifiable criteria | 0.5 | 10 |
| S10 | Input section uses table or structured format | 0.5 | 10 |
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
Primary: validate_artifact.py --kind action_prompt [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Task identified with clear input/output contract
- [ ] No existing action_prompt for this task (brain_query checked)
- [ ] Edge cases enumerated (>= 2)
