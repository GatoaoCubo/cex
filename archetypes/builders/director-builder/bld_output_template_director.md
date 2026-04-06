---
kind: output_template
id: bld_output_template_director
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for director artifact production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: director
```yaml
id: ex_director_{{topic_slug}}
kind: director
pillar: P08
title: "{{human_readable_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
topic: "{{mission_domain_scope}}"
builders: [{{builder_1}}, {{builder_2}}, {{builder_3_if_needed}}]
dispatch_mode: {{sequential_or_parallel_or_conditional}}
signal_check: {{true_or_false}}
wave_topology:
  - wave: 1
    builders: [{{wave_1_builders}}]
    gate: "{{signal_gate_name}}"
  - wave: 2
    builders: [{{wave_2_builders}}]
    gate: "{{signal_gate_name}}"
fallback_per_builder:
  {{builder_1}}: {{retry_or_skip_or_substitute_or_abort}}
  {{builder_2}}: {{retry_or_skip_or_substitute_or_abort}}
llm_function: ORCHESTRATE
domain: "{{primary_domain}}"
quality: null
tags: [director, {{domain}}, {{topic}}, orchestration, P08]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.85_to_1.00}}
```
## Identity
{{director_name}} coordinates a {{N}}-builder mission for {{mission_goal}}.
{{two_sentences_coordination_strategy_and_wave_rationale}}
## Builders
| Builder | Nucleus | Role |
|---------|---------|------|
| {{builder_1}} | {{nucleus}} | {{role_in_mission}} |
| {{builder_2}} | {{nucleus}} | {{role_in_mission}} |
## Wave Topology
Wave 1: {{wave_1_builders}} -> {{signal_gate_1}}
Wave 2: {{wave_2_builders}} -> {{signal_gate_2}}
{{additional_waves_if_needed}}
## Dispatch Config
Mode: {{dispatch_mode}}. Signal check: {{signal_check}}. Timeout: {{seconds}}s per wave.
Fallback: {{builder_1}}: {{action}}; {{builder_2}}: {{action}}.
## Routing
- Triggers: {{trigger_phrase_1}}, {{trigger_phrase_2}}
- Keywords: {{keyword_1}}, {{keyword_2}}, {{keyword_3}}
- NOT when: {{exclusion_1}}, {{exclusion_2}}
## Footer
version: {{version}} | author: {{author}} | quality: null
