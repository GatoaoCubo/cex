---
kind: knowledge_card
id: bld_knowledge_card_nucleus_def
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for nucleus_def production
quality: 9.2
title: "Knowledge Card Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, knowledge_card]
tldr: "Domain knowledge for nucleus_def production"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
nucleus_def artifacts formalize the 8 CEX nuclei (N00-N07) as composable fractal
primitives. Each nucleus is a concrete instantiation of the N00 Genesis mold: same
12-pillar structure, different domain, different sin-lens, different CLI-binding.

The fractal repeats at 3 scales: N00 defines pillars as folders, N01-N07 implement
them as subdirectories, builders (107 types) implement them as ISO files. A nucleus_def
makes this contract explicit and machine-readable.

nucleus_def is consumed by: N07 (dispatch routing), N04 (knowledge indexing),
cex_router.py (CLI selection), and spawn_grid.ps1 (boot orchestration).

## Key Concepts

| Concept | Definition | Source |
|---------|-----------|--------|
| Nucleus | One of 8 CEX processing units (N00-N07), each owning a domain | CEX Architecture |
| Genesis (N00) | Universal mold defining what can exist; N01-N07 instantiate it | N00_genesis/README.md |
| Fractal | Same 12-pillar structure repeating at nucleus/builder/ISO scales | CEX Architecture |
| Sin Lens | Creative archetype driving nucleus behavior (e.g., Ira Construtiva) | nucleus rule files |
| CLI Binding | Which CLI executable the nucleus boots (claude/gemini/codex/ollama) | nucleus_models.yaml |
| Model Tier | Capability level: opus (deep reasoning), sonnet (structured), local | nucleus_models.yaml |
| Pillars Owned | Which of P01-P12 this nucleus actually produces artifacts for | agent_card files |
| Crew Template | Composable multi-agent pattern this nucleus can assemble | N07 dispatch rules |
| Domain Agent | Non-builder agent in N0{X}_*/P02_model/ (e.g., railway_superintendent) | agent directories |
| Boot Contract | boot_script + handoff file convention + signal format | dispatch.sh docs |
| Composability | Nucleus declares upstream inputs + downstream outputs for orchestration | P12 orchestration |
| Agent Card | N0{X}_*/agent_card_n0{X}.md -- capability manifest read by N07 | N0{X} directories |

## Nucleus Registry

| Nucleus | Role | Sin Lens | CLI | Model Tier | Context |
|---------|------|----------|-----|-----------|---------|
| N00 | genesis | -- (universal mold) | -- | -- | -- |
| N01 | intelligence | Avareza Investigativa | claude | sonnet | 200K |
| N02 | marketing | Luxuria Criativa | claude | sonnet | 200K |
| N03 | builder | Soberba Inventiva | claude | opus | 1M |
| N04 | knowledge | -- | claude | sonnet | 200K |
| N05 | operations | Ira Construtiva | claude | sonnet | 200K |
| N06 | commercial | Gula Monetizadora | claude | sonnet | 200K |
| N07 | orchestrator | -- | claude | opus | 1M |

## Pillar Ownership Map

| Pillar | Primary Nucleus | Secondary |
|--------|----------------|-----------|
| P01 Knowledge | N04 | N01 |
| P02 Model | N03 | N07 |
| P03 Prompt | N03 | N02 |
| P04 Tools | N05 | N03 |
| P05 Output | N03 | N02 |
| P06 Schema | N03 | N05 |
| P07 Evals | N05 | N01 |
| P08 Architecture | N05 | N03 |
| P09 Config | N05 | N07 |
| P10 Memory | N04 | N01 |
| P11 Feedback | N05 | N03 |
| P12 Orchestration | N07 | N05 |

## Industry Standards
- Multi-agent systems (MAS) architecture -- nucleus = agent node
- Agent-to-Agent (A2A) protocol -- agent cards declare capabilities
- Actor model (Erlang, Akka) -- nucleus = actor with mailbox (handoff file)
- Microservices -- nucleus = service with defined contract
- Conway's Law -- nucleus boundaries map to domain boundaries
- Domain-Driven Design (DDD) -- nucleus = bounded context

## Common Patterns
1. Set pillars_owned to reflect actual artifact output, not aspirational scope.
2. Verify cli_binding from nucleus_models.yaml before writing -- never guess.
3. crew_templates_exposed must name patterns that exist or are planned in N07.
4. domain_agents should enumerate all .md files in N0{X}_*/P02_model/ directory.
5. Boot contract must reference the real handoff file path (n0{X}_task.md).

## Pitfalls
- Claiming all 12 pillars for one nucleus (violates domain boundaries).
- Role/nucleus mismatch (N03 is builder, not operations).
- Missing boot_script breaks N07 dispatch -- nucleus cannot be spawned.
- Stale domain_agents list (agents removed but not updated in nucleus_def).
- Confusing model_tier (sonnet) with model_specific (claude-sonnet-4-6).
