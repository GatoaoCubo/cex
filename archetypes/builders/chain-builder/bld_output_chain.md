---
kind: output_template
id: bld_output_template_chain
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a chain
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_chain
  - chain-builder
  - p03_sp_chain_builder
  - bld_output_template_workflow
  - bld_schema_chain
  - bld_knowledge_card_chain
  - p01_kc_chain
  - p11_qg_chain
  - bld_config_chain
  - bld_instruction_chain
---

# Output Template: chain
```yaml
id: p03_ch_{{pipeline_slug}}
kind: chain
pillar: P03

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

title: "{{human_readable_title}}"
steps_count: {{integer_matching_body}}
flow: {{sequential|branching|parallel|mixed}}
input_format: "{{what_first_step_receives}}"

output_format: "{{what_last_step_produces}}"
context_passing: {{full|filtered|summary}}
error_strategy: {{fail_fast|skip|retry|fallback}}
domain: "{{domain_value}}"

quality: null
tags: [chain, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Purpose
`{{why_this_chain_exists_2_to_4_sentences}}`
## Steps
### Step 1: `{{step_name}}`
1. **Input**: `{{input_type_and_description}}`
2. **Prompt**: `{{what_this_step_does}}`
3. **Output**: `{{output_type_and_description}}`
### Step 2: `{{step_name}}`
1. **Input**: `{{receives_from_step_1}}`
2. **Prompt**: `{{what_this_step_does}}`
3. **Output**: `{{output_type_and_description}}`
{{...repeat for steps_count steps}}
## Data Flow
```text
{{step_1}} --{{data_type}}--> {{step_2}} --{{data_type}}--> {{step_N}}
```
Context passing: `{{context_passing_strategy_description}}`
## Error Handling
1. **Strategy**: `{{error_strategy}}`
2. **On failure at step N**: `{{failure_behavior}}`
3. **Retry policy**: `{{retry_details_if_applicable}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | chain construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_chain]] | downstream | 0.49 |
| [[chain-builder]] | upstream | 0.45 |
| [[p03_sp_chain_builder]] | upstream | 0.45 |
| [[bld_output_template_workflow]] | sibling | 0.45 |
| [[bld_schema_chain]] | downstream | 0.43 |
| [[bld_knowledge_card_chain]] | upstream | 0.39 |
| [[p01_kc_chain]] | upstream | 0.39 |
| [[p11_qg_chain]] | downstream | 0.38 |
| [[bld_config_chain]] | downstream | 0.37 |
| [[bld_instruction_chain]] | upstream | 0.37 |
