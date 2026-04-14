---
kind: output_template
id: bld_output_template_compression_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a compression_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: compression_config
```yaml
id: p10_cc_{{name}}
kind: compression_config
pillar: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
strategy: {{summarize|truncate_oldest|rolling_window|priority_keep|tiered}}
trigger_ratio: {{0.50_to_0.99}}
preserve_types:
  - system_prompt
  - {{preserved_type_2}}
  - {{preserved_type_3}}
max_summary_tokens: {{positive_integer}}
min_context_tokens: {{positive_integer}}
decay_weights:
  system_prompt: 1.0
  tool_definition: 1.0
  {{message_type_3}}: {{0.0_to_1.0}}
  {{message_type_4}}: {{0.0_to_1.0}}
target_ratio: {{0.30_to_0.80}}
quality: null
tags: [compression_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_config_covers_max_200ch}}"
scope: "{{agent_or_system_scope}}"
tier_count: {{N_if_tiered}}
```
## Strategy Specification
`{{primary_strategy_description_and_rationale}}`
Trigger: `{{trigger_ratio}}` of context window. Target: `{{target_ratio}}` after compression.
`{{why_this_strategy_fits_the_target_agent}}`
## Preserve Types
- system_prompt: `{{why_preserved}}`
- `{{type_2}}`: `{{why_preserved}}`
- `{{type_3}}`: `{{why_preserved}}`
## Decay Weights
| Message Type | Base Priority | Age Decay | Rationale |
|-------------|--------------|-----------|-----------|
| system_prompt | 1.00 | 0.00 | `{{rationale}}` |
| `{{type}}` | {{priority}} | {{decay}} | `{{rationale}}` |
| `{{type}}` | {{priority}} | {{decay}} | `{{rationale}}` |
## Compression Pipeline
1. **`{{Stage 1 name}}`** (target: -{{N}}%): `{{description}}`
2. **`{{Stage 2 name}}`** (target: -{{N}}%): `{{description}}`
3. **`{{Stage 3 name}}`** (target: remaining): `{{description}}`
## References
- `{{reference_1}}`
- `{{reference_2}}`
