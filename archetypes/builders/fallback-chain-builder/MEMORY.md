---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: fallback-chain-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p02_fc_my_chain not p02_fc_my-chain)
3. steps_count not matching actual rows in Chain table (H07 catches this)
4. Steps not ordered by decreasing capability (step 1 must be most capable)
5. Single-step chain (minimum 2 steps — single step is just a model_card reference)
6. Omitting timeout_per_step_ms or setting to 0 (defeats purpose of fallback)
7. Including prompt content in chain steps — that belongs in chain (P03)
8. Confusing fallback_chain (model degradation) with chain (prompt sequencing)
9. Missing Circuit Breaker section — every chain needs a halt condition
10. Cost analysis omitted — degradation trades quality for cost, must be documented

### Pricing Reference (update as prices change)
| Model | Provider | Cost/1M input | Cost/1M output |
|-------|----------|--------------|----------------|
| claude-opus-4-6 | anthropic | $15.00 | $75.00 |
| claude-sonnet-4-6 | anthropic | $3.00 | $15.00 |
| claude-haiku-4-5 | anthropic | $0.25 | $1.25 |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | step ordering, timeout omission, boundary drift to P03 chain |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a fallback_chain artifact, update:
- New common mistake (if encountered)
- New pricing data (if models changed)
- Production counter increment
