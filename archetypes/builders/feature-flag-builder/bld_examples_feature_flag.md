---
kind: examples
id: bld_examples_feature_flag
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of feature_flag artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: feature-flag-builder
## Golden Example
INPUT: "Create a feature flag for the new search algorithm with gradual rollout"
OUTPUT:
```yaml
id: p09_ff_enable_vector_search
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
flag_name: "enable_vector_search"
default_state: off
category: release
rollout_percentage: 0
quality: null
tags: [feature_flag, search, release, P09, vector]
tldr: "Vector search release flag: off by default, 4-stage rollout to 100% over 2 weeks"
description: "Controls activation of vector-based search replacing keyword search"
owner: "search_team"
expires: "2026-05-01"
targeting: "percentage-based, all users"
```
## Flag Specification
Enables vector-based semantic search to replace legacy keyword search.
Default OFF — legacy keyword search serves all users until flag ramps.
Kill switch: set rollout_percentage to 0 to instantly revert to keyword search.
## Rollout Strategy
| Stage | Percentage | Duration | Criteria |
|-------|-----------|----------|----------|
| canary | 5% | 3 days | error rate < 0.1%, latency < 200ms |
| early | 25% | 4 days | no regressions, user feedback positive |
| broad | 50% | 3 days | metrics stable, no support tickets |
| full | 100% | permanent | retire flag after 2 weeks stable |
## Lifecycle
- Created: 2026-03-26 (flag defined, code deployed behind flag)
- Test: internal QA with flag ON in staging
- Ramp: canary 5% -> early 25% -> broad 50% -> full 100%
- Retire: 2026-05-01 (remove flag, vector search becomes default)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_ff_ pattern (H02 pass)
- kind: feature_flag (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 3 sections: Flag Specification, Rollout Strategy, Lifecycle (H07 pass)
- default_state: off (valid enum) (H08 pass)
- rollout_percentage: 0 (integer 0-100) (H09 pass)
- category: release (valid enum) (H10 pass)
- tldr: 74 chars <= 160 (S01 pass)
- tags: 5 items, includes "feature_flag" (S02 pass)
## Anti-Example
INPUT: "Add a feature flag for dark mode"
BAD OUTPUT:
```yaml
id: dark-mode
kind: flag
pillar: config
flag_name: Dark Mode Toggle
default_state: maybe
rollout_percentage: half
quality: 9.0
tags: [ui]
```
Turn on dark mode for users.
FAILURES:
1. id: "dark-mode" uses hyphens, no `p09_ff_` prefix -> H02 FAIL
2. kind: "flag" not "feature_flag" -> H04 FAIL
3. pillar: "config" not "P09" -> H06 FAIL
4. default_state: "maybe" not in enum [on, off] -> H08 FAIL
5. rollout_percentage: "half" not integer 0-100 -> H09 FAIL
6. quality: 9.0 (not null) -> H05 FAIL
7. Missing fields: version, created, updated, author, category, tldr -> H06 FAIL
8. tags: only 1 item, missing "feature_flag" -> S02 FAIL
9. Body missing ## Flag Specification, ## Rollout Strategy, ## Lifecycle -> H07 FAIL
10. flag_name uses spaces and uppercase (should be snake_case slug) -> S04 FAIL
11. No rollout strategy or lifecycle plan defined -> S05 FAIL
