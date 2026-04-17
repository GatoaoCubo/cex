---
id: p12_dr_orchestration
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: codex
domain: orchestration
quality: 9.0
tags: [dispatch, orchestration, orchestrator, routing, pipeline, coordination]
tldr: Route orchestration, coordination, and multi-agent workflow tasks to the N07 orchestrator nucleus
scope: orchestration
keywords: [orchestrate, orquestrar, coordinate, coordenar, dispatch, despachar, mission, missao, pipeline, plan, planejar, grid]
agent_group: orchestrator
model: opus
priority: 9
confidence_threshold: 0.72
fallback: builder
conditions:
  exclude_domains: [build, research, marketing, knowledge, operations, commercial]
load_balance: false
routing_strategy: hybrid
density_score: 0.81
title: "P12 Dispatch Rule Create Dispatch Rule For Orchestration Routing"
---
# orchestration Dispatch Rule

## Purpose
Routes high-level orchestration, coordination, and multi-agent workflow management tasks to the N07 orchestrator nucleus. N07 specializes in decomposing complex goals into task sequences, dispatching work across nuclei (N01–N06), and managing cross-domain dependencies. Captures requests for mission execution, grid coordination, pipeline planning, and nucleus dispatch — tasks that require a top-level view rather than domain execution.

## Keyword Rationale
Bilingual PT/EN coverage fires on both Portuguese operators and English documentation. Core terms (`orchestrate`, `orquestrar`, `coordinate`, `coordenar`) capture direct orchestration requests. CEX-specific keywords (`mission`, `grid`, `pipeline`) catch workflow planning patterns. Dispatch verbs (`dispatch`, `despachar`) identify routing-level requests. Planning verbs (`plan`, `planejar`) catch decomposition intent. Twelve keywords balance breadth with specificity, avoiding generic collisions with build or research domains.

## Fallback Logic
`builder` (N03) handles fallback when N07 orchestrator is unavailable. N03 can execute single-artifact pipelines directly via 8F without full orchestration overhead — appropriate degradation for tasks that would have been simple solo dispatches. Circular routing to any execution nucleus (N01–N06) is excluded; fallback must escalate capability, not route to domain specialists.

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `dispatch rule`
- **Artifact ID**: `p12_dr_orchestration`
- **Tags**: [dispatch, orchestration, orchestrator, routing, pipeline, coordination]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `dispatch rule` | Artifact type |
| Pipeline | 8F (F1→F8) |
