---
kind: output_template
id: bld_output_template_eval_framework
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for eval_framework production
quality: 8.7
title: "Output Template Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, output_template]
tldr: "Template with vars for eval_framework production"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_playground_config
  - bld_output_template_scoring_rubric
  - bld_output_template_dataset_card
  - bld_schema_sdk_example
  - bld_schema_app_directory_entry
  - bld_output_template_marketplace_app_manifest
---

```yaml
---
id: p07_efw_{{framework_name}}.md
name: {{framework_name}}
description: {{framework_description}}
version: {{version_number}}
quality: null
tags: ["{{tag1}}", "{{tag2}}"]
dependencies: ["{{dep1}}", "{{dep2}}"]
---
```

<!-- framework_name: Alphanumeric identifier for the framework -->
<!-- framework_description: Brief purpose of the framework -->
<!-- version_number: Semantic version (e.g., 1.0.0) -->
<!-- tag1/tag2: Relevant technical categories -->
<!-- dep1/dep2: Required external libraries -->

**Example Configurations**

```yaml
framework: "{{framework_name}}"
parameters:
  timeout: {{timeout_value}} <!-- seconds -->
  retries: {{retry_count}} <!-- attempts -->
```

**Framework Comparison**

| Feature         | Value       | Notes              |
|-----------------|-------------|--------------------|
| Language        | {{lang}}    | <!-- e.g., Python -->
| License         | {{license}} | <!-- e.g., MIT -->
| Performance     | {{perf}}    | <!-- e.g., 10k/s -->
| Last Updated    | {{date}}    | <!-- YYYY-MM-DD -->
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_playground_config]] | sibling | 0.21 |
| [[bld_output_template_scoring_rubric]] | sibling | 0.20 |
| [[bld_output_template_dataset_card]] | sibling | 0.16 |
| [[bld_schema_sdk_example]] | downstream | 0.16 |
| [[bld_schema_app_directory_entry]] | downstream | 0.16 |
| [[bld_output_template_marketplace_app_manifest]] | sibling | 0.15 |
