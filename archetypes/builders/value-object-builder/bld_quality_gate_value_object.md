---
id: bld_quality_gate_value_object
kind: quality_gate
pillar: P06
title: "Value Object Builder -- Quality Gate"
version: 1.0.0
quality: null
tags: [builder, value_object, quality_gate]
llm_function: GOVERN
---
# Gate: value_object
## Threshold
>= 7.0 to publish; >= 9.0 for reference
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p06_vo_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `value_object` | Any other value |
| H05 | quality == null | Non-null |
| H06 | attributes list has >= 1 entry | Empty or missing |
| H07 | equality == `structural` | Any other value |
| H08 | No attribute named id, uuid, or pk | Identity field present |
| H09 | No mutation methods in transformations | setX() or mutate() pattern |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Each attribute has type AND constraint | 0.25 |
| S02 | Invalid state examples present (>= 2) | 0.20 |
| S03 | Transformations return new instances (not mutate) | 0.20 |
| S04 | used_in references at least 1 aggregate or entity | 0.15 |
| S05 | hashable field specified | 0.10 |
| S06 | tldr <= 160 chars with immutability and equality mentioned | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |
