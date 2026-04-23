---
kind: schema
id: bld_schema_multi_modal_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for multi_modal_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Multi Modal Config"
version: "1.0.0"
author: n03_builder
tags: [multi_modal_config, builder, examples]
tldr: "Golden and anti-examples for multi modal config construction, demonstrating ideal structure and common pitfalls."
domain: "multi modal config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_vision_tool
  - bld_schema_smoke_eval
  - bld_schema_constraint_spec
  - bld_schema_unit_eval
  - bld_schema_agent_card
  - bld_schema_prompt_version
---

# Schema: multi_modal_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_mmc_{slug}) | YES | — | Namespace compliance |
| kind | literal "multi_modal_config" | YES | — | Type integrity |
| pillar | literal "P04" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| title | string | YES | — | Human-readable config name |
| supported_modalities | list[enum] | YES | [image, text] | image/audio/video/document |
| image_max_resolution | string | REC | 2048x2048 | WxH pixel limit |
| image_format | list[string] | REC | [png, jpg, webp] | Accepted image formats |
| audio_format | list[string] | REC | [mp3, wav] | Accepted audio formats |
| audio_max_duration_s | int | REC | 600 | Max audio seconds |
| video_max_duration_s | int | REC | 60 | Max video seconds |
| preprocessing | list[string] | REC | [] | resize/compress/transcribe |
| routing_model | map | REC | {} | Modality → model mapping |
| token_cost_estimate | map | REC | {} | Modality → token cost |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "multi_modal_config" |
| tldr | string <= 160ch | YES | — | Dense summary |
## ID Pattern
Regex: `^p04_mmc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Supported Modalities` — table of modality → format → limits
2. `## Preprocessing Pipeline` — steps per modality before LLM call
3. `## Routing Map` — which model handles which modality
4. `## Token Cost Estimates` — per-modality token costs for budget
5. `## Fallback Chain` — what happens when a modality isn't supported
## Constraints
- max_bytes: 2048
- naming: p04_mmc_{capability}.yaml
- supported_modalities values: image, audio, video, document, text
- image_max_resolution format: WxH (e.g., 2048x2048)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.62 |
| [[bld_schema_vision_tool]] | sibling | 0.62 |
| [[bld_schema_smoke_eval]] | sibling | 0.62 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
| [[bld_schema_unit_eval]] | sibling | 0.61 |
| [[bld_schema_agent_card]] | sibling | 0.61 |
| [[bld_schema_prompt_version]] | sibling | 0.61 |
