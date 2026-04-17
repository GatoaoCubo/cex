---
id: p05_fmt_readme_pricing
name: "CEX README Pricing Section Formatter"
kind: formatter
pillar: P05
version: 1.0.0
created: "2026-04-02"
updated: "2026-04-02"
author: n06_commercial
domain: commercial
target_format: markdown
input_type: structured
rule_count: 7
quality: 9.1
tags: [pricing, readme, commercial, cex]
tldr: "Formats CEX pricing data into professional markdown README section with table, benefits, and CTA"
---

# CEX README Pricing Section Formatter

## Input Schema
Expected data structure for CEX pricing information:
```yaml
pricing_data:
  tiers:
    - name: string      # "Explorer", "Builder", "Master"
      price: string     # "Free", "R$497", "R$997" 
      modules: string   # "M01-M03", "M04-M10", "M11-M14"
      model: string     # "No", "Yes", "Yes"
      community: string # "No", "Discord", "Discord + calls"
      support: string   # "GitHub Issues", "Email", "Priority"
  benefits:
    - description: string  # Value proposition bullets
  guarantee: string        # "30 days money back"
  cta_text: string        # "Get Started"
```

## Transform Rules
| Field | Transform Type | Rule/Template | Escape | Locale |
|-------|----------------|---------------|--------|---------|
| tiers | tabulate | Markdown table with pipe separators | None | N/A |
| tier.name | stringify | Header cell formatting | None | N/A |
| tier.price | stringify | Bold price display | None | pt-BR |
| benefits | serialize | Bullet list with dash prefix | None | N/A |
| guarantee | stringify | Emphasis with markdown italic | None | N/A |
| cta_text | template | Button placeholder format | None | N/A |
| section_headers | template | H2/H3 hierarchy with ## prefix | None | N/A |

## Output Format
Target: markdown
Produces a complete pricing section suitable for insertion into a README.md file.

### Sample Input:
```yaml
pricing_data:
  tiers:
    - {name: "Explorer", price: "Free", modules: "M01-M03", model: "No", community: "No", support: "GitHub Issues"}
    - {name: "Builder", price: "R$497", modules: "M04-M10", model: "Yes", community: "Discord", support: "Email"}
    - {name: "Master", price: "R$997", modules: "M11-M14", model: "Yes", community: "Discord + calls", support: "Priority"}
  benefits: 
    - "Free repo works with generic Ollama (quality ~7.0)"
    - "Paid course includes cex-brain:14b (quality ~9.0)"
    - "ROI: 1 client project pays for the course"
  guarantee: "30 days money back"
  cta_text: "Get Started"
```

### Sample Output:
```markdown
## Pricing

| | Explorer | Builder | Master |
|---|----------|---------|--------|
| **Price** | Free | **R$497** | **R$997** |
| **Modules** | M01-M03 | M04-M10 | M11-M14 |
| **cex-brain model** | No | Yes | Yes |
| **Community** | No | Discord | Discord + calls |
| **Support** | GitHub Issues | Email | Priority |

### Why pay?
- Free repo works with generic Ollama (quality ~7.0)
- Paid course includes cex-brain:14b (quality ~9.0)
- ROI: 1 client project pays for the course

### Get Started
[Get Started](#) - _30 days money back guarantee_
```

## Escaping
Minimal escaping required for markdown:
- Pipe characters in table cells: escaped as `\|`
- Asterisks in content: escaped as `\*` when not intended as emphasis
- No HTML entity encoding needed

## Locale Handling
- Currency format: Brazilian Real (R$) prefix
- Number format: Standard decimal notation
- No date formatting required

## Template Engine
Engine: string interpolation
Syntax: Direct field substitution
Variables: tier.*, benefits.*, guarantee, cta_text