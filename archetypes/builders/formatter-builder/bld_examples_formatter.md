---
kind: examples
id: bld_examples_formatter
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of formatter artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: formatter-builder
## Golden Example
INPUT: "Create a formatter to display product comparison data as a Markdown table"
OUTPUT:
```yaml
id: p05_fmt_product_comparison_table
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
target_format: "markdown"
input_type: "structured_data"
rule_count: 5
domain: "ecommerce_display"
quality: null
tags: [formatter, markdown, product, P05, table, comparison]
tldr: "Formats product comparison data into Markdown table with price, rating, stock, and seller columns"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [product-table, comparison, markdown-formatter, ecommerce-display]
density_score: 0.87
```
## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| title_col | product_title | stringify | `{value}` | max_length: 40, truncate: ellipsis |
| price_col | product_price | number_format | `R$ {value:,.2f}` | locale: pt-BR, swap_decimal: true |
| rating_col | product_rating | stringify | `{value}/5.0` | pad_right: 7 |
| stock_col | stock_status | stringify | `{value}` | uppercase: true |
| seller_col | seller_name | stringify | `{value}` | max_length: 25, truncate: ellipsis |
## Input Specification
Type: structured_data
Structure: list of product objects with title, price, rating, stock, seller fields.
Example:
```json
[{"product_title": "Kit Decoracao Sala", "product_price": 149.90, "product_rating": 4.7,
  "stock_status": "em estoque", "seller_name": "Loja Casa & Cia"}]
```
## Output Specification
Format: markdown
Example:
```markdown
| Produto | Preco | Avaliacao | Estoque | Vendedor |
|---------|-------|-----------|---------|----------|
| Kit Decoracao Sala | R$ 149,90 | 4.7/5.0 | EM ESTOQUE | Loja Casa & Cia |
```
## Template
Engine: string_format
```text
| Produto | Preco | Avaliacao | Estoque | Vendedor |
|---------|-------|-----------|---------|----------|
{rows}
```
## Edge Cases
- Null values: render as `-` placeholder in table cell
- Empty strings: render as `-` placeholder
- Special characters: pipe `|` escaped as `\|` in Markdown table cells
- Overflow: truncate with ellipsis at max_length per column
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p05_fmt_ pattern (H02 pass) | kind: formatter (H04 pass)
- 21 fields present (H06 pass) | rule_count: 5 matches table (H07 pass)
- target_format: markdown valid enum (H08 pass) | input_type: structured_data valid (H08 pass)
- tldr: 89ch (S01 pass) | tags: 6 items (S02 pass) | 5 formatting rules (S03 pass)
- Input Specification present (S04 pass) | Output Specification present (S05 pass)
- Template present (S06 pass) | Edge Cases cover all 4 categories (S07 pass) | density: 0.87 (S09 pass)
## Anti-Example
INPUT: "Make a formatter for data"
BAD OUTPUT:
```yaml
id: data_formatter
kind: format
pillar: P04
rule_count: 0
quality: 8.5
tags: [data]
tldr: "This formatter is designed to format various types of data into different output formats."
```
Format the data nicely and output it.
FAILURES:
1. id: no `p05_fmt_` prefix -> H02 FAIL
2. kind: "format" not "formatter" -> H04 FAIL
3. pillar: "P04" not "P05" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. rule_count: 0 (must have at least 1 rule) -> H07 FAIL
6. Missing fields: version, created, updated, author, target_format, input_type, domain -> H06 FAIL
7. tags: only 1 item, missing "formatter" -> S02 FAIL
8. tldr: 82 chars of filler ("designed to format various") -> S10 FAIL
9. No ## Formatting Rules table in body -> S03 FAIL
10. No ## Input Specification section -> S04 FAIL
11. No ## Output Specification section -> S05 FAIL
12. Prose body ("Format the data nicely") instead of structured rules -> S03 FAIL
