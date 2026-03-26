---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: parser-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p05_parser_my_parser not p05_parser_my-parser)
3. extraction_count not matching actual rules in Extraction Rules table (H07 catches this)
4. No required extraction rules (at least 1 must be required: true)
5. Using regex for JSON input (use json_path instead — regex is fragile on JSON)
6. Using regex for HTML input (use css_selector instead — regex cannot parse HTML reliably)
7. Omitting error_strategy — every parser WILL encounter malformed input
8. Confusing parser (P05, extracts data) with formatter (P05, presents data)
9. Including validation logic ("check if price > 0") — that belongs in validator (P06)
10. Missing Input Specification with sample data — extraction rules need context

### Effective Extraction Patterns
| Input Type | Best Method | Pattern Example |
|------------|-------------|-----------------|
| JSON field | json_path | `$.data.items[*].title` |
| HTML element | css_selector | `div.product h1::text` |
| Log timestamp | regex | `(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})` |
| CSV column | split | `split(",")[2]` |
| Free text entity | llm_extract | `extract product name from description` |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | method selection, extraction_count mismatch, boundary drift to formatter |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a parser artifact, update:
- New common mistake (if encountered)
- New extraction pattern (if discovered)
- Production counter increment
