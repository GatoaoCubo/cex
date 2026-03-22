---
id: p10_ax_scout_before_create
type: axiom
lp: P10
title: "Axiom: Scout Before Create (Law 8)"
version: 3.0.0
created: 2026-03-22
updated: 2026-03-22
author: PYTHA
quality: 9.5
tags: [axiom, scout, law8, discovery, pool]
tldr: "LAW 8: Always Glob/Grep before Write. Never duplicate pool artifacts. 60% similarity = adapt existing; <60% = build new"
max_bytes: 512
density_score: 0.93
source: codexa-core/records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 8 SCOUT-FIRST)
linked_artifacts:
  law: p08_law_shokunin
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
