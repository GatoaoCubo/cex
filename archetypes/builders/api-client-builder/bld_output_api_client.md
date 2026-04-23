---
kind: output_template
id: bld_output_template_client
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a client artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Api Client"
version: "1.0.0"
author: n03_builder
tags: [api_client, builder, examples]
tldr: "Golden and anti-examples for api client construction, demonstrating ideal structure and common pitfalls."
domain: "api client construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_mcp_server
  - bld_output_template_function_def
  - bld_schema_client
  - bld_output_template_connector
  - bld_instruction_client
  - bld_examples_client
  - api-client-builder
  - p03_sp_client_builder
  - p11_qg_client
  - bld_knowledge_card_client
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
pagetion: {{cursor|offset|none}}

error_codes: [{{code_1}}, {{code_2}}]
caching: "{{cache_strategy}}"
```
## Overview
`{{what_api_client_consumes_1_to_2_sentences}}`
`{{who_consumes_it_and_primary_use_case}}`
## Endpoints
### `{{endpoint_name_1}}`
`{{METHOD}}` {{path}} — `{{endpoint_description}}`
Parameters:
1. `{{param_1}}` ({{type}}, {{required|optional}}): `{{param_description}}`
2. `{{param_2}}` ({{type}}, {{required|optional}}): `{{param_description}}`
Returns: `{{return_description}}`
### `{{endpoint_name_2}}`
`{{METHOD}}` {{path}} — `{{endpoint_description}}`
Parameters:
- `{{param_1}}` ({{type}}, {{required|optional}}): `{{param_description}}`

Returns: `{{return_description}}`
## Auth & Config
Base URL: `{{base_url}}`
Auth: `{{auth_method_and_header_format}}`
Headers: `{{required_headers}}`
## Error Handling
1. `{{error_code}}`: {{description}} — `{{retry_behavior}}`
2. `{{error_code}}`: {{description}} — `{{retry_behavior}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | api client construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_mcp_server]] | sibling | 0.43 |
| [[bld_output_template_function_def]] | sibling | 0.36 |
| [[bld_schema_client]] | downstream | 0.36 |
| [[bld_output_template_connector]] | sibling | 0.35 |
| [[bld_instruction_client]] | upstream | 0.34 |
| [[bld_examples_client]] | downstream | 0.33 |
| [[api-client-builder]] | upstream | 0.33 |
| [[p03_sp_client_builder]] | upstream | 0.28 |
| [[p11_qg_client]] | downstream | 0.27 |
| [[bld_knowledge_card_client]] | upstream | 0.27 |
