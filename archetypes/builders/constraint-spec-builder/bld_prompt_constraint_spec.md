---
kind: instruction
id: bld_instruction_constraint_spec
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for constraint_spec
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_hook_config
  - bld_instruction_effort_profile
  - bld_instruction_enum_def
  - bld_instruction_function_def
---

# Instructions: How to Produce a constraint_spec
## Phase 1: RESEARCH
1. Identify the use case and target system
2. Determine which pattern fits (Regex, Enum/choice, JSON schema, Grammar (CFG))
3. List required parameters with concrete values
4. Check for existing constraint_spec artifacts to avoid duplicates
5. Confirm slug for id: snake_case, lowercase, no hyphens
6. Review KNOWLEDGE.md for domain patterns and anti-patterns
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (id, kind, pillar, version, created, updated, author, name, constraint_type, pattern, quality, tags, tldr), quality: null
4. Write Overview section: what it does, who uses it
5. Write Constraint Definition section: core definition with concrete values
6. Write Provider Compatibility section: parameter table with value and rationale columns
7. Write Integration section: upstream/downstream connections
8. Verify body <= 2048 bytes
9. Verify id matches `^p03_constraint_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p03_constraint_`
4. Confirm kind == constraint_spec
5. Confirm all required body sections present: Overview, Constraint Definition, Provider Compatibility, Integration
6. HARD gates: frontmatter valid, id pattern matches, kind correct, required fields present
7. SOFT gates: score against QUALITY_GATES.md dimensions
8. Cross-check boundary: is this truly a constraint_spec and not validation_schema (P06?
9. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify constraint
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | constraint spec construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_output_validator]] | sibling | 0.63 |
| [[bld_instruction_retriever_config]] | sibling | 0.62 |
| [[bld_instruction_memory_scope]] | sibling | 0.61 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.60 |
| [[bld_instruction_prompt_version]] | sibling | 0.59 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.58 |
| [[bld_instruction_hook_config]] | sibling | 0.51 |
| [[bld_instruction_effort_profile]] | sibling | 0.48 |
| [[bld_instruction_enum_def]] | sibling | 0.46 |
| [[bld_instruction_function_def]] | sibling | 0.45 |
