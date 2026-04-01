---
id: p05_fmt_engineering_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 6
domain: "engineering_reporting"
quality: 8.9
tags: [formatter, markdown, engineering, P05, report, status]
tldr: "Formats engineering project data into structured Markdown report with status, metrics, timeline, and team sections"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [engineering-report, status-formatter, markdown-formatter, project-display]
density_score: 0.89
---
# Engineering Report Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| project_header | project_name, status | template | `# {project_name}\n**Status:** {status}` | uppercase_status: true |
| metrics_table | metrics | tabulate | `\| Metric \| Value \| Target \|\n\|-----\|-----\|-----\|\n{rows}` | precision: 2, align: right |
| timeline_section | milestones | template | `## Timeline\n{milestone_list}` | date_format: "dd/MM/yyyy" |
| team_section | team_members | template | `## Team\n{member_list}` | role_display: true |
| issues_list | current_issues | template | `## Current Issues\n{issue_bullets}` | priority_sort: true |
| summary_section | summary_data | template | `## Summary\n**Progress:** {progress}%\n**Next Steps:** {next_steps}` | progress_bar: true |

## Input Specification
Type: structured_data
Structure: Engineering project object with name, status, metrics, milestones, team, issues, and summary fields.
Example:
```json
{
  "project_name": "Sistema de Autenticação",
  "status": "em desenvolvimento",
  "metrics": [
    {"name": "Cobertura de Testes", "value": 87.5, "target": 90},
    {"name": "Performance (ms)", "value": 245, "target": 200}
  ],
  "milestones": [
    {"name": "MVP", "date": "2026-04-15", "status": "em andamento"},
    {"name": "Beta", "date": "2026-05-01", "status": "planejado"}
  ],
  "team_members": [
    {"name": "Ana Silva", "role": "Tech Lead"},
    {"name": "Carlos Santos", "role": "Backend Dev"}
  ],
  "current_issues": [
    {"title": "Latência no banco", "priority": "alta"},
    {"title": "Documentação API", "priority": "média"}
  ],
  "summary_data": {
    "progress": 65,
    "next_steps": "Implementar cache Redis"
  }
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Sistema de Autenticação
**Status:** EM DESENVOLVIMENTO

## Metrics
| Metric | Value | Target |
|--------|-------|--------|
| Cobertura de Testes | 87,50 | 90,00 |
| Performance (ms) | 245,00 | 200,00 |

## Timeline
- **MVP** (15/04/2026) - em andamento
- **Beta** (01/05/2026) - planejado

## Team
- Ana Silva (Tech Lead)
- Carlos Santos (Backend Dev)

## Current Issues
- 🔴 Latência no banco (alta)
- 🟡 Documentação API (média)

## Summary
**Progress:** 65% [████████████████████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░]
**Next Steps:** Implementar cache Redis
```

## Template
Engine: string_format
```markdown
# {project_name}
**Status:** {status_upper}

## Metrics
| Metric | Value | Target |
|--------|-------|--------|
{metrics_rows}

## Timeline
{milestone_items}

## Team
{team_items}

## Current Issues
{issue_items}

## Summary
**Progress:** {progress}% {progress_bar}
**Next Steps:** {next_steps}
```

## Edge Cases
- Null values: render as `N/A` in tables and `-` in lists
- Empty arrays: show section header with "Nenhum item" placeholder
- Special characters: pipe `|` escaped as `\|` in table cells
- Number formatting: Brazilian locale (87,50 not 87.5) for decimal values
- Date overflow: truncate milestone names at 30 chars with ellipsis
- Progress > 100%: cap at 100% and add warning icon

## References
- Markdown table specification (CommonMark)
- Brazilian number formatting (ABNT NBR ISO 80000-1)
- Engineering metrics best practices (DORA metrics)
- Status reporting templates (Agile/Scrum)