---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: e2e-eval-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Empty stages list (H08 requires non-empty)
3. Disconnected stages (output_n must feed input_n+1)
4. Missing environment specification (H11 requires non-empty)
5. Testing single agent instead of pipeline (that is unit_eval)
6. Missing cleanup (leads to state pollution between runs)
7. Using hyphens in id slug (must be underscores: p07_e2e_research_kc)

## Pipeline Complexity Guide
| Stages | Timeout | Typical Use |
|--------|---------|-------------|
| 2-3 | 120-180s | Simple pipeline |
| 4-6 | 300s | Standard pipeline |
| 7+ | 600s | Complex orchestration |

## Production Counter
| Metric | Value |
|--------|-------|
| Tests produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | mapping stage connections; sizing timeout |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an e2e_eval, update:
- New common mistake (if encountered)
- New pipeline pattern (if discovered)
- Production counter increment
