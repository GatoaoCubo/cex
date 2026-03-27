---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: runtime-state-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Confusing runtime_state with mental_model (runtime is mutable, design-time is not)
3. Confusing runtime_state with session_state (runtime accumulates, session is snapshot)
4. Missing persistence field (must be session or cross_session)
5. Vague routing rules without conditions or confidence thresholds
6. Decision tree without clear branch logic (just prose)
7. Using hyphens in id slug (must be underscores: p10_rs_researcher)

## Proven Runtime State Patterns
| Agent domain | Routing mode | Persistence | Priority count |
|-------------|-------------|-------------|----------------|
| research | hybrid | cross_session | 4 |
| build | rule_based | session | 3 |
| marketing | keyword | session | 3 |
| orchestration | rule_based | cross_session | 5 |

## Production Counter
| Metric | Value |
|--------|-------|
| Runtime states produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | routing rule specificity; state transition triggers |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a runtime_state, update:
- New common mistake (if encountered)
- New proven runtime state pattern (if discovered)
- Production counter increment
