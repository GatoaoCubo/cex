---
kind: knowledge_card
id: bld_knowledge_card_formatter
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for formatter production — output presentation transforms
sources: Mustache/Handlebars, Jinja2, JSON serialization, Markdown table rendering
---

# Domain Knowledge: formatter

## Executive Summary

Formatters convert structured data into human-readable or machine-consumable representations (Markdown, JSON, HTML, tables). They sit downstream of parsers and apply transformation rules, templates, escaping, and locale handling. Formatters differ from parsers (data extraction), response formats (LLM output schema), and naming rules (convention enforcement).

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P05 (output/format) |
| Frontmatter fields | 14 required |
| Quality gates | 8 HARD + 10 SOFT |
| Transform types | serialize, tabulate, template, stringify |
| Template engines | mustache, handlebars, jinja2, string_format |
| Escaping | html, json, xml (mandatory per target) |
| Key fields | input_type, target_format, transforms, escaping |

## Patterns

- **Format selection**: match target to consumer — humans get markdown, APIs get json, browsers get html
- **Transform hierarchy** (most to least structured): serialize > tabulate > template > stringify

| Transform | Output | Use case |
|-----------|--------|----------|
| serialize | JSON/YAML/XML | Machine consumption, API output |
| tabulate | Markdown/ASCII table | Comparisons, inventories |
| template | Custom layout via engine | Complex presentation |
| stringify | Plain text | Fallback, simple display |

- **Escaping is mandatory**: html escapes `<>&`, json escapes `"\`, xml escapes `<>&'"`
- **Locale-aware formatting**: numbers (1.000,00 vs 1,000.00), dates, currency symbols vary by locale
- **Null handling**: explicit strategy per field — omit, empty string, placeholder, or default value
- **Truncation**: define max_length + strategy (ellipsis, cut, word-wrap) for bounded displays

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| No escaping declared | XSS in HTML, parse errors in JSON |
| Hardcoded locale | Breaks for non-default locale users |
| No null handling strategy | Unexpected "null"/"undefined" in output |
| Pretty-print for transmission | Wastes bandwidth; use minify |
| Mixing transforms in one formatter | Conflating concerns; split into separate formatters |
| No input_type defined | Formatter cannot validate its own input |

## Application

1. Identify consumer: human (markdown/table), machine (json/yaml), browser (html)
2. Select transform: serialize, tabulate, template, or stringify
3. Define escaping: mandatory per target format
4. Configure locale: number, date, and currency format rules
5. Set null handling: strategy per field (omit, default, placeholder)
6. Validate: escaping declared, input_type defined, transform matches target

## References

- Mustache: logic-less templates (mustache.github.io)
- Jinja2: full-featured Python template engine (jinja.palletsprojects.com)
- JSON: serialization specification (RFC 8259)
- Markdown: CommonMark table rendering specification
