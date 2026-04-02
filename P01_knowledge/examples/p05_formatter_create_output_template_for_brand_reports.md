---
id: p05_fmt_brand_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 7
domain: "brand_reporting"
quality: 9.1
tags: [formatter, markdown, brand, P05, report, metrics]
tldr: "Formats brand performance and identity data into structured Markdown reports with header, metrics table, values list, color palette, and KPI summaries"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [brand-report, brand-metrics, markdown-formatter, brand-identity, performance-report]
density_score: 0.87
---
## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| header_block | brand_name | template | `# {value} — Brand Report` | title_case: true, null: "Unnamed Brand" |
| report_meta | report_date, period | template | `**Date:** {report_date}  ·  **Period:** {period}` | date_fmt: DD/MM/YYYY, null: omit_field |
| metrics_table | brand_metrics | tabulate | `\| Metric \| Value \| Target \| Delta \|` | col_width: auto, null: `-` |
| values_list | brand_values | stringify | `- **{name}**: {description}` | max_length: 120, truncate: ellipsis, null: omit |
| color_swatch | brand_colors | template | `**{name}**: \`{hex_code}\`` | uppercase_hex: true, null: omit |
| perf_kpi | performance_data | number_format | `**{metric}**: {value:+.1%} vs target` | locale: pt-BR, null: `—` |
| recommendations | action_items | stringify | `{index}. {action}` | enumerate: 1-based, max_length: 200, null: omit |

## Input Specification

Type: structured_data
Structure: dict with brand_name (str), report_date (ISO date), period (str), brand_metrics (list[{metric, value, target, delta}]), brand_values (list[{name, description}]), brand_colors (list[{name, hex_code}]), performance_data (list[{metric, value}]), action_items (list[str]).

Example:
```json
{
  "brand_name": "Nexus Studio",
  "report_date": "2026-04-02",
  "period": "Q1 2026",
  "brand_metrics": [{"metric": "Awareness", "value": 0.42, "target": 0.50, "delta": -0.08}],
  "brand_values": [{"name": "Clarity", "description": "Direct communication, no jargon"}],
  "brand_colors": [{"name": "Primary Blue", "hex_code": "#1A73E8"}],
  "performance_data": [{"metric": "Conversion", "value": 0.034}],
  "action_items": ["Increase social posting frequency to 5x/week"]
}
```

## Output Specification

Format: markdown
Example:
```markdown
# Nexus Studio — Brand Report

**Date:** 02/04/2026  ·  **Period:** Q1 2026

## Metrics

| Metric | Value | Target | Delta |
|--------|-------|--------|-------|
| Awareness | 42% | 50% | -8pp |

## Brand Values

- **Clarity**: Direct communication, no jargon

## Color Palette

**Primary Blue**: `#1A73E8`

## Performance

**Conversion**: +3,4% vs target

## Recommendations

1. Increase social posting frequency to 5x/week
```

## Template

Engine: string_format
```text
{header_block}

{report_meta}

## Metrics

{metrics_table}

## Brand Values

{values_list}

## Color Palette

{color_swatch}

## Performance

{perf_kpi}

## Recommendations

{recommendations}
```

## Edge Cases

- Null values: omit optional fields (report_meta, color_swatch, values_list, recommendations); render `—` for numeric KPIs; render `-` in table cells
- Empty strings: treat as null — same omit/placeholder strategy applies per rule
- Special characters: pipe `|` escaped as `\|` in Markdown table cells; backtick in hex codes is safe (no escaping needed)
- Overflow: stringify rules truncate at max_length with ellipsis; table columns auto-width; template rules render as-is (no wrapping)

## Locale

Locale: pt-BR
- Numbers: decimal `,` separator, thousands `.` (e.g., `1.234,56`)
- Dates: DD/MM/YYYY (e.g., `02/04/2026`)
- Percentages: `%` suffix, 1 decimal, comma separator (e.g., `42,3%`)
- Currency: not in base template; extend perf_kpi with `R$ {value:,.2f}` when monetary metrics present

## Boundary

- NOT a parser: does not extract brand data from raw text — input must be pre-structured by parser or agent
- NOT a response_format: does not constrain LLM decoder output schema — applies post-generation transformation only

## References

- CommonMark Markdown table specification: commonmark.org/spec
- Python string format mini-language: docs.python.org/3/library/string.html#format-specification-mini-language
- ISO 8601 date format standard: iso.org/iso-8601-date-and-time-format.html