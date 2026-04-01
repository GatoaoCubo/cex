---
id: p05_fmt_intelligence_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "intelligence_reporting"
quality: 8.9
tags: [formatter, markdown, intelligence, P05, report, analysis]
tldr: "Formats intelligence data into structured markdown reports with threat levels, confidence scores, and actionable recommendations"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [intelligence-report, threat-analysis, markdown-formatter, research-display]
density_score: 0.89
---
# Intelligence Report Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| title_format | report_title | stringify | `# {value}` | max_length: 80, uppercase: true |
| confidence_badge | confidence_level | stringify | `**Confidence: {value}%**` | color_code: true |
| threat_level | threat_assessment | stringify | `🔴 **{value}**` | severity_icons: true |
| source_cite | source_name | stringify | `*Source: {value}*` | max_length: 50, truncate: ellipsis |
| date_format | date_collected | date_format | `**Date:** {value:%Y-%m-%d %H:%M}` | timezone: UTC |
| region_tag | geographic_region | stringify | `📍 **Region:** {value}` | uppercase: true |
| findings_list | key_findings | tabulate | `- {value}` | bullet_style: dash, max_items: 10 |
| recommendations | action_items | tabulate | `{index}. **{priority}:** {value}` | numbered: true, priority_sort: true |

## Input Specification
Type: structured_data
Structure: Intelligence data object with report metadata, threat assessment, findings, and recommendations.
Example:
```json
{
  "report_title": "APT29 Infrastructure Analysis",
  "confidence_level": 85,
  "threat_assessment": "HIGH",
  "source_name": "OSINT Collection Beta",
  "date_collected": "2026-04-01T20:30:00Z",
  "geographic_region": "Eastern Europe",
  "key_findings": [
    "New C2 infrastructure identified in Romania",
    "Domain registration patterns match previous campaigns",
    "SSL certificates share common authority"
  ],
  "action_items": [
    {"priority": "IMMEDIATE", "value": "Block identified IP ranges"},
    {"priority": "24H", "value": "Monitor associated domains"},
    {"priority": "WEEKLY", "value": "Update threat signatures"}
  ]
}
```

## Output Specification
Format: markdown
Example:
```markdown
# APT29 INFRASTRUCTURE ANALYSIS

**Confidence: 85%**
🔴 **HIGH**
*Source: OSINT Collection Beta*
**Date:** 2026-04-01 20:30
📍 **Region:** EASTERN EUROPE

## Key Findings
- New C2 infrastructure identified in Romania
- Domain registration patterns match previous campaigns
- SSL certificates share common authority

## Recommended Actions
1. **IMMEDIATE:** Block identified IP ranges
2. **24H:** Monitor associated domains
3. **WEEKLY:** Update threat signatures
```

## Template
Engine: string_format
```text
{title}

{confidence_badge}
{threat_level}
{source_cite}
{date_format}
{region_tag}

## Key Findings
{findings_list}

## Recommended Actions
{recommendations}
```

## Edge Cases
- Null values: render as `[DATA NOT AVAILABLE]` in report sections
- Empty strings: render as `[PENDING]` for status fields
- Special characters: preserve markdown syntax, escape only pipe `|` characters
- Overflow: truncate findings list at 10 items with `[...N more findings]` footer
- Missing threat level: default to `⚪ **UNKNOWN**` with white circle icon
- Invalid confidence: clamp to 0-100 range, display warning for out-of-bounds values

## References
- NIST Cybersecurity Framework: threat assessment standards
- MITRE ATT&CK: threat intelligence formatting guidelines
- CommonMark specification: markdown table and list rendering