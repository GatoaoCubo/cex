---
kind: output_template
id: bld_output_template_memory_summary
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a memory_summary artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: memory_summary
```yaml
id: p10_ms_{{summary_slug}}
kind: memory_summary
pillar: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_summary_name}}"
source_type: {{conversation|session|multi_session|document}}
compression_method: {{abstractive|extractive|hybrid|sliding_window}}
quality: null
tags: [memory_summary, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
max_tokens: {{integer_max_output_tokens}}
trigger: {{token_threshold|turn_count|explicit|time_based}}
source_window: {{integer_messages_or_turns}}
retain_entities: {{true|false}}
retain_timestamps: {{true|false}}
freshness_decay: {{float_0_to_1}}
description: "{{what_this_summary_captures_max_200ch}}"
```
## Overview
`{{what_this_summary_does_1_to_2_sentences}}`
`{{when_it_triggers_and_what_scope_it_covers}}`
## Compression
Method: {{abstractive|extractive|hybrid|sliding_window}}
Ratio: `{{input_tokens}}`:{{output_tokens}} (approx `{{compression_ratio}}`x)
Preserved: `{{list_what_is_kept}}`
Dropped: `{{list_what_is_discarded}}`
## Trigger
Condition: `{{trigger_condition_description}}`
Threshold: {{numeric_threshold — tokens, turns, or time}}
On fire: `{{what_happens_when_trigger_activates}}`
## Retention
Entities: {{retained|discarded}} — `{{entity_types_kept}}`
Decisions: {{retained|discarded}} — `{{decision_format}}`
Action items: {{retained|discarded}} — `{{action_item_format}}`
Timestamps: {{retained|discarded}} — `{{temporal_marker_format}}`

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
| Domain | memory summary construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
