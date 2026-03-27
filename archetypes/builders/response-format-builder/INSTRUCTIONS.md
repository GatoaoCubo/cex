---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for response_format
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a response_format

## Phase 1: RESEARCH
1. Identify the target_kind: which artifact or task needs a defined output format?
2. Determine format_type: json (structured data), yaml (config), markdown (docs), csv (tabular), plaintext (free)
3. List the sections the output must contain, in order
4. Determine injection_point: system_prompt (persistent) or user_message (per-request)
5. Check brain_query [IF MCP] for existing response_formats (avoid duplicates)
6. Study how the output will be consumed (by parser, by human, by validation_schema)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required fields (quality: null)
4. Define sections list with ordered names
5. Write Format Overview section: what structure and for what purpose
6. Write Sections section: ordered list with descriptions and per-section constraints
7. Write Example Output section: complete concrete example
8. Write Injection Instructions section: how to place this in the prompt

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, sections_count >= 1
3. HARD: format_type in enum, injection_point in enum, target_kind non-empty
4. SOFT: example_output present and matches sections, instructions are clear
5. Verify: still a PROMPT INSTRUCTION? Not drifting into system-side validation (validation_schema)?
6. Verify: still defining structure? Not extracting data (parser) or transforming format (formatter)?
7. If score < 8.0: revise before outputting
