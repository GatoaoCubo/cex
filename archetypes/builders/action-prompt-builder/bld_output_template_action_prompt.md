---
kind: output_template
id: bld_output_template_action_prompt
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an action_prompt
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: action_prompt
```yaml
id: p03_ap_{{task_slug}}
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
action: "{{verb_phrase_describing_task}}"
input_required:
  - "{{input_item_1_with_type}}"
  - "{{input_item_2_with_type}}"
output_expected: "{{output_structure_description}}"
purpose: "{{why_this_prompt_exists}}"
steps_count: {{integer_or_omit}}
timeout: "{{max_time_or_null}}"
edge_cases:
  - "{{edge_case_1}}"
  - "{{edge_case_2}}"
constraints:
  - "{{constraint_1}}"
domain: "{{domain_value}}"
quality: null
tags: [action_prompt, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Context
{{background_2_3_sentences}}
Purpose: {{purpose_restated_concisely}}
## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| {{input_1}} | {{type}} | {{format}} | YES |
| {{input_2}} | {{type}} | {{format}} | {{YES/NO}} |
## Execution
1. {{step_1_transform_input}}
2. {{step_2_process}}
3. {{step_3_produce_output}}
## Output
Format: {{output_format}}
Structure:
```{{format}}
{{output_structure_example}}
```
## Validation
- {{criterion_1_verifiable}}
- {{criterion_2_verifiable}}
- Edge case handled: {{edge_case_1_check}}
## References
- {{reference_1}}
- {{reference_2}}
