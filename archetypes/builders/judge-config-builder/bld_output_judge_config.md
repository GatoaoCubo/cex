---
kind: output_template
id: bld_output_template_judge_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for judge_config production
quality: 8.7
title: "Output Template Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, output_template]
tldr: "Template with vars for judge_config production"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_playground_config
  - bld_output_template_workflow_node
  - bld_config_judge_config
  - bld_output_template_sandbox_spec
  - bld_examples_tts_provider
  - p04_function_def_NAME
  - bld_output_template_reranker_config
  - bld_output_template_sdk_example
  - bld_output_template_usage_quota
  - bld_examples_workflow_primitive
---

```yaml
---
id: p07_jc_{{name}}.md
name: {{name}}
description: {{description}}
quality: null
parameters:
  - key: {{param_key}}
    value: {{param_value}}
rules:
  - {{rule_1}}
  - {{rule_2}}
---
```

<!-- id: Unique identifier following p07_jc_[a-z][a-z0-9_]+.md -->
<!-- name: Human-readable configuration name -->
<!-- description: Brief purpose of this judge config -->
<!-- param_key: Parameter name (e.g., "max_score") -->
<!-- param_value: Parameter value (e.g., "100") -->
<!-- rule_1: First validation rule (e.g., "require_signature") -->
<!-- rule_2: Second validation rule (e.g., "check_timestamp") -->

**Example Parameters Table**

| Parameter     | Value   | Description          |
|--------------|---------|----------------------|
| max_score    | 100     | Maximum possible score |
| timeout_sec  | 30      | Timeout duration     |

**Sample Code Block**
```json
{
  "judge_config": {
    "parameters": {
      "max_score": 100,
      "timeout_sec": 30
    },
    "rules": ["require_signature", "check_timestamp"]
  }
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_playground_config]] | sibling | 0.32 |
| [[bld_output_template_workflow_node]] | sibling | 0.26 |
| [[bld_config_judge_config]] | downstream | 0.23 |
| [[bld_output_template_sandbox_spec]] | sibling | 0.22 |
| [[bld_examples_tts_provider]] | downstream | 0.22 |
| [[p04_function_def_NAME]] | upstream | 0.21 |
| [[bld_output_template_reranker_config]] | sibling | 0.21 |
| [[bld_output_template_sdk_example]] | sibling | 0.21 |
| [[bld_output_template_usage_quota]] | sibling | 0.20 |
| [[bld_examples_workflow_primitive]] | downstream | 0.19 |
