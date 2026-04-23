---
kind: output_template
id: bld_output_template_workflow
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a workflow
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Workflow"
version: "1.0.0"
author: n03_builder
tags: [workflow, builder, examples]
tldr: "Golden and anti-examples for workflow construction, demonstrating ideal structure and common pitfalls."
domain: "workflow construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_workflow
  - workflow-builder
  - bld_knowledge_card_workflow
  - p12_wf_builder_8f_pipeline
  - bld_architecture_workflow
  - bld_output_template_chain
  - p01_kc_workflow
  - bld_schema_workflow
  - bld_collaboration_workflow
  - bld_memory_workflow
---

# Output Template: workflow
```yaml
id: p12_wf_{{name_slug}}
kind: workflow
pillar: P12

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

title: "{{human_readable_title}}"
steps_count: {{integer_matching_body}}
execution: {{sequential|parallel|mixed}}
agent_groups: [{{sat_1}}, {{sat_2}}]

timeout: {{total_seconds}}
retry_policy: {{none|per_step|global}}
depends_on: [{{prerequisite_1}}]
signals: [complete, error]

spawn_configs: [{{p12_spawn_ref_1}}]
domain: "{{domain_value}}"
quality: null
tags: [workflow, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Purpose
`{{why_this_workflow_exists_2_to_4_sentences}}`
## Steps
### Step 1: `{{step_name}}` [`{{agent}}`]
1. **Agent**: `{{agent_group_or_agent_name}}`
2. **Action**: `{{what_this_step_does}}`
3. **Input**: `{{input_description}}`
4. **Output**: `{{output_description}}`
5. **Signal**: `{{signal_on_completion}}`
6. **Depends on**: `{{step_dependencies_or_none}}`
### Step 2: `{{step_name}}` [`{{agent}}`]
1. **Agent**: `{{agent_group_or_agent_name}}`
2. **Action**: `{{what_this_step_does}}`
3. **Input**: `{{input_from_previous_step}}`
4. **Output**: `{{output_description}}`
5. **Signal**: `{{signal_on_completion}}`
6. **Depends on**: Step 1
{{...repeat for steps_count steps}}
## Dependencies
1. `{{prerequisite_artifact_or_condition_1}}`
2. `{{prerequisite_artifact_or_condition_2}}`
## Signals
1. **On step complete**: `{{signal_type}}` emitted by `{{agent_group}}` (see signal-builder)
2. **On workflow complete**: `{{final_signal}}`
3. **On error**: `{{error_signal_and_recovery}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | workflow construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_workflow]] | downstream | 0.46 |
| [[workflow-builder]] | downstream | 0.45 |
| [[bld_knowledge_card_workflow]] | upstream | 0.42 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.41 |
| [[bld_architecture_workflow]] | downstream | 0.39 |
| [[bld_output_template_chain]] | sibling | 0.39 |
| [[p01_kc_workflow]] | downstream | 0.38 |
| [[bld_schema_workflow]] | downstream | 0.37 |
| [[bld_collaboration_workflow]] | downstream | 0.37 |
| [[bld_memory_workflow]] | downstream | 0.37 |
