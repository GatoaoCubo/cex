---
quality: 8.4
id: bld_memory_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Memory"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-22"
author: builder
domain: value_object
quality: 8.3
tags: [builder, value_object, memory]
llm_function: INJECT
tldr: "Recalled session patterns, corrections, and taxonomy for value_object builder."
density_score: 0.92
related:
  - bld_knowledge_value_object
  - bld_schema_value_object
  - bld_architecture_value_object
  - bld_model_value_object
  - bld_prompt_value_object
  - bld_tools_value_object
  - bld_output_value_object
  - bld_eval_value_object
  - bld_feedback_value_object
  - bld_config_value_object
---
# Memory: value_object

## Session Patterns

| Pattern | Guidance | Gate |
|---------|----------|------|
| Attribute count | Most value objects have 1-3 attributes. >5 suggests decomposing. | H01 |
| The "whole value" test | If you can construct an invalid instance, invariants are broken. All checked at construction. | H02 |
| Hashability | Value objects used as dict keys or in sets must be hashable. Always specify. | H03 |
| Transformation naming | Use `withX()` or `toX()` pattern, never `setX()`. | H04 |
| Invalid examples required | Without invalid state examples, validation rules cannot be verified. | H05 |
| No `id` field | If tracking is needed, it is an entity not a value object. | H06 |

## Common Mistakes

| Mistake | Correction | Severity |
|---------|-----------|---------|
| Adding an `id` field | If you need to track this object, it is an entity | BLOCK |
| Mutable setters (`setX`) | Value objects are immutable; any mutation creates a new instance | BLOCK |
| Empty attributes list | Every value object must have at least 1 attribute with a constraint | BLOCK |
| Missing invalid examples | Add at least 2 invalid state examples to verify validation rules | WARN |
| Attribute count > 5 | Review for decomposition into multiple value objects | WARN |
| Using `==` on entity instead | Teach identity test (below) before building | TEACH |

## Identity Test (use when unsure)

Q: "If I find two instances with identical attributes in the database, are they the same thing?"

| Answer | Type | Reason |
|--------|------|--------|
| YES -- they are interchangeable | value_object | Structural equality, no identity needed |
| NO -- they must be distinguished | entity | Needs its own identity to distinguish them |

## Type Taxonomy

| Kind | Domain Contract | Identity | Equality | Example |
|------|----------------|----------|----------|---------|
| value_object | DDD, domain-meaningful | None | Structural | Money(100, USD) |
| type_def | Generic alias | None | Structural | Age = int |
| enum_def | Fixed constant set | None | Reference | Status.ACTIVE |
| aggregate_root | DDD, owns a cluster | UUID/ID | Identity | Order(id=42) |
| entity | DDD, trackable | UUID/ID | Identity | Customer(id=7) |

## Vocabulary

| User Term | Industry Term | Notes |
|-----------|--------------|-------|
| "immutable object" | value_object | Only if it has domain meaning |
| "data transfer object" | output_template or schema | Different pattern -- not a value object |
| "record" (Java) | value_object | If it enforces invariants |
| "named tuple" | type_def | If no invariants, just aliasing |
| "frozen dataclass" | value_object | If invariants enforced in `__post_init__` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_value_object]] | sibling | 0.46 |
| [[bld_schema_value_object]] | sibling | 0.44 |
| [[bld_architecture_value_object]] | sibling | 0.42 |
| [[bld_model_value_object]] | sibling | 0.40 |
| [[bld_prompt_value_object]] | sibling | 0.38 |
| [[bld_tools_value_object]] | sibling | 0.36 |
| [[bld_output_value_object]] | sibling | 0.34 |
| [[bld_eval_value_object]] | sibling | 0.32 |
| [[bld_feedback_value_object]] | sibling | 0.30 |
| [[bld_config_value_object]] | sibling | 0.28 |
