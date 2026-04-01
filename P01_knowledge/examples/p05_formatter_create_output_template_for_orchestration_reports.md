---
id: p05_fmt_orchestration_reports
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 6
domain: "orchestration"
quality: 8.9
tags: [formatter, orchestration, markdown, reports, P05, status]
tldr: "Formats CEX orchestration reports into structured Markdown with mission status, nucleus assignments, quality scores, and completion summaries"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [orchestration-reports, mission-status, nucleus-tracking, quality-dashboard]
density_score: 0.89
---
# Orchestration Reports Formatter

## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| mission_header | mission_name | template | `# 🎯 Mission: {value}\n## Status: {status}` | status_icons: true |
| task_status | task_items | tabulate | `| {task_name} | {nucleus} | {status} | {quality} |` | status_symbols: ✅❌⏳ |
| nucleus_assignment | nucleus_assignments | stringify | `**{nucleus}**: {task_count} tasks` | format: bold |
| quality_score | quality_scores | number_format | `{value}/10.0` | precision: 1, color_coding: true |
| timestamp_format | timestamps | date_format | `{value:%Y-%m-%d %H:%M}` | timezone: UTC, locale: pt-BR |
| completion_summary | completion_data | template | `## Summary\n{completed}/{total} tasks ✅ ({percentage}%)` | percentage_calc: true |

## Input Specification

Type: structured_data
Structure: CEX orchestration report object with mission metadata, task assignments, nucleus status, quality metrics, and timestamps.

Example:
```json
{
  "mission_name": "BRAND_LAUNCH",
  "status": "in_progress", 
  "task_items": [
    {"task_name": "Create brand guidelines", "nucleus": "N02", "status": "complete", "quality": 9.2},
    {"task_name": "Build landing page", "nucleus": "N03", "status": "in_progress", "quality": null}
  ],
  "nucleus_assignments": {"N02": 3, "N03": 2, "N06": 1},
  "quality_scores": [9.2, 8.7, 9.1],
  "timestamps": {"started": "2026-04-01T14:30:00Z", "last_update": "2026-04-01T18:45:00Z"},
  "completion_data": {"completed": 4, "total": 6, "percentage": 67}
}
```

## Output Specification

Format: markdown
Example:
```markdown
# 🎯 Mission: BRAND_LAUNCH
## Status: in_progress

## Task Progress
| Task | Nucleus | Status | Quality |
|------|---------|--------|---------|
| Create brand guidelines | N02 | ✅ complete | 9.2/10.0 |
| Build landing page | N03 | ⏳ in_progress | - |

## Nucleus Workload
**N02**: 3 tasks | **N03**: 2 tasks | **N06**: 1 task

## Quality Metrics
Average: 8.9/10.0 | Range: 8.7-9.2

## Summary
4/6 tasks ✅ (67%)

*Last updated: 2026-04-01 18:45*
```

## Template

Engine: string_format
```text
# 🎯 Mission: {mission_name}
## Status: {mission_status}

## Task Progress
| Task | Nucleus | Status | Quality |
|------|---------|--------|---------|
{task_rows}

## Nucleus Workload
{nucleus_summary}

## Quality Metrics
{quality_summary}

## Summary
{completion_summary}

*Last updated: {last_update}*
```

## Edge Cases

- Null quality scores: render as `-` in quality column
- Empty task lists: display "No tasks assigned" message
- Missing nucleus assignments: show "Unassigned" in nucleus column
- Timestamp overflow: truncate to date only if space constrained
- Special characters in task names: escape pipe `|` as `\|` for Markdown table compatibility
- Quality scores > 10.0: clamp to 10.0 and add `*` indicator

## References

- CEX Mission Schema: `.cex/runtime/missions/`
- Nucleus Status API: `bash _spawn/dispatch.sh status`
- Markdown Table Spec: CommonMark 0.30
- Quality Gate Documentation: `P11_quality/examples/`