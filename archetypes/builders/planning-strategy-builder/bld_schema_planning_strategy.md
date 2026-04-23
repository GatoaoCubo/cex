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
related:
  - bld_output_template_planning_strategy
  - audit_planning_strategy_builder
  - planning-strategy-builder
  - bld_schema_rl_algorithm
  - n06_schema_brand_config
  - p06_schema_kc_structure
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_agent_computer_interface
  - bld_schema_multimodal_prompt
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_planning_strategy]] | upstream | 0.51 |
| [[audit_planning_strategy_builder]] | downstream | 0.42 |
| [[planning-strategy-builder]] | downstream | 0.39 |
| [[bld_schema_rl_algorithm]] | sibling | 0.30 |
| [[n06_schema_brand_config]] | related | 0.30 |
| [[p06_schema_kc_structure]] | sibling | 0.29 |
| [[bld_schema_model_registry]] | sibling | 0.28 |
| [[bld_schema_experiment_tracker]] | sibling | 0.27 |
| [[bld_schema_agent_computer_interface]] | sibling | 0.27 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.27 |
