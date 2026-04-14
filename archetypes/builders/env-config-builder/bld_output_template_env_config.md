---
kind: output_template
id: bld_output_template_env_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an env_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: env_config
```yaml
id: p09_env_{{scope_slug}}
kind: env_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{global_or_agent_group_or_service}}"
variables:
  - {{VAR_NAME_1}}
  - {{VAR_NAME_2}}
  - {{VAR_NAME_3}}
quality: null
tags: [env_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_config_covers_max_200ch}}"
environment: {{development|staging|production|all}}
sensitive_count: {{N}}
override: "{{override_precedence_summary}}"
validation: "{{validation_strategy_summary}}"
```
## Overview
`{{what_scope_and_why_these_variables_1_to_2_sentences}}`
`{{who_consumes_these_variables}}`
## Variable Catalog
| Variable | Type | Required | Default | Sensitive | Validation |
|----------|------|----------|---------|-----------|------------|
| `{{VAR_NAME_1}}` | {{string|integer|boolean|url|secret}} | {{yes|no}} | {{default_or_dash}} | {{yes|no}} | `{{validation_rule}}` |
| `{{VAR_NAME_2}}` | {{type}} | {{yes|no}} | {{default}} | {{yes|no}} | `{{validation}}` |
| `{{VAR_NAME_3}}` | {{type}} | {{yes|no}} | {{default}} | {{yes|no}} | `{{validation}}` |
## Override Precedence
`{{override_order_description}}`
1. Environment variable (highest priority)
2. Config file (.env, yaml)
3. Default value (lowest priority)
## Sensitive Variables
`{{sensitive_var_handling_rules}}`
- `{{VAR_NAME}}`: {{masking_rule}} — `{{storage_guidance}}`
## References
- `{{reference_1}}`
- `{{reference_2}}`
