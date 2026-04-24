---
id: p05_fmt_marketing_report
kind: formatter
8f: F6_produce
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "marketing_reporting"
quality: 9.1
tags: [formatter, markdown, marketing, P05, reporting, campaigns, kpi]
tldr: "Formats campaign performance data into Markdown reports: KPI tables, channel breakdown, budget tracking, ROAS, and recommendations"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [marketing-report, campaign-formatter, kpi-table, channel-breakdown, roas-display]
density_score: 0.88
related:
  - p05_fmt_brand_report
  - p03_pt_marketing_task_execution
  - p01_kc_marketing_best_practices
  - p01_kc_supabase_realtime
  - p06_is_marketing_data_model
  - p01_kc_brand_voice_consistency_channels
  - campaign_performance_memory
  - bld_output_template_notifier
  - bld_instruction_notifier
  - n06_schema_brand_voice_contract
---
## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| report_header | campaign_name, period | template | `# {campaign_name} — Marketing Report · {period}` | title_case: true; null: "Unnamed Campaign" |
| report_meta | report_date, channel, analyst | template | `**Date:** {report_date}  ·  **Channel:** {channel}  ·  **Analyst:** {analyst}` | date_fmt: MM/DD/YYYY; null: omit_field |
| kpi_table | kpi_metrics | tabulate | `\| Metric \| Value \| Target \| Delta \|` | col_width: auto; null: `-` |
| channel_table | channel_data | tabulate | `\| Channel \| Spend \| Clicks \| CTR \| CPC \| Conv \|` | number_fmt: en-US; null: `-` |
| budget_line | budget_spent, budget_total | number_format | `**Budget:** ${budget_spent:,.0f} / ${budget_total:,.0f} ({pct:.1%} used)` | locale: en-US; null: omit |
| roas_display | revenue, ad_spend | number_format | `**ROAS:** {value:.2f}x` | precision: 2; null: `N/A` |
| conv_rate | conversions, clicks | number_format | `**CVR:** {value:.2%}` | precision: 2; null: `N/A` |
| recommendations | action_items | stringify | `- {item}` | max_length: 120; truncate: ellipsis; null: omit |

## Input Specification

Type: structured_data
Structure: Campaign performance payload — metadata fields (campaign_name, period, report_date, channel, analyst), kpi_metrics list of `{metric, value, target, delta}` objects, channel_data list of `{channel, spend, clicks, ctr, cpc, conv}` objects, scalar budget/revenue/conversion figures, and action_items list.

Example:
```json
{
  "campaign_name": "Q1 Brand Awareness",
  "period": "Jan–Mar 2026",
  "report_date": "2026-04-02",
  "channel": "Multi-channel",
  "analyst": "Marketing Team",
  "kpi_metrics": [{"metric": "CTR", "value": "3.2%", "target": "3.0%", "delta": "+0.2%"}],
  "channel_data": [{"channel": "Google Ads", "spend": 8500, "clicks": 12400, "ctr": 0.032, "cpc": 0.69, "conv": 310}],
  "budget_spent": 15200, "budget_total": 20000,
  "revenue": 76000, "ad_spend": 15200,
  "conversions": 620, "clicks": 38750,
  "action_items": ["Increase Google Ads budget by 15%"]
}
```

## Output Specification

Format: markdown

Example:
```markdown
# Q1 Brand Awareness — Marketing Report · Jan–Mar 2026
**Date:** 04/02/2026  ·  **Channel:** Multi-channel  ·  **Analyst:** Marketing Team

## KPI Summary
| Metric | Value | Target | Delta |
|--------|-------|--------|-------|
| CTR | 3.2% | 3.0% | +0.2% |

## Channel Breakdown
| Channel | Spend | Clicks | CTR | CPC | Conv |
|---------|-------|--------|-----|-----|------|
| Google Ads | $8,500 | 12,400 | 3.2% | $0.69 | 310 |

**Budget:** $15,200 / $20,000 (76.0% used)  ·  **ROAS:** 5.00x  ·  **CVR:** 1.60%

## Recommendations
- Increase Google Ads budget by 15%
```

## Template

Engine: string_format
```text
# {campaign_name} — Marketing Report · {period}
**Date:** {report_date}  ·  **Channel:** {channel}  ·  **Analyst:** {analyst}

## KPI Summary
| Metric | Value | Target | Delta |
|--------|-------|--------|-------|
{kpi_rows}

## Channel Breakdown
| Channel | Spend | Clicks | CTR | CPC | Conv |
|---------|-------|--------|-----|-----|------|
{channel_rows}

**Budget:** ${budget_spent:,.0f} / ${budget_total:,.0f} ({budget_pct:.1%} used)
**ROAS:** {roas:.2f}x  ·  **CVR:** {cvr:.2%}

## Recommendations
{recommendation_items}
```

## Edge Cases

- Null values: `-` placeholder in table cells; metadata fields (channel, analyst) omitted from meta line when null
- Empty strings: treated as null — `-` in tables, omitted in metadata line
- Special characters: pipe `|` escaped as `\|` in all Markdown table cells; `#` in campaign_name escaped as `\#` to prevent header promotion
- Overflow: campaign_name truncated at 60 chars with ellipsis; action_items at 120 chars with ellipsis; table column widths auto-sized by renderer

## Locale Handling

- Currency: en-US — comma thousands separator, period decimal (`$8,500.00`); symbol `$` prepended
- Percentages: CTR, CVR rendered as `{:.2%}` (e.g., `3.20%`); budget_pct as `{:.1%}`
- ROAS: float with 2 decimal places suffixed `x` (e.g., `5.00x`)
- Dates: `report_date` YYYY-MM-DD input rendered as MM/DD/YYYY; `period` passed as raw human-readable string

## Boundary

- NOT a parser: does not extract data from raw text — receives pre-structured dict/list from upstream pipeline
- NOT a response_format: does not instruct an LLM what to generate — transforms already-structured data into Markdown presentation

## References

- CommonMark table spec: commonmark.org/0.30/#tables
- Python format spec: docs.python.org/3/library/string.html#format-specification-mini-language
- Marketing KPI definitions: CTR = clicks/impressions; CVR = conversions/clicks; ROAS = revenue/ad_spend; CPC = spend/clicks

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_fmt_brand_report]] | sibling | 0.37 |
| [[p03_pt_marketing_task_execution]] | upstream | 0.24 |
| [[p01_kc_marketing_best_practices]] | upstream | 0.22 |
| [[p01_kc_supabase_realtime]] | upstream | 0.19 |
| [[p06_is_marketing_data_model]] | downstream | 0.19 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.19 |
| [[campaign_performance_memory]] | downstream | 0.18 |
| [[bld_output_template_notifier]] | upstream | 0.18 |
| [[bld_instruction_notifier]] | upstream | 0.18 |
| [[n06_schema_brand_voice_contract]] | downstream | 0.18 |
