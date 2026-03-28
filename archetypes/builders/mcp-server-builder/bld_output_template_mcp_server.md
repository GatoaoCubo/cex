---
kind: output_template
id: bld_output_template_mcp_server
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a mcp_server artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: mcp_server
```yaml
id: p04_mcp_{{server_slug}}
kind: mcp_server
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_server_name}}"
transport: {{stdio|sse|http}}
tools_provided:
  - {{tool_name_1}}
  - {{tool_name_2}}
resources_provided:
  - {{uri_template_1}}
  - {{uri_template_2}}
auth: {{none|api_key|oauth|bearer}}
description: "{{what_server_does_max_200ch}}"
health_check: "{{endpoint_or_command}}"
rate_limit: "{{N_requests_per_unit}}"
versioning: "{{version_negotiation_strategy}}"
quality: null
tags: [mcp_server, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Overview
{{what_the_server_does_1_to_2_sentences}}
{{who_consumes_it_and_primary_use_case}}
## Tools
### {{tool_name_1}}
{{tool_description}}
Parameters:
- `{{param_1}}` ({{type}}, {{required|optional}}): {{param_description}}
- `{{param_2}}` ({{type}}, {{required|optional}}): {{param_description}}
Returns: {{return_description}}
### {{tool_name_2}}
{{tool_description}}
Parameters:
- `{{param_1}}` ({{type}}, {{required|optional}}): {{param_description}}
Returns: {{return_description}}
## Resources
### {{uri_template_1}}
Content-Type: {{mime_type}}
{{resource_description}}
### {{uri_template_2}}
Content-Type: {{mime_type}}
{{resource_description}}
## Transport & Auth
Transport: {{stdio|sse|http}}
{{transport_connection_details}}
Auth: {{auth_method_and_config}}
