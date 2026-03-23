---
# TEMPLATE: Connector (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.connector)
# Max 1024 bytes

id: p04_conn_{{SERVICE_SLUG}}
type: connector
lp: P04
title: "Connector: {{SERVICE_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Connector: {{SERVICE_NAME}}

## Service Contract
- Service: {{SERVICE_NAME}}
- Mode: {{push|pull|bidirectional}}
- Auth: {{AUTH_MODE}}

## Data Mapping
| External Field | Internal Field | Rule |
|----------------|----------------|------|
| {{EXT_FIELD_1}} | {{INT_FIELD_1}} | {{MAPPING_RULE_1}} |
| {{EXT_FIELD_2}} | {{INT_FIELD_2}} | {{MAPPING_RULE_2}} |

## Failure Handling
- Retry: {{RETRY_POLICY}}
- Fallback: {{FALLBACK_BEHAVIOR}}
