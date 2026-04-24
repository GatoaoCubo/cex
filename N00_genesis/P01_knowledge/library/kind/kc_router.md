---
id: p01_kc_router
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P02
title: "Router — Deep Knowledge for router"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: router
quality: 9.1
tags: [router, P02, REASON, kind-kc]
tldr: "Keyword-to-agent_group routing rule that maps incoming tasks to the correct execution target"
when_to_use: "Building, reviewing, or reasoning about router artifacts"
keywords: [routing, dispatch, task-mapping]
feeds_kinds: [router]
density_score: 0.99
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_dispatch_rule
  - router-builder
  - bld_knowledge_card_dispatch_rule
  - p01_kc_routing_resilience
  - bld_architecture_router
  - bld_collaboration_router
  - bld_knowledge_card_router
  - bld_architecture_dispatch_rule
  - p03_sp_router_builder
  - bld_collaboration_dispatch_rule
---

# Router

## Spec
```yaml
kind: router
pillar: P02
llm_function: REASON
max_bytes: 1024
naming: p02_rt_{{scope}}.yaml
core: true
```

## What It Is
A router is a structured rule that maps task keywords or intent signals to the correct agent_group or agent for execution. It enables the orchestrator to reason about where to dispatch work without hardcoding decisions. It is NOT a dispatch_rule (P12, which orchestrates multi-step workflows) nor a fallback_chain (model-to-model cascading). A router is a single-hop mapping: task in, target out.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableParallel` / custom router chains | Conditional routing via LCEL branching |
| LlamaIndex | `RouterQueryEngine` / `ObjectIndex` | Selects sub-engine based on query classification |
| CrewAI | `Process.hierarchical` manager routing | Manager agent routes tasks to crew members |
| DSPy | `dspy.Module.forward()` branching logic | Programmatic routing inside module's forward method |
| Haystack | `ConditionalRouter` component | Routes pipeline flow based on conditions/templates |
| OpenAI | Function/tool selection via `tool_choice` | Model selects which function to call based on intent |
| Anthropic | `tool_choice` (auto/any/tool) | Controls which tool the model routes to |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| keywords | list[str] | required | More keywords = higher recall but risk of false matches |
| target | string | required | Single target = deterministic vs multi = needs tiebreaker |
| priority | int | 0 | Higher = preferred when multiple routers match |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Keyword match | Simple, fast routing | `keywords: [pesquisar, mercado] -> research_agent` |
| Semantic similarity | Ambiguous or novel queries | Embed query, compare to router descriptions, pick closest |
| Cascade routing | Primary target may reject | Try research_agent, if reject try marketing_agent, fallback to builder_agent |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Overlapping keywords across routers | Ambiguous routing, random target selection | Deduplicate keywords; assign each keyword to exactly one router |
| Routing by model instead of capability | Wrong agent_group gets tasks it cannot handle | Route by domain/skill, not by model name |

## Integration Graph
```
[mental_model] --> [router] --> [dispatch_rule]
                      |
              [action_prompt]
```

## Decision Tree
- IF keywords match exactly one router THEN dispatch to that target
- IF keywords match multiple routers THEN use priority field as tiebreaker
- IF no keywords match THEN fall back to semantic similarity or default target
- DEFAULT: Route to the agent_group with the broadest domain scope

## Quality Criteria
- GOOD: Has keywords, target, and scope defined; no overlapping keywords
- GREAT: Includes priority, confidence threshold, and fallback target
- FAIL: Ambiguous keywords shared across routers; missing target; >1024 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_dispatch_rule]] | sibling | 0.52 |
| [[router-builder]] | related | 0.43 |
| [[bld_knowledge_card_dispatch_rule]] | sibling | 0.38 |
| [[p01_kc_routing_resilience]] | sibling | 0.36 |
| [[bld_architecture_router]] | downstream | 0.35 |
| [[bld_collaboration_router]] | related | 0.34 |
| [[bld_knowledge_card_router]] | sibling | 0.33 |
| [[bld_architecture_dispatch_rule]] | downstream | 0.32 |
| [[p03_sp_router_builder]] | downstream | 0.32 |
| [[bld_collaboration_dispatch_rule]] | downstream | 0.32 |
