---
quality: 7.6
id: bld_rules_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Rules"
version: 1.0.0
quality: 7.3
tags: [builder, value_object, rules]
llm_function: COLLABORATE
author: builder
tldr: "Value Object schema: workflow coordination, handoffs, and lifecycle management"
density_score: 0.81
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_validation_schema
  - bld_architecture_kind
  - p03_sp_kind_builder
  - bld_collaboration_enum_def
  - kind-builder
  - p03_sp__builder_builder
  - bld_collaboration_builder
  - p03_sp_type-def-builder
  - p03_sp_system-prompt-builder
  - bld_collaboration_input_schema
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

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validation_schema]] | related | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.29 |
| [[p03_sp_kind_builder]] | upstream | 0.28 |
| [[bld_collaboration_enum_def]] | downstream | 0.28 |
| [[kind-builder]] | downstream | 0.27 |
| [[p03_sp__builder_builder]] | upstream | 0.27 |
| [[bld_collaboration_builder]] | downstream | 0.27 |
| [[p03_sp_type-def-builder]] | upstream | 0.26 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.24 |
| [[bld_collaboration_input_schema]] | downstream | 0.24 |
