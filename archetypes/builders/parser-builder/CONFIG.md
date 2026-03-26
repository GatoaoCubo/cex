---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: parser Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p05_parser_{slug}.md` | `p05_parser_marketplace_product.md` |
| Builder directory | kebab-case | `parser-builder/` |
| Frontmatter fields | snake_case | `input_format`, `extraction_count` |
| Parser slug | snake_case, lowercase | `marketplace_product`, `llm_json_response` |
| Rule names | snake_case | `product_title`, `stock_status` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P05_output/examples/p05_parser_{slug}.md`
- Compiled: `cex/P05_output/compiled/p05_parser_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80

## Input Format Enum

| Value | When to use | Preferred method |
|-------|-------------|-----------------|
| text | Free-form LLM output, logs | regex, split |
| json | Structured JSON responses | json_path |
| html | Web pages, scraped content | css_selector |
| xml | XML APIs, SOAP responses | xpath |
| yaml | YAML config or output | json_path (after yaml.load) |
| csv | Tabular data | split (by delimiter) |
| log | Log file lines | regex |
| mixed | Multiple formats in one input | llm_extract |

## Output Format Enum

| Value | When to use |
|-------|-------------|
| json | Standard structured output (default) |
| yaml | Config-like output |
| csv | Tabular output for spreadsheets |
| markdown | Human-readable structured output |
| typed_object | Language-specific typed object (Pydantic, TypeScript) |

## Extraction Method Selection

| Input | Recommended | Avoid |
|-------|-------------|-------|
| JSON | json_path | regex (fragile on JSON) |
| HTML | css_selector | regex (fragile on HTML) |
| XML | xpath | css_selector (limited on XML) |
| Free text | regex or llm_extract | json_path (no structure) |
| CSV | split | regex (delimiter handling) |
