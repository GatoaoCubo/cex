---
kind: schema
id: bld_schema_glossary_entry
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for glossary_entry
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Glossary Entry"
version: "1.0.0"
author: n03_builder
tags: [glossary_entry, builder, examples]
tldr: "Golden and anti-examples for glossary entry construction, demonstrating ideal structure and common pitfalls."
domain: "glossary entry construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_constraint_spec
  - bld_schema_action_prompt
  - bld_schema_benchmark_suite
  - bld_schema_chunk_strategy
  - bld_schema_integration_guide
  - bld_schema_golden_test
---

# Schema: glossary_entry
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_gl_{term}) | YES | - | Namespace compliance |
| kind | literal "glossary_entry" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| term | string | YES | - | The term being defined |
| definition | string, max 3 lines | YES | - | Concise definition |
| synonyms | list[string], len >= 1 | YES | - | At least one synonym |
| abbreviation | string or null | REC | null | Short form if exists |
| domain | string | YES | - | Where term is used |
| domain_specific | string or null | REC | null | CEX-specific meaning |
| context | string | REC | - | Where term appears |
| disambiguation | string or null | REC | null | Clarify vs similar terms |
| related_terms | list[string] | REC | [] | Cross-references |
| usage | string | REC | - | How term is used in forctice |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "glossary" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p01_gl_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Definition` — the concise definition (max 3 lines)
2. `## Usage` — where and how the term appears
3. `## Disambiguation` — clarification vs similar terms (if needed)
4. `## Related Terms` — cross-references to other glossary entries
## Constraints
- max_bytes: 512 (body only)
- max_definition_lines: 3
- naming: p01_gl_{term}.yaml
- machine_format: yaml
- id == filename stem
- definition MUST be <= 3 lines
- synonyms MUST have at least 1 entry
- quality: null always
- glossary_entry is CONCISE — no deep analysis (that is knowledge_card)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_handoff_protocol]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_constraint_spec]] | sibling | 0.63 |
| [[bld_schema_action_prompt]] | sibling | 0.63 |
| [[bld_schema_benchmark_suite]] | sibling | 0.62 |
| [[bld_schema_chunk_strategy]] | sibling | 0.62 |
| [[bld_schema_integration_guide]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.62 |
