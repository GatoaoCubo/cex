---
id: p05_fmt_creation_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "builder_agent"
target_format: "markdown"
input_type: "structured_data"
rule_count: 7
domain: "creation_reporting"
quality: 8.9
tags: [formatter, markdown, creation, report, P05, dashboard]
tldr: "Formats creation process data into structured Markdown reports with status, timing, quality metrics and artifact details"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [creation-report, markdown-formatter, process-dashboard, build-status]
density_score: 0.89
---
## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| artifact_name | name | stringify | `**{value}**` | max_length: 50, truncate: ellipsis |
| status_badge | status | stringify | `🟢 {value}` if success else `🔴 {value}` | uppercase: true |
| timestamp_col | created_at | date_format | `{value:%Y-%m-%d %H:%M:%S}` | timezone: UTC |
| quality_score | quality | number_format | `{value:.1f}/10.0` | color_code: green if >= 8.0 else red |
| duration_col | duration_ms | stringify | `{value}ms` if < 1000 else `{value/1000:.1f}s` | unit_convert: true |
| pillar_tag | pillar | stringify | `[{value}]` | bracket_style: square |
| error_msg | error | stringify | `❌ {value}` | max_length: 80, truncate: ellipsis |

## Input Specification
Type: structured_data
Structure: creation process records with name, status, timestamps, quality metrics, pillar assignment and error details.
Example:
```json
{
  "name": "p02_agent_task_scheduler",
  "status": "completed",
  "created_at": "2026-04-01T20:05:38Z",
  "quality": 8.7,
  "duration_ms": 2340,
  "pillar": "P02",
  "error": null
}
```

## Output Specification
Format: markdown
Example:
```markdown
## Creation Report

| Artifact | Status | Created | Quality | Duration | Pillar |
|----------|--------|---------|---------|----------|--------|
| **p02_agent_task_scheduler** | 🟢 COMPLETED | 2026-04-01 20:05:38 | 8.7/10.0 | 2.3s | [P02] |

### Summary
- **Total artifacts**: 1
- **Completed**: 1
- **Failed**: 0
- **Average quality**: 8.7/10.0
```

## Template
Engine: string_format
```markdown
## Creation Report

| Artifact | Status | Created | Quality | Duration | Pillar |
|----------|--------|---------|---------|----------|--------|
{rows}

### Summary
- **Total artifacts**: {total_count}
- **Completed**: {completed_count}
- **Failed**: {failed_count}
- **Average quality**: {avg_quality:.1f}/10.0
```

## Edge Cases
- Null values: render as `–` placeholder in table cells
- Empty strings: render as `–` placeholder  
- Special characters: pipe `|` escaped as `\|` in Markdown table cells
- Overflow: truncate artifact names and error messages with ellipsis
- Zero duration: display as `<1ms` for sub-millisecond operations
- Missing quality: render as `N/A` instead of numeric score

## References
- Markdown table specification (CommonMark)
- ISO 8601 timestamp formatting
- UTF-8 emoji rendering guidelines