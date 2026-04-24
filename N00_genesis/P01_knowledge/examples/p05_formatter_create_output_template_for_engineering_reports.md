---
id: p05_fmt_engineering_report
kind: formatter
8f: F6_produce
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
target_format: "markdown"
input_type: "structured_data"
rule_count: 7
domain: "engineering_reports"
quality: 9.1
tags: [formatter, engineering, report, markdown, P05]
tldr: "Formats engineering report data into structured Markdown with metrics, test results, deployment status, and performance benchmarks"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [engineering-report, metrics, test-results, deployment-status, performance-benchmarks]
density_score: 0.91
related:
  - p05_fmt_brand_report
  - p06_schema_health_response
  - p05_fmt_creation_report
  - p07_sr_engineering_quality
  - p05_fmt_orchestration_reports
  - bld_examples_formatter
  - tpl_response_format
  - p03_sp_engineering_nucleus
  - p06_schema_api_response_contract
  - p12_sig_builder_nucleus
---
# Engineering Report Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| metrics_table | project_metrics | tabulate | `| {metric} | {value} | {target} | {status} |` | headers: true, align: center |
| test_summary | test_results | stringify | `**{passed}/{total}** tests passed ({percentage}%)` | precision: 1 |
| build_status | build_info | stringify | `Build #{build_number}: {status} ({duration}s)` | uppercase_status: true |
| deploy_status | deployment | stringify | `**{environment}**: {status} @ {timestamp}` | timestamp_format: ISO |
| issues_count | issue_summary | stringify | `🐛 {bugs} bugs • ⚠️ {warnings} warnings • 📝 {tasks} tasks` | emoji: true |
| perf_benchmarks | performance | tabulate | `| {test_name} | {baseline} | {current} | {delta} |` | delta_color: true |
| velocity_data | sprint_metrics | stringify | `Sprint {number}: {completed}/{planned} stories ({velocity} pts)` | round_velocity: 0 |

## Input Specification
Type: structured_data
Structure: Engineering report object with metrics, test results, build info, deployment status, issues, performance data, and sprint metrics.
Example:
```json
{
  "project_metrics": [
    {"metric": "Code Coverage", "value": "87.5%", "target": "85%", "status": "✅"},
    {"metric": "Technical Debt", "value": "12h", "target": "<16h", "status": "✅"}
  ],
  "test_results": {"passed": 847, "total": 852, "percentage": 99.4},
  "build_info": {"build_number": 1247, "status": "success", "duration": 285},
  "deployment": {"environment": "production", "status": "deployed", "timestamp": "2026-04-02T10:30:00Z"},
  "issue_summary": {"bugs": 3, "warnings": 12, "tasks": 28},
  "performance": [
    {"test_name": "API Response", "baseline": "120ms", "current": "98ms", "delta": "-18%"}
  ],
  "sprint_metrics": {"number": 42, "completed": 23, "planned": 25, "velocity": 89.2}
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Engineering Report

## Project Metrics
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Code Coverage | 87.5% | 85% | ✅ |
| Technical Debt | 12h | <16h | ✅ |

## Test Results
**847/852** tests passed (99.4%)

## Build Status
Build #1247: SUCCESS (285s)

## Deployment Status
**production**: deployed @ 2026-04-02T10:30:00Z

## Issues Summary
🐛 3 bugs • ⚠️ 12 warnings • 📝 28 tasks

## Performance Benchmarks
| Test Name | Baseline | Current | Delta |
|-----------|----------|---------|-------|
| API Response | 120ms | 98ms | -18% |

## Sprint Velocity
Sprint 42: 23/25 stories (89 pts)
```

## Template
Engine: string_format
```markdown
# Engineering Report

## Project Metrics
{metrics_table}

## Test Results
{test_summary}

## Build Status
{build_status}

## Deployment Status
{deploy_status}

## Issues Summary
{issues_count}

## Performance Benchmarks
{perf_benchmarks}

## Sprint Velocity
{velocity_data}
```

## Edge Cases
- Null values: render as `N/A` placeholder in tables and `-` in summary strings
- Empty arrays: render section as "No data available" 
- Missing performance data: omit Performance Benchmarks section entirely
- Zero values: display as `0` rather than empty string
- Special characters: emoji preserved in issues summary, pipe `|` escaped as `\|` in table cells
- Long metric names: truncate at 25 chars with ellipsis in tables
- Negative deltas: prefix with `-` and color red if delta_color enabled
- Timestamp formatting: ISO 8601 format with timezone, fallback to raw string if invalid

## References
- CommonMark table specification for Markdown table rendering
- ISO 8601 timestamp format standard
- Engineering metrics best practices (DORA metrics, code coverage standards)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_fmt_brand_report]] | sibling | 0.25 |
| [[p06_schema_health_response]] | downstream | 0.21 |
| [[p05_fmt_creation_report]] | sibling | 0.21 |
| [[p07_sr_engineering_quality]] | downstream | 0.20 |
| [[p05_fmt_orchestration_reports]] | sibling | 0.19 |
| [[bld_examples_formatter]] | downstream | 0.18 |
| [[tpl_response_format]] | related | 0.17 |
| [[p03_sp_engineering_nucleus]] | upstream | 0.16 |
| [[p06_schema_api_response_contract]] | downstream | 0.16 |
| [[p12_sig_builder_nucleus]] | downstream | 0.16 |
