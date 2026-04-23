---
kind: schema
id: bld_schema_context_file
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for context_file
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 1.0.0
quality: 8.9
title: "Schema: context_file"
author: n03_builder
tags: [context_file, builder, schema, P06, hermes_origin]
tldr: "Formal field definitions for context_file: scope, injection_point, inheritance_chain, priority, applies_to_nuclei."
domain: "workspace instruction auto-injection"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.93
related:
  - bld_schema_system_prompt
  - bld_schema_workflow
  - bld_schema_golden_test
  - bld_schema_action_prompt
  - bld_schema_smoke_eval
  - bld_schema_instruction
  - bld_schema_input_schema
  - bld_schema_runtime_state
  - bld_schema_unit_eval
  - bld_schema_memory_scope
---

# Schema: context_file (v1)

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string `ctx_[a-z][a-z0-9_]+` | YES | - | Regex: `^ctx_[a-z][a-z0-9_]+$`; must equal filename stem |
| kind | literal "context_file" | YES | - | Type integrity invariant |
| pillar | literal "P03" | YES | - | Pillar assignment invariant |
| title | string | YES | - | Human-readable scope description |
| scope | enum: workspace\|nucleus\|session\|global | YES | - | Coverage domain |
| injection_point | enum: session_start\|every_turn\|f3_inject | YES | - | When injected into context |
| inheritance_chain | list[string] | YES | [] | Parent context_file IDs; empty = root |
| max_bytes | integer | YES | 8192 | Body size budget |
| priority | integer >= 0 | YES | 0 | Load order: 0 = highest priority |
| applies_to_nuclei | list | YES | [all] | `[all]` or explicit nucleus IDs |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| quality | null | YES | null | Never self-score -- invariant |
| tags | list[string], len >= 3 | YES | - | Must include scope name and `hermes_origin` |
| created | date YYYY-MM-DD | REC | - | Creation date |
| updated | date YYYY-MM-DD | REC | - | Last update |
| author | string | REC | - | Producer identity |
| tldr | string <= 160ch | REC | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density metric |

**Required count**: 13 | **Recommended count**: 5

## ID Pattern
Regex: `^ctx_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
Examples: `ctx_engineering_workspace`, `ctx_n03_nucleus`, `ctx_sprint_42_session`

## Scope Enum
| Value | Coverage | When to use |
|-------|---------|-------------|
| `global` | All sessions, all nuclei, all workspaces | System-wide standards that never change |
| `workspace` | All nuclei in one project directory | Per-repo CLAUDE.md equivalent |
| `nucleus` | One nucleus across all sessions | Per-nucleus build conventions |
| `session` | Current session only (auto-expires) | Sprint context, temporary constraints |

## Injection Point Enum
| Value | Behavior | Token cost |
|-------|---------|-----------|
| `session_start` | Injected once when session opens; stays in context | Pay once per session |
| `every_turn` | Re-injected at each user message | High cost; for compliance-critical rules only |
| `f3_inject` | Loaded explicitly during F3 INJECT of 8F pipeline | On-demand; lowest cost |

## Body Structure (required sections)
1. One or more rule sections with `##` headings (e.g., `## Build Rules`, `## Commit Rules`)
2. Each section: numbered or bulleted instruction list
3. No facts or domain knowledge (that is knowledge_card)
4. No `{{vars}}` placeholders (that is prompt_template)
5. No step-by-step procedural recipes (that is instruction kind)

## Size Calibration
| Metric | Value |
|--------|-------|
| max_bytes | 8192 (body only) |
| Recommended body | 200-4096 bytes |
| Density target | >= 0.85 |
| Sections | 1-8 instruction sections |

## Constraints
- max_bytes: 8192 (body only, CEX artifacts)
- naming: `{{scope}}_context.md`
- id MUST equal filename stem
- id MUST match `^ctx_[a-z][a-z0-9_]+$`
- quality: null always -- invariant
- Body: instructions only; no facts, no vars, no procedural recipes
- inheritance_chain: MUST be valid existing context_file IDs or empty
- priority: MUST be non-negative integer; 0 = most authoritative
- applies_to_nuclei: MUST be `[all]` or valid nucleus IDs from n01-n07

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_system_prompt]] | sibling | 0.52 |
| [[bld_schema_workflow]] | sibling | 0.51 |
| [[bld_schema_golden_test]] | sibling | 0.51 |
| [[bld_schema_action_prompt]] | sibling | 0.50 |
| [[bld_schema_smoke_eval]] | sibling | 0.50 |
| [[bld_schema_instruction]] | sibling | 0.49 |
| [[bld_schema_input_schema]] | sibling | 0.49 |
| [[bld_schema_runtime_state]] | sibling | 0.49 |
| [[bld_schema_unit_eval]] | sibling | 0.49 |
| [[bld_schema_memory_scope]] | sibling | 0.49 |
