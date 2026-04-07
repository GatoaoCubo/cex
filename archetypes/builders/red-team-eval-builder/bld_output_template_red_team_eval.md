---
kind: output_template
id: bld_output_template_red_team_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a red_team_eval artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_is_being_tested_1_to_2_sentences}}
{{threat_model_summary_and_who_runs_this_eval}}
## Attack Scenarios
### {{attack_type_1}}
Pattern: `{{adversarial_input_placeholder_no_real_exploits}}`
Expected safe response: {{what_the_model_should_do}}
OWASP ref: LLM{{NN}}
Framework config:
```yaml
{{framework_specific_snippet_if_applicable}}
```
### {{attack_type_2}}
Pattern: `{{adversarial_input_placeholder}}`
Expected safe response: {{what_the_model_should_do}}
OWASP ref: LLM{{NN}}
## Pass Criteria
{{explicit_measurable_definition_of_safe_behavior}}
- {{criterion_1_observable_refusal_or_deflection}}
- {{criterion_2_no_disclosure_condition}}
- {{criterion_3_scope_enforcement}}
## Configuration
Framework: {{framework_name}}
Setup: {{install_or_config_instructions}}
Env vars: {{env_var_list_with_purpose}}
Run: `{{framework_run_command}}`
Expected output: {{what_a_passing_report_looks_like}}
