---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: response-format-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Confusing with validation_schema P06 (response_format is LLM-SIDE, not SYSTEM-SIDE)
3. sections_count = 0 (minimum 1 section)
4. Missing example_output (most effective instruction is showing expected output)
5. format_type = "text" (not in enum; use "plaintext" instead)
6. injection_point missing (must specify where to inject)
7. Including validation logic in body (system enforcement is validation_schema P06)
8. Using hyphens in id slug (must be underscores: p05_rf_knowledge_card)

## Format Compliance Patterns
| Format Type | LLM Compliance | Best For | Sections |
|-------------|---------------|----------|----------|
| json | ~95% | Machine consumption, APIs | 3-5 |
| yaml | ~90% | Config, frontmatter + body | 5-8 |
| markdown | ~85% | Human-readable docs | 5-10 |
| csv | ~80% | Tabular data | 1-2 |
| plaintext | ~70% | Free-form, minimal structure | 1-3 |

## Production Counter
| Metric | Value |
|--------|-------|
| Formats produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | P05/P06 boundary confusion; section ordering |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a response_format, update:
- New common mistake (if encountered)
- New compliance pattern (if discovered)
- Production counter increment
