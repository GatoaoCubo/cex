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
related:
  - bld_output_template_workflow_node
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
  - bld_output_template_playground_config
  - sandbox-spec-builder
  - bld_output_template_judge_config
  - bld_collaboration_sandbox_spec
  - code-executor-builder
  - p03_sp_sandbox_config_builder
  - kc_sandbox_config
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_workflow_node]] | sibling | 0.28 |
| [[bld_schema_sandbox_spec]] | downstream | 0.26 |
| [[bld_schema_sandbox_config]] | downstream | 0.23 |
| [[bld_output_template_playground_config]] | sibling | 0.23 |
| [[sandbox-spec-builder]] | downstream | 0.22 |
| [[bld_output_template_judge_config]] | sibling | 0.21 |
| [[bld_collaboration_sandbox_spec]] | downstream | 0.20 |
| [[code-executor-builder]] | upstream | 0.20 |
| [[p03_sp_sandbox_config_builder]] | upstream | 0.20 |
| [[kc_sandbox_config]] | upstream | 0.20 |
