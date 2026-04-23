---
kind: instruction
id: bld_instruction_builder
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for type_builder (meta-builder)
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_builder
  - bld_instruction_kind
  - p03_sp__builder_builder
  - bld_instruction_golden_test
  - bld_instruction_action_prompt
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_instruction_agent
  - bld_instruction_chunk_strategy
---

# Instructions: How to Produce a type_builder

## Phase 1: RESEARCH
1. Identify the target type: which kind from the taxonomy needs a builder
2. Read the target type's `_schema.yaml` to understand fields, constraints, and body structure
3. Read `TAXONOMY_LAYERS.yaml` to determine pillar assignment and sibling types
4. Read `SEED_BANK.yaml` for domain vocabulary and keyword candidates
5. Analyze existing builders in `archetypes/builders/` for pattern consistency
6. Identify boundary types: which sibling kinds are frequently confused with the target
7. Determine crew role: what single question does this builder answer

## Phase 2: COMPOSE
1. Read META_MANIFEST.md, META_SYSTEM_PROMPT.md, META_INSTRUCTIONS.md — meta-templates
2. Read META_OUTPUT_TEMPLATE.md — fill template following META constraints
3. Generate MANIFEST.md: id, kind (type_builder), pillar, domain, capabilities, routing, crew role
4. Generate SYSTEM_PROMPT.md: persona as domain specialist, 8-12 rules, boundary enforcement
5. Generate INSTRUCTIONS.md: 3-phase pipeline adapted to the target type's complexity
6. Generate KNOWLEDGE.md: domain theory, anti-patterns, size calibration, boundaries
7. Generate SCHEMA.md: all fields from _schema.yaml with types, required/optional, constraints
8. Generate OUTPUT_TEMPLATE.md: literal fill-in template with {{variables}}
9. Generate QUALITY_GATES.md: HARD gates (must pass) + SOFT gates (score contribution)
10. Generate remaining files: EXAMPLES.md, ARCHITECTURE.md, CONFIG.md, MEMORY.md, COLLABORATION.md, TOOLS.md
11. Set quality: null in every generated artifact (NEVER self-score)

## Phase 3: VALIDATE
1. Check each generated file against its META_ template constraints
2. HARD gates: all 13 files present, YAML parses in every frontmatter, id matches builder naming pattern, kind == type_builder, quality == null everywhere, domain matches target type
3. SOFT gates: capabilities >= 4 bullets, routing keywords >= 4, crew role has exclusions, boundary types listed
4. Cross-check: is every sibling type mentioned in boundaries? Does INSTRUCTIONS.md match SCHEMA.md body sections? Are EXAMPLES.md examples realistic?
5. If score < 8.0: revise weakest file in same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify _builder
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | _builder construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_builder]] | upstream | 0.37 |
| [[bld_instruction_kind]] | sibling | 0.36 |
| [[p03_sp__builder_builder]] | related | 0.33 |
| [[bld_instruction_golden_test]] | sibling | 0.33 |
| [[bld_instruction_action_prompt]] | sibling | 0.33 |
| [[bld_instruction_memory_scope]] | sibling | 0.33 |
| [[bld_instruction_retriever_config]] | sibling | 0.31 |
| [[bld_instruction_output_validator]] | sibling | 0.31 |
| [[bld_instruction_agent]] | sibling | 0.31 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.30 |
