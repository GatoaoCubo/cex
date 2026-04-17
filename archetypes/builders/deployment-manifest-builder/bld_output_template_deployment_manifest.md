---
id: bld_output_template_deployment_manifest
kind: knowledge_card
pillar: P05
title: "Output Template: deployment_manifest"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
quality: 7.0
tags: [output_template, deployment_manifest, P09]
llm_function: PRODUCE
tldr: "Canonical output template for deployment_manifest artifacts with all required placeholders."
density_score: null
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
