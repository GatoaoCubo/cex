---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: quality-gate-builder

## Common Mistakes
1. Subjective checks ("looks good") — every gate must be measurable
2. Missing bypass policy — even strict gates need emergency override
3. Weights not summing to 100%
4. Mixing gate (criteria) with validator (code)
5. Self-scoring quality (must be null)

## Proven Gate Patterns
| Domain | HARD count | SOFT dims | Threshold |
|--------|-----------|-----------|-----------|
| knowledge_card | 10 | 5 weighted | 8.0 |
| model_card | 10 | 15 weighted | 8.0 |
| pre-commit | 5 | 5 weighted | 7.0 |

## Production Counter
| Metric | Value |
|--------|-------|
| Gates produced | 0 |
