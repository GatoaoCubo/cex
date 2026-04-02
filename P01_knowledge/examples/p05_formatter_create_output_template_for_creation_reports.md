---
id: p05_fmt_creation_reports
kind: formatter
pillar: P05
title: "Creation Reports Formatter"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "creation_reporting"
quality: 9.1
tags: [formatter, creation, reports, markdown, P05]
tldr: "Formats creation activity data into structured Markdown reports with metrics, timelines, and status summaries"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [creation-reports, activity-formatter, markdown-reports, creation-metrics]
density_score: 0.89
---
# Creation Reports Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| title_format | project_title | stringify | `# {value}` | max_length: 80, case: title |
| date_format | creation_date | date_format | `**Criado:** {value:%d/%m/%Y às %H:%M}` | locale: pt-BR, timezone: America/Sao_Paulo |
| status_format | status | stringify | `**Status:** {value}` | uppercase: true, badge: true |
| count_format | artifact_count | number_format | `**Artefatos:** {value} criados` | locale: pt-BR, unit: items |
| quality_format | avg_quality | number_format | `**Qualidade Média:** {value:.1f}/10.0` | precision: 1, range: 0-10 |
| duration_format | elapsed_time | stringify | `**Duração:** {value}` | unit: auto, round: minutes |
| creator_format | creator_name | stringify | `**Criador:** {value}` | link: true, max_length: 50 |
| progress_format | completion_pct | number_format | `**Progresso:** {value:.0f}%` | format: percentage, bar: true |

## Input Specification
Type: structured_data
Structure: creation activity object with project metadata, timing, quality metrics, and progress tracking.
Example:
```json
{
  "project_title": "Sistema de Conhecimento CEX",
  "creation_date": "2026-04-02T10:30:00",
  "status": "em_progresso",
  "artifact_count": 42,
  "avg_quality": 8.7,
  "elapsed_time": "2h 30m",
  "creator_name": "N03 Builder",
  "completion_pct": 75.5
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Sistema de Conhecimento CEX

**Criado:** 02/04/2026 às 10:30
**Status:** EM_PROGRESSO
**Artefatos:** 42 criados
**Qualidade Média:** 8.7/10.0
**Duração:** 2h 30m
**Criador:** N03 Builder
**Progresso:** 76%
```

## Template
Engine: string_format
```text
{title}

{date}
{status}
{count}
{quality}
{duration}
{creator}
{progress}
```

## Edge Cases
- Null values: render as `**Campo:** Não informado`
- Empty strings: render as `**Campo:** -`
- Special characters: pipe `|` escaped as `\|` in table contexts
- Overflow: truncate title at 80 chars with `...`, creator at 50 chars
- Invalid dates: render as `**Criado:** Data inválida`
- Quality out of range: clamp to 0.0-10.0 range
- Negative duration: render as `**Duração:** Calculando...`

## References
- Markdown CommonMark specification for formatting
- ISO 8601 date formatting standards
- Brazilian Portuguese locale formatting (ABNT NBR 14724)