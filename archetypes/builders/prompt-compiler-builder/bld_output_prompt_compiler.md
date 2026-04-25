---
kind: output_template
id: bld_output_template_prompt_compiler
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a prompt_compiler artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, output_template, P03]
tldr: "Fill-in template for prompt_compiler artifacts with kind resolution tables, verb maps, and fallback heuristics."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
related:
  - p03_ins_prompt_compiler
  - p03_sp_prompt_compiler_builder
  - p11_qg_prompt_compiler
  - prompt-compiler-builder
  - bld_examples_prompt_compiler
  - bld_architecture_prompt_compiler
  - bld_schema_prompt_compiler
  - bld_knowledge_card_prompt_compiler
  - p01_kc_prompt_compiler
  - bld_memory_prompt_compiler
---

# Output Template: prompt_compiler
```yaml
id: p03_pc_{{compiler_slug}}
kind: prompt_compiler
pillar: P03

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

title: "{{human_readable_title}}"
domain: "{{resolution_domain}}"
coverage: {{integer_kinds_covered}}
languages: [{{lang_1}}, {{lang_2}}]

quality: null
tags: [prompt_compiler, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
```
## Preamble
`{{what_this_artifact_is}}`
`{{how_an_LLM_uses_it}}`
`{{relationship_to_8F_pipeline}}`
## Kind Resolution Table
### `{{Pillar_Group}}` (`{{pillar_code}}`)
| Kind | Nucleus | Patterns (EN) | Patterns (PT) | Verb | 8F | Boundary |
|------|---------|---------------|---------------|------|----|----------|
| {{kind}} | `{{N0x}}` | {{en_patterns}} | {{pt_patterns}} | {{verb}} | {{fn}} | `{{boundary}}` |
(repeat for all 300 kinds, grouped by pillar P01-P12)
## Verb Resolution Table
| PT Verb | EN Verb | Canonical Action | Primary 8F Function |
|---------|---------|-----------------|---------------------|
| `{{pt_verb}}` | {{en_verb}} | `{{canonical}}` | {{F1-F8}} |
(minimum 30 entries)
## Ambiguity Resolution
`{{protocol_for_multi_kind_matches}}`
1. `{{step_1_context_check}}`
2. `{{step_2_specificity_rank}}`
3. `{{step_3_frequency_prefer}}`
4. `{{step_4_gdp_trigger}}`
## Fallback Heuristics
`{{protocol_for_unrecognized_input}}`
1. `{{step_1_tfidf_search}}`
2. `{{step_2_semantic_similarity}}`
3. `{{step_3_confidence_threshold}}`
4. `{{step_4_user_clarification}}`
## Nucleus Routing Matrix
| Kind | N01 | N02 | N03 | N04 | N05 | N06 | N07 |
|------|-----|-----|-----|-----|-----|-----|-----|
| {{kind}} | `{{x_or_dash}}` | ... | ... | ... | ... | ... | ... |
## Behavioral Instructions
`{{rules_for_llm_as_prompt_compiler}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | prompt_compiler construction |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_prompt_compiler]] | upstream | 0.56 |
| [[p03_sp_prompt_compiler_builder]] | upstream | 0.48 |
| [[p11_qg_prompt_compiler]] | downstream | 0.46 |
| [[prompt-compiler-builder]] | upstream | 0.46 |
| [[bld_examples_prompt_compiler]] | downstream | 0.44 |
| [[bld_architecture_prompt_compiler]] | downstream | 0.44 |
| [[bld_schema_prompt_compiler]] | downstream | 0.42 |
| [[bld_knowledge_card_prompt_compiler]] | upstream | 0.41 |
| [[p01_kc_prompt_compiler]] | upstream | 0.36 |
| [[bld_memory_prompt_compiler]] | downstream | 0.27 |
