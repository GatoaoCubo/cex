---
kind: output_template
id: bld_output_template_client
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a client artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: client
```yaml
id: p04_client_{{api_slug}}
kind: api_client
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_client_name}}"
api: "{{target_api_name}}"
base_url: "{{api_base_url}}"
auth: {{none|api_key|oauth|bearer}}
endpoints:
  - {{endpoint_name_1}}
  - {{endpoint_name_2}}
quality: null
tags: [client, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_client_does_max_200ch}}"
rate_limit: "{{N_requests_per_unit}}"
retry: "{{max_retries_and_backoff}}"
timeout: "{{request_timeout}}"
serialization: {{json|xml|protobuf}}
pagination: {{cursor|offset|none}}
error_codes: [{{code_1}}, {{code_2}}]
caching: "{{cache_strategy}}"
```
## Overview
{{what_api_client_consumes_1_to_2_sentences}}
{{who_consumes_it_and_primary_use_case}}
## Endpoints
### {{endpoint_name_1}}
{{METHOD}} {{path}} — {{endpoint_description}}
Parameters:
- `{{param_1}}` ({{type}}, {{required|optional}}): {{param_description}}
- `{{param_2}}` ({{type}}, {{required|optional}}): {{param_description}}
Returns: {{return_description}}
### {{endpoint_name_2}}
{{METHOD}} {{path}} — {{endpoint_description}}
Parameters:
- `{{param_1}}` ({{type}}, {{required|optional}}): {{param_description}}
Returns: {{return_description}}
## Auth & Config
Base URL: {{base_url}}
Auth: {{auth_method_and_header_format}}
Headers: {{required_headers}}
## Error Handling
- {{error_code}}: {{description}} — {{retry_behavior}}
- {{error_code}}: {{description}} — {{retry_behavior}}
