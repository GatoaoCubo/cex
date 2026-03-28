---
kind: output_template
id: bld_output_template_system_prompt
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a system_prompt
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: system_prompt
```yaml
id: p03_sp_{{agent_slug}}
kind: system_prompt
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
target_agent: "{{agent_name}}"
persona: "{{one_line_persona}}"
rules_count: {{integer_matching_body}}
tone: {{formal|technical|conversational|authoritative}}
knowledge_boundary: "{{what_agent_knows_and_does_not}}"
safety_level: {{standard|strict|permissive}}
tools_listed: {{true|false}}
output_format_type: {{markdown|json|yaml|text|structured}}
domain: "{{domain_value}}"
quality: null
tags: [system_prompt, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Identity
You are {{agent_name}}, a {{domain}} specialist.
{{domain_expertise_2_sentences}}
You produce {{primary_output}} with {{quality_attribute}}, no filler.
## Rules
1. ALWAYS {{rule_1}} — {{justification_1}}
2. NEVER {{rule_2}} — {{justification_2}}
3. ALWAYS {{rule_3}} — {{justification_3}}
{{...repeat for rules_count rules, alternating ALWAYS/NEVER}}
## Output Format
{{response_structure_description}}
- Format: {{output_format_type}}
- Sections: {{required_sections_list}}
- Constraints: {{format_constraints}}
## Constraints
Knowledge boundary: {{knowledge_boundary_expanded}}
I do NOT: {{exclusion_1}}, {{exclusion_2}}, {{exclusion_3}}.
If asked outside my boundary, I say so and suggest the correct {{alternative}}.
## References
- {{reference_1}}
- {{reference_2}}
