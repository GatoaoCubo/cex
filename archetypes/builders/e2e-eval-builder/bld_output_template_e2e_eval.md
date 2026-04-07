---
kind: output_template
id: bld_output_template_e2e_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for e2e_eval production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template E2E Eval"
version: "1.0.0"
author: n03_builder
tags: [e2e_eval, builder, examples]
tldr: "Golden and anti-examples for e2e eval construction, demonstrating ideal structure and common pitfalls."
domain: "e2e eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: e2e_eval
```yaml
id: p07_e2e_{{pipeline_slug}}
kind: e2e_eval
pillar: P07
title: "{{eval_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
pipeline: "{{pipeline_name}}"
stages:
  - name: "{{stage_name}}"
    agent: "{{agent_name}}"
    input: "{{stage_input}}"
    expected_output: "{{stage_expected}}"
    assertion: "{{stage_assertion}}"
input: "{{pipeline_entry_data}}"
expected_output: "{{final_pipeline_result}}"
timeout: {{seconds}}
environment: "{{target_environment}}"
data_fixtures:
  - "{{fixture_1}}"
  - "{{fixture_2}}"
cleanup: "{{post_test_reset}}"
parallel: {{true_or_false}}
reporting: "{{result_format}}"
domain: "{{domain_value}}"
quality: null
tags: [e2e-eval, {{pipeline}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
## Pipeline Overview
{{visual_flow_of_stages}}
## Stages
{{each_stage_with_agent_input_output_assertion}}
## Data Fixtures
{{test_data_for_reproducibility}}
## Expected Output
{{final_pipeline_result}}
## Cleanup
{{post_test_state_reset}}
```

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | e2e eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
