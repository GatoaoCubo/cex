---
kind: config
id: bld_config_formatter
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Formatter"
version: "1.0.0"
author: n03_builder
tags: [formatter, builder, examples]
tldr: "Golden and anti-examples for formatter construction, demonstrating ideal structure and common pitfalls."
domain: "formatter construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_parser
  - bld_knowledge_card_formatter
  - bld_schema_formatter
  - p03_sp_formatter_builder
  - bld_config_output_validator
  - formatter-builder
  - p01_kc_formatter
  - bld_instruction_formatter
  - bld_config_memory_scope
  - bld_config_retriever_config
---
# Config: formatter Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p05_fmt_{slug}.md` | `p05_fmt_product_comparison_table.md` |
| Builder directory | kebab-case | `formatter-builder/` |
| Frontmatter fields | snake_case | `target_format`, `rule_count` |
| Formatter slug | snake_case, lowercase | `product_comparison_table`, `json_pretty` |
| Rule names | snake_case | `title_col`, `price_format` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P05_output/examples/p05_fmt_{slug}.md`
- Compiled: `cex/P05_output/compiled/p05_fmt_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80
## Target Format Guide
| Value | When to use | Typical transform |
|-------|-------------|------------------|
| json | API responses, machine consumption | serialize |
| yaml | Config-like output, human-readable data | serialize |
| markdown | Documentation, chat display, tables | tabulate, template |
| html | Web display, email content | template |
| csv | Spreadsheet export, tabular data | tabulate |
| text | Plain text output, logs | stringify |
| xml | Legacy API, SOAP responses | serialize |
| table | Terminal/console display | tabulate |
## Input Type Guide
| Value | When to use |
|-------|-------------|
| structured_data | Dict/list from parser or API (most common) |
| raw_text | Unprocessed string needing formatting |
| typed_object | Language-specific typed object (Pydantic, dataclass) |
| mixed | Multiple input types in one payload |
## Escaping Strategy Guide
| Target Format | Recommended Escaping | Characters Escaped |
|---------------|---------------------|-------------------|
| html | html | `< > & " '` |
| json | json | `" \ / \n \t` |
| xml | xml | `< > & ' "` |
| markdown | none | pipe `\|` only in tables |
| csv | none | quote fields with commas |
| text | none | no escaping needed |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_parser]] | sibling | 0.38 |
| [[bld_knowledge_card_formatter]] | upstream | 0.37 |
| [[bld_schema_formatter]] | upstream | 0.36 |
| [[p03_sp_formatter_builder]] | upstream | 0.35 |
| [[bld_config_output_validator]] | sibling | 0.34 |
| [[formatter-builder]] | upstream | 0.33 |
| [[p01_kc_formatter]] | upstream | 0.32 |
| [[bld_instruction_formatter]] | upstream | 0.31 |
| [[bld_config_memory_scope]] | sibling | 0.31 |
| [[bld_config_retriever_config]] | sibling | 0.31 |
