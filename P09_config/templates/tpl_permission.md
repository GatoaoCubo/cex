---
# TEMPLATE: Permission Rule (P09 Config)
# Valide contra P09_config/_schema.yaml (types.permission)
# Max 3072 bytes

id: p09_perm_{{SCOPE_SLUG}}
type: permission
lp: P09
title: "Permission: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Permission: {{SCOPE_NAME}}

## Access Matrix
| Actor | Read | Write | Execute |
|------|------|-------|---------|
| {{ACTOR_1}} | yes | no | no |
| {{ACTOR_2}} | yes | yes | no |
| {{ACTOR_3}} | yes | yes | yes |

## Boundaries
- Forbidden path: {{FORBIDDEN_SCOPE}}
- Escalation path: {{HOW_TO_REQUEST_ACCESS}}
