---
kind: output_template
id: bld_output_template_axiom
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an axiom
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: axiom
```yaml
id: p10_ax_{{slug}}
kind: axiom
pillar: P10

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

domain: "{{domain}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"

rule: "{{axiom_statement_one_sentence}}"
scope: "{{where_it_applies}}"
rationale: "{{why_immutable}}"
enforcement: "{{how_violations_detected}}"

immutable: true
priority: {{1_to_10}}
dependencies: [{{dep_axiom_1}}]
keywords: [{{kw_1}}, {{kw_2}}, {{kw_3}}]

linked_artifacts:
  primary: {{primary_or_null}}
  related: [{{related_1}}]
```
## Rule Statement
`{{axiom_in_one_clear_sentence}}`
## Rationale
1. `{{reason_1_why_immutable}}`
2. `{{reason_2_why_immutable}}`
3. `{{reason_3_why_immutable}}`
## Scope
1. Domain: `{{domain_where_applies}}`
2. System: `{{system_boundary}}`
3. Layer: `{{architectural_layer}}`
## Enforcement
1. Detection: `{{how_to_detect_violation}}`
2. Response: `{{what_happens_on_violation}}`
## Examples
1. `{{case_where_axiom_holds_1}}`
2. `{{case_where_axiom_holds_2}}`
## Violations
1. `{{known_or_hypothetical_breach}}`
   - Impact: `{{what_breaks}}`
   - Resolution: `{{how_to_restore}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | axiom construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
