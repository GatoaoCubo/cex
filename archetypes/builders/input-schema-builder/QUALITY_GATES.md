---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for input_schema validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: input_schema

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p06_is_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "input_schema" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 11+ required fields present | Completeness |
| H07 | fields is list, len >= 1, each has name and type | Field structure |
| H08 | scope is non-empty string | Must identify target operation |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "input-schema" | 0.5 | 10 |
| S03 | Contract Definition section present and non-empty | 1.0 | 10 |
| S04 | Fields table present with all columns | 1.0 | 10 |
| S05 | scope is descriptive (>10 chars) | 0.5 | 10 |
| S06 | Coercion Rules section present (even if empty) | 0.5 | 10 |
| S07 | No filler phrases ("this document", "in summary", "basically") | 1.0 | 10 |
| S08 | Examples section present with at least one payload | 0.5 | 10 |
| S09 | Required fields have error_message | 0.5 | 10 |
| S10 | density_score >= 0.80 (if provided) | 0.5 | 10 |

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
Primary: validate_artifact.py --kind input_schema [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target operation/agent identified (what needs this input?)
- [ ] No existing input_schema for same scope (brain_query checked)
- [ ] Fields defined with types and required flags
- [ ] Optional fields have defaults
