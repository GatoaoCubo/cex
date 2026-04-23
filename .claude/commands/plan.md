---
description: "Plan a goal — decompose into tasks, identify nuclei, map dependencies. Usage: /plan <goal>"
quality: 9.0
title: "Plan"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - ctx_cex_new_dev_guide
  - p12_wf_orchestration_pipeline
  - p01_kc_cex_project_overview
  - skill
  - p04_ct_cex_crew_runner
  - p12_wf_builder_8f_pipeline
  - report_intent_resolution_value_prop
  - spec_n07_operational_intelligence
  - bld_memory_workflow
  - p03_ch_builder_pipeline
---

# /plan — Decompose a Goal

> **What**: Break a big goal into concrete tasks with nucleus assignments.
> **Output**: A plan document in `.cex/runtime/plans/`
> **Next step**: `/guide` (add decisions) → `/spec` (create blueprint) → `/grid` (execute)

## Steps

### Step 1: Understand the goal

Parse `$ARGUMENTS`. If vague, ask ONE clarifying question max.
Don't start GDP here — that's `/guide`'s job.

### Step 2: Decompose

```bash
python _tools/cex_mission.py decompose "$ARGUMENTS"
```

If the tool output is insufficient, decompose manually:
1. What artifacts need to exist?
2. Which nuclei own them?
3. What depends on what?

### Step 3: Map dependencies

```
N06 (brand) ──→ N02 (frontend) ──→ N05 (deploy)
     │                                    ↑
     └──→ N01 (research) ────────────────┘
```

Mark: which can run in PARALLEL vs which are SEQUENTIAL.

### Step 4: Estimate

Per task: kind, nucleus, artifact count, complexity (S/M/L).

### Step 5: Write plan

Save to `.cex/runtime/plans/plan_{slug}.md`:

```markdown
# Plan: {goal}
Created: {timestamp}
Status: DRAFT

## Tasks
| # | Task | Nucleus | Kind | Artifacts | Size | Depends On |
|---|------|---------|------|-----------|------|------------|
| 1 | Brand identity | N06 | agent, prompts, schemas | 16 | L | — |
| 2 | Landing page | N02 | output, schemas | 8 | M | 1 |
| 3 | Deploy pipeline | N05 | workflow, output | 6 | M | 2 |
| 4 | Market research | N01 | knowledge_card | 4 | S | 1 |

## Dependency Graph
N06 → N02 → N05
N06 → N01

## Parallel Groups
Group A: N06 (sequential, runs first)
Group B: N02 + N01 (parallel, after N06)
Group C: N05 (after N02)

## Estimated Effort
Total artifacts: ~34
Nuclei involved: 4
Estimated time: 3 grid sessions
```

### Step 6: Present to user

Show the plan. Ask: "Does this cover everything? Anything to add or remove?"

Adjust if needed. Then suggest:
> "Plan ready. Type `/guide` to make decisions, or `/spec` to jump to blueprint."

## Plan is NOT execution

`/plan` only PLANS. It does not:
1. Ask subjective questions (that's `/guide`)
2. Write detailed specs (that's `/spec`)
3. Build anything (that's `/grid` or `/build`)
4. Score or clean up (that's `/consolidate`)

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ctx_cex_new_dev_guide]] | related | 0.36 |
| [[p12_wf_orchestration_pipeline]] | related | 0.34 |
| [[p01_kc_cex_project_overview]] | related | 0.30 |
| [[skill]] | related | 0.28 |
| [[p04_ct_cex_crew_runner]] | related | 0.28 |
| [[p12_wf_builder_8f_pipeline]] | related | 0.27 |
| [[report_intent_resolution_value_prop]] | related | 0.25 |
| [[spec_n07_operational_intelligence]] | related | 0.25 |
| [[bld_memory_workflow]] | related | 0.25 |
| [[p03_ch_builder_pipeline]] | related | 0.25 |
