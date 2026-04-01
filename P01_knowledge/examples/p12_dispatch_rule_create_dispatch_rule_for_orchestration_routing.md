---
id: p12_dr_orchestration
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: dispatch-rule-builder
domain: orchestration
quality: 8.5
tags: [dispatch, orchestration, maestro, routing, coordination]
tldr: Route orchestration, coordination, and multi-agent management tasks to maestro orchestrator
scope: orchestration
keywords: [orquestrar, orchestrate, coordenar, coordinate, dirigir, direct, despachar, dispatch, gerenciar, manage, conductor, maestro]
agent_node: maestro
model: opus
priority: 9
confidence_threshold: 0.75
fallback: atlas
conditions:
  exclude_domains: [build, research, marketing]
routing_strategy: hybrid
density_score: 0.81
---
# orchestration Dispatch Rule

## Purpose
Routes high-level coordination, multi-agent orchestration, and task delegation workflows to the maestro orchestrator. The maestro specializes in decomposing complex goals into agent-specific tasks, managing handoffs between nuclei, and ensuring proper workflow sequencing across the CEX system.

## Keyword Rationale
Bilingual PT/EN coverage captures both Portuguese operator commands ("orquestrar", "coordenar", "dirigir") and English task descriptions ("orchestrate", "coordinate", "manage"). Terms like "conductor" and "maestro" match leadership metaphors commonly used in orchestration contexts. "Despachar" covers the critical dispatch function while "gerenciar" handles broader management requests.

## Fallback Logic
Atlas serves as fallback for general routing and coordination when maestro is unavailable. While atlas lacks maestro's specialized multi-agent orchestration capabilities, it can handle basic task routing and delegation, ensuring system continuity during orchestrator downtime.