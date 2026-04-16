---
kind: output_template
id: bld_output_template_trajectory_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for trajectory_eval production
quality: 9.1
title: "Output Template Trajectory Eval"
version: "1.1.0"
author: n01_hybrid_review4
tags: [trajectory_eval, builder, output_template]
tldr: "Template for trajectory_eval artifacts: LLM agent step-level evaluation records."
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
---

```yaml
---
id: p07_te_{{task_slug}}          # e.g. p07_te_webArena_045_gpt4o
kind: trajectory_eval
pillar: P07
title: "{{agent_name}} on {{task_id}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
domain: "{{domain}}"              # e.g. web_navigation, software_engineering
quality: null
tags: [trajectory_eval, {{benchmark}}, {{agent_name}}]
tldr: "{{one sentence: agent X on task Y, outcome Z}}"
agent_id: "{{agent_id}}"
task_id: "{{task_id}}"
benchmark: "{{benchmark}}"       # AgentBench | WebArena | SWE-bench | OSWorld | tau-bench
step_count: {{N}}
task_success: {{true|false}}
partial_credit: {{0.0-1.0}}
path_efficiency: {{steps_taken/steps_optimal}}
tool_call_accuracy: {{precision_float}}
---
```

## Trajectory Overview
| Field | Value |
|---|---|
| Agent | {{agent_id}} |
| Task | {{task_id}} ({{benchmark}}) |
| Environment | {{environment_description}} |
| Total steps | {{step_count}} |
| Task success | {{task_success}} |

## Step Log
| Step | Observation Summary | Reasoning Summary | Action | Outcome |
|---|---|---|---|---|
| 1 | {{obs_1}} | {{reasoning_1}} | {{action_1}} | {{pass/fail/partial}} |
| 2 | {{obs_2}} | {{reasoning_2}} | {{action_2}} | {{pass/fail/partial}} |
| ... | | | | |

## Evaluation Metrics
| Metric | Value | Benchmark Threshold |
|---|---|---|
| Task success | {{true/false}} | >= 0.5 (AgentBench) |
| Path efficiency | {{float}} | >= 0.7 |
| Tool call accuracy | {{float}} | >= 0.8 |
| Partial credit | {{float}} | >= 0.6 |
| Backtrack count | {{int}} | <= 2 |

## Step-level Scores
| Step | Score | Judge Rationale |
|---|---|---|
| {{step_n}} | {{0-10}} | {{one-line rationale}} |

## Failure Analysis
- First failure step: {{step_n}}
- Root cause: {{hallucination | grounding_error | tool_misuse | reasoning_drift}}
- Impact: {{how the failure propagated to subsequent steps}}

## Recommendations
- {{targeted fix 1 for the observed failure mode}}
- {{targeted fix 2}}
