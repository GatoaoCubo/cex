---
kind: output_template
id: bld_output_template_llm_evaluation_scenario
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for llm_evaluation_scenario production
quality: 9.1
title: "Output Template LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, output_template, helm]
tldr: "Template with vars for llm_evaluation_scenario production"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_llm_evaluation_scenario
  - bld_examples_llm_evaluation_scenario
  - bld_config_llm_evaluation_scenario
  - bld_instruction_llm_evaluation_scenario
  - p03_sp_llm_evaluation_scenario_builder
  - p07_qg_llm_evaluation_scenario
  - llm-evaluation-scenario-builder
  - bld_knowledge_card_llm_evaluation_scenario
  - bld_collaboration_llm_evaluation_scenario
  - p10_lr_llm_evaluation_scenario_builder
---

```markdown
---
id: p07_evs_{{subject_area}}_{{capability_slug}}.md
kind: llm_evaluation_scenario
pillar: P07
title: "HELM Scenario: {{subject_area}} / {{capability}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{subject_area}}"
quality: null
tags: [helm, {{subject_area}}, {{capability_slug}}, evaluation, scenario]
tldr: "{{one_line_description}}"
subject_area: {{subject_area}}
capability: {{capability}}
task_format: {{task_format}}
primary_metric: {{primary_metric}}
num_instances: {{num_instances}}
num_few_shot: {{num_few_shot}}
adapter_ref: "{{prompt_template_id}}"
dataset_source: "{{dataset_name}} ({{license}})"
canonicalization_fn: "{{normalization_function}}"
token_cost_estimate: "{{estimate}}"
---

## Scenario Overview
**Subject Area**: {{subject_area}} (HELM taxonomy)
**Capability Tested**: {{capability}}
**Task Format**: {{task_format}}

| Field | Value |
|-------|-------|
| HELM Taxonomy | {{helm_category}} |
| IBM Extension | {{ibm_extension_domain}} <!-- or N/A --> |
| Upstream Dataset | {{dataset_name}} |
| License | {{license}} |

## Task Instance Specification
**Input Format**: {{input_description}}
**Output Format**: {{output_description}}
**Answer Key**: {{answer_key_description}}

### Sample Instance
```yaml
input: "{{sample_input}}"
expected_output: "{{sample_output}}"
metadata:
  source: {{dataset_name}}
  split: {{split}}
  difficulty: {{difficulty_label}}
```

## Few-Shot Pool
- **Pool Size**: {{pool_size}} instances
- **Selection Strategy**: {{selection_strategy}}
- **Demonstration Format**: {{demo_format}}

| # | Input Snippet | Output | Notes |
|---|--------------|--------|-------|
| 1 | {{demo_1_input}} | {{demo_1_output}} | |
| 2 | {{demo_2_input}} | {{demo_2_output}} | |
| 3 | {{demo_3_input}} | {{demo_3_output}} | |

## Adapter Configuration
| Parameter | Value |
|-----------|-------|
| prompt_template | {{prompt_template_id}} |
| num_train_trials | {{num_train_trials}} |
| num_test_instances | {{num_instances}} |
| max_tokens | {{max_tokens}} |
| temperature | {{temperature}} |
| stop_sequences | {{stop_sequences}} |

## Metric Mapping
| Metric | Family | Aggregation | Threshold |
|--------|--------|-------------|-----------|
| {{primary_metric}} | {{helm_family}} | {{aggregation_fn}} | {{target_score}} |

## Canonicalization Rules
1. {{rule_1}}
2. {{rule_2}}
3. {{rule_3}}

**Normalization Function**: `{{canonicalization_fn}}`

## Token Cost Estimate
| Component | Tokens |
|-----------|--------|
| Prompt (per instance) | {{prompt_tokens}} |
| Completion (per instance) | {{completion_tokens}} |
| Total ({{num_instances}} instances) | {{total_tokens}} |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_llm_evaluation_scenario]] | downstream | 0.55 |
| [[bld_examples_llm_evaluation_scenario]] | downstream | 0.52 |
| [[bld_config_llm_evaluation_scenario]] | downstream | 0.50 |
| [[bld_instruction_llm_evaluation_scenario]] | upstream | 0.48 |
| [[p03_sp_llm_evaluation_scenario_builder]] | upstream | 0.41 |
| [[p07_qg_llm_evaluation_scenario]] | downstream | 0.40 |
| [[llm-evaluation-scenario-builder]] | downstream | 0.39 |
| [[bld_knowledge_card_llm_evaluation_scenario]] | upstream | 0.35 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.25 |
| [[p10_lr_llm_evaluation_scenario_builder]] | downstream | 0.25 |
