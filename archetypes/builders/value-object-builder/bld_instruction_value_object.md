---
id: bld_instruction_value_object
kind: instruction
pillar: P06
title: "Value Object Builder -- Instruction"
version: 1.0.0
quality: 5.4
tags: [builder, value_object, instruction]
llm_function: REASON
density_score: 0.83
updated: "2026-04-17"
---
# Instructions: How to Produce a value_object
## Phase 1: RESEARCH
1. Identify the domain concept -- what real-world attribute needs typed representation?
2. Verify no identity needed: two instances with same attributes should be interchangeable.
3. Enumerate attributes: what fields make up this value? What are their types and constraints?
4. Define validation rules: what makes an instance valid vs invalid?
5. Define allowed transformations: what operations produce a new valid instance?
6. Identify context: which aggregate_root or entity uses this value_object?
## Phase 2: COMPOSE
1. Read bld_schema_value_object.md -- source of truth for required fields
2. Fill frontmatter: id pattern p06_vo_{slug}, kind: value_object, quality: null
3. Write Attributes section: field name, type, constraint for each attribute
4. Write Equality section: structural equality contract (all attributes equal = value equal)
5. Write Validation section: invariants for the value (invalid state examples)
6. Write Transformations section: operations that produce new instances (never mutate)
7. Write Usage section: which aggregates or entities use this value_object
## Phase 3: VALIDATE
1. HARD gates: id matches `p06_vo_[a-z][a-z0-9_]+`, kind == value_object, quality == null
2. Value has >= 1 attribute with type and constraint
3. Equality is structural (not by reference)
4. No mutation methods -- only transformations returning new instances
5. Invalid state examples present
