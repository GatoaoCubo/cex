---
# TEMPLATE: Guardrail (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.guardrail)
# Max 4096 bytes

id: p11_gr_{{SCOPE_SLUG}}
kind: guardrail
pillar: P11
title: "Guardrail: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Guardrail: {{SCOPE_NAME}}

## Boundary
- Protects: {{ASSET_OR_USER}}
- Blocks: {{DANGEROUS_ACTION}}
- Severity: {{low|medium|high|critical}}

## Check
1. {{SIGNAL_TO_INSPECT}}
2. {{CONDITION_TO_BLOCK}}
3. {{WHAT_TO_LOG_OR_SIGNAL}}

## Recovery
- Safe alternative: {{ALTERNATIVE_PATH}}
- Escalation owner: {{OWNER}}
