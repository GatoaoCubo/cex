---
kind: output_template
id: bld_output_template_glossary_entry
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a glossary_entry
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
usage: "{{how_the_term_is_used_in_practice}}"
quality: null
tags: [glossary, {{domain_tag}}, {{term_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Definition
{{concise_definition_1_to_3_lines}}
## Usage
{{where_and_how_this_term_appears_in_practice}}
## Disambiguation
{{how_this_term_differs_from_commonly_confused_terms}}
## Related Terms
- {{related_term_1}}: {{brief_relation}}
- {{related_term_2}}: {{brief_relation}}
## References
- {{reference_1}}
- {{reference_2}}
