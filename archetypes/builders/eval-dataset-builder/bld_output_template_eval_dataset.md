---
kind: output_template
id: bld_output_template_eval_dataset
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an eval_dataset artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Eval Dataset"
version: "1.0.0"
author: n03_builder
tags: [eval_dataset, builder, examples]
tldr: "Golden and anti-examples for eval dataset construction, demonstrating ideal structure and common pitfalls."
domain: "eval dataset construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: eval_dataset
```yaml
id: p07_ds_{{dataset_slug}}
kind: eval_dataset
pillar: P07
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_dataset_name}}"
size: {{integer_total_cases}}
splits:
  {{train: 0.0 | omit if zero}}
  test: {{float}}
  {{val: 0.0 | omit if zero}}
schema_fields:
  - input
  - expected_output
  - {{optional_field_3}}
quality: null
tags: [eval_dataset, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_dataset_covers_max_200ch}}"
source: "{{human|synthetic|scraped|adversarial|hybrid}}"
framework: "{{braintrust|langsmith|deepeval|huggingface|costm}}"
task_type: "{{classification|qa|summarization|tool_use|reasoning|other}}"
language: "{{en|pt|es|...}}"
license: "{{MIT|CC-BY-4.0|proprietary|...}}"
refresh_cadence: "{{weekly|monthly|on-demand|frozen}}"
```
## Overview
`{{what_llm_behavior_this_dataset_evaluates_1_to_2_sentences}}`
`{{who_uses_it_and_primary_use_case}}`

## Schema
### input
Type: {{string|dict}}
`{{description_of_what_input_contains}}`
Example: `"{{example_input_value}}"`

### expected_output
Type: {{string|list|dict}}
`{{description_of_ground_truth_format}}`
Example: `"{{example_expected_output_value}}"`

### `{{optional_metadata_field}}`
Type: {{dict|string|enum}}
`{{description_of_optional_field}}`
Values: `{{enum_values_or_schema}}`

## Splits
| Split | Percentage | Cases | Rationale |
|-------|-----------|-------|-----------|
| `{{train}}` | {{0-100}}% | {{n}} | `{{why_this_split_exists}}` |
| test | {{0-100}}% | `{{n}}` | `{{why_this_split_exists}}` |
| `{{val}}` | {{0-100}}% | {{n}} | `{{why_this_split_exists}}` |
Total: 100% (`{{total_cases}}` cases)
Split rationale: `{{why_these_percentages_were_chosen}}`

## Integration
Framework: {{braintrust|langsmith|deepeval|huggingface|costm}}
Loading:
```python
{{framework_loading_snippet_5_to_10_lines}}
```
Version migration: `{{how_to_migrate_from_v1_to_v2_if_schema_changes}}`
