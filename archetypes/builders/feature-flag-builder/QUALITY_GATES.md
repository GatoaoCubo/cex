---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for feature_flag validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: feature_flag

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p09_ff_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "feature_flag" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, flag_name, default_state, category, rollout_percentage, quality, tags, tldr | Completeness |
| H07 | body has ## Flag Specification, ## Rollout Strategy, ## Lifecycle | Core sections required |
| H08 | default_state in [on, off] | Valid state enum |
| H09 | rollout_percentage is integer 0-100 | Valid range |
| H10 | category in [release, experiment, ops, permission] | Valid category enum |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "feature_flag" | 0.5 | 10 |
| S03 | flag_name is snake_case, descriptive | 0.5 | 10 |
| S04 | Rollout strategy has stages with percentages | 1.0 | 10 |
| S05 | Lifecycle includes retire/cleanup date | 0.5 | 10 |
| S06 | description <= 200 chars and non-generic | 0.5 | 10 |
| S07 | density_score >= 0.80 (no filler) | 0.5 | 10 |
| S08 | Kill switch behavior documented for ops flags | 0.5 | 10 |
| S09 | owner field populated | 0.5 | 10 |
| S10 | expires date set for non-permanent flags | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 10 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Pre-Production Checklist
- [ ] Feature identified with clear scope
- [ ] Category determined (release, experiment, ops, permission)
- [ ] Default state decided (on/off)
- [ ] No existing feature_flag for this feature (brain_query checked)
- [ ] Rollout strategy planned with stages
