---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: guardrail-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Invalid severity enum ("important", "danger" instead of critical/high/medium/low)
3. Invalid enforcement enum ("stop", "prevent" instead of block/warn/log)
4. Subjective rules ("be careful") instead of concrete restrictions
5. Missing bypass policy (even critical guardrails need emergency override)
6. Confusing guardrail with permission (access vs safety)
7. Using hyphens in id slug (must be underscores: p11_gr_dest_cmds)

## Proven Guardrail Patterns
| Domain | Severity | Rules count | Enforcement |
|--------|----------|------------|-------------|
| filesystem safety | critical | 7 | block (pre-exec hook) |
| data exposure | high | 5 | block (output filter) |
| rate limiting | medium | 3 | warn (monitoring) |
| logging compliance | low | 4 | log (audit) |

## Production Counter
| Metric | Value |
|--------|-------|
| Guardrails produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | concrete rule wording; severity classification |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a guardrail, update:
- New common mistake (if encountered)
- New proven guardrail pattern (if discovered)
- Production counter increment
