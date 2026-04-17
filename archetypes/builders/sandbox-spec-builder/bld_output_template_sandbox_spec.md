---
kind: output_template
id: bld_output_template_sandbox_spec
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sandbox_spec production
quality: 8.7
title: "Output Template Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, output_template]
tldr: "Template with vars for sandbox_spec production"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p09_sb_{{name}}.yaml
name: {{name}}
description: {{description}}
version: {{version}}
quality: null
sandbox_type: {{sandbox_type}}
environment: {{environment}}
parameters:
  - {{param1}}
  - {{param2}}
---
```

<!-- id: Unique identifier following p09_sb_[a-z][a-z0-9_]+.yaml pattern -->
<!-- name: Human-readable name of the sandbox -->
<!-- description: Brief summary of the sandbox's purpose -->
<!-- version: Semantic version (e.g., 1.0.0) -->
<!-- sandbox_type: Type of sandbox (e.g., isolated, shared) -->
<!-- environment: Target environment (e.g., dev, test) -->
<!-- param1: First configuration parameter -->
<!-- param2: Second configuration parameter -->

| Parameter       | Value       | Description                  |
|----------------|-------------|------------------------------|
| sandbox_type   | isolated    | Isolation level              |
| environment    | dev         | Target environment           |
| max_users      | 10          | Maximum concurrent users     |

```yaml
sandbox:
  id: p09_sb_dev_env
  environment: development
  resources:
    cpu: 2
    memory: 4GB
```
