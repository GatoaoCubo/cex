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
