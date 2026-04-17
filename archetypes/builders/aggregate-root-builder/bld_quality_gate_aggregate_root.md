---
id: bld_quality_gate_aggregate_root
kind: quality_gate
pillar: P06
title: "Aggregate Root Builder -- Quality Gate"
version: 1.0.0
quality: null
tags: [builder, aggregate_root, quality_gate]
llm_function: GOVERN
---
# Gate: aggregate_root
## Threshold
>= 7.0 to publish; >= 9.0 for reference
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p06_ar_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `aggregate_root` | Any other value |
| H05 | quality == null | Non-null |
| H06 | bounded_context present | Missing |
| H07 | invariants list has >= 2 entries | Fewer than 2 |
| H08 | commands list has >= 1 entry | Empty |
| H09 | domain_events list has >= 1 entry | Empty |
| H10 | repository field present | Missing |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Invariants are concrete measurable rules, not aspirational | 0.20 |
| S02 | Commands have pre/postconditions | 0.15 |
| S03 | Domain events have payload defined | 0.10 |
| S04 | cluster_members lists all entities and value_objects | 0.15 |
| S05 | No cross-aggregate object references (ID only) | 0.20 |
| S06 | repository interface is find_by_id + save only | 0.10 |
| S07 | Boundaries section distinguishes inside vs outside | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |
