---
kind: schema
id: bld_schema_audio_tool
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for audio_tool
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Audio Tool"
version: "1.0.0"
author: n03_builder
tags: [audio_tool, builder, examples]
tldr: "Golden and anti-examples for audio tool construction, demonstrating ideal structure and common pitfalls."
domain: "audio tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_vision_tool
  - bld_schema_cli_tool
  - bld_schema_search_tool
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_constraint_spec
  - bld_schema_action_prompt
  - bld_schema_handoff_protocol
  - bld_schema_golden_test
---

# Schema: audio_tool
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_audio_{capability_slug}) | YES | - | Namespace compliance |
| kind | literal "audio_tool" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable tool name |
| direction | enum: input, output, analysis, bidirectional | YES | - | Audio processing direction |
| models | list[string], len >= 1 | YES | - | Supported audio models |
| formats | list[enum: mp3, wav, ogg, flac, webm, m4a, aac, pcm] | YES | - | Accepted/produced audio formats |
| languages | list[string (BCP-47)], len >= 1 | YES | - | Supported languages |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "audio_tool" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the tool does |
| sample_rate | int (Hz) | REC | 16000 | Default sample rate |
| max_duration | int (seconds) | REC | 300 | Maximum audio duration |
| streaming | boolean | REC | false | Supports real-time streaming |
| voice_id | string | REC | - | Default voice for TTS output |
| word_timestamps | boolean | REC | false | Returns per-word timing |
| provider | string | REC | - | Primary API provider |
## ID Pattern
Regex: `^p04_audio_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the tool does, use case, direction
2. `## Direction` — input (STT), output (TTS), analysis, or bidirectional — with processing flow
3. `## Models` — each supported model with provider, accuracy tier, latency, cost tier
4. `## Formats` — input/output format compatibility matrix
5. `## Languages` — supported languages with BCP-47 codes and quality tier per model
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_audio_{capability_slug}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- models list MUST match model names defined in ## Models section
- direction must be one of: input, output, analysis, bidirectional
- quality: null always
- formats must be subset of allowed enum values
- languages must use BCP-47 codes (en, pt-BR, es-MX, fr, de, ja, zh)
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_vision_tool]] | sibling | 0.63 |
| [[bld_schema_cli_tool]] | sibling | 0.62 |
| [[bld_schema_search_tool]] | sibling | 0.61 |
| [[bld_schema_retriever_config]] | sibling | 0.60 |
| [[bld_schema_output_validator]] | sibling | 0.60 |
| [[bld_schema_unit_eval]] | sibling | 0.60 |
| [[bld_schema_constraint_spec]] | sibling | 0.59 |
| [[bld_schema_action_prompt]] | sibling | 0.59 |
| [[bld_schema_handoff_protocol]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.59 |
