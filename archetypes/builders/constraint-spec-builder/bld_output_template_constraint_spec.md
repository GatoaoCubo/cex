---
kind: output_template
id: bld_output_template_constraint_spec
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a constraint_spec artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: constraint_spec
```yaml
id: p03_constraint_{{slug}}
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
constraint_type: "{{constraint_type}}}}"
pattern: "{{pattern}}}}"
quality: null
tags: [constraint_spec, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
provider_compat: "{{provider_compat}}}}"
fallback: "{{fallback}}}}"
temperature_override: "{{temperature_override}}}}"
max_tokens: "{{max_tokens}}}}"
```
## Overview
`{{overview_content}}`
## Constraint Definition
`{{constraint_definition_content}}`
## Provider Compatibility
`{{provider_compatibility_content}}`
## Integration
`{{integration_content}}`

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
| Domain | constraint spec construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
