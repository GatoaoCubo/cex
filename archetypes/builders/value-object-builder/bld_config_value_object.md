---
id: bld_context_sources_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Context Sources"
version: 1.0.0
quality: 7.4
tags: [builder, value_object, context]
llm_function: CONSTRAIN
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_tools_kind
  - bld_instruction_kind
  - bld_collaboration_kind
  - kind-builder
  - bld_examples_handoff
  - bld_output_template_function_def
  - bld_collaboration_validation_schema
  - bld_collaboration_builder
  - bld_knowledge_card_kind
---
# Context Sources: value_object
## Mandatory Loads (F3 INJECT)
| Source | Path | Purpose |
|--------|------|---------|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_value_object.md | Primary definition |
| Schema | archetypes/builders/value-object-builder/bld_schema_value_object.md | Field constraints |
| Template | archetypes/builders/value-object-builder/bld_output_template_value_object.md | Structure |
| Examples | archetypes/builders/value-object-builder/bld_examples_value_object.md | Golden patterns |
| Pillar schema | N00_genesis/P06_schema/_schema.yaml | Pillar constraints |
## Related Kind KCs
| KC | Relationship |
|----|-------------|
| kc_aggregate_root.md | aggregate that contains this value object |
| kc_type_def.md | simpler type alias (no DDD contract) |
| kc_enum_def.md | fixed-set constant type |
| kc_input_schema.md | raw input validation before constructing value objects |
## External References
| Source | Relevance |
|--------|----------|
| Evans DDD (2003) Ch. 5 | Original value object definition |
| Vernon IDDD (2013) Ch. 6 | Implementation patterns for value objects |
| Functional domain modeling | Immutable data types + smart constructors |

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.27 |
| [[bld_tools_kind]] | upstream | 0.26 |
| [[bld_instruction_kind]] | upstream | 0.23 |
| [[bld_collaboration_kind]] | downstream | 0.23 |
| [[kind-builder]] | downstream | 0.22 |
| [[bld_examples_handoff]] | downstream | 0.21 |
| [[bld_output_template_function_def]] | upstream | 0.21 |
| [[bld_collaboration_validation_schema]] | related | 0.20 |
| [[bld_collaboration_builder]] | downstream | 0.20 |
| [[bld_knowledge_card_kind]] | sibling | 0.19 |
