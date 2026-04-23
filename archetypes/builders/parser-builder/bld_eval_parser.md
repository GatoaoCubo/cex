---
kind: quality_gate
id: p11_qg_parser
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of parser artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: parser"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, parser, P11, P05, governance, data-extraction]
tldr: "Gates for parser artifacts — input format defined, extraction rules tested, output schema matched to consumer."
domain: parser
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - parser-builder
  - bld_architecture_parser
  - bld_examples_parser
  - bld_schema_parser
  - p03_ins_parser
  - p03_sp_parser_builder
  - bld_output_template_parser
  - p01_kc_parser
  - bld_collaboration_parser
  - bld_memory_parser
---

## Quality Gate

# Gate: parser
## Definition
| Field     | Value                                               |
|-----------|-----------------------------------------------------|
| metric    | extraction rule coverage + output schema fidelity   |
| threshold | 8.0                                                 |
| operator  | >=                                                  |
| scope     | all parser artifacts (P05)                          |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = parser silently skipped |
| H02 | id matches `^p05_parser_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "parser" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | input_format field names the raw source format (json, html, csv, plain_text, yaml, xml, or other) | Unknown input = undefined extraction behavior |
| H08 | extraction_rules list has >= 1 entry, each with field, method, and expression | Rules without expressions cannot be automated |
| H09 | output_schema block defines >= 1 field with name and type | Consumers need a contract before wiring |
| H10 | At least one extraction rule has required: true | A parser extracting only optional fields has no guaranteed output |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "parser" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | Each extraction rule expression tested with a passing sample input in examples block | 1.0 |
| S05 | error_handling block describes strategy for malformed input (skip, default, raise, or partial) | 1.0 |
| S06 | normalization_steps list documents transforms applied after extraction (trim, lowercase, cast, etc.) | 0.5 |
| S07 | fallback_rule defined for when primary extraction finds no match | 1.0 |
| S08 | edge_cases block lists >= 2 known malformed or ambiguous input variants | 1.0 |
| S09 | output_schema consumer field names the downstream artifact or service that receives output | 0.5 |
| S10 | extraction is idempotent — same input always produces same output (documented or trivially true) | 1.0 |
| S11 | performance_note states whether parser is line-by-line or document-level and expected throughput | 0.5 |
| S12 | No filler phrases ("this parser", "designed to extract", "various fields") | 1.0 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference parser for this input format |
| >= 8.0 | PUBLISH — wire to ingestion pipeline |
| >= 7.0 | REVIEW — add edge cases, fallback rule, or error handling |
| < 7.0  | REJECT — rework extraction rules and output schema |
## Bypass
| Field | Value |
|-------|-------|
| conditions | One-time migration requiring parser before full validation when input format is stable and small volume |
| approver | p05-chief |
| audit_trail | Log in records/audits/ with input sample, output produced, and timestamp |
| expiry | 48h — parser must pass all gates before production ingestion begins |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
