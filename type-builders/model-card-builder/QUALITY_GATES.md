---
lp: P11
llm_function: GOVERN
purpose: Automated quality gates for model_card validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
source: validate_kc.py v2.0 architecture + EDISON CEX analysis
---

# Quality Gates: model_card

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id starts with "p02_mc_" | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | type == "model_card" | Type integrity |
| H05 | lp == "P02" | LP assignment |
| H06 | quality == null | Never self-score (Mitchell principle) |
| H07 | model_name is non-empty string | Core identity field |
| H08 | provider in valid enum | Prevents typos |
| H09 | context_window is integer > 0 | Must be exact number |
| H10 | max_output is integer > 0 | Must be exact number |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr < 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3 | 0.5 | 10 |
| S03 | pricing has concrete numbers (not null for commercial) | 1.0 | 10 |
| S04 | modalities object has >= 3 boolean fields | 0.5 | 10 |
| S05 | features object has >= 5 boolean fields | 0.5 | 10 |
| S06 | body has Boundary section | 1.0 | 10 |
| S07 | body has Specifications table with Source column | 1.0 | 10 |
| S08 | body has Capabilities table (booleans) | 1.0 | 10 |
| S09 | body has When to Use table >= 3 rows | 0.5 | 10 |
| S10 | body has References >= 1 URL | 0.5 | 10 |
| S11 | no filler phrases ("this document", "in summary") | 0.5 | 10 |
| S12 | data_source is valid URL | 0.5 | 10 |
| S13 | density >= 0.85 (pure spec, no narrative) | 1.0 | 10 * ratio |
| S14 | updated within 90 days (freshness) | 0.5 | 10 |
| S15 | linked_artifacts present | 0.5 | 10 |

## Scoring Formula
```
hard_score = 10 if all HARD pass, else 0
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_score > 0 ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD pass + 95% SOFT)
PUBLISH: >= 8.0 (all HARD pass + 80% SOFT)
REVIEW:  >= 7.0 (all HARD pass + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Pre-Production Checklist
Before composing, verify:
- [ ] Official provider docs accessible (not behind paywall)
- [ ] Pricing page has current numbers
- [ ] No existing model_card for this model in pool (brain_query first)
- [ ] Model is not sunset (no point documenting dead models)
