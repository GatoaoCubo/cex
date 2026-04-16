---
kind: output_template
id: bld_output_template_playground_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for playground_config production
quality: 8.7
title: "Output Template Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, output_template]
tldr: "Template with vars for playground_config production"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p09_pg_{{name}}.yaml
quality: null
description: {{description}}
version: {{version}}
parameters:
  {{parameter_name}}: {{parameter_value}}
---
```

<!-- Replace {{name}} with a lowercase alphanumeric identifier (e.g., "demo") -->
<!-- quality MUST remain null -->
<!-- Replace {{description}} with a brief config purpose -->
<!-- Replace {{version}} with semantic version (e.g., "1.0.0") -->
<!-- Add parameters under "parameters" key -->

**Example Parameters Table:**

| Parameter Name  | Type   | Description              |
|-----------------|--------|--------------------------|
| timeout         | int    | Max wait time in seconds |
| enable_logging  | bool   | Toggle debug output      |

**Sample Code Block:**
```yaml
parameters:
  timeout: 30
  enable_logging: true
  api_key: {{api_key}}  <!-- Replace with actual key -->
```
