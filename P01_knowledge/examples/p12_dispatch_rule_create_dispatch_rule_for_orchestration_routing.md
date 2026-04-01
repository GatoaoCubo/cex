---
id: p12_dr_orchestration
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: dispatch-rule-builder
domain: orchestration
quality: 8.6
tags: [dispatch, orchestration, routing, coordination, N07, pipeline]
tldr: Route orchestration, coordination, and multi-agent workflow tasks to N07 orchestrator nucleus
scope: orchestration
keywords: [orchestrate, orchestration, coordinate, coordination, dispatch, despacho, manage, gerenciar, pipeline, workflow, route, rotear, grid, mission, missao, plan, planejar, sequence, sequenciar]
agent_node: n07
model: opus
priority: 10
confidence_threshold: 0.75
fallback: human
conditions:
  exclude_domains: [single_agent_build, knowledge_retrieval, marketing_copy]
routing_strategy: hybrid
density_score: 0.81
---
# orchestration Dispatch Rule

## Purpose
Routes high-level orchestration, coordination, and multi-agent workflow management tasks to the N07 orchestrator nucleus. N07 specializes in decomposing complex goals into task sequences, coordinating multiple nuclei, and managing cross-domain dependencies. This rule captures requests for workflow planning, mission execution, grid coordination, and system-level task routing.

## Keyword Rationale
Bilingual PT/EN coverage ensures both Portuguese operators and English documentation trigger correctly. Core orchestration terms like "orchestrate", "coordinate", "dispatch" capture direct requests. Workflow terms like "pipeline", "mission", "grid" catch CEX-specific orchestration patterns. Management verbs like "manage", "plan", "sequence" identify coordination intent. All keywords focus on multi-agent coordination rather than single-agent execution.

## Fallback Logic
Falls back to human operator when N07 orchestrator is unavailable or overloaded. Orchestration decisions often require business context and priority judgment that only humans can provide. Alternative automated fallback to a general-purpose agent would risk inappropriate task decomposition or misrouted subtasks, making human intervention the safer degradation path for critical coordination workflows.