---
kind: output_template
id: bld_output_template_handoff_protocol
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a handoff_protocol artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Handoff Protocol"
version: "1.0.0"
author: n03_builder
tags: [handoff_protocol, builder, examples]
tldr: "Golden and anti-examples for handoff protocol construction, demonstrating ideal structure and common pitfalls."
domain: "handoff protocol construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_handoff_protocol
  - bld_instruction_handoff_protocol
  - bld_output_template_runtime_rule
  - bld_output_template_output_validator
  - bld_output_template_input_schema
  - p03_sp_handoff_protocol_builder
  - bld_output_template_feature_flag
  - bld_schema_handoff_protocol
  - bld_output_template_hook_config
  - bld_output_template_constraint_spec
---

# Output Template: handoff_protocol
```yaml
id: p02_handoff_{{slug}}
kind: handoff_protocol
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
trigger: "{{trigger}}}}"
context_passed: "{{context_passed}}}}"
return_contract: "{{return_contract}}}}"
quality: null
tags: [handoff_protocol, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
source_agent: "{{source_agent}}}}"
target_agent: "{{target_agent}}}}"
timeout: "{{timeout}}}}"
retry_policy: "{{retry_policy}}}}"
escalation: "{{escalation}}}}"
```
## Overview
`{{overview_content}}`
## Trigger
`{{trigger_content}}`
## Context Transfer
`{{context_transfer_content}}`
## Return Contract
`{{return_contract_content}}`

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
| Domain | handoff protocol construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_handoff_protocol]] | downstream | 0.44 |
| [[bld_instruction_handoff_protocol]] | upstream | 0.41 |
| [[bld_output_template_runtime_rule]] | sibling | 0.38 |
| [[bld_output_template_output_validator]] | sibling | 0.38 |
| [[bld_output_template_input_schema]] | sibling | 0.38 |
| [[p03_sp_handoff_protocol_builder]] | upstream | 0.37 |
| [[bld_output_template_feature_flag]] | sibling | 0.37 |
| [[bld_schema_handoff_protocol]] | downstream | 0.36 |
| [[bld_output_template_hook_config]] | sibling | 0.36 |
| [[bld_output_template_constraint_spec]] | sibling | 0.35 |
