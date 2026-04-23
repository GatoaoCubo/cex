---
kind: instruction
id: bld_instruction_glossary_entry
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for glossary_entry
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Glossary Entry"
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
  - p01_kc_glossary_entry
  - bld_knowledge_card_glossary_entry
  - p01_gl_TERM_SLUG
  - bld_instruction_context_doc
  - bld_instruction_action_prompt
  - bld_instruction_golden_test
  - bld_instruction_memory_scope
  - p10_lr_glossary_entry_builder
  - bld_collaboration_glossary_entry
---

# Instructions: How to Produce a glossary_entry
## Phase 1: CLASSIFY
1. Identify the term to define — what single word or phrase needs a precise definition?
2. Determine domain context — in which domain or system does this term carry its specific meaning?
3. Check for existing definitions of the same term — avoid duplicating or contradicting an existing entry
4. List synonyms and abbreviations — what other names or short forms does this term go by?
5. Identify potential confusion with similar terms — which nearby terms could be mistaken for this one?
6. Find canonical usage examples — where in the codebase, documentation, or domain is this term used correctly?
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all 15+ required fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: all 15+ fields, null is acceptable for optional fields, quality: null (never self-score)
4. Write Term section: the exact term being defined, including casing and any abbreviation form
5. Write Definition section: maximum 3 lines, precise and unambiguous, no filler or aspirational language
6. Write Synonyms section: alternative names and abbreviations, even if only one exists
7. Write Context section: the domain where this definition applies and any scope restrictions
8. Write Related Terms section: linked terms for navigation to nearby concepts
9. Write Usage Example section: one sentence showing correct usage of the term in context
10. Check body size — must stay at or below 1024 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p01_ge_[a-z][a-z0-9_]+`
   - [ ] kind == `glossary_entry`
   - [ ] quality == null
   - [ ] definition is 3 lines or fewer
   - [ ] term is a single concept (not a phrase defining a whole domain)
   - [ ] at least 1 synonym or abbreviation listed
   - [ ] body <= 1024 bytes
3. SOFT gates: tldr <= 160 chars, tags >= 3, usage example present, related terms linked
4. Cross-check: single term not deep knowledge (that is knowledge_card)? Not domain overview (that is context_doc)? Not an embedding configuration? Definition is precise not aspirational?
5. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify glossary
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | glossary entry construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_glossary_entry_builder]] | related | 0.47 |
| [[p01_kc_glossary_entry]] | upstream | 0.41 |
| [[bld_knowledge_card_glossary_entry]] | upstream | 0.41 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.41 |
| [[bld_instruction_context_doc]] | sibling | 0.41 |
| [[bld_instruction_action_prompt]] | sibling | 0.38 |
| [[bld_instruction_golden_test]] | sibling | 0.38 |
| [[bld_instruction_memory_scope]] | sibling | 0.37 |
| [[p10_lr_glossary_entry_builder]] | downstream | 0.36 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.36 |
