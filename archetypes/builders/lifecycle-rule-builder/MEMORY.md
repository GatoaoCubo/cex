```yaml
---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---
```

# Memory: lifecycle-rule-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Using string for freshness_days ("about 3 months" instead of 90)
3. Using hyphens in id slug (must be underscores: p11_lc_kc_freshness)
4. Invalid review_cycle enum ("regularly", "as needed" instead of weekly/monthly/quarterly/yearly)
5. Subjective transition triggers ("when it feels outdated" instead of "90 days since updated")
6. Confusing lifecycle_rule with runtime_rule (artifact state vs system behavior)
7. Missing ownership field (unowned rules are never enforced)

## Proven Lifecycle Patterns
| Domain | freshness_days | review_cycle | States count |
|--------|---------------|-------------|-------------|
| knowledge_card | 90 | quarterly | 7 |
| model_card | 60 | monthly | 5 |
| (more patterns accumulated after production) | | | |

## Production Counter
| Metric | Value |
|--------|-------|
| Rules produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | freshness_days calibration; state machine completeness |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a lifecycle_rule, update:
- New common mistake (if encountered)
- New proven lifecycle pattern (if discovered)
- Production counter increment
