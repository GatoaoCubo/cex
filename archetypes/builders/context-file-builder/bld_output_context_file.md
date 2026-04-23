---
kind: output_template
id: bld_output_template_context_file
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a context_file
pattern: every field here exists in bld_schema_context_file.md -- template derives, never invents
quality: 8.8
title: "Output Template: context_file"
version: "1.0.0"
author: n03_builder
tags: [context_file, builder, output_template, hermes_origin]
tldr: "Fill-in template for context_file artifacts: scope, injection_point, inheritance_chain, priority, instruction-only body."
domain: "workspace instruction auto-injection"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - p03_sp_system-prompt-builder
  - p03_sp_engineering_nucleus
  - bld_instruction_dispatch_rule
  - p03_sp_n03_creation_nucleus
  - bld_output_template_system_prompt
  - bld_instruction_memory_scope
  - bld_output_template_input_schema
  - bld_norms
  - bld_output_template_instruction
  - bld_instruction_golden_test
---

# Output Template: context_file

```yaml
id: ctx_{{scope_slug}}
kind: context_file
pillar: P03

title: "{{human_readable_scope_description}}"
scope: {{workspace|nucleus|session|global}}
injection_point: {{session_start|every_turn|f3_inject}}
inheritance_chain: {{[parent_ctx_ids]|[]}}

max_bytes: {{8192|custom_integer}}
priority: {{0_to_N}}
applies_to_nuclei: {{[all]|[n01,n02,...]}}

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

quality: null
tags: [context_file, {{scope_name}}, hermes_origin, {{additional_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```

## {{Primary Rule Section Title}}
1. ALWAYS {{rule_1}}
2. NEVER {{rule_2}}
3. ALWAYS {{rule_3}}
{{...add more rules up to byte budget}}

## {{Optional Second Section Title}}
- {{rule_A}}
- {{rule_B}}
- {{rule_C}}

## {{Optional Third Section Title}}
{{...repeat as needed; all sections must be instructions, never facts or template vars}}

---

## Fill Guide

| Placeholder | How to fill |
|-------------|------------|
| `{{scope_slug}}` | snake_case scope name: `engineering_workspace`, `n03_nucleus`, `sprint42_session` |
| `{{human_readable_scope_description}}` | E.g.: "N03 Build Conventions", "Engineering Workspace Rules" |
| `{{workspace\|nucleus\|session\|global}}` | Pick narrowest scope that applies |
| `{{session_start\|every_turn\|f3_inject}}` | session_start unless compliance-critical or pipeline-specific |
| `{{[parent_ctx_ids]\|[]}}` | List parent IDs (must exist); empty list for root context_file |
| `{{0_to_N}}` | 0 = most authoritative; increment for narrower scopes |
| `{{[all]\|[n01,n02,...]}}` | [all] for cross-nucleus; explicit list for nucleus-specific |
| `{{rule_N}}` | Behavioral instruction: ALWAYS/NEVER pattern preferred; actionable and verifiable |
| Section titles | Match the rule domain: "Build Rules", "Commit Rules", "Quality Rules", etc. |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | workspace instruction auto-injection |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_system-prompt-builder]] | upstream | 0.23 |
| [[p03_sp_engineering_nucleus]] | upstream | 0.23 |
| [[bld_instruction_dispatch_rule]] | upstream | 0.22 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.21 |
| [[bld_output_template_system_prompt]] | sibling | 0.20 |
| [[bld_instruction_memory_scope]] | upstream | 0.20 |
| [[bld_output_template_input_schema]] | sibling | 0.20 |
| [[bld_norms]] | downstream | 0.19 |
| [[bld_output_template_instruction]] | sibling | 0.19 |
| [[bld_instruction_golden_test]] | upstream | 0.19 |
