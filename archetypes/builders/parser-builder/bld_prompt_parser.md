---
id: p03_ins_parser
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Parser Builder Instructions
target: parser-builder agent
phases_count: 3
prerequisites:
  - At least one raw input sample is available (text snippet, JSON blob, log line, HTML fragment)
  - Target fields to extract are named with expected types (string, integer, float, boolean, list)
  - Downstream consumer of the parsed data is known (API, database, another builder)
validation_method: checklist
domain: parser
quality: 9.0
tags:
  - instruction
  - parser
  - extraction
  - P05
idempotent: true
atomic: false
rollback: "Delete the produced parser artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Research input format and extraction targets, compose rules with normalization and error handling, validate gates and write a parser artifact."
density_score: 0.91
llm_function: REASON
related:
  - p03_sp_parser_builder
  - bld_schema_parser
  - bld_instruction_input_schema
  - p11_qg_parser
  - bld_knowledge_card_parser
  - bld_memory_parser
  - bld_output_template_parser
  - bld_examples_parser
  - parser-builder
  - bld_collaboration_parser
---
## Context
The parser-builder receives a **raw input sample** and a **list of target fields**, then produces a `parser` artifact encoding how to extract structured data from that input format.
**Input variables**:
- `{{input_format}}` — one of: `text`, `json`, `html`, `log`, `csv`, `xml`, `yaml`, `markdown`, `mixed`
- `{{raw_sample}}` — one or more representative samples of the actual raw input (minimum 1, ideally 3 covering edge cases)
- `{{target_fields}}` — named list of fields with expected type: e.g., `id: integer, title: string, price: float`
- `{{consumer}}` — who/what receives the parsed output (e.g., "pricing API endpoint", "product database table")
- `{{error_strategy}}` — one of: `skip` (default), `default`, `fail`, `retry`
**Output**: a single `parser` artifact at `p05_parser_{{domain}}_{{input_format}}.md` with extraction rules, normalization pipeline, error handling config, and test vectors.
**Boundaries**: defines extraction logic only. Does NOT format output for display (formatter-builder), validate business rules on extracted values (validator-builder), or define naming conventions (naming-rule-builder).
## Phases
### Phase 1: RESEARCH
**Goal**: Analyze the input format, identify extraction points for every target field, and determine error strategy.
1. Identify `{{input_format}}`. Select the apownte extraction notation:
   - `text` / `log`: regex with named capture groups `(?P<field_name>...)`
   - `json`: JSONPath expressions (e.g., `$.data.items[*].id`)
   - `html`: CSS selectors (e.g., `div.product-title > span`) or XPath
   - `csv`: column index or header name
   - `xml` / `yaml`: XPath or key path
2. Collect and inspect `{{raw_sample}}`. For each field in `{{target_fields}}`, locate the extraction point in the sample. Note whether the field is always present, sometimes present, or never guaranteed (`required` / `optional` / `conditional`).
3. Identify structural variations across samples (if multiple provided): field absent, nested differently, value encoded differently (ISO date vs Unix timestamp, string int vs integer).
4. Determine normalization needs per field: trim whitespace, lowercase, type casting, date parsing, HTML entity decode, currency symbol strip, split to list.
5. Confirm `{{error_strategy}}`. Default to `skip` if not specified:
   - `skip`: omit field from output if extraction fails
   - `default`: substitute configured default value
   - `fail`: raise extraction error with field name in message
   - `retry`: re-attempt with fallback rule before failing
6. Search for existing parsers via brain_query [IF MCP]: `parser {{input_format}} {{domain}}`. Avoid duplicates; if found, determine whether an update is needed.
**Exit**: every target field has an identified extraction point, presence guarantee, and normalization plan. `{{error_strategy}}` is confirmed.
### Phase 2: COMPOSE
**Goal**: Write all extraction rules, normalization steps, test vectors, and complete artifact body.
7. Read SCHEMA.md — source of truth for all required fields.
8. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints exactly.
9. Generate `parser_slug` in snake_case (e.g., `shopee_product_html`). Set `id = p05_parser_{{parser_slug}}`.
10. Fill frontmatter: all 14 required fields. Set `quality: null` — never self-score.
11. Set `input_format` and `output_format` from their respective enums.
12. Set `error_strategy` from Phase 1 step 5.
13. Write **Extraction Rules** section: table with columns `name | target | method | pattern | required`. For fields with variations, add fallback rules in priority order.
14. Write **Input Specification** section: describe the format and embed one raw example.
15. Write **Output Specification** section: output schema with one parsed example.
16. Write **Error Handling** section: document per-strategy behavior. Always include: format change (log + alert, do not fail silently), encoding issue (normalize to UTF-8 before extraction), empty input (return `{success: false, reason: "empty_input"}` immediately).
17. Write **Normalization** section: post-extraction transforms per field (e.g., `price: strip "$", cast float`).
18. Create test vectors — one per target field plus two edge cases:
    - Edge case 1: minimal valid input (only required fields present)
    - Edge case 2: malformed input that triggers error handling
19. Set `extraction_count` to match the actual number of rules in the Extraction Rules table.
20. Verify body <= 4096 bytes.
**Exit**: all target fields have rules, `extraction_count` matches table, body within byte limit.
### Phase 3: VALIDATE
**Goal**: Verify all quality gates before writing the final artifact.
21. Check QUALITY_GATES.md — verify all 8 HARD gates manually.
22. Confirm `id` matches `^p05_parser_[a-z][a-z0-9_]+$`.
23. Confirm `kind == parser`.
24. Confirm `quality == null`.
25. Confirm `extraction_count` matches the actual number of rows in the Extraction Rules table (zero drift).
26. Confirm at least 1 rule has `required: true`.
27. Confirm `input_format` and `output_format` are valid enum values.
28. Confirm at least `len(target_fields) + 2` test vectors exist.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_parser_builder]] | related | 0.47 |
| [[bld_schema_parser]] | downstream | 0.45 |
| [[bld_instruction_input_schema]] | sibling | 0.42 |
| [[p11_qg_parser]] | downstream | 0.41 |
| [[bld_knowledge_card_parser]] | upstream | 0.40 |
| [[bld_memory_parser]] | downstream | 0.36 |
| [[bld_output_template_parser]] | downstream | 0.35 |
| [[bld_examples_parser]] | downstream | 0.34 |
| [[parser-builder]] | downstream | 0.34 |
| [[bld_collaboration_parser]] | downstream | 0.33 |
