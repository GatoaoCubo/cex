---
kind: instruction
id: bld_instruction_context_doc
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for context_doc
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_component_map
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
  - bld_instruction_prompt_version
  - bld_instruction_constraint_spec
  - bld_instruction_enum_def
  - bld_instruction_hook_config
---

# Instructions: How to Produce a context_doc
## Phase 1: RESEARCH
1. Identify the domain to document (snake_case label, e.g., `ecommerce_imports`, `api_auth_jwt`)
2. Define scope boundaries: write one sentence — "This context covers [X] within [Y] for [Z] audience"
3. List what is explicitly out of scope (minimum 1-3 items)
4. Catalog stakeholders and their needs: who consumes this document and for what purpose (agent, human, or both)
5. Identify constraints: technical, business, or regulatory rules that cannot change
6. List assumptions: what is taken as given without requiring proof
7. Identify dependencies on other domains, services, or artifacts
8. Check existing context_docs for overlapping scope to avoid duplication
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields, id as `p01_cd_{{topic_slug}}` (quality: null — never self-score)
4. Write Domain Scope section: restate scope sentence, list included and excluded topics explicitly
5. Write Stakeholders section: who uses this context and why, one entry per stakeholder type
6. Write Constraints section: technical, business, and regulatory constraints that bound the domain
7. Write Assumptions section: working assumptions taken as given, one per line
8. Write Dependencies section: other domains, services, and artifacts this document references
9. Write Key Concepts section: 3-5 essential ideas required to understand this domain
10. Verify body <= 2048 bytes; if over limit, trim Key Concepts first, then Dependencies
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p01_cd_`
4. Confirm kind == context_doc
5. Confirm scope boundary is defined (Domain Scope section present and at least 3 lines)
6. Confirm at least 1 stakeholder is listed
7. Confirm constraints are listed (not empty)
8. Confirm body <= 2048 bytes
9. HARD gates: frontmatter valid, id pattern matches, scope defined, stakeholder present, constraints listed
10. SOFT gates: score against QUALITY_GATES.md
11. Cross-check: domain context for hydration (not an atomic fact = knowledge_card)? Not a single-term definition (glossary_entry)? Not step-by-step procedural guidance (instruction)?
12. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify context
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | context doc construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.47 |
| [[bld_instruction_output_validator]] | sibling | 0.46 |
| [[bld_instruction_retriever_config]] | sibling | 0.45 |
| [[bld_instruction_component_map]] | sibling | 0.44 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.44 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.44 |
| [[bld_instruction_prompt_version]] | sibling | 0.43 |
| [[bld_instruction_constraint_spec]] | sibling | 0.42 |
| [[bld_instruction_enum_def]] | sibling | 0.40 |
| [[bld_instruction_hook_config]] | sibling | 0.40 |
