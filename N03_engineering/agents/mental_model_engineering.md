---
id: p02_mm_builder_nucleus
kind: mental_model
pillar: P02
title: Mental Model -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [mental-model, builder, N03, routing, decision]
tldr: Decision logic for builder -- intent classification, builder selection, crew composition, cost optimization.
density_score: 0.88
---

# Mental Model: Builder Nucleus

## Decision Tree



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
