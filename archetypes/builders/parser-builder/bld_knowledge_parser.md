---
kind: knowledge_card
id: bld_knowledge_card_parser
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for parser production — atomic searchable facts
sources: parser-builder MANIFEST.md + SCHEMA.md, regex standards, JSONPath RFC 9535
quality: 9.1
title: "Knowledge Card Parser"
version: "1.0.0"
author: n03_builder
tags: [parser, builder, examples]
tldr: "Golden and anti-examples for parser construction, demonstrating ideal structure and common pitfalls."
domain: "parser construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_parser_builder
  - p03_ins_parser
  - bld_schema_parser
  - bld_memory_parser
  - p01_kc_parser
  - bld_config_parser
  - parser-builder
  - p11_qg_parser
  - bld_examples_parser
  - bld_architecture_parser
---

# Domain Knowledge: parser
## Executive Summary
Parsers are data extraction artifacts that convert raw, semi-structured, or unstructured output into typed structured data. Each parser declares extraction rules (regex, JSON paths, CSS selectors, or LLM-based), error handling strategy, and normalization pipeline. They differ from formatters (which present output), validators (which check content), naming rules (which define naming conventions), and scrapers (which collect from web) by transforming local raw input into structured, typed output.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P05 (formatting/extraction) |
| Kind | `parser` (exact literal) |
| ID pattern | `p05_parser_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 10 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Extraction methods | regex, json_path, css_selector, xpath, llm_extract |
| Error strategies | fail, retry, default, skip |
## Patterns
| Pattern | Application |
|---------|-------------|
| Method selection | json_path for JSON, css_selector for HTML, regex for free text, llm_extract as last resort |
| Error strategy hierarchy | fail (strict) > retry (resilient) > default (tolerant) > skip (lenient) |
| Required vs optional extractions | At least one extraction must be required |
| Normalization pipeline | Extract first, normalize second (trim, lowercase, type cast) |
| Fallback extraction | If primary method fails, try simpler alternative method |
| Chunking for large inputs | Split into manageable chunks before parsing |
| LLM extraction | Use only when pattern-based methods cannot work |
### Method Decision Table
| Input Format | Primary Method | Fallback |
|-------------|---------------|----------|
| JSON | json_path | regex |
| HTML | css_selector | xpath |
| Free text | regex | llm_extract |
| Log files | regex with named groups | line-by-line split |
| XML | xpath | css_selector |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No error strategy defined | Undefined behavior on extraction failure |
| LLM extraction as first choice | Expensive and non-deterministic; use pattern-based first |
| All extractions optional | No guaranteed output fields; downstream consumers break |
| Missing normalization step | Raw extracted values vary in format (whitespace, case) |
| No extraction_count in frontmatter | Cannot verify body matches declared extractions |
| Regex without named groups | Positional capture is fragile; named groups are self-documenting |
## Application
1. Analyze input format (JSON, HTML, free text, logs, XML)
2. Select primary extraction method and fallback
3. Define each extraction: field name, method, pattern/path, required/optional
4. Set error_strategy per extraction (fail/retry/default/skip)
5. Define normalization steps (trim, lowercase, type cast, etc.)
6. Set extraction_count in frontmatter matching body extractions
7. Validate: body <= 3072 bytes, density >= 0.80, 8 HARD + 10 SOFT gates
## References
- parser-builder SCHEMA.md v1.0.0
- JSONPath specification (RFC 9535)
- PCRE2 regex syntax
- CSS Selectors Level 4 (W3C)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_parser_builder]] | downstream | 0.57 |
| [[p03_ins_parser]] | downstream | 0.48 |
| [[bld_schema_parser]] | downstream | 0.45 |
| [[bld_memory_parser]] | downstream | 0.43 |
| [[p01_kc_parser]] | sibling | 0.42 |
| [[bld_config_parser]] | downstream | 0.40 |
| [[parser-builder]] | downstream | 0.40 |
| [[p11_qg_parser]] | downstream | 0.37 |
| [[bld_examples_parser]] | downstream | 0.34 |
| [[bld_architecture_parser]] | downstream | 0.32 |
