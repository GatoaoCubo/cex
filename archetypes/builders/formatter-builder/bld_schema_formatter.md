---
kind: schema
id: bld_schema_formatter
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for formatter
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Formatter"
version: "1.0.0"
author: n03_builder
tags: [formatter, builder, examples]
tldr: "Golden and anti-examples for formatter construction, demonstrating ideal structure and common pitfalls."
domain: "formatter construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_action_prompt
  - bld_schema_memory_scope
  - bld_schema_input_schema
  - bld_schema_handoff_protocol
  - bld_schema_workflow
  - bld_schema_smoke_eval
  - bld_schema_constraint_spec
  - bld_schema_golden_test
---

# Schema: formatter
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p05_fmt_{slug}) | YES | - | Namespace compliance |
| kind | literal "formatter" | YES | - | Type integrity |
| pillar | literal "P05" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| target_format | enum [json, yaml, markdown, html, csv, text, xml, table] | YES | - | What the formatter outputs |
| input_type | enum [structured_data, raw_text, typed_object, mixed] | YES | - | What the formatter accepts |
| rule_count | integer | YES | - | Must match formatting rules in body |
| domain | string | YES | - | Domain this formatter serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "formatter" |
| tldr | string <= 160ch | YES | - | Dense summary |
| template_engine | enum [mustache, jinja2, handlebars, string_format, costm, none] | REC | "none" | How templates are rendered |
| pretty_print | boolean | REC | true | Whether output is indented |
| escaping | enum [html, url, json, xml, shell, none] | REC | "none" | Escape strategy for special chars |
| encoding | enum [utf8, ascii, latin1] | REC | "utf8" | Output encoding |
| locale | string | REC | - | Locale for formatting (e.g., pt-BR) |
| streaming | boolean | REC | false | Whether formatter handles streaming |
| keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Formatting Rule Object
```yaml
rule:
  name: string (snake_case identifier)
  input_field: string (field to format)
  transform: enum [template, serialize, tabulate, stringify, number_format, date_format, truncate, wrap, costm]
  pattern: string (the formatting pattern or template)
  options: object (transform-specific options: indent, separator, max_length)
```
## ID Pattern
Regex: `^p05_fmt_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Formatting Rules` — rule table: name, input_field, transform, pattern, options
2. `## Input Specification` — what the formatter expects (structure, types)
3. `## Output Specification` — what the formatter produces (format, example)
4. `## Template` — the formatting template (if template-based) or serialization config
5. `## Edge Cases` — handling of nulls, empty strings, special characters, overflow
6. `## References` — sources and documentation
## Constraints
- max_bytes: 4096 (body only)
- naming: p05_fmt_{slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- rule_count MUST match actual rules in Formatting Rules table
- target_format and input_type MUST be from their respective enums
- Each formatting rule name MUST be unique
- At least 1 formatting rule must be present

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.56 |
| [[bld_schema_output_validator]] | sibling | 0.55 |
| [[bld_schema_action_prompt]] | sibling | 0.55 |
| [[bld_schema_memory_scope]] | sibling | 0.55 |
| [[bld_schema_input_schema]] | sibling | 0.55 |
| [[bld_schema_handoff_protocol]] | sibling | 0.54 |
| [[bld_schema_workflow]] | sibling | 0.54 |
| [[bld_schema_smoke_eval]] | sibling | 0.54 |
| [[bld_schema_constraint_spec]] | sibling | 0.54 |
| [[bld_schema_golden_test]] | sibling | 0.54 |
