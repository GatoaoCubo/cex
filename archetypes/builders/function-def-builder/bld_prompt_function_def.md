---
kind: instruction
id: bld_instruction_function_def
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for function_def
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Function Def"
version: "1.0.0"
author: n03_builder
tags: [function_def, builder, examples]
tldr: "Golden and anti-examples for function def construction, demonstrating ideal structure and common pitfalls."
domain: "function def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_instruction_chunk_strategy
  - bld_instruction_memory_scope
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_prompt_version
  - bld_instruction_search_tool
  - p03_sp_function_def_builder
  - bld_instruction_hook_config
---

# Instructions: How to Produce a function_def
## Phase 1: RESEARCH
1. Identify the action the function performs (search, create, update, delete, analyze, etc.)
2. Define the function name as snake_case verb_noun (e.g., search_web, create_ticket)
3. List all input parameters with types, constraints, and whether required/optional
4. Determine return type and structure (object, array, primitive)
5. Identify which LLM providers this targets (OpenAI, Anthropic, Gemini, Bedrock)
6. Check JSON Schema compatibility — no provider-specific extensions in core schema
7. Check for existing function_def artifacts to avoid duplicates
8. Confirm function slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write parameters as valid JSON Schema object with type, properties, required
5. Write description as LLM-facing: explain WHEN to call, not just WHAT it does
6. Write Returns section: type, structure, example values
7. Write Examples section: 2+ concrete input/output pairs
8. Verify body <= 2048 bytes
9. Verify id matches `^p04_fn_[a-z][a-z0-9_]+$`
10. Verify parameters is valid JSON Schema (parseable, no circular refs)
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_fn_`
4. Confirm kind == function_def
5. Confirm parameters is valid JSON Schema with type: object
6. Confirm returns has type and structure defined
7. Confirm description is LLM-readable (explains when to call)
8. HARD gates: frontmatter valid, id pattern, parameters valid, returns defined, description present
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: is this a schema def (not a protocol server)? Not an HTTP client? Not a runtime?

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify function
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | function def construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_retriever_config]] | sibling | 0.51 |
| [[bld_instruction_output_validator]] | sibling | 0.50 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.48 |
| [[bld_instruction_memory_scope]] | sibling | 0.48 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.47 |
| [[bld_instruction_constraint_spec]] | sibling | 0.47 |
| [[bld_instruction_prompt_version]] | sibling | 0.46 |
| [[bld_instruction_search_tool]] | sibling | 0.45 |
| [[p03_sp_function_def_builder]] | downstream | 0.43 |
| [[bld_instruction_hook_config]] | sibling | 0.42 |
