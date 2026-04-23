---
id: bld_quality_gate_value_object
kind: quality_gate
pillar: P06
title: "Value Object Builder -- Quality Gate"
version: 1.0.0
quality: 8.3
tags: [builder, value_object, quality_gate]
llm_function: GOVERN
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_function_def
  - p11_qg_entity_memory
  - p11_qg_boot_config
  - p11_qg_chunk_strategy
  - p11_qg_glossary_entry
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_naming_rule
  - p11_qg_constraint_spec
  - p11_qg_few_shot_example
---

## Quality Gate

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

## Examples

# Examples: value_object
## Golden Example: Money
```yaml
id: p06_vo_money
kind: value_object
attributes:
  - name: amount
    type: Decimal
    constraint: "amount >= 0"
  - name: currency
    type: string
    constraint: "ISO 4217 code, len == 3"
equality: structural
transformations:
  - "add(other: Money) -> Money: requires same currency, returns new Money(amount+other.amount, currency)"
  - "scale(factor: Decimal) -> Money: returns new Money(amount*factor, currency)"
hashable: true
used_in: [Order, Invoice]
tldr: "Money: immutable amount+currency value, structural equality, used in financial aggregates"
```
## Golden Example: Email
```yaml
id: p06_vo_email
kind: value_object
attributes:
  - name: address
    type: string
    constraint: "matches RFC 5322, len <= 320"
equality: structural
transformations:
  - "domain() -> string: returns the part after @"
hashable: true
used_in: [UserAccount, ContactInfo]
```
## Anti-Pattern: Mutable Value Object
```yaml
# WRONG -- value objects must be immutable
transformations:
  - "setAmount(n): mutates amount field"
# CORRECT
transformations:
  - "withAmount(n: Decimal) -> Money: returns new Money(n, currency)"
```
## Anti-Pattern: Value Object with Identity
```yaml
# WRONG -- value objects have no identity
attributes:
  - name: id
    type: UUID
# CORRECT: if identity is needed, use entity or aggregate_root
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
