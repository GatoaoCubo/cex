---
kind: output_template
id: bld_output_template_lens
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a lens
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Lens"
version: "1.0.0"
author: n03_builder
tags: [lens, builder, examples]
tldr: "Golden and anti-examples for lens construction, demonstrating ideal structure and common pitfalls."
domain: "lens construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: lens
```yaml
id: p02_lens_{{perspective_slug}}
kind: lens
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
perspective: "{{perspective_name}}"
applies_to: [{{kind_1}}, {{kind_2}}]
focus: "{{what_this_lens_emphasizes}}"
filters: [{{filter_1}}, {{filter_2}}]
bias: "{{declared_directional_bias_or_null}}"
interpretation: "{{how_this_lens_reads_artifacts}}"
weight: {{float_0_to_1}}
priority: {{integer}}
scope: "{{boundaries_of_perspective}}"
domain: "{{domain_value}}"
quality: null
tags: [lens, {{domain_tag}}, {{perspective_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Perspective
`{{what_this_lens_sees_and_emphasizes}}`
## Filters
`{{specific_attributes_highlighted_or_suppressed}}`
## Application
`{{how_to_apply_this_lens_to_artifacts}}`
## Limitations
`{{what_this_lens_misses_or_de_emphasizes}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | lens construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
