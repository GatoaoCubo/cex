---
kind: instruction
id: bld_instruction_prompt_version
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prompt_version
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_hook_config
  - bld_instruction_effort_profile
  - bld_instruction_enum_def
  - bld_instruction_function_def
---

# Instructions: How to Produce a prompt_version
## Phase 1: RESEARCH
1. Identify the use case and target system
2. Determine which pattern fits (Sequential, Branching, Optimized, Rollback)
3. List required parameters with concrete values
4. Check for existing prompt_version artifacts to avoid duplicates
5. Confirm slug for id: snake_case, lowercase, no hyphens
6. Review KNOWLEDGE.md for domain patterns and anti-patterns
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (id, kind, pillar, version, created, updated, author, name, prompt_ref, quality, tags, tldr), quality: null
4. Write Overview section: what it does, who uses it
5. Write Prompt Snapshot section: core definition with concrete values
6. Write Metrics section: parameter table with value and rationale columns
7. Write Lineage section: upstream/downstream connections
8. Verify body <= 2048 bytes
9. Verify id matches `^p03_pv_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p03_pv_`
4. Confirm kind == prompt_version
5. Confirm all required body sections present: Overview, Prompt Snapshot, Metrics, Lineage
6. HARD gates: frontmatter valid, id pattern matches, kind correct, required fields present
7. SOFT gates: score against QUALITY_GATES.md dimensions
8. Cross-check boundary: is this truly a prompt_version and not prompt_template (P03?
9. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify prompt
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | prompt version construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_retriever_config]] | sibling | 0.62 |
| [[bld_instruction_output_validator]] | sibling | 0.62 |
| [[bld_instruction_memory_scope]] | sibling | 0.61 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.60 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.59 |
| [[bld_instruction_constraint_spec]] | sibling | 0.58 |
| [[bld_instruction_hook_config]] | sibling | 0.51 |
| [[bld_instruction_effort_profile]] | sibling | 0.48 |
| [[bld_instruction_enum_def]] | sibling | 0.45 |
| [[bld_instruction_function_def]] | sibling | 0.44 |
