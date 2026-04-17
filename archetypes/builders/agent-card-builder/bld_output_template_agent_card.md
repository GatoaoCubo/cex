---
kind: output_template
id: bld_output_template_agent_card
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a agent_card
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: agent_card
```yaml
id: p08_ac_{{name_lower}}
kind: agent_card
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{AGENT_GROUP_NAME}}"
role: "{{primary_function_description}}"
model: "{{llm_model}}"
mcps: [{{mcp_1}}, {{mcp_2}}]
domain_area: "{{domain_this_agent_group_covers}}"
boot_sequence:
  - "{{boot_step_1}}"
  - "{{boot_step_2}}"
constraints:
  - "{{constraint_1}}"
  - "{{constraint_2}}"
dispatch_keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
tools: [{{tool_1}}, {{tool_2}}]
dependencies: [{{dependency_1}}]
scaling:
  max_concurrent: {{integer}}
  timeout_minutes: {{integer}}
  memory_limit_mb: {{integer}}
monitoring:
  health_check: "{{command_or_url}}"
  signal_on_complete: {{boolean}}
  alert_on_failure: {{boolean}}
runtime: "{{claude_or_codex}}"
mcp_config_file: "{{path_to_mcp_json_or_null}}"
flags: [{{flag_1}}, {{flag_2}}]
domain: "{{domain_value}}"
quality: null
tags: [agent_group, {{domain_tag}}, {{name_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Role
`{{what_the_agent_group_does_and_primary_function}}`
## Model & MCPs
`{{llm_model_details_and_mcp_server_specs}}`
## Boot Sequence
`{{ordered_initialization_steps}}`
## Dispatch
`{{keywords_and_routing_rules}}`
## Constraints
`{{operational_limits_and_prohibitions}}`
## Dependencies
`{{external_services_and_sibling_agent_groups}}`
## Scaling & Monitoring
`{{concurrency_timeouts_health_checks}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | agent card construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
