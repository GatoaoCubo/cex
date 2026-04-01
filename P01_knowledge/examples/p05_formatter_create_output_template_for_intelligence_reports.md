---
id: p05_fmt_intelligence_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "builder_agent"
target_format: "markdown"
input_type: "structured_data"
rule_count: 7
domain: "intelligence_analysis"
quality: 8.9
tags: [formatter, intelligence, report, markdown, P05, analysis]
tldr: "Formats intelligence analysis data into structured Markdown reports with executive summary, findings table, threat assessment, and source attribution"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [intelligence-report, analysis-formatter, threat-assessment, markdown-report]
density_score: 0.89
---
# Intelligence Report Formatter

## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| executive_summary | summary_text | stringify | `## Executive Summary\n\n{value}\n` | max_length: 500, wrap: word |
| threat_level | threat_assessment | stringify | `**Threat Level:** {value}` | uppercase: true, color_coding: true |
| findings_table | key_findings | tabulate | `\| Finding \| Confidence \| Impact \|\n\|------\|----------\|-------\|\n{rows}` | separator: pipe |
| source_attribution | sources | stringify | `**Sources:** {value}` | format: numbered_list, anonymize: false |
| confidence_score | confidence_level | number_format | `**Confidence:** {value}%` | precision: 1, range: 0-100 |
| timestamp | report_date | date_format | `**Report Date:** {value}` | format: YYYY-MM-DD HH:mm UTC, timezone: UTC |
| classification | security_level | stringify | `**Classification:** {value}` | uppercase: true, prefix: bracket |

## Input Specification

Type: structured_data
Structure: intelligence analysis object with summary, threat assessment, findings array, sources, confidence metrics, and metadata.

Example:
```json
{
  "summary_text": "Analysis of emerging cyber threat targeting financial institutions",
  "threat_assessment": "high",
  "key_findings": [
    {"finding": "New malware variant detected", "confidence": 85, "impact": "Critical"},
    {"finding": "Attribution to known threat group", "confidence": 70, "impact": "High"}
  ],
  "sources": ["OSINT-2024-0401", "Internal Analysis", "Partner Intelligence"],
  "confidence_level": 78,
  "report_date": "2026-04-01T20:55:00Z",
  "security_level": "confidential"
}
```

## Output Specification

Format: markdown
Example:
```markdown
**Classification:** [CONFIDENTIAL]

## Executive Summary

Analysis of emerging cyber threat targeting financial institutions shows coordinated attack patterns consistent with advanced persistent threat activity.

**Threat Level:** HIGH

**Confidence:** 78.0%

**Report Date:** 2026-04-01 20:55 UTC

## Key Findings

| Finding | Confidence | Impact |
|---------|------------|--------|
| New malware variant detected | 85% | Critical |
| Attribution to known threat group | 70% | High |

**Sources:** 1. OSINT-2024-0401 2. Internal Analysis 3. Partner Intelligence
```

## Template

Engine: string_format
```text
**Classification:** [{classification}]

{executive_summary}

{threat_level}

{confidence_score}

{timestamp}

## Key Findings

{findings_table}

{source_attribution}
```

## Edge Cases

- Null values: render as `[DATA NOT AVAILABLE]` for critical fields, omit optional fields
- Empty findings array: render as "No key findings identified in this analysis period"
- Special characters: pipe `|` escaped as `\|` in Markdown tables, brackets escaped in classification
- Overflow: truncate summary at 500 words with `[TRUNCATED]` indicator
- Invalid confidence: clamp to 0-100 range, flag out-of-range values
- Missing classification: default to `[UNCLASSIFIED]` with warning annotation

## References

- Intelligence Community Directive 203: Analytic Standards
- Markdown CommonMark Specification for table formatting
- ISO 8601 date format for temporal data consistency