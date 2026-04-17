---
id: bld_examples_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Examples"
version: 1.0.0
quality: 5.1
tags: [builder, value_object, examples]
llm_function: GOVERN
density_score: 1.0
updated: "2026-04-17"
---
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
