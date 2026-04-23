---
quality: 8.2
quality: 7.7
id: bld_output_template_deployment_manifest
kind: knowledge_card
pillar: P05
title: "Output Template: deployment_manifest"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
tags: [output_template, deployment_manifest, P09]
llm_function: PRODUCE
tldr: "Canonical output template for deployment_manifest artifacts with all required placeholders."
density_score: null
related:
  - bld_output_template_dataset_card
  - bld_output_template_type_def
  - bld_collaboration_prompt_version
  - bld_output_template_input_schema
  - bld_schema_search_strategy
  - bld_output_template_prompt_template
  - bld_output_template_runtime_rule
  - bld_output_template_instruction
  - bld_output_template_quickstart_guide
  - bld_schema_rl_algorithm
---

# Output Template: deployment_manifest

## Frontmatter Template
```yaml
---
id: p09_dm_{{name_slug}}
kind: deployment_manifest
pillar: P09
version: 1.0.0
manifest_name: "{{manifest_name}}"
target_env: {{target_env}}
artifacts_count: {{artifacts_count}}
rollback_to: "{{rollback_to}}"
domain: "{{domain}}"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: null
tags: [deployment_manifest, {{domain}}, {{target_env}}]
tldr: "{{one_sentence_summary}}"
---
```

## Body Template
```markdown
# {{manifest_name}}

## Artifacts
| Name | Version | Checksum (SHA256) | Source |
|------|---------|-------------------|--------|
| {{artifact_name}} | {{version}} | {{sha256}} | {{registry_path}} |

## Target Environment
- **environment**: {{target_env}}
- **namespace**: {{namespace}}
- **region**: {{region}}
- **cluster**: {{cluster_id}}

## Config Overrides
| Key | Value | Notes |
|-----|-------|-------|
| {{env_var}} | {{value}} | {{note}} |

Secrets:
- {{secret_name}}: {{vault_path_or_k8s_secret}}

## Rollback Strategy
- **rollback_to**: {{rollback_to}}
- **trigger**: health check fails after {{readiness_timeout_seconds}}s
- **health_check**: GET {{health_check_endpoint}} -> 2xx
- **auto_rollback**: {{true|false}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_dataset_card]] | related | 0.19 |
| [[bld_output_template_type_def]] | related | 0.19 |
| [[bld_collaboration_prompt_version]] | downstream | 0.17 |
| [[bld_output_template_input_schema]] | related | 0.17 |
| [[bld_schema_search_strategy]] | downstream | 0.17 |
| [[bld_output_template_prompt_template]] | related | 0.17 |
| [[bld_output_template_runtime_rule]] | related | 0.16 |
| [[bld_output_template_instruction]] | related | 0.16 |
| [[bld_output_template_quickstart_guide]] | related | 0.16 |
| [[bld_schema_rl_algorithm]] | downstream | 0.16 |
