---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: feature-flag-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p09_ff_enable_dark_mode not p09_ff_enable-dark-mode)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. default_state: "maybe" or "partial" (must be "on" or "off" only)
4. rollout_percentage as string "50%" (must be integer 0-100, no % symbol)
5. category: "feature" or "toggle" (must be: release, experiment, ops, permission)
6. Missing kill switch documentation for ops flags
7. No expiration date (stale flags = tech debt — always set expires)
8. Confusing feature_flag with permission (flag is WHETHER feature exists; perm is WHO)
9. Body exceeding 1536 bytes (tightest P09 kind — be extremely concise)
10. Missing ## Lifecycle section (every flag needs create/retire plan)

### Category Patterns
| Category | Default | Typical Lifetime | Kill Switch |
|----------|---------|-----------------|-------------|
| release | off | 2-6 weeks | revert to old code |
| experiment | off | 1-4 weeks | disable experiment |
| ops | on | permanent | emergency disable |
| permission | off | permanent | revoke access |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | body size limit, category confusion, stale flags |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a feature_flag, update:
- New common mistake (if encountered)
- New category pattern (if discovered)
- Production counter increment
