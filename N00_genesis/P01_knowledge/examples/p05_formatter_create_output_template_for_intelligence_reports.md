---
id: p05_fmt_intelligence_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "intelligence_analysis"
quality: 9.2
tags: [formatter, markdown, intelligence, P05, report, analysis, threat-assessment]
tldr: "Formats structured intelligence analysis data into Markdown reports with executive summary, findings table, threat assessment, and source attribution"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [intelligence-report, analysis-formatter, findings-table, threat-assessment, markdown-report]
density_score: 0.88
---
## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| report_header | report_title | template | `# {value}\n**Classification:** {classification_level} \| **Type:** {intelligence_type}\n\n---\n` | sibling_fields: [classification_level, intelligence_type] |
| timestamp_format | analysis_date | date_format | `**Date:** {value}` | format: YYYY-MM-DD, locale: en-US |
| executive_summary | summary_text | stringify | `## Executive Summary\n\n{value}\n` | max_length: 500, wrap: word |
| threat_assessment | threat_level | stringify | `## Threat Assessment\n\n**Threat Level:** {value}` | uppercase: true |
| confidence_score | confidence_level | number_format | `**Overall Confidence:** {value}%` | precision: 1, range: 0-100 |
| findings_table | key_findings | tabulate | `## Key Findings\n\n\| # \| Finding \| Confidence \| Impact \|\n\|---\|--------\|----------\|--------\|\n{rows}` | separator: pipe, index: true |
| recommendations | action_items | tabulate | `## Recommendations\n\n\| Priority \| Action \| Owner \|\n\|--------\|-------\|------\|\n{rows}` | separator: pipe |
| source_attribution | sources | stringify | `## Sources\n\n{value}` | format: numbered_list, anonymize: false |

## Input Specification

Type: structured_data
Structure: single intelligence report object with nested findings list and action items list.

Example:
```json
{
  "report_title": "Threat Actor Q2 Assessment",
  "classification_level": "CONFIDENTIAL",
  "intelligence_type": "threat",
  "analysis_date": "2026-04-02",
  "summary_text": "Actor X has increased operational tempo targeting financial sector APIs.",
  "threat_level": "HIGH",
  "confidence_level": 87.5,
  "key_findings": [
    {"finding": "Credential stuffing campaigns up 34%", "confidence": "HIGH", "impact": "CRITICAL"},
    {"finding": "New C2 infrastructure in AS14061", "confidence": "MEDIUM", "impact": "HIGH"}
  ],
  "action_items": [
    {"priority": "P1", "action": "Rotate exposed API keys", "owner": "SecOps"},
    {"priority": "P2", "action": "Block AS14061 egress", "owner": "NetOps"}
  ],
  "sources": ["OSINT feed 2026-04-01", "Internal honeypot logs", "ISAC bulletin TLP:AMBER"]
}
```

## Output Specification

Format: markdown

Example:
```markdown
# Threat Actor Q2 Assessment
**Classification:** CONFIDENTIAL | **Type:** threat

---

**Date:** 2026-04-02

## Executive Summary

Actor X has increased operational tempo targeting financial sector APIs.

## Threat Assessment

**Threat Level:** HIGH
**Overall Confidence:** 87.5%

## Key Findings

| # | Finding | Confidence | Impact |
|---|---------|------------|--------|
| 1 | Credential stuffing campaigns up 34% | HIGH | CRITICAL |
| 2 | New C2 infrastructure in AS14061 | MEDIUM | HIGH |

## Recommendations

| Priority | Action | Owner |
|----------|--------|-------|
| P1 | Rotate exposed API keys | SecOps |
| P2 | Block AS14061 egress | NetOps |

## Sources

1. OSINT feed 2026-04-01
2. Internal honeypot logs
3. ISAC bulletin TLP:AMBER
```

## Template

Engine: string_format
```text
{report_header}
{timestamp_format}

{executive_summary}
{threat_assessment}
{confidence_score}

{findings_table}

{recommendations}

{source_attribution}
```

## Edge Cases

- Null values: render as `—` in table cells; omit optional sections (recommendations, sources) if list is empty
- Empty strings: treat as null — render `—` in tables, skip section heading if entire section is empty
- Special characters: pipe `|` escaped as `\|` in Markdown table cells; backticks in finding text wrapped in code span
- Overflow: summary_text truncated at 500 chars with word-wrap; finding text truncated at 120 chars with ellipsis in table cells
- Missing classification_level: default to `UNCLASSIFIED`
- confidence_level out of range (< 0 or > 100): clamp to [0, 100] and flag with `*` suffix
- Locale note: confidence_level uses en-US decimal (87.5%, not 87,5%); date output is ISO 8601 regardless of locale

## References

- CommonMark table spec: spec.commonmark.org/0.31.2/#tables
- ISO 8601 date format: iso.org/iso-8601-date-and-time-format.html
- TLP (Traffic Light Protocol): cisa.gov/tlp