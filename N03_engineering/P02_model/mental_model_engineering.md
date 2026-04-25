---
id: p02_mm_builder_nucleus
kind: mental_model
8f: F4_reason
pillar: P02
title: Mental Model -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [mental-model, builder, N03, routing, decision]
tldr: "N03 decision logic: 7 routing rules (direct 8F, motor resolve, nucleus bootstrap, kind register, batch forge, diagnostic, feedback edit), 8-step temperature map (0.0 for deterministic, 0.3 for planning, 0.7 for generation), 4-step crew selection for multi-kind intents."
density_score: 0.88
related:
  - p08_pat_builder_construction
  - p02_agent_builder_nucleus
  - bld_architecture_kind
  - bld_collaboration_kind
  - agent_card_engineering_nucleus
  - bld_schema_kind
  - p06_if_builder_nucleus
  - kind-builder
  - bld_instruction_kind
  - p03_sp_builder_nucleus
---

# Mental Model: Builder Nucleus

## Decision Tree

```
User Intent
  |
  +-- Contains explicit kind name? ──YES──> Direct 8F (cex_8f_runner.py)
  |                                          |
  |                                          +-- Kind exists in kinds_meta.json? ──NO──> Error: suggest closest
  |
  +-- Contains "scaffold/bootstrap nucleus"? ──YES──> cex_nucleus_builder.py (P3 Bootstrap)
  |
  +-- Contains "register/new kind"? ──YES──> cex_kind_register.py (taxonomy expansion)
  |
  +-- Contains "batch/forge/all"? ──YES──> cex_forge.py (parallel multi-artifact)
  |
  +-- Contains "check/health/doctor"? ──YES──> cex_doctor.py (diagnostic, not a build)
  |
  +-- General build intent ──> cex_8f_motor.py (resolve kind from natural language)
       |
       +-- Motor resolves 1 kind ──> Direct 8F
       +-- Motor resolves 2+ kinds ──> Crew selection (see below)
       +-- Motor resolves 0 kinds ──> GDP fallback: ask user to clarify
```

## Routing Rules

| Signal | Route | Tool |
|--------|-------|------|
| create a {{kind}} | Direct 8F, single kind | cex_8f_runner.py |
| build {{thing}} for {{domain}} | Motor resolve + 8F | cex_8f_motor.py + runner |
| scaffold nucleus N0x | Multi-kind sequential | cex_nucleus_builder.py |
| register new kind {{name}} | Taxonomy expansion | cex_kind_register.py |
| check health | Diagnostic | cex_doctor.py |
| batch build {{list}} | Parallel multi-artifact | cex_forge.py |
| update {{artifact}} with {{feedback}} | Feedback-driven edit | cex_feedback.py |

## Temperature Map

| Step | Temp | Reason |
|------|------|--------|
| F1 CONSTRAIN | 0.0 | Schema lookup deterministic |
| F2 BECOME | 0.0 | Builder loading deterministic |
| F3 INJECT | 0.0 | KC retrieval deterministic |
| F4 REASON | 0.3 | Planning benefits from creativity |
| F5 CALL | 0.0 | Tool listing deterministic |
| F6 PRODUCE | 0.7 | Content generation needs creativity |
| F7 GOVERN | 0.0 | Validation deterministic |
| F8 COLLABORATE | 0.0 | Save/compile/index deterministic |

## Crew Selection

When Motor resolves 2+ kinds:
1. Match exact crew name from 235 pre-defined (bld_collaboration_*.md)
2. If no exact match, find crew with > 60% kind overlap
3. If no crew, compose ad-hoc: sort by dependency, build sequentially
4. Rule: never build a kind that depends on an unbuilt kind

## State

| Variable | Type | Purpose |
|----------|------|---------|
| current_kind | string | Kind being built now |
| current_step | F1-F8 | Active pipeline step |
| retry_count | int | Retries on current artifact (max 2) |
| quality_score | float | Last gate result |
| crew_queue | list | Remaining kinds in crew |
| built_artifacts | list | Paths built this session |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_builder_construction]] | downstream | 0.31 |
| [[p02_agent_builder_nucleus]] | related | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.27 |
| [[bld_collaboration_kind]] | downstream | 0.26 |
| [[agent_card_engineering_nucleus]] | related | 0.25 |
| [[bld_schema_kind]] | downstream | 0.25 |
| [[p06_if_builder_nucleus]] | downstream | 0.24 |
| [[kind-builder]] | downstream | 0.24 |
| [[bld_instruction_kind]] | downstream | 0.23 |
| [[p03_sp_builder_nucleus]] | downstream | 0.23 |
