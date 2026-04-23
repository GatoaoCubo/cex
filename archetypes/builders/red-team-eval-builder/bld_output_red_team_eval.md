---
kind: output_template
id: bld_output_template_red_team_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a red_team_eval artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Red Team Eval"
version: "1.0.0"
author: n03_builder
tags: [red_team_eval, builder, examples]
tldr: "Golden and anti-examples for red team eval construction, demonstrating ideal structure and common pitfalls."
domain: "red team eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_red_team_eval_builder
  - bld_examples_red_team_eval
  - bld_instruction_red_team_eval
  - red-team-eval-builder
  - bld_knowledge_card_red_team_eval
  - bld_schema_red_team_eval
  - p11_qg_red_team_eval
  - bld_architecture_red_team_eval
  - p10_lr_red_team_eval_builder
  - bld_config_red_team_eval
---

# Output Template: red_team_eval
```yaml
id: p07_rt_{{eval_slug}}
kind: red_team_eval
pillar: P07

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_eval_name}}"
attack_types:
  - {{prompt_injection|jailbreak|pii_leak|toxicity|bias|data_extraction|indirect_injection|privilege_escalation|hallucination_exploit|denial_of_service}}
  - {{attack_type_2}}

target: "{{specific_agent_or_prompt_component}}"
pass_criteria: "{{observable_safe_behavior_definition}}"
quality: null
tags: [red_team_eval, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
description: "{{what_eval_tests_max_200ch}}"
framework: {{promptfoo|garak|deepeval|patronus|costm}}
severity: {{critical|high|medium|low}}

test_count: {{integer_number_of_test_cases}}
owasp_refs: [{{LLM01}}, {{LLM06}}]
env_vars: [{{ENV_VAR_1}}, {{ENV_VAR_2}}]
```
## Overview
`{{what_is_being_tested_1_to_2_sentences}}`
`{{threat_model_summary_and_who_runs_this_eval}}`
## Attack Scenarios
### `{{attack_type_1}}`
Pattern: `{{adversarial_input_placeholder_no_real_exploits}}`
Expected safe response: `{{what_the_model_should_do}}`
OWASP ref: LLM`{{NN}}`

Framework config:
```yaml
{{framework_specific_snippet_if_applicable}}
```
### `{{attack_type_2}}`
Pattern: `{{adversarial_input_placeholder}}`
Expected safe response: `{{what_the_model_should_do}}`
OWASP ref: LLM`{{NN}}`
## Pass Criteria
`{{explicit_measurable_definition_of_safe_behavior}}`
1. `{{criterion_1_observable_refusal_or_deflection}}`
2. `{{criterion_2_no_disclosure_condition}}`
3. `{{criterion_3_scope_enforcement}}`
## Configuration
Framework: `{{framework_name}}`
Setup: `{{install_or_config_instructions}}`
Env vars: `{{env_var_list_with_purpose}}`

Run: `{{framework_run_command}}`
Expected output: `{{what_a_passing_report_looks_like}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | red team eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_red_team_eval_builder]] | downstream | 0.42 |
| [[bld_examples_red_team_eval]] | downstream | 0.38 |
| [[bld_instruction_red_team_eval]] | upstream | 0.36 |
| [[red-team-eval-builder]] | downstream | 0.35 |
| [[bld_knowledge_card_red_team_eval]] | upstream | 0.35 |
| [[bld_schema_red_team_eval]] | downstream | 0.34 |
| [[p11_qg_red_team_eval]] | downstream | 0.33 |
| [[bld_architecture_red_team_eval]] | downstream | 0.32 |
| [[p10_lr_red_team_eval_builder]] | downstream | 0.30 |
| [[bld_config_red_team_eval]] | downstream | 0.27 |
