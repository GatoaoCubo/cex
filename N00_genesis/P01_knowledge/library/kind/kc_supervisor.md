---
id: p01_kc_supervisor
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P08
title: "Supervisor — Deep Knowledge for supervisor"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: supervisor
quality: 9.1
tags: [supervisor, P08, ORCHESTRATE, kind-kc]
tldr: "supervisor is a crew orchestrator artifact that composes and coordinates multiple builders — it dispatches, sequences, and collects results without executing tasks itself."
when_to_use: "Building, reviewing, or reasoning about supervisor artifacts"
keywords: [orchestrator, crew_director, multi_agent_coordination]
feeds_kinds: [supervisor]
density_score: null
related:
  - supervisor-builder
  - bld_knowledge_card_supervisor
  - p03_sp_director_builder
  - bld_architecture_supervisor
  - bld_collaboration_supervisor
  - bld_instruction_supervisor
  - p11_qg_director
  - bld_examples_supervisor
  - bld_config_supervisor
  - bld_schema_supervisor
---

# Supervisor

## Spec
```yaml
kind: supervisor
pillar: P08
llm_function: ORCHESTRATE
max_bytes: 2048
naming: ex_director_{topic}.md
core: false
```

## What It Is
A supervisor is a crew orchestrator that composes and coordinates multiple builders — defining dispatch mode, wave sequencing, signal waiting, and fallback behavior without executing tasks itself. It is NOT a builder (which executes tasks), NOT a workflow (which is a generic execution sequence), NOT a law (which constrains rather than orchestrates).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableParallel` + LCEL compose | Orchestrates multiple chains with fan-out |
| LlamaIndex | `AgentWorkflow` multi-agent | Coordinates event-driven agent steps |
| CrewAI | `Crew` (hierarchical) + `manager_agent` | Most direct: manager_agent delegates to worker agents |
| DSPy | `Ensemble` / pipeline `Module` | Coordinates multiple sub-modules with voting |
| Haystack | `AsyncPipeline` + `SuperComponent` | Wraps sub-pipelines as coordinated units |
| OpenAI | Orchestrator assistant pattern | Meta-assistant calling other assistants via function tools |
| Anthropic | orchestrator agent_group pattern | Dispatching spawns and monitoring completion signals |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| topic | string | required | Domain scope — narrow = predictable; broad = flexible |
| builders | list[str] | required | Named builders — more = more parallelism but harder to debug |
| dispatch_mode | enum | sequential | sequential/parallel/conditional — parallel = speed; sequential = safe |
| signal_check | bool | true | true = wait for completion; false = fire-and-forget |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Wave dispatch | Builders have dependencies between waves | Wave1: research (research_agent); Wave2: build (builder_agent) |
| Conditional routing | Route to builder based on task type | IF research keyword THEN research_agent; IF build THEN builder_agent |
| Consensus gather | Collect all builder outputs before synthesis | Wait all signals → merge → synthesize |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Supervisor that executes | Supervisor writing code violates orchestration boundary | Supervisor ONLY dispatches, NEVER executes tasks |
| No signal wait | Supervisor assumes builders finish instantly | Always check signal files before next wave |
| Nested directors | Supervisor → supervisor → supervisor = spaghetti | Max 2 nesting levels; flatten if deeper |

## Integration Graph
```
agent_card, workflow --> [supervisor] --> spawn_config, signal_file
                              |
                         law, pattern, component_map
```

## Decision Tree
- IF single builder task THEN no supervisor needed — direct spawn
- IF 2+ builders with dependencies THEN wave supervisor
- IF routing depends on task content THEN conditional supervisor
- DEFAULT: wave supervisor for multi-agent_group missions, sequential first then optimize

## Quality Criteria
- GOOD: topic, builders list, dispatch_mode, signal_check all defined
- GREAT: wave topology documented, failure fallback per builder specified
- FAIL: supervisor that writes code or executes tasks (purity violation)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[supervisor-builder]] | upstream | 0.67 |
| [[bld_knowledge_card_supervisor]] | sibling | 0.64 |
| [[p03_sp_director_builder]] | upstream | 0.64 |
| [[bld_architecture_supervisor]] | related | 0.62 |
| [[bld_collaboration_supervisor]] | downstream | 0.61 |
| [[bld_instruction_supervisor]] | upstream | 0.59 |
| [[p11_qg_director]] | downstream | 0.55 |
| [[bld_examples_supervisor]] | upstream | 0.50 |
| [[bld_config_supervisor]] | downstream | 0.47 |
| [[bld_schema_supervisor]] | upstream | 0.45 |
