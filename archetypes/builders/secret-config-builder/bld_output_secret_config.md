---
kind: output_template
id: bld_output_template_secret_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a secret_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_secret_config_builder
  - bld_instruction_secret_config
  - bld_schema_secret_config
  - bld_knowledge_card_secret_config
  - p11_qg_secret_config
  - p10_lr_secret_config_builder
  - bld_examples_secret_config
  - bld_config_secret_config
  - secret-config-builder
  - bld_architecture_secret_config
---

# Output Template: secret_config
```yaml
id: p09_sec_{{secret_slug}}
kind: secret_config
pillar: P09

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_config_name}}"
provider: {{vault|k8s|aws|portkey|1password|sops}}
rotation_policy:
  frequency: {{daily|weekly|monthly|on-breach}}

  method: {{automatic|manual|triggered}}
encryption:
  at_rest: {{AES-256-GCM|KMS|SOPS-age|envelope}}
  in_transit: {{TLS 1.3|mTLS}}

access_pattern: {{dynamic|static|injected|env}}
quality: null
tags: [secret_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"

description: "{{what_credentials_this_governs_max_200ch}}"
secret_paths:
  - "{{provider_path_or_arn_placeholder_1}}"
  - "{{provider_path_or_arn_placeholder_2}}"

lease_duration: "{{TTL_or_null}}"
audit_log: {{true|false}}
namespaces: [{{namespace_or_region_1}}, {{namespace_or_region_2}}]
fallback: "{{fallback_provider_or_null}}"
```
## Overview
`{{what_credentials_this_config_governs_1_to_2_sentences}}`
`{{which_system_or_agent_uses_them_and_risk_classification}}`
## Provider
Backend: `{{provider_name}}` — `{{auth_method}}`
Paths:
1. `{{secret_path_placeholder_1}}` — `{{what_it_stores}}`
2. `{{secret_path_placeholder_2}}` — `{{what_it_stores}}`
`{{any_provider_specific_notes}}`
## Rotation Policy
1. Frequency: `{{rotation_frequency}}`
2. Method: `{{rotation_method}}`
3. Trigger: `{{what_triggers_rotation}}`
4. Rollback: `{{how_to_rollback_if_rotation_fails}}`
## Access Pattern
Pattern: {{dynamic|static|injected|env}}
`{{how_agents_retrieve_at_runtime_step_by_step}}`
Lease/TTL: {{lease_duration_or_N/A}}

Fallback: `{{fallback_behavior_if_provider_unavailable}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | secret config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_secret_config_builder]] | downstream | 0.57 |
| [[bld_instruction_secret_config]] | upstream | 0.46 |
| [[bld_schema_secret_config]] | downstream | 0.44 |
| [[bld_knowledge_card_secret_config]] | upstream | 0.43 |
| [[p11_qg_secret_config]] | downstream | 0.42 |
| [[p10_lr_secret_config_builder]] | downstream | 0.41 |
| [[bld_examples_secret_config]] | downstream | 0.38 |
| [[bld_config_secret_config]] | downstream | 0.37 |
| [[secret-config-builder]] | downstream | 0.32 |
| [[bld_architecture_secret_config]] | downstream | 0.31 |
