---
kind: instruction
id: bld_instruction_enum_def
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for enum_def
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Enum Def"
version: "1.0.0"
author: n03_builder
tags: [enum_def, builder, examples]
tldr: "Golden and anti-examples for enum def construction, demonstrating ideal structure and common pitfalls."
domain: "enum def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p11_qg_enum_def
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_context_doc
  - bld_instruction_function_def
---

# Instructions: How to Produce an enum_def
## Phase 1: RESEARCH
1. Identify the domain field or concept being enumerated (status, category, type, state, role, etc.)
2. List every candidate value from domain knowledge — be exhaustive before filtering
3. Filter to only values that are meaningfully distinct (no synonyms, no overlapping semantics)
4. Determine value naming convention: SCREAMING_SNAKE for GraphQL/constants, lowercase for JSON/TypeScript
5. Identify the default value if the field has a natural fallback
6. Identify deprecated values (values that exist in production but are being phased out)
7. Declare extensibility: is this a closed set (finite, exhaustive) or open (new values expected)?
8. Check for existing enum_def artifacts in pool to avoid duplicates
9. Confirm enum slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write values list in frontmatter first — this forces scope decision before prose
5. Write descriptions map in frontmatter: one line per value explaining meaning and when to use
6. Write Overview section: what domain concept this enum represents, who references it
7. Write Values section: for each value, a heading + 1-2 sentences of description
8. Write Usage section: framework representations for at least JSON Schema + one of Pydantic/Zod/TypeScript
9. Write Constraints section: default value, extensibility declaration, deprecation notes
10. Verify body <= 1024 bytes
11. Verify id matches `^p06_enum_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p06_enum_` prefix pattern
4. Confirm kind == enum_def
5. Confirm values list has >= 2 entries
6. Confirm every value in frontmatter `values` has a matching `### VALUE` section in body
7. Confirm every value in `deprecated` also appears in `values`
8. Confirm `default` (if set) appears in `values`
9. HARD gates: frontmatter valid, id pattern matches, values >= 2, value/body sync, quality null
10. SOFT gates: score against QUALITY_GATES.md dimensions
11. Cross-check: is this truly a finite list? Not a type with methods (type_def)? Not a full schema (input_schema)? Not a single value (constant)?
12. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify enum
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | enum def construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_enum_def]] | downstream | 0.50 |
| [[bld_instruction_output_validator]] | sibling | 0.49 |
| [[bld_instruction_retriever_config]] | sibling | 0.49 |
| [[bld_instruction_memory_scope]] | sibling | 0.49 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.47 |
| [[bld_instruction_prompt_version]] | sibling | 0.47 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.47 |
| [[bld_instruction_constraint_spec]] | sibling | 0.47 |
| [[bld_instruction_context_doc]] | sibling | 0.42 |
| [[bld_instruction_function_def]] | sibling | 0.42 |
