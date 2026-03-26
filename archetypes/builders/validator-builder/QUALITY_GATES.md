---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for validator validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: validator

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p06_val_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "validator" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 15+ required fields present | Completeness |
| H07 | severity in [error, warning, info] | Enum compliance |
| H08 | conditions is list, len >= 1 | Must have at least one rule |
| H09 | auto_fix is boolean (true/false) | Type correctness |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "validator" | 0.5 | 10 |
| S03 | error_message is actionable (contains fix instruction) | 1.0 | 10 |
| S04 | Rule Definition section present and non-empty | 1.0 | 10 |
| S05 | Conditions table present with field/operator/value columns | 1.0 | 10 |
| S06 | Error Handling section present with severity + remediation | 0.5 | 10 |
| S07 | No filler phrases ("this document", "in summary", "basically") | 1.0 | 10 |
| S08 | Each condition has explicit target (frontmatter/body/filename) | 0.5 | 10 |
| S09 | Bypass Policy section present (even if bypass: null) | 0.5 | 10 |
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
Primary: validate_artifact.py --kind validator [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target domain identified (what artifact kind does this validate?)
- [ ] No existing validator for same rule (brain_query checked)
- [ ] Conditions structured as field/operator/value triples
- [ ] error_message written as actionable fix instruction
