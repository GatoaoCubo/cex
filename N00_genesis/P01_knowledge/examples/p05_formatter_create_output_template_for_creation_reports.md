---
id: p05_fmt_creation_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "creation_reporting"
quality: 9.1
tags: [formatter, markdown, creation, P05, reporting, pipeline]
tldr: "Formats creation pipeline data into structured Markdown reports with artifact counts, quality scores, nucleus stats, and 8F timeline"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [creation-report, pipeline-output, artifact-summary, quality-metrics, nucleus-stats]
density_score: 0.88
related:
  - p05_fmt_orchestration_reports
  - p05_fmt_artifact_creation_report
  - bld_examples_formatter
  - p05_fmt_engineering_report
  - p05_fmt_brand_report
  - formatter-builder
  - bld_knowledge_card_formatter
  - bld_collaboration_formatter
  - bld_instruction_formatter
  - p10_lr_formatter_builder
---
## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| report_title | mission_name | stringify | `# Creation Report: {value}` | case: title, max_length: 80 |
| creation_date | timestamp | date_format | `**Data:** {value:%d/%m/%Y às %H:%M}` | locale: pt-BR, timezone: America/Sao_Paulo |
| artifact_count | artifacts_created | number_format | `**Artefatos Criados:** {value}` | locale: pt-BR, unit: items |
| quality_avg | avg_quality_score | number_format | `**Qualidade Média:** {value:.1f}/10.0` | precision: 1, range: 0.0-10.0 |
| nucleus_id | nucleus | stringify | `**Núcleo:** {value}` | uppercase: true, max_length: 10 |
| status_badge | pipeline_status | stringify | `**Status:** {value}` | uppercase: true |
| stage_progress | current_stage | stringify | `**Etapa:** {value}/8` | prefix: "F" |
| elapsed_time | duration_seconds | stringify | `**Duração:** {value}` | unit: auto, round: true |

## Input Specification

Type: structured_data  
Structure: Single creation run record produced by the 8F pipeline executor.

```json
{
  "mission_name": "build_knowledge_card_react",
  "timestamp": "2026-04-02T13:18:46",
  "artifacts_created": 3,
  "avg_quality_score": 9.1,
  "nucleus": "n03",
  "pipeline_status": "complete",
  "current_stage": 8,
  "duration_seconds": 142
}
```

## Output Specification

Format: markdown

```markdown
# Creation Report: Build Knowledge Card React

**Data:** 02/04/2026 às 13:18
**Artefatos Criados:** 3
**Qualidade Média:** 9.1/10.0
**Núcleo:** N03
**Status:** COMPLETE
**Etapa:** F8/8
**Duração:** 2 min 22 s
```

## Template

Engine: string_format

```text
# Creation Report: {mission_name}

**Data:** {timestamp:%d/%m/%Y às %H:%M}
**Artefatos Criados:** {artifacts_created}
**Qualidade Média:** {avg_quality_score:.1f}/10.0
**Núcleo:** {nucleus}
**Status:** {pipeline_status}
**Etapa:** F{current_stage}/8
**Duração:** {duration_seconds}
```

## Edge Cases

- Null values: render as `—` em-dash placeholder in all fields
- Empty strings: render as `—` em-dash placeholder
- Special characters: pipe `|` escaped as `\|` only if formatter output is nested in a Markdown table
- Overflow: `mission_name` truncated at 80 chars with ellipsis; `nucleus` truncated at 10 chars
- `avg_quality_score` out of range (< 0 or > 10): clamp and append `⚠` flag
- `current_stage` outside 1–8: render raw value with `?/8` suffix
- `duration_seconds` < 60: render as `{n} s`; >= 60: render as `{m} min {s} s`

## References

- Python strftime format codes: docs.python.org/3/library/datetime.html#strftime-strptime-behavior
- Locale pt-BR number formatting: ABNT NBR 5892
- CEX 8F pipeline stage definitions: `.claude/rules/n03-8f-enforcement.md`
- CEX formatter schema: `archetypes/builders/formatter-builder/bld_schema_formatter.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_fmt_orchestration_reports]] | sibling | 0.38 |
| [[p05_fmt_artifact_creation_report]] | sibling | 0.30 |
| [[bld_examples_formatter]] | downstream | 0.29 |
| [[p05_fmt_engineering_report]] | sibling | 0.27 |
| [[p05_fmt_brand_report]] | sibling | 0.26 |
| [[formatter-builder]] | related | 0.23 |
| [[bld_knowledge_card_formatter]] | upstream | 0.22 |
| [[bld_collaboration_formatter]] | downstream | 0.22 |
| [[bld_instruction_formatter]] | upstream | 0.22 |
| [[p10_lr_formatter_builder]] | downstream | 0.22 |
