---
id: n07_taught_terms_registry
kind: entity_memory
pillar: P10
title: "Taught Terms Registry -- Didactic Protocol Tracker"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: n03_builder
nucleus: N07
quality: 9.0
tags: [didactic, terminology, taught-terms, memory, tracking]
tldr: "Registry of industry terms N07 has taught the user. Check BEFORE teaching to avoid repetition. Update AFTER teaching to persist knowledge."
density_score: 0.92
related:
  - spec_metaphor_dictionary
  - n07_memory_user_directive
  - report_intent_resolution_value_prop
  - spec_context_assembly
  - bld_schema_context_window_config
  - bld_schema_bugloop
  - bld_schema_runtime_state
  - n01_readme_comparison
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
---

# Taught Terms Registry

## Purpose

N07 checks this registry before every teaching opportunity. If a term appears here,
N07 uses it without explanation. If absent, N07 teaches once (one line or one table row),
then logs it here.

## Protocol

1. **Before teaching**: search this registry for the metaphor the user just used
2. **If found**: use the industry term silently, zero explanation
3. **If not found**: teach with one-line inline or table row, then log below
4. **If user asks to be re-taught**: comply, do NOT update the date
5. **If user self-corrects**: acknowledge ("Correct -- [term] maps to [industry]")
6. **If in rapid-fire flow**: skip teaching even for new terms (momentum > education)
7. **If error would cause wrong dispatch**: teach immediately regardless of flow state

## Registry

| Metaphor (user says) | Industry Term | Taught On | Context | Acknowledged? |
|----------------------|---------------|-----------|---------|---------------|
| card | artifact (MLOps, CI/CD) | 2026-04-07 | explaining knowledge cards | yes |
| deck (file) | agent card (Google A2A) | 2026-04-07 | deck file = agent card | yes |
| deck (concept) | context assembly / prompt composition | 2026-04-07 | deck concept = prompt composition | yes |
| filled mold | instance (OOP class->instance) | 2026-04-07 | archetype->instance mapping | yes |
| draw | retrieval (the R in RAG) | 2026-04-07 | RAG retrieval explanation | yes |
| fractal | convention over configuration (Rails) | 2026-04-07 | Rails pattern analogy | yes |
| dealer | orchestrator / supervisor agent | 2026-04-07 | N07 role explanation | yes |
| table / grid | multi-agent orchestration (LangGraph, CrewAI) | 2026-04-07 | grid dispatch | yes |
| round | pipeline run (MLOps) | 2026-04-07 | 8F cycle | yes |
| play | generation / inference | 2026-04-07 | LLM inference | yes |
| spawn | spawn/fork (POSIX) | 2026-04-07 | already correct term | yes |
| artifact | artifact (MLOps) | 2026-04-07 | card = artifact | yes |

## Terms Not Yet Taught (Candidates)

These terms appear in the metaphor dictionary but have not been used by the user yet.
N07 should be ready to teach them on first encounter.

| Metaphor | Industry Term | Framework Source |
|----------|---------------|------------------|
| hand | working context / working set | OS memory management |
| mold | archetype / template | OOP class definition |
| combo | prompt composition | prompt engineering |
| library | knowledge base / artifact store | information retrieval |
| game | pipeline (MLOps, CI/CD) | DevOps |
| genesis | schema layer / archetype layer | data architecture |
| building | system / repository | software engineering |
| floor | agent domain | multi-agent systems |
| superintendent | autonomous agent | agent frameworks |
| department | domain | domain-driven design |
| boot | bootstrap (POSIX) | systems programming |
| overnight | batch job / cron job | operations |
| wave | execution phase | deployment strategies |
| signal | event/signal (POSIX) | event-driven architecture |
| handoff | task spec (CEX convention) | multi-agent systems |
| improve | optimize / AutoML evolve | ML optimization |
| fix | refactor / patch | software maintenance |
| check | audit / lint | code quality |
| clean | sanitize | security / encoding |
| gate | quality gate (CI/CD) | continuous delivery |
| ship | release | software delivery |
| blank brain | unconfigured instance | provisioning |
| assimilate | bootstrap / provision | DevOps |
| the X | brand identity | branding |
| translate / transmute | intent resolution (NLU) | NLU frameworks |
| feed it | injection / input provision | prompt engineering |
| spit out | generation / inference | LLM inference |
| cook / bake | pipeline execution (MLOps) | MLOps |
| filter | retrieval filtering / re-ranking | information retrieval |
| mix / blend | fusion / ensemble | ML ensemble methods |
| stamp / seal | quality gate (CI/CD) | continuous delivery |
| teach it | in-context learning | ML / prompt engineering |
| remember this | entity memory / knowledge persistence | knowledge management |
| forget this | memory eviction | cache management |
| connect to X | tool registration / MCP server | MCP protocol |
| speed it up | inference optimization | ML optimization |
| make it cheaper | token budget optimization | LLM cost management |
| make it smarter | prompt optimization / model upgrade | ML engineering |
| test it | evaluation (unit/e2e/smoke) | software testing |

## Merge Rules

- If the same metaphor maps to different industry terms in different contexts
  (e.g., "deck" -> agent_card vs. context_assembly), keep BOTH entries with context column
- If a term is taught in one context but user uses it in another, teach the new mapping
- Deduplicate only when metaphor + industry term + context are all identical

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_metaphor_dictionary]] | upstream | 0.55 |
| [[n07_memory_user_directive]] | related | 0.36 |
| [[report_intent_resolution_value_prop]] | upstream | 0.28 |
| [[spec_context_assembly]] | related | 0.27 |
| [[bld_schema_context_window_config]] | upstream | 0.26 |
| [[bld_schema_bugloop]] | downstream | 0.26 |
| [[bld_schema_runtime_state]] | upstream | 0.26 |
| [[n01_readme_comparison]] | upstream | 0.26 |
| [[bld_schema_usage_report]] | upstream | 0.26 |
| [[bld_schema_quickstart_guide]] | upstream | 0.26 |
