---
kind: output_template
id: bld_output_template_pattern
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a pattern
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_learning_record
  - bld_output_template_axiom
  - pattern-builder
  - bld_memory_pattern
  - p03_sp_pattern_builder
  - p11_qg_pattern
  - p03_ins_pattern
  - bld_architecture_pattern
  - bld_schema_pattern
  - bld_output_template_invariant
---

# Output Template: pattern
```yaml
id: p08_pat_{{slug}}
kind: pattern
pillar: P08

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

domain: "{{domain}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"

name: "{{pattern_name_2_5_words}}"
problem: "{{recurring_problem_one_sentence}}"
solution: "{{core_solution_approach}}"
context: "{{when_where_pattern_applies}}"

forces: [{{force_1}}, {{force_2}}]
consequences: [{{consequence_1}}, {{consequence_2}}]
related_patterns: [{{related_1}}]
anti_patterns: [{{anti_1}}]

applicability: "{{when_to_use_and_when_not}}"
keywords: [{{kw_1}}, {{kw_2}}, {{kw_3}}]
```
## Problem
`{{recurring_problem_in_concrete_terms}}`
## Context
1. Environment: `{{where_problem_occurs}}`
2. Frequency: `{{how_often_encountered}}`
3. Severity: `{{impact_if_unsolved}}`
## Forces
1. `{{tension_1}}`: `{{why_hard_1}}`
2. `{{tension_2}}`: `{{why_hard_2}}`
3. `{{tension_3}}`: `{{why_hard_3}}`
## Solution
`{{reusable_approach_concrete_steps}}`
```text
{{optional_ascii_diagram_of_solution}}
```
## Consequences
Benefits:
1. `{{benefit_1}}`
2. `{{benefit_2}}`
Costs:
1. `{{cost_1}}`
2. `{{cost_2}}`
## Examples
1. **`{{example_name_1}}`**: `{{concrete_application_1}}`
2. **`{{example_name_2}}`**: `{{concrete_application_2}}`
## Anti-Patterns
1. **`{{anti_name_1}}`**: `{{why_wrong_1}}`
2. **`{{anti_name_2}}`**: `{{why_wrong_2}}`
## Related Patterns
1. `{{related_pattern_1}}`: `{{relationship_description_1}}`
2. `{{related_pattern_2}}`: `{{relationship_description_2}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_learning_record]] | sibling | 0.41 |
| [[bld_output_template_axiom]] | sibling | 0.36 |
| [[pattern-builder]] | downstream | 0.35 |
| [[bld_memory_pattern]] | downstream | 0.34 |
| [[p03_sp_pattern_builder]] | upstream | 0.32 |
| [[p11_qg_pattern]] | downstream | 0.32 |
| [[p03_ins_pattern]] | upstream | 0.31 |
| [[bld_architecture_pattern]] | downstream | 0.31 |
| [[bld_schema_pattern]] | downstream | 0.31 |
| [[bld_output_template_invariant]] | sibling | 0.30 |
