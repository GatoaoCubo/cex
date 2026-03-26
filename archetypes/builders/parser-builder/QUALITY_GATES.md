---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for parser validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: parser

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p05_parser_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "parser" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 14 required fields present (id, kind, pillar, version, created, updated, author, input_format, output_format, extraction_count, domain, quality, tags, tldr) | Completeness |
| H07 | extraction_count matches rules in table AND extraction_count >= 1 | Rule integrity |
| H08 | input_format and output_format are valid enum values | Format compliance |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "parser" | 0.5 | 10 |
| S03 | Extraction Rules table has >= 1 row with all columns | 1.0 | 10 |
| S04 | Input Specification section present with format and example | 1.0 | 10 |
| S05 | Error Handling section present with strategy description | 1.0 | 10 |
| S06 | Output Specification section present with schema | 0.5 | 10 |
| S07 | At least 1 extraction rule has required: true | 1.0 | 10 |
| S08 | Normalization section present (even if empty pipeline) | 0.5 | 10 |
| S09 | density_score >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases ("this parser", "designed to", "various types") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind parser [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Input format identified with sample data available
- [ ] Target fields identified with extraction methods chosen
- [ ] No existing parser for this domain (brain_query checked)
- [ ] At least 1 required extraction rule defined
- [ ] Error handling strategy selected
