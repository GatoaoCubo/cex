---
kind: schema
id: bld_schema_parser
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for parser
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Parser"
version: "1.0.0"
author: n03_builder
tags: [parser, builder, examples]
tldr: "Golden and anti-examples for parser construction, demonstrating ideal structure and common pitfalls."
domain: "parser construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: parser
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p05_parser_{slug}) | YES | - | Namespace compliance |
| kind | literal "parser" | YES | - | Type integrity |
| pillar | literal "P05" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| input_format | enum [text, json, html, xml, yaml, csv, log, mixed] | YES | - | What the parser consumes |
| output_format | enum [json, yaml, csv, markdown, typed_object] | YES | - | What the parser produces |
| extraction_count | integer | YES | - | Must match extraction rules in body |
| domain | string | YES | - | Domain this parser serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "parser" |
| tldr | string <= 160ch | YES | - | Dense summary |
| error_strategy | enum [skip, default, fail, retry] | REC | "skip" | What to do when extraction fails |
| streaming | boolean | REC | false | Whether parser handles streaming input |
| chunking | boolean | REC | false | Whether parser splits large input |
| chunk_size | integer | REC | - | Bytes per chunk (if chunking: true) |
| normalization | list[string] | REC | [] | Post-extraction normalization steps |
| keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Extraction Rule Object
```yaml
rule:
  name: string (snake_case identifier)
  target: string (field to extract)
  method: enum [regex, json_path, css_selector, xpath, split, llm_extract]
  pattern: string (the extraction pattern)
  required: boolean
  default: any (value when extraction fails and error_strategy is "default")
  normalize: string (optional post-extraction transform)
```
## ID Pattern
Regex: `^p05_parser_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Extraction Rules` — rule table: name, target, method, pattern, required
2. `## Input Specification` — what the parser expects (format, structure, examples)
3. `## Output Specification` — what the parser produces (schema, example)
4. `## Error Handling` — behavior per error_strategy, fallback extraction
5. `## Normalization` — post-extraction transforms (trim, lowercase, type cast)
6. `## References` — sources and documentation
## Constraints
- max_bytes: 4096 (body only)
- naming: p05_parser_{slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- extraction_count MUST match actual rules in Extraction Rules table
- input_format and output_format MUST be from their respective enums
- Each extraction rule name MUST be unique
- At least 1 extraction rule must be required: true
