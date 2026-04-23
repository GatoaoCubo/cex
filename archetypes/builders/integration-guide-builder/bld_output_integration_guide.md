---
kind: output_template
id: bld_output_template_integration_guide
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for integration_guide production
quality: 8.9
title: "Output Template Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, output_template]
tldr: "Template with vars for integration_guide production"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_api_reference
  - kc_api_reference
  - n06_api_access_pricing
  - bld_schema_api_reference
  - bld_examples_api_reference
  - bld_output_template_playground_config
  - bld_tools_model_provider
  - bld_schema_integration_guide
  - bld_output_template_sdk_example
  - bld_instruction_api_reference
---

```markdown
```yaml
id: p05_ig_{{name}}.md <!-- Use kebab-case, e.g., p05_ig_user_auth -->
name: {{integration_name}} <!-- Human-readable integration name -->
pillar: P05 <!-- Must be P05 -->
quality: null <!-- Always null -->
description: {{brief_description}} <!-- 1-2 sentence overview -->
version: {{version}} <!-- e.g., 1.0.0 -->
author: {{author}} <!-- Maintainer name -->
date: {{date}} <!-- YYYY-MM-DD -->
```

## Prerequisites
- Install {{dependency}} <!-- e.g., "Python 3.8+" -->
- API key from {{platform}} <!-- e.g., "CEX.io dashboard" -->

## API Endpoints
| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/v1/{{endpoint}}` <!-- e.g., "/v1/trade" --> | {{endpoint_description}} <!-- e.g., "Place orders" --> |

## Example Request
```bash
curl -X POST https://api.{{platform}}.com/v1/{{endpoint}} <!-- e.g., "https://api.cex.io/v1/trade" -->
  -H "Authorization: Bearer {{api_key}}" <!-- Replace with actual key -->
  -d '{"symbol": "BTC/USD", "amount": 0.5}' <!-- Sample payload -->
```

## Authentication
- Use HMAC-SHA256 with {{secret}} <!-- e.g., "API secret from dashboard" -->
- Timestamp required in ISO 8601 format <!-- e.g., "2023-10-05T14:48:00Z" -->
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_api_reference]] | sibling | 0.27 |
| [[kc_api_reference]] | upstream | 0.26 |
| [[n06_api_access_pricing]] | downstream | 0.24 |
| [[bld_schema_api_reference]] | downstream | 0.24 |
| [[bld_examples_api_reference]] | downstream | 0.22 |
| [[bld_output_template_playground_config]] | sibling | 0.21 |
| [[bld_tools_model_provider]] | upstream | 0.21 |
| [[bld_schema_integration_guide]] | downstream | 0.21 |
| [[bld_output_template_sdk_example]] | sibling | 0.20 |
| [[bld_instruction_api_reference]] | upstream | 0.20 |
