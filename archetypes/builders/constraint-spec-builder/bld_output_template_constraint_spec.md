---
kind: output_template
id: bld_output_template_constraint_spec
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a constraint_spec artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{overview_content}}
## Constraint Definition
{{constraint_definition_content}}
## Provider Compatibility
{{provider_compatibility_content}}
## Integration
{{integration_content}}

