---
# TEMPLATE: Bugloop (Detect-Fix-Verify Cycle)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P11_feedback/_schema.yaml (types.bugloop)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p11_bl_{{SCOPE_SLUG}}
type: bugloop
lp: P11
title: "Bugloop: {{SCOPE_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, bugloop, feedback]
tldr: "{{ONE_SENTENCE_WHAT_THIS_LOOP_FIXES}}"
density_score: {{0.80_TO_1.00}}
---

# Bugloop: {{SCOPE_NAME}}

## Trigger

| Property | Value |
|----------|-------|
| Detect | {{HOW_BUG_IS_DETECTED}} |
| Condition | {{WHEN_TO_ACTIVATE}} |
| Frequency | {{HOW_OFTEN_CHECKED}} |

## Cycle

```
[DETECT] --> [ANALYZE] --> [FIX] --> [VERIFY] --> [COMMIT]
                |                       |
           [root cause]          [RETRY if fail]
                                   (max {{MAX_RETRIES}})
```

### Phase 1: Detect
- Signal: {{WHAT_TRIGGERS_DETECTION}}
- Data: {{WHAT_DATA_TO_COLLECT}}

### Phase 2: Analyze
- Root cause method: {{APPROACH_TO_FIND_CAUSE}}
- Context needed: {{FILES_LOGS_METRICS}}

### Phase 3: Fix
- Strategy: {{PRIMARY_FIX_APPROACH}}
- Fallback: {{ALTERNATIVE_IF_PRIMARY_FAILS}}
- Scope: {{FILES_OR_SYSTEMS_TOUCHED}}

### Phase 4: Verify
- Command: `{{VERIFICATION_COMMAND}}`
- Expected: {{WHAT_SUCCESS_LOOKS_LIKE}}
- Timeout: {{MAX_SECONDS}}

### Phase 5: Commit
- Message: `{{COMMIT_TEMPLATE}}`
- Files: {{PATHS_TO_STAGE}}

## Limits

| Limit | Value | On Exceed |
|-------|-------|-----------|
| Max retries | {{MAX_RETRIES}} | {{ESCALATION_ACTION}} |
| Max duration | {{MINUTES}} min | {{TIMEOUT_ACTION}} |
| Max files touched | {{N}} | {{SCOPE_GUARD}} |

## Escalation

- After {{MAX_RETRIES}} failures: {{WHAT_HAPPENS}}
- Owner: {{WHO_GETS_NOTIFIED}}
