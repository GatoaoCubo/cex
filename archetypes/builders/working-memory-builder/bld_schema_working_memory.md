---
kind: schema
id: bld_schema_working_memory
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for working_memory
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: null
title: "Schema Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, schema]
tldr: "Frontmatter + body schema for working_memory: task_id, context_slots, capacity, expiry, clear policy."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Schema: working_memory

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_wm_{slug}) | YES | - | Namespace compliance |
| kind | literal "working_memory" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| task_id | string | YES | - | Task instance this memory binds to |
| context_slots | map[string, type_string] | YES | - | Slot names with declared types |
| capacity_limit | {value: int, unit: tokens|slots} | YES | - | Max working memory size |
| expiry | string (TTL or trigger) | YES | - | When this memory is cleared |
| clear_on_complete | enum: clear, promote | YES | - | Post-task disposal policy |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "working_memory" |
| tldr | string <= 160ch | YES | - | Dense summary |
| promote_targets | list[string] | REC | - | Memory kinds to promote slots to (if clear_on_complete: promote) |
| nucleus | string | REC | - | Which nucleus owns this working memory |
| description | string <= 200ch | REC | - | What task this serves |

## ID Pattern
Regex: `^p10_wm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` -- what task this serves, why working memory is needed
2. `## Context Slots` -- table: slot_name, type, purpose, example_value
3. `## Capacity and Expiry` -- capacity limit, expiry trigger, rationale
4. `## Clear Policy` -- what happens on task completion (discard or promote)

## Context Slot Types
| Type | Example Values | Notes |
|------|---------------|-------|
| string | "current_step", "last_output" | Text state |
| int | "retry_count", "step_index" | Counter state |
| float | "confidence", "progress" | Numeric state |
| list[string] | "accumulated_results" | Collection state |
| bool | "is_complete", "has_error" | Flag state |
| json | "intermediate_data" | Structured state |

## Constraints
- max_bytes: 3072
- naming: p10_wm_{scope}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- context_slots MUST have >= 1 slot
- task_id MUST be non-empty
- expiry MUST be declared
- quality: null always
