---
kind: output_template
id: bld_output_template_personality
pillar: P05
llm_function: PRODUCE
purpose: Canonical output template for personality artifacts
quality: 9.1
title: "Output Template: personality"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, output-template, P05, hermes_origin]
tldr: "Full template for personality artifact with frontmatter + 6-section body. Variables: name, register, verbosity, humor, values, examples."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_output_template_enum_def
  - p06_enum_def
  - bld_output_template_input_schema
  - n06_schema_brand_voice_contract
  - p03_ins_prompt_template
  - p01_kc_mental_model
  - bld_examples_tts_provider
  - p01_kc_brand_voice_consistency_channels
  - bld_output_template_function_def
---

# Output Template: personality

## Full Artifact Template

```markdown
---
id: per_{{name}}
kind: personality
title: "Personality: {{name}}"
name: {{name}}
voice:
  register: {{register}}        # formal | casual | technical | playful
  verbosity: {{verbosity}}      # terse | balanced | verbose
  humor: {{humor}}              # off | dry | warm
values:
  - {{value_1}}
  - {{value_2}}
  - {{value_3}}
  # optional: value_4, value_5 (max 5)
tone_examples:
  - "{{example_1}}"
  - "{{example_2}}"
  - "{{example_3}}"
  # add more as needed
anti_patterns:
  - "{{anti_1}}"
  - "{{anti_2}}"
  - "{{anti_3}}"
  # add more as needed
activation_cue: "/personality {{name}}"
deactivation_cue: "/personality default"
hot_swap_compatible: true
version: 1.0.0
quality: null
tags: [personality, hermes_origin, hot_swap, {{domain_tag}}]
tldr: "{{one-line description under 160 chars}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
---

## Voice Profile
| Dimension | Value | Notes |
|-----------|-------|-------|
| Register | {{register}} | {{register_notes}} |
| Verbosity | {{verbosity}} | {{verbosity_notes}} |
| Humor | {{humor}} | {{humor_notes}} |

## Values
- **{{value_1}}**: {{value_1_rationale}}
- **{{value_2}}**: {{value_2_rationale}}
- **{{value_3}}**: {{value_3_rationale}}

## Tone Examples
1. "{{example_1}}" -- {{context_1}}
2. "{{example_2}}" -- {{context_2}}
3. "{{example_3}}" -- {{context_3}}

## Anti-Patterns
1. "{{anti_1}}" -- {{reason_1}}
2. "{{anti_2}}" -- {{reason_2}}
3. "{{anti_3}}" -- {{reason_3}}

## Activation
- **activation_cue**: /personality {{name}}
- **deactivation_cue**: /personality default
- **hot_swap_compatible**: true

## Related Personalities
| Persona | Contrast |
|---------|----------|
| {{sibling_1}} | {{contrast_1}} |
```

## Variable Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{name}}` | Persona slug (snake_case, <= 30 chars) | researcher |
| `{{register}}` | Voice register enum | technical |
| `{{verbosity}}` | Verbosity enum | verbose |
| `{{humor}}` | Humor enum | dry |
| `{{value_1..5}}` | Core value (3-5 required) | epistemic_rigor |
| `{{example_1..N}}` | Verbatim sample phrase (>= 3) | "Based on evidence..." |
| `{{anti_1..N}}` | Forbidden phrase (>= 3) | "Everyone knows..." |
| `{{domain_tag}}` | Domain keyword tag | academic |

## Size Budget
Target: 800-2000 bytes. Hard max: 3072 bytes.
If over budget: reduce tone_examples to 3, anti_patterns to 3, values to 3.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_enum_def]] | sibling | 0.26 |
| [[p06_enum_def]] | downstream | 0.22 |
| [[bld_output_template_input_schema]] | sibling | 0.18 |
| [[n06_schema_brand_voice_contract]] | downstream | 0.16 |
| [[p03_ins_prompt_template]] | upstream | 0.16 |
| [[p01_kc_mental_model]] | upstream | 0.16 |
| [[bld_examples_tts_provider]] | downstream | 0.16 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.16 |
| [[bld_output_template_function_def]] | sibling | 0.16 |
