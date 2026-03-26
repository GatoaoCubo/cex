---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for instruction
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: instruction

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_ins_{task_slug}) | YES | - | Namespace compliance |
| kind | literal "instruction" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable instruction name |
| target | string | YES | - | Who executes this (agent or role) |
| steps_count | integer | YES | - | Number of steps in body |
| prerequisites | list[string] | YES | - | What must be true before starting |
| validation_method | enum: checklist, automated, manual, none | YES | "checklist" | How to verify success |
| idempotent | boolean | YES | - | Safe to re-run? |
| atomic | boolean | YES | - | All-or-nothing execution? |
| rollback | string or null | REC | null | How to undo (required if atomic: false) |
| dependencies | list[string] | REC | [] | Tools/files/services required |
| logging | boolean | REC | true | Log execution steps? |
| domain | string | YES | - | Domain this instruction belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "instruction" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |

## ID Pattern
Regex: `^p03_ins_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Prerequisites` — what must be true before starting
2. `## Steps` — numbered step-by-step procedure (one action per step)
3. `## Validation` — how to verify the instruction succeeded
4. `## Rollback` — how to undo if execution fails midway

## Constraints
- max_bytes: 4096 (body only)
- naming: p03_ins_{task_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- steps_count MUST match actual numbered steps in body
- Each step MUST have exactly one action (no compound steps)
- Prerequisites MUST be verifiable (not vague)
- quality: null always
- instruction defines HOW to execute — no identity (system_prompt) or I/O spec (action_prompt)
