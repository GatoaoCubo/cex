---
id: p08_pat_nucleus_fractal
kind: pattern
pillar: P08
title: "Pattern: Nucleus as Fractal of 12 Pillars"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: orchestrator
quality: 9.2
tags: [pattern, nucleus, fractal, agent_group, orchestration, 12-pillars]
tldr: "A nucleus mirrors all 12 CEX pillars filled with domain-specific content — not a new kind, but a composition pattern of existing kinds"
density_score: 1.0
---

# Pattern: Nucleus as Fractal of 12 Pillars

## Problem
How to represent an autonomous agent_group (nucleus) that has its own identity,
knowledge, tools, workflows, and quality gates — without inventing new taxonomy.

## Solution
A nucleus is a DIRECTORY that mirrors the 12 CEX pillars, filled with domain-specific
instances of existing kinds. No new kind needed.

## Framework References
| Framework | Concept | CEX Mapping |
|-----------|---------|-------------|
| CrewAI | Crew (agents+tasks+process) | director(P08) + workflow(P12) |
| CrewAI | Agent (role+goal+tools) | agent(P02) + system_prompt(P03) |
| A2A | AgentCard (name+skills+endpoint) | agent_card(P08) + agent_package(P02) |
| LangGraph | StateGraph (nodes+edges+state) | dag(P12) + checkpoint(P12) |
| CrewAI | Process (sequential/hierarchical) | workflow(P12) mode field |

## Composition (minimum viable nucleus)
| Kind | Pillar | Role in Nucleus |
|------|--------|-----------------|
| agent_card | P08 | Identity: who, what domain, what model |
| agent | P02 | Persona + capabilities |
| system_prompt | P03 | Voice and operating rules |
| boot_config | P02 | Provider-specific initialization |
| dispatch_rule | P12 | How work reaches this nucleus |
| workflow | P12 | 8F execution pipeline |
| spawn_config | P12 | How to launch this nucleus |
| agent_package | P02 | Portable distributable bundle |
| knowledge_card | P01 | Domain knowledge (N cards) |
| quality_gate | P11 | Domain quality standards |
| mcp_server | P04 | Tools available to nucleus |

## Directory Structure
```
nuclei/
  {name}/
    manifest.yaml             # agent_card (P08)
    P01_knowledge/            # KCs of this domain
    P02_model/                # agent + router + boot_config + fallback
    P03_prompt/               # system_prompt + instructions
    P04_tools/                # mcp_servers + function_defs
    P05_output/               # domain output formats
    P06_schema/               # domain interfaces
    P07_evals/                # domain quality evals
    P08_architecture/         # domain patterns + agent_card
    P09_config/               # env + path + runtime rules
    P10_memory/               # learnings + session state
    P11_feedback/             # quality_gates + guardrails
    P12_orchestration/        # workflows + dispatch + signals
```

## 8F Runner Integration
When a nucleus receives an intent:
1. dispatch_rule routes intent to this nucleus
2. 8F Runner loads builders from THIS nucleus (not genesis)
3. F1 CONSTRAIN: uses nucleus P06 schemas + P11 guardrails
4. F2 BECOME: uses nucleus P02 agent + P03 system_prompt
5. F3 INJECT: uses nucleus P01 knowledge_cards + KC library
6. F4-F8: same pipeline, domain-scoped context

## The 7 organization Nuclei
| # | Name | Domain | Model | Pecado |
|---|------|--------|-------|--------|
| 01 | research_agent | Research | sonnet | Inveja |
| 02 | marketing_agent | Marketing | sonnet | Luxuria |
| 03 | builder_agent | Build | opus | Soberba |
| 04 | operations_agent | Execute | opus | Ira |
| 05 | commercial_agent | Monetize | sonnet | Avareza |
| 06 | knowledge_agent | Knowledge | sonnet | Gula |
| 07 | orchestrator | Orchestrate | opus | — |

## Anti-Patterns
| Anti-Pattern | Why |
|-------------|-----|
| New kind "nucleus" | Composition of existing kinds, not a new type |
| Flat agent_card | Single file cant capture 12-pillar depth |
| Shared knowledge pool | Each nucleus owns its domain knowledge |
| Cross-nucleus execution | Nucleus 03 never does research (thats 01) |
