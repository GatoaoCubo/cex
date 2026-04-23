---
kind: instruction
id: bld_instruction_hook_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for hook_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
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
  - bld_instruction_effort_profile
  - bld_examples_hook_config
  - p03_sp_hook_config_builder
---

# Instructions: How to Produce a hook_config
## Phase 1: RESEARCH
1. Identify the target builder and its 8F pipeline phases
2. Determine which hook events are needed (pre-build, post-build, on-error, quality-fail)
3. List required hooks with phase, event, and action declarations
4. Check for existing hook_config artifacts to avoid duplicates
5. Confirm slug for id: snake_case, lowercase, no hyphens
6. Review KNOWLEDGE.md for domain patterns and anti-patterns
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (id, kind, pillar, version, created, updated, author, name, target_builder, phases, quality, tags, tldr), quality: null
4. Write Overview section: what hooks this config declares, which builder it targets
5. Write Hooks section: hook declaration table with phase, event, action, and condition
6. Write Lifecycle section: execution order, error handling, retry behavior
7. Write Integration section: upstream/downstream connections to builder pipeline
8. Verify body <= 4096 bytes
9. Verify id matches `^p04_hookconf_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_hookconf_`
4. Confirm kind == hook_config
5. Confirm all required body sections present: Overview, Hooks, Lifecycle, Integration
6. HARD gates: frontmatter valid, id pattern matches, kind correct, required fields present
7. SOFT gates: score against QUALITY_GATES.md dimensions
8. Cross-check boundary: is this truly a hook_config and not hook (implementation code)?
9. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify hook
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | hook config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_retriever_config]] | sibling | 0.56 |
| [[bld_instruction_output_validator]] | sibling | 0.56 |
| [[bld_instruction_memory_scope]] | sibling | 0.56 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.53 |
| [[bld_instruction_prompt_version]] | sibling | 0.53 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.52 |
| [[bld_instruction_constraint_spec]] | sibling | 0.52 |
| [[bld_instruction_effort_profile]] | sibling | 0.46 |
| [[bld_examples_hook_config]] | downstream | 0.43 |
| [[p03_sp_hook_config_builder]] | downstream | 0.42 |
