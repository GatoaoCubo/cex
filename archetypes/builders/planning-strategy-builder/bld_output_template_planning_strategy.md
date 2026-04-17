---
kind: output_template
id: bld_output_template_planning_strategy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for planning_strategy production
quality: 9.1
title: "Output Template Planning Strategy"
version: "1.0.0"
author: builder_agent
tags: [planning_strategy, builder, output_template, react, tot, htn]
tldr: "Concrete template for planning_strategy artifacts: strategy class, step schema, budget, termination, tradeoffs."
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Output Template -- planning_strategy

```markdown
---
id: p08_ps_{{slug}}
kind: planning_strategy
pillar: P08
title: "{{strategy_name}}"
version: "1.0.0"
author: {{author}}
created: "{{iso_date}}"
updated: "{{iso_date}}"
tags: [planning_strategy, {{class}}, {{algorithm}}]
tldr: "{{one_line_summary}}"
strategy_class: {{linear|tree|graph|hierarchical|reflective}}
algorithm: {{react|cot|tot|mcts|llm_compiler|htn|plan_and_execute|reflexion|self_refine}}
quality: null
density_score: 0.85
---

# Planning Strategy: {{strategy_name}}

## Summary
One paragraph: what goal shape this strategy solves, why this class was chosen,
what it explicitly does NOT handle.

## Step Schema
```yaml
step:
  thought: string       # internal reasoning (CoT/ReAct)
  action: enum          # tool name OR "finish"
  action_input: object  # tool args
  observation: string   # tool result (ReAct) | null (CoT)
  reflection: string    # self-critique (Reflexion) | null
  confidence: float     # 0.0-1.0
  parent_step_id: str   # for Tree/Graph classes | null
```

## Branching Policy
| Param | Value | Notes |
|-------|-------|-------|
| max_depth | {{int}} | longest step chain (ReAct=10, ToT=4, HTN=6) |
| max_breadth | {{int}} | siblings per node (Linear=1, ToT=3-5, MCTS=variable) |
| selection | {{greedy|bfs|dfs|ucb1|llm_vote}} | how to pick next node |
| expansion | {{single|k_samples|decomposition}} | how new children are generated |

## Budget & Termination
| Criterion | Threshold | Action |
|-----------|-----------|--------|
| goal_reached | finish action emitted | return plan |
| max_depth | {{N}} | terminate + return best-so-far |
| max_tokens | {{N}} | terminate + return best-so-far |
| max_wall_seconds | {{N}} | terminate + return best-so-far |
| confidence_floor | < {{0.3}} for 2 consecutive steps | revise or abort |
| no_progress | 2 identical observations | prune branch |

## Revision / Reflection
- trigger: {{on_error | on_low_confidence | every_n_steps | null}}
- mechanism: {{reflexion | self_refine | backtrack | none}}
- max_revisions: {{int}}

## Tradeoffs
- Strengths: (e.g., ReAct = transparent, cheap)
- Weaknesses: (e.g., ReAct = single path, no backtracking)
- Avoid when: (e.g., goal has >5 reversible subgoals -> prefer ToT/HTN)

## Example Trace (3-5 steps, redacted)
```
Thought: ...  Action: search(...)  Obs: ...
Thought: ...  Action: finish       Obs: plan ready
```
```
