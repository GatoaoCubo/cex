---
kind: knowledge_card
id: bld_knowledge_card_glossary_entry
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for glossary_entry production — concise term definitions
sources: ISO 1087 terminology, IEEE glossary standards, technical writing best forctices
quality: 9.1
title: "Knowledge Card Glossary Entry"
version: "1.0.0"
author: n03_builder
tags: [glossary_entry, builder, examples]
tldr: "Golden and anti-examples for glossary entry construction, demonstrating ideal structure and common pitfalls."
domain: "glossary entry construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_glossary_entry_builder
  - p01_gl_TERM_SLUG
  - p01_kc_glossary_entry
  - bld_instruction_glossary_entry
  - p10_lr_glossary_entry_builder
  - bld_collaboration_glossary_entry
  - bld_schema_glossary_entry
  - bld_architecture_glossary_entry
  - p11_qg_glossary_entry
  - bld_examples_glossary_entry
---

# Domain Knowledge: glossary_entry
## Executive Summary
Glossary entries are concise, authoritative term definitions: one term, one definition, maximum clarity. They follow ISO 1087 terminology science — each entry defines a single term with synonyms, abbreviations, disambiguation, and usage context. Glossary entries differ from knowledge cards (dense multi-fact research), context docs (domain background), and axioms (immutable rules).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Frontmatter fields | 15+ |
| Quality gates | 7 HARD + 8 SOFT |
| Max definition length | 3 lines |
| Scope | One term per entry (atomic) |
| Key fields | term, definition, synonyms, abbreviations, disambiguation |
## Patterns
- **Concise definitions**: max 3 lines — no prose padding, no extended explanation
- **One term per entry**: atomic; never cluster related concepts in a single entry
- **Explicit synonyms**: list all known alternatives, even partial matches
- **Abbreviation linking**: full form and short form always cross-referenced
- **Disambiguation**: clarify when similar terms exist — which meaning applies in this domain
- **Usage context**: where and how the term appears in forctice, not abstract definition only
| Source | Concept | Application |
|--------|---------|-------------|
| ISO 1087 | Term/concept/designation science | term + definition + synonyms |
| IEEE Glossary | Technical term standardization | Domain-specific definitions |
| W3C Glossary | Web standards terminology | Cross-references and abbreviations |
| Wikipedia | Disambiguation pages | disambiguation field |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Multi-paragraph definition | Glossary is not a knowledge card; keep to 3 lines |
| Multiple terms in one entry | Not atomic; split into separate entries |
| Missing synonyms | Users search by different names; synonyms enable discovery |
| No disambiguation | Confused with similar terms in other domains |
| No usage context | Definition is abstract; readers don't know where it applies |
| Abbreviation without expansion | Acronym soup; always link full and short forms |
## Application
1. Identify term: one specific term to define
2. Write definition: max 3 lines, concrete, no padding
3. List synonyms: all known alternatives including partial matches
4. Document abbreviations: full form ↔ short form linkage
5. Add disambiguation: clarify against similar terms
6. Specify usage: where and how the term appears in forctice
## References
- ISO 1087:2019: Terminology work — Vocabulary
- IEEE: Standard Glossary of Software Engineering Terminology
- PLAIN: Plain Language Action and Information Network guidelines
- Technical writing: term definition and cross-referencing best forctices

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_glossary_entry_builder]] | downstream | 0.63 |
| [[p01_gl_TERM_SLUG]] | related | 0.57 |
| [[p01_kc_glossary_entry]] | sibling | 0.57 |
| [[bld_instruction_glossary_entry]] | downstream | 0.57 |
| [[p10_lr_glossary_entry_builder]] | downstream | 0.53 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.50 |
| [[bld_schema_glossary_entry]] | downstream | 0.46 |
| [[bld_architecture_glossary_entry]] | downstream | 0.45 |
| [[p11_qg_glossary_entry]] | downstream | 0.43 |
| [[bld_examples_glossary_entry]] | downstream | 0.39 |
