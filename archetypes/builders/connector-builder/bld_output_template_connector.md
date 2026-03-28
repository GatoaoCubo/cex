---
kind: output_template
id: bld_output_template_connector
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a connector artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: connector
```yaml
id: p04_conn_{{service_slug}}
kind: connector
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_connector_name}}"
service: "{{external_service_name}}"
protocol: {{rest|websocket|grpc|mqtt}}
auth: {{none|api_key|oauth|bearer|hmac}}
endpoints:
  - {{endpoint_name_1}}
  - {{endpoint_name_2}}
quality: null
tags: [connector, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_connector_does_max_200ch}}"
health_check: "{{health_check_endpoint_or_strategy}}"
mapping: "{{data_mapping_summary}}"
transform: "{{transform_rules_summary}}"
retry: "{{max_retries_and_backoff}}"
rate_limit: "{{N_requests_per_unit}}"
logging: {{structured|plaintext|none}}
versioning: "{{api_version_strategy}}"
```
## Overview
{{what_service_and_integration_pattern_1_to_2_sentences}}
{{who_uses_it_and_primary_data_flow}}
## Endpoints
### {{endpoint_name_1}} ({{inbound|outbound}})
{{METHOD_or_TOPIC}} {{path_or_channel}} — {{endpoint_description}}
Data shape:
- `{{field_1}}` ({{type}}): {{field_description}}
- `{{field_2}}` ({{type}}): {{field_description}}
### {{endpoint_name_2}} ({{inbound|outbound}})
{{METHOD_or_TOPIC}} {{path_or_channel}} — {{endpoint_description}}
Data shape:
- `{{field_1}}` ({{type}}): {{field_description}}
## Data Mapping
Inbound (external -> CEX): {{inbound_mapping_rules}}
Outbound (CEX -> external): {{outbound_mapping_rules}}
Idempotency: {{dedup_strategy}}
## Health & Errors
Health: {{health_check_details}}
- {{error_code}}: {{description}} — {{retry_behavior}}
- {{error_code}}: {{description}} — {{retry_behavior}}
Circuit breaker: {{circuit_breaker_strategy}}
## References
- {{reference_1}}
- {{reference_2}}
