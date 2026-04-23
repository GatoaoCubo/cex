---
kind: schema
id: bld_schema_instruction
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for instruction
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 2.0.0
quality: 9.1
title: "Schema Instruction"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_action_prompt
  - bld_schema_system_prompt
  - bld_schema_smoke_eval
  - bld_schema_unit_eval
  - bld_schema_workflow
  - bld_schema_golden_test
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_input_schema
---

# Schema: instruction (v2)
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_ins_{task_slug}) | YES | - | Namespace compliance. Regex: `^p03_ins_[a-z][a-z0-9_]+$` |
| kind | literal "instruction" | YES | - | Type integrity — invariant |
| pillar | literal "P03" | YES | - | Pillar assignment — invariant |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable instruction name |
| target | string | YES | - | Who executes this (agent or role) |
| phases_count | integer (3-5) | YES | - | Number of phases in body. Universal: Analyze -> Generate -> Validate |
| prerequisites | list[string] | YES | - | Verifiable prerequisites ("Python 3.10+" not "environment ready") |
| validation_method | enum: checklist, automated, manual, none | YES | "checklist" | How to verify success |
| domain | string | YES | - | Domain this instruction belongs to |
| quality | null | YES | null | Never self-score — invariant |
| tags | list[string], len >= 3 | YES | - | Must include "instruction" |
| idempotent | boolean | REC | false | Safe to re-run? KNOWLEDGE: principle of re-execution |
| atomic | boolean | REC | true | All-or-nothing execution? |
| rollback | string or null | REC | null | How to undo (required if atomic: false) |
| dependencies | list[string] | REC | [] | Tools/files/services required |
| logging | boolean | REC | true | Log execution steps? |
| tldr | string <= 160ch | REC | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density metric |
**Required count**: 15 | **Recommended count**: 7
## ID Pattern
Regex: `^p03_ins_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Context` — Background, input/output contracts. Define every variable: `$var_name (required|optional) - type - "description"`. 15-20% of doc.
2. `## Phases` — 3-5 phased execution steps. Universal pattern: `Analyze -> Generate -> Validate`. Each phase: atomic (one action), verifiable. Include pseudocode for complex logic. 40-50% of doc — this is the core.
3. `## Output Contract` — Exact deliverable format with `{{variables}}`. Literal template, not prose description. 5-10% of doc.
4. `## Validation` — Quality gates with numeric thresholds. Checklist format. 8-12% of doc.
5. `## Metacognition` (recommended) — "Does / Does NOT" block + chaining: `[upstream] -> THIS -> [downstream]`. Prevents scope creep.
## Size Calibration
| Metric | CEX Builders | Real task prompts | Limit |
|--------|-------------|-----------|-------|
| Avg body bytes | 1,924 | 14,538 | - |
| Max body bytes | 3,711 | 41,974 | - |
| Median body bytes | - | 12,311 | - |
| **max_bytes** | **8,192** | exceeds (complex) | **8,192** |
| Body tokens | 3,000-3,500 | varies | ~6,000 |
| Phases | 4-5 | 3-5 | 5 |
| Input vars | 4-5 | 3-6 | 6 |
> **Note**: max_bytes raised from 4096 to 8192. KNOWLEDGE sweet spot is 3-4KB body but real instructions median at 12KB. 8KB covers dense CEX format with margin for complex multi-phase instructions. P03 _schema.yaml maps instruction as user_prompt (max 2048B) — this schema supersedes for instruction-specific artifacts.
## Constraints
- max_bytes: 8192 (body only)
- naming: p03_ins_{task_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- phases_count MUST match actual count of `## Phase N` sections in body
- Each phase MUST have exactly one primary action (no compound steps)
- Prerequisites MUST be verifiable (not vague)
- Input contract MUST define every variable with type + required/optional + default

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_action_prompt]] | sibling | 0.60 |
| [[bld_schema_system_prompt]] | sibling | 0.57 |
| [[bld_schema_smoke_eval]] | sibling | 0.56 |
| [[bld_schema_unit_eval]] | sibling | 0.56 |
| [[bld_schema_workflow]] | sibling | 0.56 |
| [[bld_schema_golden_test]] | sibling | 0.56 |
| [[bld_schema_retriever_config]] | sibling | 0.56 |
| [[bld_schema_handoff_protocol]] | sibling | 0.55 |
| [[bld_schema_output_validator]] | sibling | 0.55 |
| [[bld_schema_input_schema]] | sibling | 0.55 |
