---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: smoke-eval-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Timeout exceeding 30 seconds (H07 hard limit)
3. Missing fast_fail field or setting to false (H08 requires true)
4. Empty critical_path list (H09 requires non-empty)
5. Deep testing scope (that belongs in unit_eval, not smoke)
6. Missing prerequisites (leads to false negatives)
7. Using hyphens in id slug (must be underscores: p07_se_brain_mcp)

## Smoke vs Unit Decision Guide
| Question | Answer: Smoke | Answer: Unit |
|----------|---------------|-------------|
| How long? | < 30 seconds | 30-300 seconds |
| How deep? | Surface level | Gate-by-gate |
| On failure? | Abort all tests | Report specific gate |
| Frequency? | Every deploy/session | CI pipeline |

## Production Counter
| Metric | Value |
|--------|-------|
| Tests produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | identifying critical path; scoping to 30s |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a smoke_eval, update:
- New common mistake (if encountered)
- New smoke pattern (if discovered)
- Production counter increment
