---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for formatter validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: formatter

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p05_fmt_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "formatter" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 14 required fields present (id, kind, pillar, version, created, updated, author, target_format, input_type, rule_count, domain, quality, tags, tldr) | Completeness |
| H07 | rule_count matches rules in table AND rule_count >= 1 | Rule integrity |
| H08 | target_format and input_type are valid enum values | Format compliance |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "formatter" | 0.5 | 10 |
| S03 | Formatting Rules table has >= 1 row with all columns | 1.0 | 10 |
| S04 | Input Specification section present with structure and example | 1.0 | 10 |
| S05 | Output Specification section present with formatted example | 1.0 | 10 |
| S06 | Template section present (even if engine: none) | 0.5 | 10 |
| S07 | Edge Cases section covers null, empty, special chars | 1.0 | 10 |
| S08 | escaping strategy declared and appropriate for target_format | 0.5 | 10 |
| S09 | density_score >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases ("this formatter", "designed to", "various formats") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind formatter [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target format identified with sample output available
- [ ] Input data structure identified with sample data
- [ ] No existing formatter for this domain (brain_query checked)
- [ ] At least 1 formatting rule defined
- [ ] Escaping strategy selected for target format
