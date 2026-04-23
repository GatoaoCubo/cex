---
id: p05_fmt_orchestration_reports
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "orchestration_monitoring"
quality: 9.1
tags: [formatter, markdown, orchestration, P05, report, nucleus, mission]
tldr: "Converts orchestration run data into structured Markdown with mission status, nucleus activity, quality metrics, and resource utilization tables"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [orchestration-report, mission-status, nucleus-activity, quality-metrics, markdown-formatter]
density_score: 0.88
related:
  - p05_fmt_creation_report
  - p12_sig_builder_nucleus
  - p08_pat_nucleus_fractal
  - p03_sp_n03_creation_nucleus
  - p01_kg_cex_system_architecture
  - bld_collaboration_nucleus_def
  - p12_sig_admin_orchestration
  - p12_wf_create_orchestration_agent
  - p08_ac_orchestrator
  - agent_card_engineering_nucleus
---
## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| mission_header | mission_name | template | `## Mission: {value}` | uppercase_first: true |
| status_badge | mission_status | stringify | `**Status:** {value}` | map: {running: "🟡 RUNNING", complete: "✅ COMPLETE", failed: "❌ FAILED", partial: "⚠️ PARTIAL"} |
| quality_score | quality_avg | number_format | `{value:.1f}/10.0` | precision: 1, min_width: 5, fallback: "N/A" |
| timestamp_fmt | completed_at | date_format | `{value:%Y-%m-%d %H:%M} UTC` | timezone: UTC, fallback: "In Progress" |
| nucleus_table | nucleus_activity | tabulate | `\| {nucleus} \| {tasks_done} \| {pct_complete}% \| {quality_avg:.1f} \|` | headers: ["Nucleus", "Tasks", "Complete", "Quality"], align: left |
| artifact_table | artifacts_produced | tabulate | `\| {kind} \| {name} \| {score:.1f} \|` | headers: ["Kind", "Artifact", "Score"], align: left, max_rows: 20 |
| resource_pct | resource_utilization | number_format | `{value:.0%}` | percent_style: true, fallback: "—" |
| error_list | errors | template | `- **{nucleus}**: {message}` | omit_if_empty: true, section_header: "## Errors" |

## Input Specification

Type: structured_data
Structure: Single orchestration run object with nested nucleus activity records and artifact inventory.

Example:
```json
{
  "mission_name": "BRAND_LAUNCH_v2",
  "mission_status": "complete",
  "completed_at": "2026-04-02T14:07:30Z",
  "quality_avg": 9.1,
  "resource_utilization": 0.74,
  "nucleus_activity": [
    {"nucleus": "N03", "tasks_done": 12, "pct_complete": 100, "quality_avg": 9.2},
    {"nucleus": "N02", "tasks_done": 5, "pct_complete": 100, "quality_avg": 8.9}
  ],
  "artifacts_produced": [
    {"kind": "agent", "name": "p02_agent_brand_core", "score": 9.3}
  ],
  "errors": []
}
```

## Output Specification

Format: markdown

Example:
```markdown
## Mission: BRAND_LAUNCH_v2
**Status:** ✅ COMPLETE
**Completed:** 2026-04-02 14:07 UTC | **Quality Avg:** 9.1/10.0 | **Resources:** 74%

### Nucleus Activity
| Nucleus | Tasks | Complete | Quality |
|---------|-------|----------|---------|
| N03     | 12    | 100%     | 9.2     |
| N02     | 5     | 100%     | 8.9     |

### Artifacts Produced
| Kind  | Artifact               | Score |
|-------|------------------------|-------|
| agent | p02_agent_brand_core   | 9.3   |
```

## Template

Engine: string_format

```text
{mission_header}
{status_badge}
**Completed:** {timestamp_fmt} | **Quality Avg:** {quality_score} | **Resources:** {resource_pct}

### Nucleus Activity
{nucleus_table}

### Artifacts Produced
{artifact_table}
{error_list}
```

## Edge Cases

- Null `completed_at`: render as `In Progress` via date_format fallback
- Null `quality_avg`: render as `N/A`; never compute average over zero samples
- Empty `errors` list: omit `## Errors` section entirely (omit_if_empty: true)
- Empty `nucleus_activity`: render table with header row and single `— no nuclei active —` row
- Pipe characters in artifact names: escaped as `\|` in all table cells
- `pct_complete` > 100 or < 0: clamp to [0, 100] range before rendering
- `mission_status` not in map: render raw value uppercased with no badge emoji

## References

- CommonMark table spec: https://spec.commonmark.org/0.30/#tables-extension
- Python strftime directives: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
- CEX formatter schema: `archetypes/builders/formatter-builder/bld_schema_formatter.md`
- Orchestration monitoring KC: `P01_knowledge/library/kind/kc_formatter.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_fmt_creation_report]] | sibling | 0.32 |
| [[p12_sig_builder_nucleus]] | downstream | 0.23 |
| [[p08_pat_nucleus_fractal]] | downstream | 0.22 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.22 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.21 |
| [[bld_collaboration_nucleus_def]] | downstream | 0.21 |
| [[p12_sig_admin_orchestration]] | downstream | 0.20 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.19 |
| [[p08_ac_orchestrator]] | downstream | 0.19 |
| [[agent_card_engineering_nucleus]] | upstream | 0.19 |
