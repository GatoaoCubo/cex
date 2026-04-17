---
kind: knowledge_card
id: bld_knowledge_card_crew_template
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for crew_template production
quality: 9.2
title: "Knowledge Card Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, knowledge_card, composable, crewai, autogen, swarm]
tldr: "Domain knowledge for crew_template production"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
---

## Domain Overview
Crew templates are the composable-crew primitive of the 2025-2026 multi-agent era. They declaratively specify a reusable team: which roles participate (role_assignment references), how they collaborate (process topology), what they remember (memory_scope), and how success is measured (success_criteria). The three reference implementations -- CrewAI Process, Microsoft AutoGen GroupChat, and OpenAI Swarm -- converge on this pattern: a blueprint that any runtime can instantiate to spawn a coordinated team.

CrewAI Process introduced the `sequential` / `hierarchical` topology distinction in 2024 and extended it with consensus-style voting in 2025. AutoGen GroupChat adds `round_robin`, `manager_delegated`, and `auto` speaker-selection. OpenAI Swarm (v0.6+) formalizes handoffs as transfer functions between agents. All three map cleanly to CEX kinds: crew_template (blueprint) + role_assignment (agent binding) + supervisor (runtime executor) + handoff (task transfer).

## Key Concepts
| Concept | Definition | Source |
|---------|------------|--------|
| Crew | Reusable team blueprint = roles + process + memory + success | CrewAI Process |
| Process | Coordination topology (sequential, hierarchical, consensus) | CrewAI 2024+ |
| Role Assignment | Binding of agent/sub-agent to named role (CrewAI Agent class) | CrewAI Agent |
| Handoff Protocol | Format for inter-role task transfer (A2A, OpenAI transfer fn) | Google A2A + OpenAI Swarm |
| Memory Scope | Visibility rules (private / shared / persistent) | AutoGen + CrewAI Memory |
| Success Criteria | Measurable post-conditions (threshold, count, gate) | quality_gate linkage |
| Manager Agent | Role with delegation authority (hierarchical process) | CrewAI hierarchical |
| Speaker Selection | Turn-taking policy in multi-agent dialogue | AutoGen GroupChat |

## Industry Standards
- CrewAI Process API (v0.80+): `Process.sequential`, `Process.hierarchical`, `Process.consensus`.
- Microsoft Agent Framework (MAF): merged AutoGen GroupChat + Semantic Kernel (Q4 2025).
- OpenAI Agents SDK v0.6+: breaking handoff changes; transfer functions as first-class primitive.
- Google A2A v0.3.0: Task semantics for agent-to-agent transfer.
- LangGraph StateGraph: conditional edges map to consensus topology.

## Common Patterns
1. **Sequential assembly-line**: research -> draft -> edit -> review (CrewAI sequential).
2. **Manager delegation**: manager role dispatches to specialists, reassembles output (CrewAI hierarchical, AutoGen manager_delegated).
3. **Consensus voting**: N peer roles produce, voting rule selects winner (CrewAI consensus, LangGraph edge condition).
4. **Triage-and-transfer**: entry-point role routes to specialist via transfer function (OpenAI Swarm).
5. **Round-robin debate**: roles take turns until termination criterion (AutoGen round_robin).

## Pitfalls
- Inlining role identity instead of referencing role_assignment (duplicates content, breaks reuse).
- Over-sharing memory_scope (context bleed, prompt-cache misses, higher cost).
- Picking sequential process when task has inherent parallelism (wastes wall-clock time).
- Missing success_criteria -> crew runs forever or signals too early.
- Mixing handoff-protocols within one crew (A2A + OpenAI transfer mid-flight) breaks compatibility.
- Treating crew_template as concrete instance; it MUST be reusable across domains.
