---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a chain
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: chain

```yaml
---
id: p03_ch_{{pipeline_slug}}
kind: chain
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
steps_count: {{integer_matching_body}}
flow: {{sequential|branching|parallel|mixed}}
input_format: "{{what_first_step_receives}}"
output_format: "{{what_last_step_produces}}"
context_passing: {{full|filtered|summary}}
error_strategy: {{fail_fast|skip|retry|fallback}}
domain: "{{domain_value}}"
quality: null
tags: [chain, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
---
```

## Purpose
{{why_this_chain_exists_2_to_4_sentences}}

## Steps

### Step 1: {{step_name}}
- **Input**: {{input_type_and_description}}
- **Prompt**: {{what_this_step_does}}
- **Output**: {{output_type_and_description}}

### Step 2: {{step_name}}
- **Input**: {{receives_from_step_1}}
- **Prompt**: {{what_this_step_does}}
- **Output**: {{output_type_and_description}}

{{...repeat for steps_count steps}}

## Data Flow
```text
{{step_1}} --{{data_type}}--> {{step_2}} --{{data_type}}--> {{step_N}}
```
Context passing: {{context_passing_strategy_description}}

## Error Handling
- **Strategy**: {{error_strategy}}
- **On failure at step N**: {{failure_behavior}}
- **Retry policy**: {{retry_details_if_applicable}}

## References
- {{reference_1}}
- {{reference_2}}
