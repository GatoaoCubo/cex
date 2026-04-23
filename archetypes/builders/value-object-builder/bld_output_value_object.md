---
id: bld_output_template_value_object
kind: output_template
pillar: P06
title: "Value Object Builder -- Output Template"
version: 1.0.0
quality: 7.8
tags: [builder, value_object, template]
llm_function: PRODUCE
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_examples_constraint_spec
  - bld_examples_workflow_node
  - bld_collaboration_constraint_spec
  - bld_output_template_input_schema
  - bld_examples_workflow_primitive
  - constraint-spec-builder
  - p11_qg_type_def
  - p10_lr_constraint_spec_builder
  - type-def-builder
  - bld_output_template_sdk_example
---
# Output Template: value_object
```yaml
---
id: p06_vo_{slug}
kind: value_object
pillar: P06
title: "Value Object: {Name}"
version: 0.1.0
attributes:
  - name: "{attr1}"
    type: "{Type}"
    constraint: "{rule}"
  - name: "{attr2}"
    type: "{Type}"
    constraint: "{rule}"
equality: structural
used_in:
  - "{AggregateRoot or Entity name}"
transformations:
  - "{methodName}({param}: {Type}) -> {Name}: returns new instance with {change}"
hashable: true
quality: null
tags: [value_object, {domain_slug}, P06]
tldr: "{Name}: immutable value defined by {N} attributes, structural equality, used in {context}"
---

## Attributes
| Attribute | Type | Constraint | Valid Example | Invalid Example |
|-----------|------|-----------|---------------|-----------------|
| {attr1} | {Type} | {rule} | {ok} | {bad} |
| {attr2} | {Type} | {rule} | {ok} | {bad} |

## Equality
Two `{Name}` instances are equal if and only if all attributes are equal.
No identity field. Reference equality is NOT domain equality.

## Validation
**Valid**: {example of valid instance}
**Invalid**: {example 1 -- which constraint violated}
**Invalid**: {example 2 -- which constraint violated}

## Transformations
- `{methodName}({param})` -> new `{Name}` with {changed attribute}: `{example}`

## Usage
Used as attribute in: {AggregateRoot.fieldName}, {Entity.fieldName}
```

## Output Template Checklist

- Verify output format matches target kind schema
- Validate all frontmatter fields are present in template
- Cross-reference with eval gate for completeness
- Test template rendering with sample data before publishing

## Output Pattern

```yaml
# Output validation
format_match: true
frontmatter_complete: true
eval_gate_aligned: true
sample_rendered: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_constraint_spec]] | downstream | 0.25 |
| [[bld_examples_workflow_node]] | downstream | 0.22 |
| [[bld_collaboration_constraint_spec]] | downstream | 0.22 |
| [[bld_output_template_input_schema]] | sibling | 0.20 |
| [[bld_examples_workflow_primitive]] | downstream | 0.19 |
| [[constraint-spec-builder]] | upstream | 0.19 |
| [[p11_qg_type_def]] | related | 0.19 |
| [[p10_lr_constraint_spec_builder]] | downstream | 0.18 |
| [[type-def-builder]] | related | 0.18 |
| [[bld_output_template_sdk_example]] | sibling | 0.18 |
