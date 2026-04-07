---
kind: examples
id: bld_examples_parser
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of parser artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: parser-builder
## Golden Example
INPUT: "Create a parser for extracting product data from marketplace HTML pages"
OUTPUT:
```yaml
id: p05_parser_marketplace_product
kind: parser
pillar: P05
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
input_format: "html"
output_format: "json"
extraction_count: 6
domain: "marketplace_scraping"
quality: null
tags: [parser, marketplace, product, P05, extraction, html]
tldr: "Extracts product title, price, rating, seller, stock, and image from marketplace HTML pages"
error_strategy: "default"
streaming: false
chunking: false
normalization: [trim, lowercase_seller, price_to_float, rating_to_float]
keywords: [marketplace, product, html-parser, price-extraction, scraper-output]
density_score: 0.89
```
## Extraction Rules
| Name | Target | Method | Pattern | Required | Default |
|------|--------|--------|---------|----------|---------|
| title | product_title | css_selector | `h1.product-title` | true | - |
| price | product_price | css_selector | `span.price-current::text` | true | - |
| rating | product_rating | css_selector | `span.rating-value::text` | false | "0.0" |
| seller | seller_name | css_selector | `a.seller-link::text` | true | - |
| stock | stock_status | regex | `(em estoque|esgotado|ultimas unidades)` | false | "unknown" |
| image | image_url | css_selector | `img.product-main::attr(src)` | false | null |
## Input Specification
Format: html
Structure: standard marketplace product page with semantic CSS classes.
Example:
```html
<h1 class="product-title">Kit Decoraction Sala</h1>
<span class="price-current">R$ 149,90</span>
<span class="rating-value">4.7</span>
```
## Output Specification
Format: json
Schema:
```json
{"product_title": "string", "product_price": "float", "product_rating": "float",
 "seller_name": "string", "stock_status": "string", "image_url": "string|null"}
```
## Error Handling
Strategy: default (use default values for optional fields, fail on required).
- On extraction failure (required): raise ParseError with field name and selector
- On extraction failure (optional): use declared default value
- On malformed HTML: attempt partial extraction of available fields
## Normalization
1. trim: remove whitespace from all extracted strings
2. lowercase_seller: normalize seller name to lowercase
3. price_to_float: "R$ 149,90" -> 149.90 (strip currency, swap comma)
4. rating_to_float: "4.7" -> 4.7
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p05_parser_ pattern (H02 pass) | kind: parser (H04 pass)
- 21 fields present (H06 pass) | extraction_count: 6 matches table (H07 pass)
- input_format: html valid enum (H08 pass) | output_format: json valid enum (H08 pass)
- 3 required rules present (H08 pass) | tldr: 82ch (S01 pass) | tags: 6 items (S02 pass)
- Extraction Rules 6 rows (S03 pass) | Error Handling present (S05 pass) | density: 0.89 (S09 pass)
## Anti-Example
INPUT: "Make a parser for data"
BAD OUTPUT:
```yaml
id: data_parser
kind: extractor
pillar: P04
extraction_count: 0
quality: 9.0
tags: [data]
tldr: "This parser is designed to extract and process various types of data from different sources."
```
Parse the data and return the results. Handle errors gracefully.
FAILURES:
1. id: no `p05_parser_` prefix -> H02 FAIL
2. kind: "extractor" not "parser" -> H04 FAIL
3. pillar: "P04" not "P05" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. extraction_count: 0 (must have at least 1 rule) -> H07 FAIL
6. Missing fields: version, created, updated, author, input_format, output_format, domain -> H06 FAIL
7. tags: only 1 item, missing "parser" -> S02 FAIL
8. tldr: 83 chars of filler ("designed to extract and process various") -> S10 FAIL
9. No ## Extraction Rules table in body -> S03 FAIL
10. No ## Input Specification section -> S04 FAIL
11. No ## Error Handling section -> S05 FAIL
