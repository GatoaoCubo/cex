---
kind: output_template
id: bld_output_template_workflow_primitive
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a workflow_primitive
pattern: every field here exists in the schema; template derives, never invents
quality: 9.0
title: "Output Template Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: workflow_primitive
Naming pattern: `p12_wp_{type}.yaml`
Filename: `p12_wp_{{type}}.yaml` or `p12_wp_{{type}}_{{name}}.yaml`
```yaml
---
id: p12_wp_{{type}}
kind: workflow_primitive
pillar: P12
quality: null
tags: [workflow_primitive, {{type}}, P12]
---

type: "{{step|condition|loop|parallel|router|gate|merge}}"
description: "{{one_line_purpose_of_this_primitive}}"
inputs:
  - name: "{{input_field_name}}"
    type: "{{string|integer|float|boolean|list|object|artifact_ref}}"
    required: {{true|false}}
    description: "{{one_line_purpose_or_omit}}"
outputs:
  - name: "{{output_field_name}}"
    type: "{{string|integer|float|boolean|list|object|artifact_ref}}"
    required: {{true|false}}
    description: "{{one_line_purpose_or_omit}}"

# --- Type-specific fields (include only the block matching your type) ---

# condition:
condition_expr: "{{boolean_expression_or_omit}}"
true_branch: "{{primitive_ref_or_omit}}"
false_branch: "{{primitive_ref_or_omit}}"

# loop:
max_iter: {{1_to_100_or_omit}}
break_condition: "{{early_exit_expression_or_omit}}"
feedback_input: "{{input_field_name_or_omit}}"

# parallel:
branches: [{{primitive_refs_or_omit}}]
merge_ref: "{{merge_primitive_ref_or_omit}}"
timeout_s: {{integer_seconds_or_omit}}

# router:
routes:
  - match: "{{pattern_or_omit}}"
    target: "{{primitive_ref_or_omit}}"
default_route: "{{primitive_ref_or_omit}}"

# gate:
threshold: {{0.0_to_1.0_or_integer_or_omit}}
wait_for: [{{primitive_refs_or_omit}}]
timeout_s: {{integer_seconds_or_omit}}

# merge:
strategy: "{{all|any|first|majority_or_omit}}"
source_refs: [{{primitive_refs_or_omit}}]

# --- Optional fields (all types) ---
name: "{{instance_name_or_omit}}"
retry_count: {{integer_or_omit}}
on_error: "{{error_handler_primitive_ref_or_omit}}"
composable_after: [{{primitive_types_or_omit}}]
composable_before: [{{primitive_types_or_omit}}]
```
## Derivation Notes
- The four top-level fields (type, description, inputs, outputs) are required for ALL types
- Include ONLY the type-specific block matching your primitive type
- Omit type-specific fields from other types entirely
- Omit absent optional fields instead of filling with placeholder strings
- Every input/output MUST have name + type + required
- Loops MUST have max_iter. Parallel MUST have merge_ref. Gates MUST have threshold.
- Keep the primitive atomic: one type, one operation, one file
