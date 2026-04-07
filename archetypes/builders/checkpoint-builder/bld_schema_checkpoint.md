---
kind: schema
id: bld_schema_checkpoint
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for checkpoint
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: checkpoint
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_ck_{slug}) | YES | - | Namespace compliance |
| kind | literal "checkpoint" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable checkpoint name |
| workflow_ref | string | YES | - | ID of the workflow this checkpoint belongs to |
| step | string | YES | - | Which step in the workflow this checkpoint captures |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "checkpoint" |
| tldr | string <= 160ch | YES | - | Dense summary |
| state | map | REC | - | Serialized state at this point (keys, types, sizes) |
| resumable | boolean | REC | true | Can workflow resume from here |
| ttl | string | REC | - | Time to live: "24h", "7d", "30d" |
| parent_checkpoint | string | REC | - | ID of previous checkpoint in chain |
| retry_count | integer | REC | 0 | How many times this step has been retried |
| error | string or null | REC | null | Error message if step failed |
| description | string <= 200ch | REC | - | What this checkpoint captures |
## ID Pattern
Regex: `^p12_ck_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what workflow state this checkpoint captures
2. `## State` — serialized state keys, types, sizes
3. `## Resume` — how to resume from this checkpoint, prerequisites
4. `## Lifecycle` — TTL, cleanup, archival policy
## Constraints
- max_bytes: 2048 (body only — workflow state can be dense)
- naming: p12_ckpt_{workflow}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- workflow_ref MUST reference a valid workflow artifact id
- quality: null always
- NO raw state data in body — schema/shape only, not values
