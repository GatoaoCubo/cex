---
# TEMPLATE: Signal (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.signal)
# Max 4096 bytes

id: p12_sig_{{EVENT_SLUG}}
type: signal
lp: P12
title: "Signal: {{EVENT_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Signal: {{EVENT_NAME}}

## Payload
```json
{
  "satellite": "{{SATELLITE_NAME}}",
  "status": "{{complete|error|progress}}",
  "quality_score": {{QUALITY_SCORE}},
  "timestamp": "{{ISO_TIMESTAMP}}"
}
```

## Emission Rules
- Emit when: {{EVENT_TRIGGER}}
- Consumer: {{EXPECTED_CONSUMER}}
- Retry: {{RETRY_RULE}}
