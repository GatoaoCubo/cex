---
kind: instruction
id: bld_instruction_formatter
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for formatter
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Formatter"
version: "1.0.0"
author: n03_builder
tags: [formatter, builder, examples]
tldr: "Golden and anti-examples for formatter construction, demonstrating ideal structure and common pitfalls."
domain: "formatter construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_formatter_builder
  - bld_instruction_action_prompt
  - bld_instruction_golden_test
  - p10_lr_formatter_builder
  - bld_instruction_input_schema
  - bld_instruction_few_shot_example
  - p11_qg_formatter
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
---

# Instructions: How to Produce a formatter
## Phase 1: RESEARCH
1. Identify the input data structure — what shape is the data coming in (structured object, raw text, typed record, mixed)?
2. Determine the target output format: JSON, YAML, Markdown, HTML, CSV, plain text, or table
3. Define transformation rules — per-field: what mapping, type conversion, or aggregation is needed?
4. Specify escaping and sanitization needs — which characters must be escaped or stripped in the target format?
5. Assess locale requirements — are date, number, or currency values involved? Which locale conventions apply?
6. Check existing formatters for the same format — avoid duplicating a formatter that already exists
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all 14 required fields
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Fill frontmatter: all 14 required fields, quality: null (never self-score)
4. Write Input Schema section: expected data structure with field names and types
5. Write Transform Rules section: table with field, transform type, pattern, and options for each rule
6. Write Output Format section: target format name plus a literal before/after example
7. Write Escaping section: sanitization rules and special character handling for the target format
8. Write Locale Handling section: date format, number format, currency format rules (omit if not applicable)
9. Write Template section: if template-based, include engine name, syntax, and all variables; otherwise state "none"
10. Set rule_count to match the actual number of rows in the Transform Rules table
11. Check body size — must stay at or below 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p05_fmt_[a-z][a-z0-9_]+`
   - [ ] kind == `formatter`
   - [ ] quality == null
   - [ ] input schema defined
   - [ ] output format specified
   - [ ] at least 1 transform rule present
   - [ ] rule_count matches actual rule count
3. SOFT gates: target_format and input_type are valid enum values, escaping rules present, locale section present when locale-sensitive data involved
4. Cross-check: output transformation not input extraction (that is parser)? Not validation (that is validator)? Not naming convention (that is naming_rule)?
5. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify formatter
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | formatter construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_formatter_builder]] | related | 0.41 |
| [[bld_instruction_action_prompt]] | sibling | 0.41 |
| [[bld_instruction_golden_test]] | sibling | 0.40 |
| [[p10_lr_formatter_builder]] | downstream | 0.39 |
| [[bld_instruction_input_schema]] | sibling | 0.38 |
| [[bld_instruction_few_shot_example]] | sibling | 0.38 |
| [[p11_qg_formatter]] | downstream | 0.37 |
| [[bld_instruction_output_validator]] | sibling | 0.35 |
| [[bld_instruction_retriever_config]] | sibling | 0.33 |
| [[bld_instruction_memory_scope]] | sibling | 0.33 |
