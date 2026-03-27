---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for runtime_rule validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: runtime_rule

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p09_rr_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "runtime_rule" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, rule_name, rule_type, scope, quality, tags, tldr | Completeness |
| H07 | body has ## Rule Specification, ## Trigger Behavior, ## Tuning Guide | Core sections required |
| H08 | rule_type in [timeout, retry, rate_limit, circuit_breaker, concurrency] | Valid rule enum |
| H09 | All numeric values include units (ms, s, req/s, count, etc.) | Ambiguous values cause outages |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "runtime_rule" | 0.5 | 10 |
| S03 | Rule Specification has parameter table with value + unit columns | 1.0 | 10 |
| S04 | Trigger Behavior defines fallback for every failure mode | 1.0 | 10 |
| S05 | No vague terms ("fast", "many", "some", "a bit") — all concrete | 1.0 | 10 |
| S06 | fallback field populated in frontmatter | 0.5 | 10 |
| S07 | Tuning Guide includes safe ranges for parameters | 0.5 | 10 |
| S08 | Tuning Guide includes metrics to monitor | 0.5 | 10 |
| S09 | description <= 200 chars and non-generic | 0.5 | 10 |
| S10 | density_score >= 0.80 (no filler) | 0.5 | 10 |
| S11 | severity field populated | 0.5 | 10 |

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

## Pre-Production Checklist
- [ ] Operation/component identified
- [ ] Rule type determined (timeout, retry, rate_limit, circuit_breaker, concurrency)
- [ ] Numeric values researched with units
- [ ] Fallback behavior defined
- [ ] No existing runtime_rule for this scope (brain_query checked)
