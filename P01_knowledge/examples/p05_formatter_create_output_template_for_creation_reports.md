---
id: p05_fmt_creation_report_table
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 6
domain: "creation_reporting"
quality: 8.8
tags: [formatter, markdown, creation-report, P05, table, artifacts]
tldr: "Formats creation report data into Markdown table with artifact name, kind, quality, timestamp, author, and status columns"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [creation-report, artifact-table, markdown-formatter, build-summary]
density_score: 0.89
---
# Creation Report Table Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| artifact_col | artifact_name | stringify | `{value}` | max_length: 45, truncate: ellipsis |
| kind_col | artifact_kind | stringify | `{value}` | uppercase: true, max_length: 20 |
| quality_col | quality_score | number_format | `{value:.1f}/10` | locale: pt-BR, null_value: "N/A" |
| time_col | created_timestamp | date_format | `{value:%d/%m %H:%M}` | locale: pt-BR, timezone: America/Sao_Paulo |
| author_col | author_name | stringify | `{value}` | max_length: 25, truncate: ellipsis |
| status_col | build_status | stringify | `{value}` | uppercase: true, color_map: {"SUCCESS": "✅", "FAILED": "❌", "PENDING": "⏳"} |

## Input Specification
Type: structured_data
Structure: list of creation report objects containing artifact metadata from CEX build pipeline.
Example:
```json
[{
  "artifact_name": "p02_agent_content_creator",
  "artifact_kind": "agent", 
  "quality_score": 8.7,
  "created_timestamp": "2026-04-01T20:05:21",
  "author_name": "builder-agent",
  "build_status": "SUCCESS"
}]
```

## Output Specification
Format: markdown
Example:
```markdown
| Artefato | Tipo | Qualidade | Criado | Autor | Status |
|----------|------|-----------|--------|-------|--------|
| p02_agent_content_creator | AGENT | 8.7/10 | 01/04 20:05 | builder-agent | ✅ SUCCESS |
| p05_fmt_product_table | FORMATTER | 9.2/10 | 01/04 19:45 | formatter-builder | ✅ SUCCESS |
```

## Template
Engine: string_format
```text
| Artefato | Tipo | Qualidade | Criado | Autor | Status |
|----------|------|-----------|--------|-------|--------|
{rows}
```

## Edge Cases
- Null quality_score: render as "N/A" in quality column
- Empty author_name: render as "sistema" placeholder  
- Invalid timestamp: render as "--/-- --:--"
- Special characters in artifact names: pipe `|` escaped as `\|` for Markdown tables
- Overflow: truncate artifact names and authors at specified max_length with ellipsis
- Unknown status: render as "UNKNOWN" with ❓ icon

## References
- CEX artifact metadata schema: .cex/kinds_meta.json
- Markdown table specification: CommonMark 0.30
- Portuguese locale formatting: ABNT NBR ISO 8601