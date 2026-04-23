---
kind: knowledge_card
id: bld_knowledge_card_builder
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for meta-builder construction — building builders themselves
sources: CEX archetype system, builder pattern literature, meta-programming patterns
quality: 9.2
title: "Knowledge Card Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_builder
  - bld_architecture_kind
  - kind-builder
  - p03_sp__builder_builder
  - bld_collaboration_validation_schema
  - _builder-builder
  - bld_instruction_builder
  - bld_architecture_builder
  - p10_lr_kind_builder
  - bld_collaboration_kind
---

# Domain Knowledge: _builder (meta)

## Executive Summary

The meta-builder is the factory that produces other builders. It operates one abstraction level above regular builders: while a knowledge-card-builder produces knowledge_cards, the _builder-builder produces the builders themselves. Every builder in the system was either directly generated or validated against the meta-builder's templates and quality gates.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P02 (agent/builder identity) |
| Output kind | type_builder (any) |
| Required files per builder | MANIFEST, SYSTEM_PROMPT, KNOWLEDGE, INSTRUCTIONS, SCHEMA, EXAMPLES, QUALITY_GATES, CONFIG, ARCHITECTURE, TOOLS, OUTPUT_TEMPLATE, MEMORY, COLLABORATION |
| Meta-file prefix | META_ (e.g., META_MANIFEST.md) |
| llm_function | BECOME (builders assume specialist identity) |
| Naming | {type_name}-builder (kebab-case) |
| Min builder files | 7 (MANIFEST + SYSTEM_PROMPT + KNOWLEDGE + INSTRUCTIONS + SCHEMA + EXAMPLES + QUALITY_GATES) |
| Max builder files | 13 (full complement) |

## Patterns

- **Template-driven generation**: META_ files are fill-in templates with {{variables}} that produce concrete builder files when instantiated with a target type's schema
- **Schema-first**: always read the target type's _schema.yaml before writing any builder file — the schema is the single source of truth for fields, constraints, and validation
- **Capability extraction**: derive builder capabilities directly from the target schema's field count, required fields, and validation rules
- **Boundary mapping**: every builder must explicitly name 3-5 sibling types it does NOT handle, sourced from the same pillar's taxonomy
- **Routing keywords**: 4-8 terms that a user would literally type when searching for this builder via semantic search
- **Crew role pattern**: one question the builder answers + explicit exclusion list

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Generic capabilities ("can help with anything") | No routing signal; brain search returns noise |
| Missing boundary section | Builders overlap, producing wrong artifact types |
| Copy-paste from another builder | Domain knowledge is wrong; validation gates don't match |
| Skipping schema read | Field counts, constraints, and validation rules drift from truth |
| Over-scoping (>8 capabilities) | Builder tries to do too much; split into two builders |

## Application

1. Read META_MANIFEST.md template and target type's _schema.yaml
2. Instantiate each META_ file by replacing {{variables}} with concrete values
3. Validate: field counts match schema, boundary types are real siblings, routing keywords are specific
4. Quality gate: all 13 files present, no template residue ({{...}}), density >= 0.80

## References

- CEX archetype system: archetypes/builders/_builder-builder/META_*.md (13 templates)
- Builder pattern: Gang of Four, applied to LLM artifact production
- Meta-programming: code that writes code, adapted to prompt-driven artifact systems

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_builder]] | downstream | 0.51 |
| [[bld_architecture_kind]] | downstream | 0.45 |
| [[kind-builder]] | downstream | 0.42 |
| [[p03_sp__builder_builder]] | downstream | 0.41 |
| [[bld_collaboration_validation_schema]] | downstream | 0.39 |
| [[_builder-builder]] | downstream | 0.38 |
| [[bld_instruction_builder]] | downstream | 0.37 |
| [[bld_architecture_builder]] | downstream | 0.37 |
| [[p10_lr_kind_builder]] | downstream | 0.37 |
| [[bld_collaboration_kind]] | downstream | 0.36 |
