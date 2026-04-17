---
kind: schema
id: bld_schema_planning_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for planning_strategy
quality: 9.1
title: "Schema Planning Strategy"
version: "1.0.0"
author: builder_agent
tags: [planning_strategy, builder, schema, P08]
tldr: "Schema for planning_strategy: class, algorithm, step schema, branching, budget, termination."
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Frontmatter Fields

### Required
| Field | Type | Enum / Pattern | Notes |
|-------|------|----------------|-------|
| id | string | `^p08_ps_[a-z0-9_]+$` | e.g. p08_ps_react_search_agent |
| kind | const | `planning_strategy` | exact match |
| pillar | const | `P08` | architecture |
| title | string | <= 80 chars | human-readable name |
| version | semver | `x.y.z` | |
| created | date | ISO 8601 | |
| updated | date | ISO 8601 | |
| author | string | | |
| tags | array | >= 3 items | must include class + algorithm |
| tldr | string | <= 250 chars | |
| strategy_class | enum | linear \| tree \| graph \| hierarchical \| reflective | |
| algorithm | enum | react \| cot \| tot \| mcts \| llm_compiler \| htn \| plan_and_execute \| reflexion \| self_refine | |
| quality | null | `null` on build | never self-score |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| density_score | float | 0.0-1.0, target >= 0.85 |
| parent_strategy | string | id of strategy this extends (e.g. Reflexion extends ReAct) |
| source_paper | string | arxiv id or DOI |

## ID Pattern
`^p08_ps_[a-z0-9_]+$`  (example: `p08_ps_tot_bfs_depth4`)

## Body Structure (required sections, in order)
1. **Summary** -- goal shape, class choice rationale, non-goals
2. **Step Schema** -- YAML block with fields: thought, action, action_input, observation, reflection, confidence, parent_step_id
3. **Branching Policy** -- table: max_depth, max_breadth, selection, expansion
4. **Budget & Termination** -- table: criterion, threshold, action (min 4 rows)
5. **Revision / Reflection** -- trigger, mechanism, max_revisions
6. **Tradeoffs** -- strengths, weaknesses, avoid-when
7. **Example Trace** -- 3-5 concrete steps

## Constraints
- strategy_class MUST match algorithm family:
  - linear -> {react, cot}
  - tree -> {tot, mcts}
  - graph -> {llm_compiler}
  - hierarchical -> {htn, plan_and_execute}
  - reflective -> {reflexion, self_refine}
- max_depth >= 1, max_breadth >= 1
- At least one termination criterion besides goal_reached (safety net)
- If algorithm in {reflexion, self_refine}: Revision section MUST define mechanism != none
- If strategy_class == tree: max_breadth >= 2
- max_bytes: 5120
- TLDR <= 250 chars

## Validation Command
```bash
python _tools/cex_score.py --apply p08_ps_{name}.md
```
