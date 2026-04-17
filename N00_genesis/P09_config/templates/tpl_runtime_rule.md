---
# TEMPLATE: Runtime Rule (P09 Config)
# Valide contra P09_config/_schema.yaml (types.runtime_rule)
# Max 3072 bytes

id: p09_rr_{{RULE_SLUG}}
kind: runtime_rule
pillar: P09
title: "Runtime Rule: {{RULE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Runtime Rule: {{RULE_NAME}}

## Parameters
| Parameter | Value | Reason |
|-----------|-------|--------|
| timeout | {{SECONDS}} | {{WHY_TIMEOUT}} |
| retries | {{RETRY_COUNT}} | {{WHY_RETRIES}} |
| concurrency | {{CONCURRENCY}} | {{WHY_CONCURRENCY}} |

## Enforcement
1. {{WHEN_RULE_APPLIES}}
2. {{WHAT_IS_LIMITED}}
3. {{WHAT_HAPPENS_ON_EXCEED}}
