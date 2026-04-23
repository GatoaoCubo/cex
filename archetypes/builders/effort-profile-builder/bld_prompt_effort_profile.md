---
kind: instruction
id: bld_instruction_effort_profile
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for effort_profile
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Effort Profile"
version: "1.0.0"
author: n03_builder
tags: [effort_profile, builder, examples]
tldr: "Golden and anti-examples for effort profile construction, demonstrating ideal structure and common pitfalls."
domain: "effort profile construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_hook_config
  - bld_instruction_search_tool
  - bld_instruction_context_doc
---

# Instructions: How to Produce an effort_profile
## Phase 1: RESEARCH
1. Identify the target builder and its complexity requirements
2. Determine which model fits (haiku for simple, sonnet for medium, opus for complex)
3. Determine which thinking level fits (low, medium, high, max)
4. Check for existing effort_profile artifacts to avoid duplicates
5. Confirm slug for id: snake_case, lowercase, no hyphens
6. Review KNOWLEDGE.md for domain patterns and anti-patterns
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (id, kind, pillar, version, created, updated, author, name, model, thinking_level, quality, tags, tldr), quality: null
4. Write Overview section: what builder this profile targets and why
5. Write Configuration section: model choice, thinking level, rationale
6. Write Levels section: when to escalate or reduce effort
7. Write Integration section: how this profile connects to dispatch and runtime
8. Verify body <= 4096 bytes
9. Verify id matches `^p09_effort_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p09_effort_`
4. Confirm kind == effort_profile
5. Confirm all required body sections present: Overview, Configuration, Levels, Integration
6. HARD gates: frontmatter valid, id pattern matches, kind correct, required fields present
7. SOFT gates: score against QUALITY_GATES.md dimensions
8. Cross-check boundary: is this truly an effort_profile and not runtime_rule (execution rules)?
9. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify effort
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | effort profile construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_retriever_config]] | sibling | 0.58 |
| [[bld_instruction_output_validator]] | sibling | 0.58 |
| [[bld_instruction_memory_scope]] | sibling | 0.56 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.55 |
| [[bld_instruction_prompt_version]] | sibling | 0.55 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.54 |
| [[bld_instruction_constraint_spec]] | sibling | 0.54 |
| [[bld_instruction_hook_config]] | sibling | 0.51 |
| [[bld_instruction_search_tool]] | sibling | 0.43 |
| [[bld_instruction_context_doc]] | sibling | 0.43 |
