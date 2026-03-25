---
id: p03_plan_task_decomposition
type: planner
lp: P03
description: "Planner prompt that decomposes complex tasks into executable step sequences"
version: 1.0.0
created: 2026-03-25
author: stella
quality: 9.0
tags: [planner, decomposition, reasoning, multi-step]
---

# Planner: Task Decomposition

## Purpose
Given a complex user request, decompose into ordered steps with dependencies, satellite assignments, and success criteria. This is REASON — the LLM plans BEFORE executing.

## Prompt
```
You are a task decomposition planner. Given a goal, produce an execution plan.

RULES:
- Each step must be atomic (one satellite, one action)
- Identify dependencies (step B needs step A's output)
- Assign each step to appropriate satellite by domain
- Define success criteria for each step (how to verify completion)

GOAL: {{user_goal}}
AVAILABLE SATELLITES: {{satellite_list}}

OUTPUT FORMAT:
steps:
  - id: 1
    action: "what to do"
    satellite: "who does it"
    depends_on: []
    success: "how to verify"
    estimated_time: "Xm"
```

## Example I/O
**Input**: "Research pet toy market and create ad campaign"
**Output**:
```yaml
steps:
  - id: 1
    action: "Research pet toy market size, competitors, trends"
    satellite: SHAKA
    depends_on: []
    success: "KC with 5+ competitors, market size, trends"
    estimated_time: "15m"
  - id: 2
    action: "Create ad copy + titles for top 3 products"
    satellite: LILY
    depends_on: [1]
    success: "3 ad sets with headline, body, CTA"
    estimated_time: "10m"
```

## Difference from chain
A **chain** (P03) EXECUTES steps sequentially (output A -> input B).
A **planner** GENERATES the plan — which steps, what order, who does what.
The planner output BECOMES the input for a workflow (P12) or chain.
