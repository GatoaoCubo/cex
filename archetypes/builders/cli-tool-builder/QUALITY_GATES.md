---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for cli_tool validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: cli_tool

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_cli_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "cli_tool" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, name, commands, output_format, exit_codes, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Commands, ## Output, ## Configuration | Core sections |
| H08 | body <= 1024 bytes | Compact tool spec |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "cli_tool" | 0.5 | 10 |
| S03 | commands list matches command names in ## Commands section (zero drift) | 1.0 | 10 |
| S04 | Each command has: syntax, flags/args, description, return | 1.0 | 10 |
| S05 | exit_codes map includes at least codes 0 and 1 | 1.0 | 10 |
| S06 | output_format is valid enum value | 0.5 | 10 |
| S07 | No implementation code in body (spec only) | 1.0 | 10 |
| S08 | config_file field present with path and format | 0.5 | 10 |
| S09 | description <= 200 chars and non-generic | 0.5 | 10 |
| S10 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S11 | env_vars listed with purpose | 0.5 | 10 |
| S12 | platforms field present | 0.5 | 10 |

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

## Pre-Production Checklist
- [ ] Tool name and purpose identified
- [ ] All commands enumerated with concrete names
- [ ] Exit codes defined with semantic meanings
- [ ] Output format selected matching consumer needs
- [ ] No existing cli_tool for this purpose (brain_query checked)
