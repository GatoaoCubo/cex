---
id: p10_ax_scout_before_create
kind: axiom
8f: F4_reason
pillar: P10
title: "Axiom: Scout Before Create (Law 8)"
version: 3.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.1
tags: [axiom, scout, law8, discovery, pool]
tldr: "LAW 8: Always Glob/Grep before Write. Never duplicate pool artifacts. 60% similarity = adapt existing; <60% = build new"
max_bytes: 512
density_score: 0.93
source: organization-core/records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 8 SCOUT-FIRST)
linked_artifacts:
  law: p08_law_shokunin
domain: "memory"
related:
  - p10_rs_edison
  - bld_tools_naming_rule
  - p08_pat_construction_triad
  - p11_opt_pool_density
  - bld_tools_quality_gate
  - skill
  - build
  - research_then_build
  - bld_tools_action_prompt
  - bld_tools_voice_pipeline
---

# Axiom: Scout Before Create (Law 8)

## Statement

> Before creating any file, artifact, agent, or template — search the pool first. If similar exists (>= 60% overlap), adapt it. If not, build new with full structure.

## Rule

```
Glob/Grep → found similar (>= 60%) → adapt existing artifact
                                    → credit source in frontmatter
Glob/Grep → not found (<60%) → build new from scratch
                              → add to pool at quality >= 8.0
```

## Implementation

```bash
# Step 1: Glob by name pattern
Glob("**/KC_*DEPLOY*", path="records/pool/knowledge/")

# Step 2: Grep by content keywords
Grep("railway.*deploy|deploy.*checklist", path="records/pool/")

# Step 3: If found → Read → assess similarity → adapt or skip
# Step 4: If not found → Build new → quality gate → pool write
```

## Violations and Costs

| Violation | Cost |
|-----------|------|
| Create duplicate KC | Bloat pool, confuse brain search |
| Skip scouting before agent build | Duplicate agent dirs, routing conflicts |
| Build template that exists | Wasted 20-40min build time |

## Trigger

Auto-trigger on: any `Write` tool call for new file in `records/` or `.claude/`

## Decision Threshold

```
similarity >= 0.60 → ADAPT (never build duplicate)
similarity 0.40-0.59 → EXTEND (build new, link to existing)
similarity < 0.40 → BUILD NEW (independent artifact)
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `axiom` |
| Pillar | P10 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_rs_edison]] | related | 0.35 |
| [[bld_tools_naming_rule]] | upstream | 0.31 |
| [[p08_pat_construction_triad]] | upstream | 0.30 |
| [[p11_opt_pool_density]] | downstream | 0.30 |
| [[bld_tools_quality_gate]] | upstream | 0.29 |
| [[skill]] | upstream | 0.28 |
| [[build]] | upstream | 0.27 |
| [[research_then_build]] | upstream | 0.26 |
| [[bld_tools_action_prompt]] | upstream | 0.25 |
| [[bld_tools_voice_pipeline]] | upstream | 0.25 |
