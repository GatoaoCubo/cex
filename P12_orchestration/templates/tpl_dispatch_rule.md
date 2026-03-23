---
# TEMPLATE: Dispatch Rule (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.dispatch_rule)
# Max 3072 bytes

id: p12_dr_{{SCOPE_SLUG}}
type: dispatch_rule
lp: P12
title: "Dispatch Rule: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Dispatch Rule: {{SCOPE_NAME}}

## Routing Table
| Condition | Satellite | Confidence |
|-----------|-----------|------------|
| {{KEYWORD_OR_SIGNAL_1}} | {{SATELLITE_1}} | {{0.0_TO_1.0}} |
| {{KEYWORD_OR_SIGNAL_2}} | {{SATELLITE_2}} | {{0.0_TO_1.0}} |
| {{KEYWORD_OR_SIGNAL_3}} | {{SATELLITE_3}} | {{0.0_TO_1.0}} |

## Fallbacks
- No match: {{DEFAULT_ROUTE}}
- Conflict: {{TIEBREAKER_RULE}}
- Escalation: {{ESCALATION_ROUTE}}
