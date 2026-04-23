---
kind: output_template
id: bld_output_template_dispatch_rule
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a dispatch_rule
pattern: every field here exists in SCHEMA.md; template derives, never invents
quality: 9.0
title: "Output Template Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_dispatch_rule
  - dispatch-rule-builder
  - p03_sp_dispatch_rule_builder
  - p11_qg_dispatch_rule
  - bld_schema_dispatch_rule
  - bld_instruction_dispatch_rule
  - bld_examples_dispatch_rule
  - bld_architecture_dispatch_rule
  - bld_collaboration_dispatch_rule
  - bld_tools_dispatch_rule
---

# Output Template: dispatch_rule
Naming pattern: `p12_dr_{scope}.yaml`
Filename: `p12_dr_{{scope}}.yaml`
```yaml
id: p12_dr_{{scope}}
kind: dispatch_rule
pillar: P12

version: 1.0.0
created: {{ISO_8601_date}}
updated: {{ISO_8601_date}}
author: {{author_slug}}

domain: {{domain_name}}
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{agent_group_slug}}]
tldr: {{one_line_summary_max_120_chars}}

scope: {{scope_slug}}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
agent_group: {{agent_group_slug}}
model: {{sonnet|opus|haiku|flash}}

priority: {{1_to_10}}
confidence_threshold: {{0.0_to_1.0}}
fallback: {{fallback_agent_group_slug}}
conditions: {{object_or_omit}}

load_balance: {{true|false_or_omit}}
routing_strategy: {{keyword_match|semantic|hybrid_or_omit}}
# {{scope}} Dispatch Rule
## Purpose
{{one_paragraph_explaining_what_this_rule_routes_and_why}}
## Keyword Rationale
{{brief_explanation_of_why_these_keywords_trigger_this_agent_group}}
## Fallback Logic
{{brief_explanation_of_when_fallback_fires_and_what_it_handles}}
```
## Derivation Notes
1. All frontmatter fields derive from SCHEMA.md required or optional fields
2. Omit `conditions`, `load_balance`, `routing_strategy` if not needed
3. Body sections are human commentary only; routing logic lives in frontmatter
4. `quality: null` must never be changed at authoring time
5. `fallback` must be a different agent_group slug than `agent_group`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | dispatch rule construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_dispatch_rule]] | downstream | 0.44 |
| [[dispatch-rule-builder]] | downstream | 0.43 |
| [[p03_sp_dispatch_rule_builder]] | upstream | 0.38 |
| [[p11_qg_dispatch_rule]] | downstream | 0.37 |
| [[bld_schema_dispatch_rule]] | downstream | 0.35 |
| [[bld_instruction_dispatch_rule]] | upstream | 0.34 |
| [[bld_examples_dispatch_rule]] | downstream | 0.32 |
| [[bld_architecture_dispatch_rule]] | downstream | 0.31 |
| [[bld_collaboration_dispatch_rule]] | downstream | 0.29 |
| [[bld_tools_dispatch_rule]] | upstream | 0.29 |
