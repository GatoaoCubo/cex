---
id: p05_fmt_engineering_reports
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "formatter_builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "engineering_reporting"
quality: 8.8
tags: [formatter, engineering, reports, markdown, P05, metrics]
tldr: "Formats engineering project data into structured Markdown reports with status, metrics, issues, and timeline sections"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [engineering-reports, project-status, metrics-display, markdown-formatter]
density_score: 0.89
---
# Engineering Reports Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| status_badge | project_status | template | `## Status: {value}` | uppercase: true, badges: ["🟢 HEALTHY", "🟡 AT_RISK", "🔴 BLOCKED"] |
| metric_display | metrics | number_format | `**{key}:** {value:,}` | group_separator: true, precision: 0 |
| issue_count | issue_summary | template | `- **{severity}:** {count} issues` | sort_by: severity, colors: {"critical": "🔴", "high": "🟠", "medium": "🟡"} |
| timeline_format | milestones | date_format | `- **{name}:** {date:%B %d, %Y}` | date_style: full, overdue_marker: "⚠️" |
| team_roster | team_members | template | `- {name} ({role})` | sort_by: role, group_leads: true |
| progress_bar | completion_pct | template | `Progress: {value}% [{bar}]` | bar_width: 20, fill_char: "█", empty_char: "░" |
| priority_list | priorities | stringify | `{rank}. {item}` | max_items: 5, truncate: "..." |
| blockers_alert | blockers | template | `⚠️ **BLOCKER:** {description}` | highlight: true, max_length: 80 |

## Input Specification
Type: structured_data
Structure: Engineering project object containing status, metrics, issues, timeline, team, and blocker data.
Example:
```json
{
  "project_status": "healthy",
  "metrics": {"velocity": 23, "bugs_fixed": 14, "code_coverage": 87},
  "issue_summary": [{"severity": "critical", "count": 0}, {"severity": "high", "count": 3}],
  "milestones": [{"name": "Beta Release", "date": "2026-04-15", "status": "on_track"}],
  "team_members": [{"name": "Alice Chen", "role": "Tech Lead"}, {"name": "Bob Smith", "role": "Engineer"}],
  "completion_pct": 67,
  "priorities": ["Fix authentication bug", "Complete API documentation"],
  "blockers": [{"description": "Waiting on security review for deployment"}]
}
```

## Output Specification
Format: markdown
Example:
```markdown
## Status: 🟢 HEALTHY

### Key Metrics
**velocity:** 23
**bugs_fixed:** 14
**code_coverage:** 87

### Issues Summary
- **critical:** 0 issues
- **high:** 🟠 3 issues

### Timeline
- **Beta Release:** April 15, 2026

### Team
- Alice Chen (Tech Lead)
- Bob Smith (Engineer)

### Progress
Progress: 67% [█████████████░░░░░░░]

### Current Priorities
1. Fix authentication bug
2. Complete API documentation

### Blockers
⚠️ **BLOCKER:** Waiting on security review for deployment
```

## Template
Engine: string_format
```text
## Status: {status_badge}

### Key Metrics
{metrics_section}

### Issues Summary
{issues_section}

### Timeline
{timeline_section}

### Team
{team_section}

### Progress
{progress_section}

### Current Priorities
{priorities_section}

{blockers_section}
```

## Edge Cases
- Null values: render as "Not available" for metrics, skip section if entire category missing
- Empty arrays: display "None" for issues/blockers, "No milestones set" for timeline
- Special characters: escape pipe `|` as `\|` in any table cells
- Overflow: truncate descriptions at 80 chars with "..." for blockers, limit priorities to top 5
- Invalid dates: display as "TBD" with validation warning
- Missing status: default to "UNKNOWN" with 🔵 indicator

## References
- GitHub Issues API for issue severity mapping
- Markdown specification (CommonMark) for table formatting
- Engineering metrics standards (DORA, SPACE framework)
- Project status conventions (RAG status indicators)