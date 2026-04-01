---
description: "Plan a goal — decompose into tasks, identify nuclei, map dependencies. Usage: /plan <goal>"
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
- What artifacts need to exist?
- Which nuclei own them?
- What depends on what?

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
- Ask subjective questions (that's `/guide`)
- Write detailed specs (that's `/spec`)
- Build anything (that's `/grid` or `/build`)
- Score or clean up (that's `/consolidate`)
