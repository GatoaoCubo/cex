---
id: bld_output_template_naming_rule
pillar: P05
llm_function: PRODUCE
kind: output_template
domain: naming_rule
version: 1.0.0
quality: 9.0
title: "Output Template Naming Rule"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_naming_rule
  - bld_schema_naming_rule
  - bld_examples_naming_rule
  - bld_knowledge_card_naming_rule
  - p11_qg_naming_rule
  - bld_architecture_naming_rule
  - bld_schema_voice_pipeline
  - bld_memory_naming_rule
  - bld_schema_action_paradigm
  - bld_schema_thinking_config
---

# Output Template — Naming Rule
```yaml
id: p05_nr_{{scope_slug}}
kind: naming_rule
pillar: P05

version: {{version}}
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: {{author}}

scope: {{scope_description}}
pattern: "{{regex_pattern}}"
prefix: "{{prefix_string}}"
suffix: {{suffix_string_or_null}}

separator: "{{separator_char}}"
case_style: {{snake_case|kebab-case|camelCase|PascalCase|UPPER_SNAKE}}
versioning: {{versioning_description_or_null}}
collision_strategy: {{append_sequence|append_hash|append_date|reject|overwrite}}

domain: {{domain_slug}}
quality: null
tags: [{{tag1}}, {{tag2}}, {{tag3}}]
tldr: "{{one_sentence_summary}}"

keywords: [{{kw1}}, {{kw2}}, {{kw3}}, {{kw4}}, {{kw5}}]
density_score: REC
```
## Scope
`{{scope_full_description}}`
Artifacts governed by this rule: `{{artifact_kinds_list}}`
## Pattern Definition
**Regex**: `{{regex_pattern}}`
**Human-readable**: `{{plain_language_pattern_description}}`
**Segments**:
| Position | Segment | Required | Description |
|----------|---------|----------|-------------|
| 1 | `{{segment_1}}` | yes | `{{segment_1_description}}` |
| 2 | `{{segment_2}}` | yes | `{{segment_2_description}}` |
| 3 | `{{segment_3}}` | {{yes|no}} | `{{segment_3_description}}` |
## Examples
**Valid**:
1. `{{valid_example_1}}` — `{{reason_1}}`
2. `{{valid_example_2}}` — `{{reason_2}}`
3. `{{valid_example_3}}` — `{{reason_3}}`
**Invalid**:
1. `{{invalid_example_1}}` — VIOLATES: `{{violation_reason_1}}`
2. `{{invalid_example_2}}` — VIOLATES: `{{violation_reason_2}}`
## Collision Resolution
Strategy: `{{collision_strategy}}`
`{{collision_resolution_description}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | naming_rule |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_naming_rule]] | upstream | 0.46 |
| [[bld_schema_naming_rule]] | downstream | 0.45 |
| [[bld_examples_naming_rule]] | downstream | 0.42 |
| [[bld_knowledge_card_naming_rule]] | upstream | 0.36 |
| [[p11_qg_naming_rule]] | downstream | 0.32 |
| [[bld_architecture_naming_rule]] | downstream | 0.29 |
| [[bld_schema_voice_pipeline]] | downstream | 0.28 |
| [[bld_memory_naming_rule]] | downstream | 0.27 |
| [[bld_schema_action_paradigm]] | downstream | 0.27 |
| [[bld_schema_thinking_config]] | downstream | 0.27 |
