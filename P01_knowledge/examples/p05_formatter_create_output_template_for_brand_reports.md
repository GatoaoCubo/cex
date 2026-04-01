---
id: p05_fmt_brand_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "builder_agent"
target_format: "markdown"
input_type: "structured_data"
rule_count: 8
domain: "brand_analytics"
quality: 8.9
tags: [formatter, markdown, brand, report, P05, analytics]
tldr: "Formats brand analysis data into structured Markdown report with metrics, positioning, competitive insights, and recommendations"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [brand-report, brand-analytics, markdown-formatter, brand-metrics, competitive-analysis]
density_score: 0.88
---
# Brand Report Formatter

## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| brand_title | brand_name | stringify | `# Relatório de Marca: {value}` | uppercase_first: true |
| brand_score | overall_score | number_format | `**Score Geral**: {value:.1f}/10.0` | locale: pt-BR, precision: 1 |
| market_rank | market_position | stringify | `**Posição**: #{value} no mercado` | pad_left: 2, zero_fill: true |
| awareness_pct | brand_awareness | number_format | `**Conhecimento**: {value:.1f}%` | locale: pt-BR, suffix: % |
| sentiment_val | sentiment_score | number_format | `**Sentiment**: {value:+.2f}` | show_sign: true, precision: 2 |
| competitive_table | competitors | tabulate | `{markdown_table}` | headers: true, align: left |
| recommendation_list | recommendations | stringify | `- {value}` | join_with: \n, bullet: - |
| report_date | analysis_date | date_format | `*Análise de {value}*` | format: %d/%m/%Y, locale: pt-BR |

## Input Specification
Type: structured_data
Structure: brand analysis object with name, scores, market data, competitive intelligence, and recommendations.
Example:
```json
{
  "brand_name": "TechFlow Solutions",
  "overall_score": 7.8,
  "market_position": 3,
  "brand_awareness": 68.5,
  "sentiment_score": 0.15,
  "competitors": [
    {"name": "CompetitorA", "score": 8.1, "share": "25%"},
    {"name": "CompetitorB", "score": 7.9, "share": "22%"}
  ],
  "recommendations": ["Increase digital presence", "Focus on customer retention"],
  "analysis_date": "2026-04-01"
}
```

## Output Specification
Format: markdown
Example:
```markdown
# Relatório de Marca: TechFlow Solutions

## Métricas Principais
**Score Geral**: 7.8/10.0
**Posição**: #03 no mercado
**Conhecimento**: 68.5%
**Sentiment**: +0.15

## Análise Competitiva
| Concorrente | Score | Participação |
|-------------|-------|--------------|
| CompetitorA | 8.1   | 25%          |
| CompetitorB | 7.9   | 22%          |

## Recomendações
- Increase digital presence
- Focus on customer retention

*Análise de 01/04/2026*
```

## Template
Engine: string_format
```text
{brand_title}

## Métricas Principais
{brand_score}
{market_rank}
{awareness_pct}
{sentiment_val}

## Análise Competitiva
{competitive_table}

## Recomendações
{recommendation_list}

{report_date}
```

## Edge Cases
- Null values: render as `--` placeholder for missing metrics
- Empty strings: render as `Não informado` for text fields
- Special characters: none needed for Markdown (no HTML escaping)
- Overflow: truncate brand names at 50 chars, recommendations at 120 chars with ellipsis

## References
- Markdown table formatting: CommonMark specification
- Brazilian locale formatting: ABNT NBR standards for dates and numbers
- Brand analytics industry standards: Brand Keys, YouGov methodology