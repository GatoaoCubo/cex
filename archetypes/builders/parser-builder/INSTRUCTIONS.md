---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for parser artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a parser

## Phase 1: RESEARCH
1. Identify the input format (text, JSON, HTML, XML, YAML, CSV, log, mixed)
2. Collect sample inputs (at least 2 representative examples)
3. Identify the target fields to extract from the input
4. Determine extraction method per field (regex, json_path, css_selector, xpath, split, llm_extract)
5. Define which extractions are required vs optional
6. Determine error handling strategy (skip, default, fail, retry)
7. Search for existing parsers via brain_query [IF MCP] (avoid duplicates)
8. Identify normalization needs (trim, lowercase, type casting, date parsing)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate parser_slug in snake_case (e.g., llm_json_response)
4. Fill frontmatter: all 14 required fields (quality: null, never self-score)
5. Set input_format and output_format from enums
6. Set error_strategy (default: "skip")
7. Write Extraction Rules section: table with name, target, method, pattern, required
8. Write Input Specification section: format description with example
9. Write Output Specification section: output schema with example
10. Write Error Handling section: per-strategy behavior
11. Write Normalization section: post-extraction transforms
12. Set extraction_count to match actual rules in table
13. Check body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 8 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p05_parser_ pattern
5. Confirm kind == parser
6. Confirm quality == null
7. Confirm extraction_count matches actual rules in table
8. Confirm at least 1 rule has required: true
9. Confirm input_format and output_format are valid enums
10. If score < 8.0: revise before outputting
