---
kind: output_template
id: bld_output_template_workflow
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a workflow
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
satellites: [{{sat_1}}, {{sat_2}}]
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
{{why_this_workflow_exists_2_to_4_sentences}}
## Steps
### Step 1: {{step_name}} [{{agent}}]
- **Agent**: {{satellite_or_agent_name}}
- **Action**: {{what_this_step_does}}
- **Input**: {{input_description}}
- **Output**: {{output_description}}
- **Signal**: {{signal_on_completion}}
- **Depends on**: {{step_dependencies_or_none}}
### Step 2: {{step_name}} [{{agent}}]
- **Agent**: {{satellite_or_agent_name}}
- **Action**: {{what_this_step_does}}
- **Input**: {{input_from_previous_step}}
- **Output**: {{output_description}}
- **Signal**: {{signal_on_completion}}
- **Depends on**: Step 1
{{...repeat for steps_count steps}}
## Dependencies
- {{prerequisite_artifact_or_condition_1}}
- {{prerequisite_artifact_or_condition_2}}
## Signals
- **On step complete**: {{signal_type}} emitted by {{satellite}} (see signal-builder)
- **On workflow complete**: {{final_signal}}
- **On error**: {{error_signal_and_recovery}}
## References
- {{reference_1}}
- {{reference_2}}
