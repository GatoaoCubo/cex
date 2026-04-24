---
# TEMPLATE: API Client (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.client)
# Max 1024 bytes

id: p04_client_{{API_SLUG}}
kind: api_client
8f: F5_call
pillar: P04
title: "Client: {{API_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Client: {{API_NAME}}

## Connection
- Base URL: {{BASE_URL}}
- Auth: {{api_key|oauth|none}}
- Timeout: {{TIMEOUT_SECONDS}}s

## Operations
| Method | Endpoint | Purpose |
|--------|----------|---------|
| {{GET|POST}} | {{/path}} | {{WHAT_IT_DOES}} |
| {{GET|POST}} | {{/path}} | {{WHAT_IT_DOES}} |

## Contract
```yaml
request:
  {{FIELD_1}}: {{TYPE}}
response:
  {{FIELD_2}}: {{TYPE}}
```
