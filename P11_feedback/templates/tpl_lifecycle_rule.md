---
# TEMPLATE: Lifecycle Rule (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.lifecycle_rule)
# Max 4096 bytes

id: p11_lc_{{RULE_SLUG}}
type: lifecycle_rule
lp: P11
title: "Lifecycle Rule: {{RULE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Lifecycle Rule: {{RULE_NAME}}

## Scope
- Artifact: {{ARTIFACT_TYPE}}
- State flow: {{draft -> active -> archived}}
- Trigger: {{FRESHNESS_OR_EVENT}}

## Rules
1. {{PROMOTE_RULE}}
2. {{ARCHIVE_RULE}}
3. {{DELETE_OR_REVIEW_RULE}}

## Evidence
- Metric used: {{METRIC}}
- Owner: {{OWNER}}
