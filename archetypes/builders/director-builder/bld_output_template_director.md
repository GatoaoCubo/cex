---
kind: output_template
id: bld_output_template_director
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a satellite_spec
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: satellite_spec
```yaml
id: p08_sat_{{name_lower}}
kind: satellite_spec
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{SATELLITE_NAME}}"
role: "{{primary_function_description}}"
model: "{{llm_model}}"
mcps: [{{mcp_1}}, {{mcp_2}}]
domain_area: "{{domain_this_satellite_covers}}"
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
tags: [satellite, {{domain_tag}}, {{name_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Role
{{what_the_satellite_does_and_primary_function}}
## Model & MCPs
{{llm_model_details_and_mcp_server_specs}}
## Boot Sequence
{{ordered_initialization_steps}}
## Dispatch
{{keywords_and_routing_rules}}
## Constraints
{{operational_limits_and_prohibitions}}
## Dependencies
{{external_services_and_sibling_satellites}}
## Scaling & Monitoring
{{concurrency_timeouts_health_checks}}
## References
- {{reference_1}}
- {{reference_2}}
