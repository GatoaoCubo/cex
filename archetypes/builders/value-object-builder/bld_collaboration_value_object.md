---
id: bld_rules_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Rules"
version: 1.0.0
quality: 5.7
tags: [builder, value_object, rules]
llm_function: COLLABORATE
density_score: 0.81
updated: "2026-04-17"
---
# Rules: value_object
## Absolute Rules (HARD -- never violate)
1. No identity fields: never add id, uuid, or pk to a value object.
2. Immutability: no setters, no mutation methods, no mutable state.
3. Structural equality: two instances with same attributes are equal (always).
4. Validation at construction: if invalid state can be constructed, the design is broken.
5. Transformations return new instances: withX() -> new VO, never this.x = x.
6. quality: null always -- never self-score.
## Soft Rules (RECOMMEND)
1. Keep attribute count <= 5. More than 5 suggests decomposing into nested value objects.
2. Always specify hashable: true/false explicitly.
3. Include at least 2 invalid state examples to document the validation contract.
4. Name transformations with `with` or `to` prefix for clarity.
## Boundary Rules
1. THIS BUILDER handles: value_object (P06)
2. NOT this builder: type_def (generic alias without DDD contract) -> type-def-builder
3. NOT this builder: enum_def (fixed constants) -> enum-def-builder
4. NOT this builder: aggregate_root (entity with identity) -> aggregate-root-builder
5. NOT this builder: input_schema (raw input validation) -> input-schema-builder
## CEX-Specific Rules
1. id pattern: p06_vo_{slug} -- always prefix p06_vo_
2. Pillar: always P06 (Schema)
3. Producing nucleus: N03 (Engineering)
4. max_bytes: 2048 (smaller than aggregate_root, value objects are concise)
