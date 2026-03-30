---
id: p01_kc_director
kind: knowledge_card
type: kind
pillar: P08
title: "Director — Deep Knowledge for director"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: york
domain: director
quality: null
tags: [director, P08, ORCHESTRATE, kind-kc]
tldr: "director is a crew orchestrator artifact that composes and coordinates multiple builders — it dispatches, sequences, and collects results without executing tasks itself."
when_to_use: "Building, reviewing, or reasoning about director artifacts"
keywords: [orchestrator, crew_director, multi_agent_coordination]
feeds_kinds: [director]
density_score: null
---

# Director

## Spec
```yaml
kind: director
pillar: P08
llm_function: ORCHESTRATE
max_bytes: 2048
naming: ex_director_{topic}.md
core: false
```

## What It Is
A director is a crew orchestrator that composes and coordinates multiple builders — defining dispatch mode, wave sequencing, signal waiting, and fallback behavior without executing tasks itself. It is NOT a builder (which executes tasks), NOT a workflow (which is a generic execution sequence), NOT a law (which constrains rather than orchestrates).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableParallel` + LCEL compose | Orchestrates multiple chains with fan-out |
| LlamaIndex | `AgentWorkflow` multi-agent | Coordinates event-driven agent steps |
| CrewAI | `Crew` (hierarchical) + `manager_agent` | Most direct: manager_agent delegates to worker agents |
| DSPy | `Ensemble` / pipeline `Module` | Coordinates multiple sub-modules with voting |
| Haystack | `AsyncPipeline` + `SuperComponent` | Wraps sub-pipelines as coordinated units |
| OpenAI | Orchestrator assistant pattern | Meta-assistant calling other assistants via function tools |
| Anthropic | STELLA satellite pattern | Dispatching spawns and monitoring completion signals |

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
| Wave dispatch | Builders have dependencies between waves | Wave1: research (SHAKA); Wave2: build (EDISON) |
| Conditional routing | Route to builder based on task type | IF research keyword THEN SHAKA; IF build THEN EDISON |
| Consensus gather | Collect all builder outputs before synthesis | Wait all signals → merge → synthesize |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Director that executes | Director writing code violates orchestration boundary | Director ONLY dispatches, NEVER executes tasks |
| No signal wait | Director assumes builders finish instantly | Always check signal files before next wave |
| Nested directors | Director → director → director = spaghetti | Max 2 nesting levels; flatten if deeper |

## Integration Graph
```
agent_card, workflow --> [director] --> spawn_config, signal_file
                              |
                         law, pattern, component_map
```

## Decision Tree
- IF single builder task THEN no director needed — direct spawn
- IF 2+ builders with dependencies THEN wave director
- IF routing depends on task content THEN conditional director
- DEFAULT: wave director for multi-satellite missions, sequential first then optimize

## Quality Criteria
- GOOD: topic, builders list, dispatch_mode, signal_check all defined
- GREAT: wave topology documented, failure fallback per builder specified
- FAIL: director that writes code or executes tasks (purity violation)
