---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: permission-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Invalid access enum ("yes", "no" instead of allow/deny/conditional)
3. Roles as string instead of list (H09 requires list type)
4. Missing execute field (all three access levels required)
5. Missing deny_list (deny overrides allow is fundamental)
6. Confusing permission with guardrail (access vs safety)
7. Using hyphens in id slug (must be underscores: p09_perm_pool_access)

## Proven Permission Patterns
| Domain | Roles count | Access model | Audit level |
|--------|------------|-------------|-------------|
| knowledge pool | 5 | RBAC with inheritance | high (golden card writes) |
| agent filesystem | 3 | deny-by-default | medium (write operations) |
| config files | 4 | conditional by environment | high (all modifications) |
| API endpoints | 3 | RBAC with escalation | high (all access events) |

## Production Counter
| Metric | Value |
|--------|-------|
| Permissions produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | role granularity; deny_list completeness |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a permission, update:
- New common mistake (if encountered)
- New proven permission pattern (if discovered)
- Production counter increment
