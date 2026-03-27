---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: validation-schema-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Confusing with response_format P05 (validation_schema is SYSTEM-SIDE, not LLM-SIDE)
3. Using non-JSON types (e.g., "date" instead of "string" with pattern constraint)
4. Missing target_kind (schema must specify what it validates)
5. fields_count = 0 (minimum 1 field to validate)
6. on_failure = "retry" (not valid; must be reject, warn, or auto_fix)
7. Including LLM instructions in schema body (this is NOT a prompt)
8. Using hyphens in id slug (must be underscores: p06_vs_knowledge_card)

## Validation Patterns
| Target Kind | Fields | on_failure | Typical constraints |
|-------------|--------|------------|---------------------|
| knowledge_card | 8-12 | reject | id pattern, quality null, tags list |
| model_card | 10-15 | reject | provider enum, context_window integer |
| signal | 4-6 | warn | status enum, quality_score range |
| benchmark | 8-10 | reject | iterations range, unit non-empty |

## Production Counter
| Metric | Value |
|--------|-------|
| Schemas produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | P05/P06 boundary confusion; JSON type mapping |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a validation_schema, update:
- New common mistake (if encountered)
- New validation pattern (if discovered)
- Production counter increment
