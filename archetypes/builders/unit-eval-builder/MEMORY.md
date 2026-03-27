---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: unit-eval-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Missing assertions list entirely (H09 rejects empty)
3. Vague expected_output like "good output" (S04 rejects vagueness)
4. Missing gate_ref in assertions (S03 requires gate mapping)
5. Mixing unit scope with pipeline scope (unit = isolated, pipeline = e2e_eval)
6. Missing timeout field (H10 requires positive integer)
7. Using hyphens in id slug (must be underscores: p07_ue_kc_parse)

## Assertion Patterns
| Pattern | When | Example |
|---------|------|---------|
| Exact match | Field must equal value | kind == "knowledge_card" |
| Prefix match | ID pattern check | id starts with "p01_kc_" |
| Type check | Field must be type | quality == null |
| Range check | Numeric bounds | density >= 0.80 |
| List check | Collection constraints | tags.length >= 3 |

## Production Counter
| Metric | Value |
|--------|-------|
| Tests produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | mapping assertions to correct gate_refs |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a unit_eval, update:
- New common mistake (if encountered)
- New assertion pattern (if discovered)
- Production counter increment
