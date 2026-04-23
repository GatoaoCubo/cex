---
kind: config
id: bld_config_llm_evaluation_scenario
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for llm_evaluation_scenario production
quality: 8.8
title: "Config LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, config, helm]
tldr: "Naming, paths, limits for llm_evaluation_scenario production"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_llm_evaluation_scenario
  - bld_examples_llm_evaluation_scenario
  - bld_schema_llm_evaluation_scenario
  - bld_config_model_registry
  - bld_instruction_llm_evaluation_scenario
  - bld_config_transport_config
  - bld_config_usage_quota
  - bld_config_fhir_agent_capability
  - bld_config_ab_test_config
  - bld_config_search_strategy
---

## Naming Convention
Pattern: `p07_evs_{{subject_area}}_{{capability_slug}}.md`
Examples: `p07_evs_medical_clinical_mcq.md`, `p07_evs_legal_contract_reasoning.md`, `p07_evs_code_python_generation.md`

## Paths
Artifacts stored in: `P07_evaluation/scenarios/{{subject_area}}/{{id}}.md`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: validate HELM taxonomy for subject_area
post_build: register in helm_scenario_registry.yaml
on_error: null
on_quality_fail: return to instruction phase 2

## Registry
Scenarios register in `.cex/registry/helm_scenarios.yaml` on F8 completion.
Registry entry format:
```yaml
id: p07_evs_{{subject_area}}_{{capability_slug}}
subject_area: {{subject_area}}
capability: {{capability}}
task_format: {{task_format}}
primary_metric: {{primary_metric}}
num_instances: {{num_instances}}
dataset_source: {{dataset_source}}
created: {{date}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_llm_evaluation_scenario]] | upstream | 0.52 |
| [[bld_examples_llm_evaluation_scenario]] | upstream | 0.40 |
| [[bld_schema_llm_evaluation_scenario]] | upstream | 0.34 |
| [[bld_config_model_registry]] | sibling | 0.34 |
| [[bld_instruction_llm_evaluation_scenario]] | upstream | 0.33 |
| [[bld_config_transport_config]] | sibling | 0.31 |
| [[bld_config_usage_quota]] | sibling | 0.29 |
| [[bld_config_fhir_agent_capability]] | sibling | 0.29 |
| [[bld_config_ab_test_config]] | sibling | 0.29 |
| [[bld_config_search_strategy]] | sibling | 0.29 |
