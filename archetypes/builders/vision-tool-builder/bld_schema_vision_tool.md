---
kind: schema
id: bld_schema_vision_tool
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for vision_tool
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Vision Tool"
version: "1.0.0"
author: n03_builder
tags: [vision_tool, builder, examples]
tldr: "Golden and anti-examples for vision tool construction, demonstrating ideal structure and common pitfalls."
domain: "vision tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_cli_tool
  - bld_schema_retriever_config
  - bld_schema_action_prompt
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_golden_test
  - bld_schema_search_tool
  - bld_schema_smoke_eval
---

# Schema: vision_tool
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_vision_{capability_slug}) | YES | - | Namespace compliance |
| kind | literal "vision_tool" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable tool name |
| input_types | list[enum: base64, url, file_path, buffer, screenshot] | YES | - | Accepted visual input formats |
| capabilities | list[string], len >= 1 | YES | - | What the tool can detect/extract |
| output_format | enum: json, text, table | YES | json | Primary output format |
| providers | list[string] | YES | - | Supported vision API providers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "vision_tool" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the tool does |
| max_resolution | string | REC | - | Maximum input resolution e.g. "4096x4096" |
| supported_formats | list[enum: png, jpg, jpeg, webp, gif, bmp, tiff, pdf] | REC | - | Accepted image file formats |
| confidence_threshold | float 0.0-1.0 | REC | 0.8 | Minimum confidence for results |
| batch_support | boolean | REC | false | Supports multiple images per call |
| max_bytes_per_image | integer | REC | - | Max image payload size in bytes |
## ID Pattern
Regex: `^p04_vision_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the tool does, use case, who uses it
2. `## Input Types` — each accepted input type with format details and size limits
3. `## Capabilities` — each capability with description, confidence, and examples
4. `## Output Format` — structured output schema with field descriptions
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_vision_{capability_slug}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- capabilities list MUST match capability names in ## Capabilities section
- quality: null always
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_cli_tool]] | sibling | 0.66 |
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_action_prompt]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_unit_eval]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_golden_test]] | sibling | 0.63 |
| [[bld_schema_search_tool]] | sibling | 0.63 |
| [[bld_schema_smoke_eval]] | sibling | 0.63 |
