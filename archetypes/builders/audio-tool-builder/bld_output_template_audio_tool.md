---
kind: output_template
id: bld_output_template_audio_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an audio_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Audio Tool"
version: "1.0.0"
author: n03_builder
tags: [audio_tool, builder, examples]
tldr: "Golden and anti-examples for audio tool construction, demonstrating ideal structure and common pitfalls."
domain: "audio tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: audio_tool
```yaml
id: p04_audio_{{capability_slug}}
kind: audio_tool
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_tool_name}}"
direction: {{input|output|analysis|bidirectional}}
models:
  - {{model_id_1}}
  - {{model_id_2}}
formats:
  - {{mp3|wav|ogg|flac|webm|m4a|aac|pcm}}
languages:
  - {{bcp47_code_1}}
  - {{bcp47_code_2}}
quality: null
tags: [audio_tool, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_tool_does_max_200ch}}"
sample_rate: {{16000|22050|44100|8000}}
max_duration: {{seconds_int}}
streaming: {{true|false}}
word_timestamps: {{true|false}}
voice_id: "{{default_voice_id_for_tts_or_omit}}"
provider: "{{primary_provider_name}}"
```
## Overview
`{{what_the_tool_does_1_to_2_sentences}}`
`{{who_uses_it_and_primary_use_case}}`
## Direction
`{{direction_processing_flow}}`
`{{input_payload_description}}` -> {{model_processing_step}} -> `{{output_payload_description}}`
`{{streaming_note_if_applicable}}`
## Models
| Model | Provider | Accuracy | Latency | Cost |
|-------|----------|----------|---------|------|
| `{{model_id_1}}` | `{{provider_1}}` | {{high|medium|low}} | {{<1s|1-5s|5-30s}} | {{$x/min}} |
| `{{model_id_2}}` | `{{provider_2}}` | {{high|medium|low}} | {{<1s|1-5s|5-30s}} | {{$x/min}} |
## Formats
| Format | Input | Output | Notes |
|--------|-------|--------|-------|
| `{{format_1}}` | {{yes|-}} | {{yes|-}} | `{{format_note}}` |
| `{{format_2}}` | {{yes|-}} | {{yes|-}} | `{{format_note}}` |
## Languages
| Code | Language | `{{model_id_1}}` | `{{model_id_2}}` |
|------|----------|----------------|----------------|
| `{{bcp47_1}}` | `{{language_name_1}}` | {{high|medium|low}} | {{high|medium|low}} |
| `{{bcp47_2}}` | `{{language_name_2}}` | {{high|medium|low}} | {{high|medium|low}} |
