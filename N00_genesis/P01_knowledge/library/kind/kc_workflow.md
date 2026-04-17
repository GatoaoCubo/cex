---
id: p01_kc_workflow
kind: knowledge_card
type: kind
pillar: P12
title: "Workflow — Deep Knowledge for workflow"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: workflow
quality: 9.1
tags: [workflow, P12, PRODUCE, kind-kc]
tldr: "Executable specification of sequential and parallel agent+tool steps that transforms inputs to outputs with defined agents, tools, and quality gates"
when_to_use: "Building, reviewing, or reasoning about workflow artifacts"
keywords: [execution, steps, orchestration]
feeds_kinds: [workflow]
density_score: null
aliases: ["pipeline", "process flow", "agent workflow", "automation sequence", "orchestration flow"]
user_says: ["create a workflow", "fluxo de trabalho", "chain agents together", "automate this process", "build a multi-step pipeline", "set up an automation"]
long_tails: ["I need to chain multiple agents together in sequence", "set up an automated multi-step process with quality gates", "build a pipeline where agent A feeds into agent B", "orchestrate parallel tasks with dependencies and checkpoints"]
cross_provider:
  langchain: "RunnableSequence / LCEL pipeline"
  llamaindex: "Workflow + AgentWorkflow"
  crewai: "Crew(process=Process.sequential/hierarchical)"
  dspy: "dspy.Module.forward() composition"
  openai: "Assistants API with tool use loop"
  anthropic: "Tool use agentic loop + system prompt"
  haystack: "Pipeline (directed multigraph)"
---

# Workflow

## Spec
```yaml
kind: workflow
pillar: P12
llm_function: PRODUCE
max_bytes: 3072
naming: p12_wf_{{name}}.md + .yaml
core: true
```

## What It Is
A workflow is an executable specification defining ordered steps — sequential or parallel — with assigned agents, tools, inputs, outputs, and quality gates. It produces a tangible artifact or state change. It is NOT chain (P03 — a sequence of prompts; workflow includes agents, tools, and execution orchestration beyond prompting) nor dag (P12 — dependency structure only; workflow is the full executable specification that includes the DAG plus agents, tools, and quality gates).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` / LCEL pipeline | Sequential/parallel runnables compose full workflow |
| LlamaIndex | `Workflow` + `AgentWorkflow` | Event-driven workflow with `@step` decorators; multi-agent support |
| CrewAI | `Crew(process=Process.sequential/hierarchical)` | Crew = workflow container; tasks = steps; agents = executors |
| DSPy | `dspy.Module.forward()` composition | Nested module calls compose a program-level workflow |
| Haystack | `Pipeline` (directed multigraph) | `Pipeline.add_component()` + `connect()` = workflow definition |
| OpenAI | Assistants API with tool use loop | Run loop: submit → tool calls → submit results → completion |
| Anthropic | Tool use agentic loop + system prompt | Tool use loop with multiple tool invocations = workflow execution |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| steps | list | required | Ordered steps; each has agent, tool, input, output |
| execution | enum | sequential | sequential/parallel/mixed — parallel = faster; sequential = simpler debug |
| quality_gate | string | null | gate name applied at workflow output; null = no gate |
| timeout_minutes | int | 30 | Lower = fail fast; higher = tolerates slow steps |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Research→Build→Validate | Standard feature workflow | research agent research → builder_agent build → operations_agent validate |
| Fan-out parallel | Independent subtasks | Step 1: spawn research_agent+marketing_agent in parallel → Step 2: builder_agent combines outputs |
| Retry-with-quality-gate | High-quality output required | Step N output → quality_gate → retry if fail → max 3 retries |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Workflow without agent assignments | Steps execute on default/wrong agent | Assign explicit agent per step; no implicit assignment |
| No timeout | Hanging step blocks entire workflow | Always set timeout_minutes; default 30; adjust per step complexity |
| Deeply nested workflows calling other workflows | Stack overflow; debugging impossible | Max 2 levels of nesting; flatten or use DAG for deep dependencies |

## Integration Graph
```
[handoff] --> [workflow] --> [signal: complete]
[dag] ----------^       |
[spawn_config] --^  [checkpoint]
                    [quality_gate]
                    [learning_record]
```

## Decision Tree
- IF steps are independent THEN execution: parallel
- IF step B needs step A output THEN sequential; encode in dag
- IF output quality critical THEN add quality_gate at final step
- IF workflow >10 steps THEN split into sub-workflows with signals between
- DEFAULT: execution: sequential for new workflows; optimize to parallel after validation

## Quality Criteria
- GOOD: Has name, steps (with agent+tool+input+output), execution mode, timeout_minutes; YAML parseable
- GREAT: Quality gate at output; checkpoint after each commit step; parallel where possible; sub-workflow boundary defined
- FAIL: No agent assignments; no timeout; steps lack output definition; no quality gate on critical outputs
