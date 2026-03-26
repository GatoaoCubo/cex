---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for formatter artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a formatter

## Phase 1: RESEARCH
1. Identify the target format (json, yaml, markdown, html, csv, text, xml, table)
2. Identify the input data structure (structured_data, raw_text, typed_object, mixed)
3. Collect sample input data (at least 2 representative examples)
4. Determine formatting transforms per field (template, serialize, tabulate, stringify, etc.)
5. Select template engine if template-based (mustache, jinja2, handlebars, string_format, custom)
6. Determine escaping strategy for the target format
7. Search for existing formatters via brain_query [IF MCP] (avoid duplicates)
8. Identify edge cases (nulls, empty strings, special characters, overflow)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate formatter_slug in snake_case (e.g., product_markdown_table)
4. Fill frontmatter: all 14 required fields (quality: null, never self-score)
5. Set target_format and input_type from enums
6. Set template_engine (default: "none")
7. Write Formatting Rules section: table with name, input_field, transform, pattern, options
8. Write Input Specification section: expected structure with example
9. Write Output Specification section: formatted output with example
10. Write Template section: the formatting template or serialization config
11. Write Edge Cases section: null, empty, special char, overflow handling
12. Set rule_count to match actual rules in table
13. Check body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 8 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p05_fmt_ pattern
5. Confirm kind == formatter
6. Confirm quality == null
7. Confirm rule_count matches actual rules in table
8. Confirm target_format and input_type are valid enums
9. Confirm at least 1 formatting rule exists
10. If score < 8.0: revise before outputting
