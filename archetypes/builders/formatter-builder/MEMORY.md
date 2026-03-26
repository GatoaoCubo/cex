---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: formatter-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p05_fmt_my_formatter not p05_fmt_my-formatter)
3. rule_count not matching actual rules in Formatting Rules table (H07 catches this)
4. No formatting rules in body (at least 1 must exist)
5. Wrong escaping for target format (html needs html escaping, json needs json escaping)
6. Missing locale for number formatting (1.000,00 vs 1,000.00 depends on locale)
7. Confusing formatter (P05, presents data) with parser (P05, extracts data)
8. Including extraction logic ("extract price from HTML") — that belongs in parser
9. Including validation logic ("check if price > 0") — that belongs in validator (P06)
10. Missing edge case handling for null values — every formatter encounters nulls

### Effective Formatting Patterns
| Target Format | Best Transform | Pattern Example |
|---------------|---------------|-----------------|
| markdown table | tabulate | `| {col1} | {col2} |` |
| json pretty | serialize | `JSON.stringify(data, null, 2)` |
| currency (pt-BR) | number_format | `R$ {value:,.2f}` with swap_decimal |
| date (pt-BR) | date_format | `{value:%d/%m/%Y}` |
| truncated text | truncate | `{value[:40]}...` |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | escaping selection, locale handling, template vs direct formatting |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a formatter artifact, update:
- New common mistake (if encountered)
- New formatting pattern (if discovered)
- Production counter increment
