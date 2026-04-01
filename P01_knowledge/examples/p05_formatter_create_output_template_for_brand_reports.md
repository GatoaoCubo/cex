---
id: p05_fmt_brand_reports
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "formatter_builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "brand_reporting"
quality: 8.9
tags: [formatter, brand, reports, markdown, P05, analytics]
tldr: "Formats brand performance data into structured Markdown reports with metrics, KPIs, insights, and recommendations"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [brand-report, performance, metrics, markdown-formatter, analytics]
density_score: 0.89
---
# Brand Report Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| report_header | report_period | template | `# Relatório da Marca - {value}` | date_format: "MMMM yyyy" |
| revenue_metric | total_revenue | number_format | `R$ {value:,.2f}` | locale: pt-BR, swap_decimal: true |
| growth_metric | growth_rate | number_format | `{value:+.1f}%` | show_sign: true, precision: 1 |
| engagement_score | engagement_rate | number_format | `{value:.1f}%` | precision: 1, suffix: "%" |
| conversion_metric | conversion_rate | number_format | `{value:.2f}%` | precision: 2, suffix: "%" |
| audience_size | total_audience | number_format | `{value:,}` | thousand_separator: "." |
| top_channels | channel_performance | tabulate | `| {channel} | {impressions:,} | {engagement:.1f}% |` | sort_by: engagement, limit: 5 |
| insights_list | key_insights | template | `- {insight}` | bullet_style: dash, max_items: 8 |

## Input Specification
Type: structured_data
Structure: brand performance object with revenue, growth, engagement, channels, and insights arrays.
Example:
```json
{
  "report_period": "2026-03-01",
  "total_revenue": 125000.50,
  "growth_rate": 15.7,
  "engagement_rate": 8.4,
  "conversion_rate": 3.25,
  "total_audience": 45230,
  "channel_performance": [
    {"channel": "Instagram", "impressions": 15000, "engagement": 9.2},
    {"channel": "LinkedIn", "impressions": 8500, "engagement": 6.8}
  ],
  "key_insights": ["Aumento significativo no engajamento", "Conversões cresceram 20%"]
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Relatório da Marca - março 2026

## Métricas Principais
- **Receita Total**: R$ 125.000,50
- **Taxa de Crescimento**: +15,7%
- **Taxa de Engajamento**: 8,4%
- **Taxa de Conversão**: 3,25%
- **Audiência Total**: 45.230

## Performance por Canal
| Canal | Impressões | Engajamento |
|-------|------------|-------------|
| Instagram | 15.000 | 9,2% |
| LinkedIn | 8.500 | 6,8% |

## Principais Insights
- Aumento significativo no engajamento
- Conversões cresceram 20%
```

## Template
Engine: string_format
```text
# Relatório da Marca - {report_month}

## Métricas Principais
- **Receita Total**: {revenue_formatted}
- **Taxa de Crescimento**: {growth_formatted}
- **Taxa de Engajamento**: {engagement_formatted}
- **Taxa de Conversão**: {conversion_formatted}
- **Audiência Total**: {audience_formatted}

## Performance por Canal
{channel_table}

## Principais Insights
{insights_list}

## Recomendações
{recommendations_section}
```

## Edge Cases
- Null values: render as "Dados não disponíveis" placeholder
- Empty strings: render as "—" em dash placeholder  
- Special characters: pipe `|` escaped as `\|` in Markdown tables
- Overflow: truncate insights at 8 items with "...e mais" suffix
- Zero/negative growth: display with proper sign formatting (+/-)
- Missing channel data: show "Sem dados de canal" message
- Large numbers: use Brazilian thousand separator (.) and decimal comma (,)

## References
- Brazilian locale formatting (ABNT NBR ISO/IEC 14651)
- Markdown table specification (CommonMark)
- Brand analytics industry standards
- Portuguese business reporting conventions