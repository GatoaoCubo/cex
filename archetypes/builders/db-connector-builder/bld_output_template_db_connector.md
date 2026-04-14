---
kind: output_template
id: bld_output_template_connector
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a connector artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Db Connector"
version: "1.0.0"
author: n03_builder
tags: [db_connector, builder, examples]
tldr: "Golden and anti-examples for db connector construction, demonstrating ideal structure and common pitfalls."
domain: "db connector construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: connector

This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.
```yaml
id: p04_conn_{{service_slug}}
kind: db_connector
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
`{{what_service_and_integration_pattern_1_to_2_sentences}}`
`{{who_uses_it_and_primary_data_flow}}`
## Endpoints
### `{{endpoint_name_1}}` ({{inbound|outbound}})
`{{METHOD_or_TOPIC}}` {{path_or_channel}} — `{{endpoint_description}}`
Data shape:
1. `{{field_1}}` ({{type}}): `{{field_description}}`
2. `{{field_2}}` ({{type}}): `{{field_description}}`
### `{{endpoint_name_2}}` ({{inbound|outbound}})
`{{METHOD_or_TOPIC}}` {{path_or_channel}} — `{{endpoint_description}}`
Data shape:
- `{{field_1}}` ({{type}}): `{{field_description}}`
## Data Mapping
Inbound (external -> CEX): `{{inbound_mapping_rules}}`
Outbound (CEX -> external): `{{outbound_mapping_rules}}`
Idempotency: `{{dedup_strategy}}`
## Health & Errors
Health: `{{health_check_details}}`
1. `{{error_code}}`: {{description}} — `{{retry_behavior}}`
2. `{{error_code}}`: {{description}} — `{{retry_behavior}}`
Circuit breaker: `{{circuit_breaker_strategy}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | db connector construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
