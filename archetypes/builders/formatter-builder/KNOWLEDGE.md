---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for formatter production
sources: CEX taxonomy, template engines, serialization standards, output formatting literature
---

# Domain Knowledge: formatter

## Foundational Concept
A formatter is an output presentation artifact that converts structured data into a human-readable
or machine-consumable representation. In LLM-powered systems, formatters sit downstream of parsers
and transform extracted data into display formats (Markdown tables, JSON pretty-print, HTML cards).
The CEX formatter (P05) defines transformation rules with template support, escaping, locale
handling, and edge case management, producing consistent formatted output from typed input.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Mustache/Handlebars | Logic-less templates with {{vars}} | template_engine: mustache/handlebars |
| Jinja2 | Full-featured Python template engine | template_engine: jinja2 |
| Python string.format | String interpolation with format specs | template_engine: string_format |
| JSON.stringify | JSON serialization with indent option | transform: serialize, target: json |
| Markdown tables | Pipe-delimited table rendering | transform: tabulate, target: markdown |

## Key Patterns
- Format selection: match target_format to consumer (humans get markdown, APIs get json)
- Transform hierarchy: serialize (structured) > tabulate (tabular) > template (custom) > stringify (fallback)
- Escaping is mandatory: html escapes `<>&`, json escapes `"\`, xml escapes `<>&'"`
- Pretty print vs minify: pretty for debugging/display, minify for transmission/storage
- Locale-aware: number formatting (1.000,00 vs 1,000.00), date formatting, currency symbols
- Null handling: explicit strategy per field (omit, empty string, placeholder, default value)
- Truncation: define max_length + strategy (ellipsis, cut, word-wrap) for bounded displays
- Streaming: for large datasets, emit formatted chunks without buffering entire output

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| rule_count | Integrity check: frontmatter matches body | No direct equivalent |
| input_type | CEX mandates explicit input typing for every formatter | Jinja2 context type |
| escaping | CEX requires explicit escape strategy declaration | Template auto-escape |
| transform enum | Standardized transform vocabulary across formatters | No standard |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT formatter |
|------|------------|------------------------|
| parser (P05) | Data extraction from raw output | EXTRACTS data, does not PRESENT |
| response_format (P05) | LLM output schema definition | DEFINES what LLM produces, does not TRANSFORM |
| naming_rule (P05) | Naming convention for artifacts | NAMES things, does not FORMAT data |
| validator (P06) | Content validation against rules | VALIDATES data, does not FORMAT |

## References
- CEX TAXONOMY_LAYERS.yaml — formatter in runtime layer
- CEX SEED_BANK.yaml — P05_formatter seeds
- Mustache specification: mustache.github.io
- Jinja2 documentation: jinja.palletsprojects.com
