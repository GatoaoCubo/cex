---
kind: output_template
id: bld_output_template_secret_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a secret_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_credentials_this_config_governs_1_to_2_sentences}}
{{which_system_or_agent_uses_them_and_risk_classification}}
## Provider
Backend: {{provider_name}} — {{auth_method}}
Paths:
- `{{secret_path_placeholder_1}}` — {{what_it_stores}}
- `{{secret_path_placeholder_2}}` — {{what_it_stores}}
{{any_provider_specific_notes}}
## Rotation Policy
- Frequency: {{rotation_frequency}}
- Method: {{rotation_method}}
- Trigger: {{what_triggers_rotation}}
- Rollback: {{how_to_rollback_if_rotation_fails}}
## Access Pattern
Pattern: {{dynamic|static|injected|env}}
{{how_agents_retrieve_at_runtime_step_by_step}}
Lease/TTL: {{lease_duration_or_N/A}}
Fallback: {{fallback_behavior_if_provider_unavailable}}
