---
kind: schema
id: bld_schema_computer_use
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for computer_use
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Computer Use"
version: "1.0.0"
author: n03_builder
tags: [computer_use, builder, examples]
tldr: "Golden and anti-examples for computer use construction, demonstrating ideal structure and common pitfalls."
domain: "computer use construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_action_prompt
  - bld_schema_constraint_spec
  - bld_schema_unit_eval
  - bld_schema_cli_tool
  - bld_schema_vision_tool
  - bld_schema_golden_test
---

# Schema: computer_use

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_cu_{target_slug}) | YES | - | Namespace compliance |
| kind | literal "computer_use" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable tool name |
| target | enum: desktop, browser, mobile, terminal | YES | - | Target environment |
| resolution | string (WxH format) | YES | - | Screen resolution defining coordinate space |
| actions_supported | list[enum], len >= 1 | YES | - | click, type, scroll, key_press, drag, double_click, screenshot |
| coordinate_system | enum: absolute, relative | REC | absolute | Coordinate reference system |
| screenshot_mode | enum: before_action, on_demand, continuous | REC | before_action | When screenshots are captured |
| safety_constraints | list[string] | REC | - | Restrictions (no credentials, sandbox only) |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "computer_use" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the tool does |
## ID Pattern
Regex: `^p04_cu_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this controls, use case, observe-act loop description
2. `## Actions` — each supported action with parameters and behavior
3. `## Coordinate System` — resolution, origin, coordinate format
4. `## Safety` — restrictions, sandboxing requirements, credential policy
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_cu_{target_slug}.md + .yaml (compiled)
- machine_format: yaml (compiled artifact)
- id == filename stem
- actions_supported MUST be non-empty
- resolution MUST be WxH format (e.g., "1024x768")
- quality: null always
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.62 |
| [[bld_schema_memory_scope]] | sibling | 0.62 |
| [[bld_schema_action_prompt]] | sibling | 0.62 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
| [[bld_schema_unit_eval]] | sibling | 0.61 |
| [[bld_schema_cli_tool]] | sibling | 0.61 |
| [[bld_schema_vision_tool]] | sibling | 0.61 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
