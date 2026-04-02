---
id: p05_fmt_creation_reports
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 6
domain: "creation_reporting"
quality: 9.1
tags: [formatter, markdown, creation, reports, P05, artifacts]
tldr: "Formats creation activity data into structured Markdown reports with artifact summaries, quality metrics, and progress tracking"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [creation-reports, artifact-summary, quality-metrics, progress-formatter]
density_score: 0.86
---
# Creation Reports Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| artifact_name | artifact_id | stringify | `**{value}**` | max_length: 60, truncate: ellipsis |
| quality_badge | quality_score | number_format | `🎯 {value:.1f}/10` | color_threshold: 8.0 |
| status_icon | status | stringify | `{icon} {value}` | icon_map: completed=✅, progress=🔄, failed=❌ |
| creation_date | created | date_format | `📅 {value:%d/%m/%Y}` | locale: pt-BR |
| author_info | author | stringify | `👤 {value}` | max_length: 20, truncate: ellipsis |
| pillar_tag | pillar | stringify | `📂 {value}` | uppercase: true |

## Input Specification
Type: structured_data
Structure: List of creation activity objects containing artifact metadata, quality scores, timestamps, and authorship information.
Example:
```json
{
  "artifacts": [
    {
      "artifact_id": "p01_kc_react_patterns",
      "quality_score": 8.7,
      "status": "completed",
      "created": "2026-04-02T10:30:00",
      "author": "knowledge-builder",
      "pillar": "P01",
      "domain": "frontend_development"
    }
  ],
  "summary": {
    "total_artifacts": 5,
    "avg_quality": 8.4,
    "completion_rate": 0.8
  }
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Creation Report - 2026-04-02

## Summary
- **Total Artifacts**: 5
- **Average Quality**: 8.4/10
- **Completion Rate**: 80%

## Artifacts Created

### **p01_kc_react_patterns**
🎯 8.7/10 | ✅ completed | 📅 02/04/2026 | 👤 knowledge-builder | 📂 P01

### **p02_agent_content_creator**  
🎯 9.2/10 | ✅ completed | 📅 02/04/2026 | 👤 agent-builder | 📂 P02
```

## Template
Engine: string_format
```text
# Creation Report - {date}

## Summary
- **Total Artifacts**: {total_artifacts}
- **Average Quality**: {avg_quality:.1f}/10
- **Completion Rate**: {completion_rate:.0%}

## Artifacts Created

{artifact_rows}
```

## Edge Cases
- Null quality scores: render as `⚪ N/A` instead of numeric badge
- Empty author field: render as `👤 System` placeholder
- Status not in icon map: render as `❓ {status}` with unknown icon
- Date parsing errors: render as `📅 Invalid Date` fallback

## References
- Markdown specification: CommonMark 0.30
- Date formatting: Python strftime patterns
- Unicode icons: GitHub emoji shortcodes standard