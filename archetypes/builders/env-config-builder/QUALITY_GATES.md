---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for env_config validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: env_config

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p09_env_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "env_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, scope, variables, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Variable Catalog, ## Override Precedence, ## Sensitive Variables | Core sections required |
| H08 | body <= 4096 bytes | Size limit for env config |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "env_config" | 0.5 | 10 |
| S03 | variables names match variable names in ## Variable Catalog (zero drift) | 1.0 | 10 |
| S04 | Each variable has: type, required, default, sensitive, validation in catalog | 1.0 | 10 |
| S05 | Validation rule defined for each variable (not empty) | 1.0 | 10 |
| S06 | sensitive_count matches actual sensitive vars in catalog | 0.5 | 10 |
| S07 | No actual secret values anywhere in artifact | 1.0 | 10 |
| S08 | Override precedence clearly defined with priority order | 0.5 | 10 |
| S09 | description <= 200 chars and non-generic | 0.5 | 10 |
| S10 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S11 | Variable names use UPPER_SNAKE_CASE convention | 0.5 | 10 |

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
- [ ] Scope identified (global, satellite, or service)
- [ ] All variables enumerated with concrete names
- [ ] Sensitive variables identified and marked
- [ ] No existing env_config for this scope (brain_query checked)
- [ ] No actual secret values in any field
