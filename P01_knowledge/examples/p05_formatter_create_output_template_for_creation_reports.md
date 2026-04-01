---
id: p05_fmt_creation_report
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
quality: 8.9
tags: [formatter, creation, report, markdown, P05, activity]
title: "Creation Report Formatter"
tldr: "Formats creation activity data into structured Markdown reports with quality scores, artifact status, and execution metrics"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [creation-report, activity-summary, quality-dashboard, artifact-status]
density_score: 0.89
---
# Creation Report Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| activity_header | activity_name | stringify | `# {value}` | uppercase: false |
| quality_badge | quality_score | number_format | `**Quality: {value:.1f}/10.0**` | color_threshold: 8.0 |
| status_indicator | status | stringify | `**Status:** {value}` | uppercase: true, color_map: true |
| artifact_list | artifacts | tabulate | `- [{name}]({path}) — {description}` | bullet_style: dash |
| timestamp_format | created_at | date_format | `*Created: {value:%Y-%m-%d %H:%M}*` | locale: pt-BR, timezone: UTC |
| metrics_table | execution_metrics | tabulate | `| {metric} | {value} | {unit} |` | headers: true, align: right |

## Input Specification
Type: structured_data
Structure: creation activity object with name, quality score, status, artifacts list, timestamps, and execution metrics.
Example:
```json
{
  "activity_name": "Build Knowledge Card for React Patterns",
  "quality_score": 8.7,
  "status": "complete",
  "artifacts": [
    {"name": "kc_react_patterns", "path": "P01_knowledge/kc_react_patterns.md", "description": "React component patterns and best practices"}
  ],
  "created_at": "2026-04-01T20:05:38Z",
  "execution_metrics": [
    {"metric": "Duration", "value": 12.3, "unit": "minutes"},
    {"metric": "Token Count", "value": 4567, "unit": "tokens"}
  ]
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Build Knowledge Card for React Patterns

**Quality: 8.7/10.0** | **Status: COMPLETE**

## Artifacts
- [kc_react_patterns](P01_knowledge/kc_react_patterns.md) — React component patterns and best practices

## Execution Metrics
| Metric | Value | Unit |
|--------|--------|------|
| Duration | 12.3 | minutes |
| Token Count | 4567 | tokens |

*Created: 2026-04-01 20:05*
```

## Template
Engine: string_format
```text
# {activity_name}

{quality_badge} | {status_indicator}

## Artifacts
{artifact_list}

## Execution Metrics
{metrics_table}

{timestamp_format}
```

## Edge Cases
- Null quality_score: render as `**Quality: N/A**`
- Empty artifacts array: render as `*No artifacts generated*`
- Missing execution_metrics: omit entire Execution Metrics section
- Special characters in artifact names: escape brackets `[]` as `\[\]` in Markdown links
- Long activity names: truncate at 80 characters with ellipsis

## References
- Markdown specification: CommonMark 0.30
- ISO 8601 date formatting for timestamps
- CEX quality scoring system (0-10 scale)