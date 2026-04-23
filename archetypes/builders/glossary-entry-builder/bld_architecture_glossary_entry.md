---
kind: architecture
id: bld_architecture_glossary_entry
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of glossary_entry — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Glossary Entry"
version: "1.0.0"
author: n03_builder
tags: [glossary_entry, builder, examples]
tldr: "Golden and anti-examples for glossary entry construction, demonstrating ideal structure and common pitfalls."
domain: "glossary entry construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_glossary_entry
  - p03_sp_glossary_entry_builder
  - bld_knowledge_card_glossary_entry
  - p11_qg_glossary_entry
  - bld_instruction_glossary_entry
  - p01_gl_TERM_SLUG
  - context-doc-builder
  - bld_architecture_context_doc
  - bld_schema_glossary_entry
  - bld_examples_glossary_entry
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| term | The canonical name of the domain concept being defined | glossary_entry | required |
| definition | Concise explanation of the term; max 3 lines | glossary_entry | required |
| domain | Subject area that scopes the term's meaning | glossary_entry | required |
| synonyms | Alternative names or abbreviations for the same concept | glossary_entry | optional |
| related_terms | Other glossary entries that share conceptual proximity | glossary_entry | optional |
| disambiguation | Clarification when the term overlaps with a similar concept | glossary_entry | conditional |
| usage_context | Short note on where or how the term appears in forctice | glossary_entry | optional |
## Dependency Graph
```
knowledge_card (P01) --produces--> glossary_entry
glossary_entry       --produces--> system_prompt (P03)
glossary_entry       --produces--> context_doc (P01)
knowledge_index (P10)    --depends-->  glossary_entry
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | glossary_entry | produces | source concepts requiring concise term definitions |
| glossary_entry | system_prompt (P03) | data_flow | term definitions injected for LLM terminology grounding |
| glossary_entry | context_doc (P01) | data_flow | term references embedded in domain context documents |
| knowledge_index (P10) | glossary_entry | depends | indexes entries for fast lookup and semantic search |
## Boundary Table
| glossary_entry IS | glossary_entry IS NOT |
|-------------------|-----------------------|
| A short definition of one domain term (max 3 lines) | A deep knowledge distillation with density scoring |
| The smallest knowledge unit — single-term scope | A context document explaining a full domain or system |
| A lookup artifact for quick terminology reference | An input/output demonstration pair for format teaching |
| Allowed to list synonyms and related terms | A naming convention rule that enforces identifier patterns |
| Scoped to one term with optional disambiguation | An immutable operational rule that governs system behavior |
| Indexed for search and referenced by other knowledge artifacts | An evaluation artifact with quality scores or assertions |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Source | knowledge_card (P01) | Provide source concepts that need term-level definitions |
| Core | term, definition, domain | The essential triad — name, meaning, and scope |
| Enrichment | synonyms, related_terms, disambiguation, usage_context | Improve discoverability and reduce ambiguity |
| Index | knowledge_index (P10) | Make the entry searchable across the knowledge system |
| Consumption | system_prompt (P03), context_doc (P01) | Inject terminology into LLM context and domain documents |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_glossary_entry]] | upstream | 0.54 |
| [[p03_sp_glossary_entry_builder]] | upstream | 0.50 |
| [[bld_knowledge_card_glossary_entry]] | upstream | 0.43 |
| [[p11_qg_glossary_entry]] | downstream | 0.42 |
| [[bld_instruction_glossary_entry]] | upstream | 0.42 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.39 |
| [[context-doc-builder]] | upstream | 0.39 |
| [[bld_architecture_context_doc]] | sibling | 0.38 |
| [[bld_schema_glossary_entry]] | upstream | 0.38 |
| [[bld_examples_glossary_entry]] | upstream | 0.37 |
