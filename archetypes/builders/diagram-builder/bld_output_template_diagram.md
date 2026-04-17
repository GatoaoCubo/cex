---
kind: output_template
id: bld_output_template_diagram
pillar: P00
quality: 9.0
title: "Output Template Diagram"
version: "1.0.0"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
---
id: p08_diag_`{{scope_slug}}`
kind: diagram
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "`{{who_produced}}`"
domain: "`{{domain}}`"
quality: null
tags: [`{{tag_1}}`, {{tag_2}}, `{{tag_3}}`]
tldr: "`{{dense_summary_max_160ch}}`"
scope: "`{{what_system_or_subsystem}}`"
notation: "{{ascii|mermaid}}"
zoom_level: "{{system|subsystem|component}}"
components: [`{{component_1}}`, {{component_2}}, `{{component_3}}`]
connections: [`{{connection_1}}`, `{{connection_2}}`]
layers: [`{{layer_1}}`, `{{layer_2}}`]
annotations: [`{{annotation_1}}`, `{{annotation_2}}`]
keywords: [`{{keyword_1}}`, {{keyword_2}}, `{{keyword_3}}`]
---

## Scope
`{{what_is_visualized_and_boundaries}}`
## Diagram
``{{notation}}`
{{the_actual_diagram}}
```
## Legend
`{{symbol_and_arrow_explanations}}`
## Components
| Component | Role | Layer |
|-----------|------|-------|
| `{{component_1}}` | {{role_1}} | `{{layer_1}}` |
| `{{component_2}}` | {{role_2}} | `{{layer_2}}` |
## Connections
| From | To | Type | Data |
|------|-----|------|------|
| `{{from_1}}` | {{to_1}} | {{type_1}} | `{{data_1}}` |
| `{{from_2}}` | {{to_2}} | {{type_2}} | `{{data_2}}` |
## Annotations
`{{non_obvious_design_decisions}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks
