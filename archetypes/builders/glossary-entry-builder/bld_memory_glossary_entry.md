---
id: p10_lr_glossary_entry_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Glossary definitions longer than 3 lines consistently contain content that belongs in a knowledge_card — they start adding context, history, and operational steps. Synonyms field written as a string rather than a list fails schema validation. Empty synonyms list violates the minimum-one-synonym requirement. Terms capitalized when not proper nouns signal the author is treating the glossary as documentation rather than a definitional reference. Disambiguation notes absent from terms with near-identical names cause cross-pillar confusion downstream."
pattern: "Definition max 3 lines: line 1 defines the term, line 2 gives concrete scope or example, line 3 disambiguates from the most-confused related term. Synonyms is always a list with at least one entry. Term field is lowercase unless a proper noun. Abbreviation entries must expand the abbreviation on line 1 before defining it. Cross-pillar terms include a disambiguation note naming which pillar owns each interpretation. Depth beyond 3 lines signals the content should be a knowledge_card."
evidence: "11 glossary entries reviewed. Entries exceeding 3 lines required content to be m..."
confidence: 0.70
outcome: SUCCESS
domain: glossary_entry
tags: [glossary_entry, disambiguation, conciseness, synonyms, definition_discipline, cross_pillar]
tldr: "3-line max definition; synonyms as list; lowercase term; always disambiguate from the most-confused neighbor."
impact_score: 7.0
decay_rate: 0.04
agent_group: edison
keywords: [glossary, definition, synonym, abbreviation, disambiguation, conciseness, term, cross_pillar, knowledge_card]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Glossary Entry"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_glossary_entry
  - p01_kc_glossary_entry
  - p03_sp_glossary_entry_builder
  - bld_instruction_glossary_entry
  - p01_gl_TERM_SLUG
  - bld_manifest_memory_type
  - bld_examples_glossary_entry
  - p11_qg_glossary_entry
  - bld_collaboration_glossary_entry
  - bld_schema_glossary_entry
---
## Summary
A glossary entry defines one term in 3 lines maximum. Line 1 states what it is. Line 2 scopes it or gives a concrete example. Line 3 disambiguates it from the term most commonly confused with it. Anything beyond 3 lines is a knowledge_card, not a glossary entry.
## Pattern
1. `term` field is lowercase unless the term is a proper noun or established abbreviation.
2. `definition` is at most 3 lines. No bullet points, no sections, no operational steps.
3. Structure: line 1 = what it is; line 2 = concrete scope or example; line 3 = "Not to be confused with [X], which [distinction]."
4. `synonyms` is always a YAML list with at least one entry. If no synonyms exist, invent the nearest alias used in conversation.
5. Abbreviation entries: line 1 expands the abbreviation, then defines it. Example: "RAG — Retrieval-Augmented Generation. A technique..."
6. Cross-pillar terms must name which pillar owns each interpretation in the disambiguation line.
7. If the definition requires more than 3 lines to be accurate, create a knowledge_card instead and reference it.
## Anti-Pattern
1. Definition exceeding 3 lines — depth beyond 3 lines signals knowledge_card territory.
2. Adding sections (## Usage, ## Examples, ## History) — that is knowledge_card (P01), not glossary.
3. Including operational steps ("to use X, first do Y then Z") — that is an instruction (P03).
4. `synonyms: "also known as X"` — synonyms must be a list: `synonyms: [X, Y]`.
5. `synonyms: []` — empty list violates minimum-one requirement.
6. Capitalizing common nouns in the term field: `term: "Quality Gate"` should be `term: "quality gate"`.
7. Omitting disambiguation — terms like "chain", "pipeline", "workflow" exist across multiple pillars and must be disambiguated.
## Context
Applies when: defining a term that appears in artifact metadata, documentation, or conversation and needs a single authoritative definition.
Does not apply when: the term requires historical context, usage examples, or operational guidance — use knowledge_card.

## Builder Context

This ISO operates within the `glossary-entry-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_glossary_entry_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_glossary_entry_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | glossary_entry |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_glossary_entry]] | upstream | 0.46 |
| [[p01_kc_glossary_entry]] | upstream | 0.45 |
| [[p03_sp_glossary_entry_builder]] | upstream | 0.44 |
| [[bld_instruction_glossary_entry]] | upstream | 0.43 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.43 |
| [[bld_manifest_memory_type]] | upstream | 0.36 |
| [[bld_examples_glossary_entry]] | upstream | 0.36 |
| [[p11_qg_glossary_entry]] | downstream | 0.36 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.36 |
| [[bld_schema_glossary_entry]] | upstream | 0.34 |
