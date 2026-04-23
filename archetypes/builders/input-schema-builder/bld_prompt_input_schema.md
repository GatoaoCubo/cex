---
kind: instruction
id: bld_instruction_input_schema
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for input_schema
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Input Schema"
version: "1.0.0"
author: n03_builder
tags: [input_schema, builder, examples]
tldr: "Golden and anti-examples for input schema construction, demonstrating ideal structure and common pitfalls."
domain: "input schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_input_schema
  - p11_qg_input_schema
  - p10_lr_input_schema_builder
  - bld_instruction_instruction
  - bld_schema_input_schema
  - p03_sp_input_schema_builder
  - bld_instruction_action_prompt
  - bld_instruction_interface
  - p03_ins_validation_schema
  - bld_instruction_env_config
---

# Instructions: How to Produce an input_schema
## Phase 1: RESEARCH
1. Identify the operation or agent that needs this input contract — name it explicitly
2. List every piece of data the caller must provide; one field per line
3. Classify each field as required or optional; required fields have no fallback
4. Assign a type to each field: string, integer, float, boolean, list, or object
5. Define default values for every optional field (null is a valid default)
6. Specify coercion rules: what happens when a string arrives where an integer is expected, how nulls are treated, what triggers a type cast failure
7. Identify validation patterns per field: regex for strings, min/max for numbers, enum for fixed sets
8. Check existing input_schemas via brain_query [IF MCP] for the same operation — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: all 17 fields (null is acceptable for recommended fields)
4. Set quality: null — never self-score
5. Write the Fields section: one row per field with columns name / type / required / default / description
6. Write the Validation Rules section: per-field rules (regex pattern, numeric range, allowed enum values, costm constraints)
7. Write the Coercion Rules section: document every type conversion and null-handling behavior
8. Write the Error Messages section: one failure message per field that can fail validation
9. Write the Examples section: at least one complete, valid input object in YAML or JSON
10. Write the Constraints section: maximum field count, nesting depth limit, total payload size ceiling
11. Verify body is within 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p06_is_[a-z][a-z0-9_]+`
   - kind == input_schema
   - fields list has at least one entry
   - every field entry has name and type
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - all required fields are explicitly marked
   - optional fields each have a default value specified
   - at least one complete example present
   - error messages cover all required fields
   - coercion behavior documented for any mixed-type field
4. Cross-check scope boundaries:
   - unilateral input contract (one receiver), not a bilateral interface?
   - not validation logic that belongs in a validator?
   - not an abstract type definition (type_def)?
   - defaults specified for all optional fields?
5. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_input_schema]] | upstream | 0.41 |
| [[p11_qg_input_schema]] | downstream | 0.40 |
| [[p10_lr_input_schema_builder]] | downstream | 0.37 |
| [[bld_instruction_instruction]] | sibling | 0.36 |
| [[bld_schema_input_schema]] | downstream | 0.36 |
| [[p03_sp_input_schema_builder]] | related | 0.35 |
| [[bld_instruction_action_prompt]] | sibling | 0.34 |
| [[bld_instruction_interface]] | sibling | 0.33 |
| [[p03_ins_validation_schema]] | sibling | 0.33 |
| [[bld_instruction_env_config]] | sibling | 0.31 |
