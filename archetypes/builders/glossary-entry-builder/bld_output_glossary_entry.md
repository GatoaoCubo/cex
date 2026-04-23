---
kind: output_template
id: bld_output_template_glossary_entry
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a glossary_entry
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Glossary Entry"
version: "1.0.0"
author: n03_builder
tags: [glossary_entry, builder, examples]
tldr: "Golden and anti-examples for glossary entry construction, demonstrating ideal structure and common pitfalls."
domain: "glossary entry construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_glossary_entry
  - bld_schema_glossary_entry
  - bld_instruction_glossary_entry
  - bld_knowledge_card_glossary_entry
  - bld_config_glossary_entry
  - bld_architecture_glossary_entry
  - p01_gl_TERM_SLUG
  - p01_kc_glossary_entry
  - glossary-entry-builder
  - p11_qg_glossary_entry
---

# Output Template: glossary_entry
```yaml
id: p01_gl_{{term_slug}}
kind: glossary_entry
pillar: P01

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

term: "{{the_term}}"
definition: "{{concise_definition_max_3_lines}}"
synonyms: [{{synonym_1}}, {{synonym_2}}]
abbreviation: "{{abbrev_or_null}}"

domain: "{{domain_where_term_is_used}}"
domain_specific: "{{cex_specific_meaning_or_null}}"
context: "{{where_this_term_appears}}"
disambiguation: "{{how_differs_from_similar_terms_or_null}}"

related_terms: [{{related_1}}, {{related_2}}]
usage: "{{how_the_term_is_used_in_forctice}}"
quality: null
tags: [glossary, {{domain_tag}}, {{term_tag}}]

tldr: "{{dense_summary_max_160ch}}"
```
## Definition
`{{concise_definition_1_to_3_lines}}`
## Usage
`{{where_and_how_this_term_appears_in_forctice}}`
## Disambiguation
`{{how_this_term_differs_from_commonly_confused_terms}}`
## Related Terms
1. `{{related_term_1}}`: `{{brief_relation}}`
2. `{{related_term_2}}`: `{{brief_relation}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
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
| [[bld_examples_glossary_entry]] | downstream | 0.42 |
| [[bld_schema_glossary_entry]] | downstream | 0.36 |
| [[bld_instruction_glossary_entry]] | upstream | 0.36 |
| [[bld_knowledge_card_glossary_entry]] | upstream | 0.35 |
| [[bld_config_glossary_entry]] | downstream | 0.35 |
| [[bld_architecture_glossary_entry]] | downstream | 0.34 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.33 |
| [[p01_kc_glossary_entry]] | upstream | 0.33 |
| [[glossary-entry-builder]] | upstream | 0.33 |
| [[p11_qg_glossary_entry]] | downstream | 0.33 |
