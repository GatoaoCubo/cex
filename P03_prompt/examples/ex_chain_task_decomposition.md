---
id: p03_plan_task_decomposition
kind: planner
pillar: P03
description: "Planner prompt that decomposes complex tasks into executable step sequences"
version: 1.0.0
created: 2026-03-25
author: orchestrator
quality: 9.0
tags: [planner, decomposition, reasoning, multi-step]
---

# Planner: Task Decomposition

## Purpose
Given a complex user request, decompose into ordered steps with dependencies, agent_group assignments, and success criteria. This is REASON — the LLM plans BEFORE executing.

## Prompt
```
You are a task decomposition planner. Given a goal, produce an execution plan.

RULES:
- Each step must be atomic (one agent_group, one action)
- Identify dependencies (step B needs step A's output)
- Assign each step to appropriate agent_group by domain
- Define success criteria for each step (how to verify completion)

GOAL: {{user_goal}}
AVAILABLE AGENT_GROUPS: {{agent_group_list}}

OUTPUT FORMAT:
steps:
  - id: 1
    action: "what to do"
    agent_group: "who does it"
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
    agent_group: research_agent
    depends_on: []
    success: "KC with 5+ competitors, market size, trends"
    estimated_time: "15m"
  - id: 2
    action: "Create ad copy + titles for top 3 products"
    agent_group: marketing_agent
    depends_on: [1]
    success: "3 ad sets with headline, body, CTA"
    estimated_time: "10m"
```

## Difference from chain
A **chain** (P03) EXECUTES steps sequentially (output A -> input B).
A **planner** GENERATES the plan — which steps, what order, who does what.
The planner output BECOMES the input for a workflow (P12) or chain.
