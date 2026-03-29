---
kind: output_template
id: bld_output_template_output_validator
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a output_validator artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: output_validator
```yaml
id: p05_oval_{{slug}}
kind: output_validator
pillar: P05
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
checks: "{{checks}}}}"
on_fail: "{{on_fail}}}}"
quality: null
tags: [output_validator, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
retry_count: "{{retry_count}}}}"
fix_prompt: "{{fix_prompt}}}}"
severity: "{{severity}}}}"
applies_to: "{{applies_to}}}}"
```
## Overview
{{overview_content}}
## Checks
{{checks_content}}
## Failure Actions
{{failure_actions_content}}
## Integration
{{integration_content}}

