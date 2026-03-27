---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for unit_eval production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: unit_eval

```yaml
---
id: p07_ue_{{target_slug}}
kind: unit_eval
pillar: P07
title: "{{eval_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target: "{{agent_or_prompt_name}}"
target_kind: "{{artifact_kind_of_target}}"
input: "{{exact_input_prompt}}"
expected_output: "{{correct_output_description}}"
assertions:
  - gate_ref: "{{gate_id}}"
    check: "{{what_to_verify}}"
    expected: {{true_or_value}}
    severity: "{{HARD_or_SOFT}}"
timeout: {{seconds}}
setup: "{{preconditions}}"
teardown: "{{cleanup}}"
edge_case: {{true_or_false}}
coverage_scope: "{{what_gates_this_covers}}"
domain: "{{domain_value}}"
quality: null
tags: [unit-eval, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
---

## Input
{{verbatim_input_prompt}}

## Expected Output
{{concrete_expected_output}}

## Assertions
{{gate_mapped_checks_with_expected_values}}

## Setup
{{preconditions_and_state_init}}

## Teardown
{{cleanup_after_execution}}
```
