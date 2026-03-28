---
kind: output_template
id: bld_output_template_lens
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a lens
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_this_lens_sees_and_emphasizes}}
## Filters
{{specific_attributes_highlighted_or_suppressed}}
## Application
{{how_to_apply_this_lens_to_artifacts}}
## Limitations
{{what_this_lens_misses_or_de_emphasizes}}
## References
- {{reference_1}}
- {{reference_2}}
