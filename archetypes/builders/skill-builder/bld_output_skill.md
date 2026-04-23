---
kind: output_template
id: bld_output_template_skill
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a skill
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Skill"
version: "1.0.0"
author: n03_builder
tags: [skill, builder, examples]
tldr: "Golden and anti-examples for skill construction, demonstrating ideal structure and common pitfalls."
domain: "skill construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_input_schema
  - bld_output_template_feature_flag
  - bld_collaboration_skill
  - bld_output_template_golden_test
  - bld_output_template_runtime_rule
  - bld_output_template_output_validator
  - bld_schema_skill
  - bld_output_template_hook_config
  - bld_knowledge_card_skill
  - bld_output_template_embedding_config
---

# Output Template: skill
```yaml
id: p04_skill_{{name}}
kind: skill
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_name}}"
description: "{{one_line_capability_max_120ch}}"
user_invocable: {{true|false}}
trigger: "{{slash_command_or_keyword_or_event}}"
phases:
  - "{{phase_1_name}}"
  - "{{phase_2_name}}"
  - "{{phase_3_name}}"
when_to_use:
  - "{{condition_1}}"
  - "{{condition_2}}"
when_not_to_use:
  - "{{exclusion_1}}"
  - "{{exclusion_2}}"
examples:
  - "{{invocation_example_1}}"
  - "{{invocation_example_2}}"
quality: null
references_dir: "{{optional_path_or_omit}}"
sub_skills: ["{{optional_skill_id_or_omit}}"]
platforms: ["{{optional_platform_or_omit}}"]
stack_default: "{{optional_stack_or_omit}}"
```
## Purpose
`{{what_capability_this_provides}}`
`{{why_it_exists_as_a_skill_not_agent_or_prompt}}`
## Workflow Phases

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
| Domain | skill construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_input_schema]] | sibling | 0.41 |
| [[bld_output_template_feature_flag]] | sibling | 0.37 |
| [[bld_collaboration_skill]] | downstream | 0.36 |
| [[bld_output_template_golden_test]] | sibling | 0.36 |
| [[bld_output_template_runtime_rule]] | sibling | 0.36 |
| [[bld_output_template_output_validator]] | sibling | 0.36 |
| [[bld_schema_skill]] | downstream | 0.36 |
| [[bld_output_template_hook_config]] | sibling | 0.35 |
| [[bld_knowledge_card_skill]] | upstream | 0.35 |
| [[bld_output_template_embedding_config]] | sibling | 0.34 |
