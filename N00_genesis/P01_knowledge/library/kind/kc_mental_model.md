---
id: p01_kc_mental_model
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P02
title: "Mental Model — Deep Knowledge for mental_model"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: mental_model
quality: 9.1
tags: [mental_model, P02, BECOME, kind-kc]
tldr: "YAML identity map encoding an agent's routing logic, decision boundaries, and personality constraints"
when_to_use: "Building, reviewing, or reasoning about mental_model artifacts"
keywords: [identity, routing, decision-map]
feeds_kinds: [mental_model]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_agent
  - agent-builder
  - bld_collaboration_mental_model
  - bld_architecture_agent
  - p03_ins_mental_model
  - mental-model-builder
  - bld_collaboration_agent
  - p01_kc_agent_card
  - bld_knowledge_card_mental_model
  - bld_architecture_mental_model
---

# Mental Model

## Spec
```yaml
kind: mental_model
pillar: P02
llm_function: BECOME
max_bytes: 2048
naming: p02_mm_{{agent}}.yaml
core: true
```

## What It Is
A mental model is a YAML identity map that encodes an agent's routing logic, decision boundaries, tool affinities, and personality constraints. It is loaded at boot time so the LLM "becomes" the agent. Unlike a system_prompt (P03, text-based identity), a mental model is machine-parseable structured data. It is NOT a mental_model in the P10 sense (variable session state); this is a fixed identity artifact.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Agent config dict / `create_agent` params | Agent role, tools, model are configured declaratively |
| LlamaIndex | `Settings` + `AgentWorkflow` config | Global settings + per-agent workflow configuration |
| CrewAI | `Agent(role, goal, backstory)` | Role/goal/backstory triple maps directly to mental model fields |
| DSPy | `dspy.Module` class attributes | Module's signature + forward() define its identity |
| Haystack | `Pipeline` topology + component config | Pipeline DAG structure encodes the agent's decision graph |
| OpenAI | `Assistant` instructions + model config | Persistent instructions define assistant identity |
| Anthropic | `system` message + `tool_choice` config | System prompt + tool configuration shape agent behavior |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| domain | string | required | Narrow = focused expertise vs broad = flexible but shallow |
| tools | list | [] | More tools = more capable but slower routing decisions |
| constraints | list | [] | More constraints = safer but less creative output |
| personality | map | neutral | Strong personality = consistent voice vs generic = adaptable |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Domain-scoped model | Agent owns one vertical | `domain: marketing, tools: [copy, seo]` |
| Multi-tool generalist | Orchestrator or gateway agent | `domain: orchestration, tools: [all_agent_groups]` |
| Constraint-heavy model | Safety-critical or compliance tasks | `constraints: [no_pii, audit_trail, max_tokens_2000]` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Embedding instructions in mental model | Mixes identity (BECOME) with execution (INJECT) | Keep instructions in system_prompt or action_prompt |
| Overlapping domains across agents | Routing ambiguity, duplicate work | Define clear boundary per agent in domain field |

## Integration Graph
```
[system_prompt] --> [mental_model] --> [router]
                         |
                    [model_card]
```

## Decision Tree
- IF agent is core agent_group THEN mental_model required (boot dependency)
- IF agent is ephemeral/one-shot THEN mental_model optional (use system_prompt only)
- DEFAULT: Create mental_model for any agent that persists across sessions

## Quality Criteria
- GOOD: Has domain, tools, constraints; parseable YAML; under 2048 bytes
- GREAT: Routing logic is unambiguous; personality consistent with domain; all fields populated
- FAIL: Free-text instead of structured YAML; mixes instructions with identity; >2048 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | sibling | 0.46 |
| [[agent-builder]] | related | 0.40 |
| [[bld_collaboration_mental_model]] | related | 0.39 |
| [[bld_architecture_agent]] | downstream | 0.38 |
| [[p03_ins_mental_model]] | downstream | 0.38 |
| [[mental-model-builder]] | related | 0.38 |
| [[bld_collaboration_agent]] | downstream | 0.38 |
| [[p01_kc_agent_card]] | sibling | 0.37 |
| [[bld_knowledge_card_mental_model]] | sibling | 0.36 |
| [[bld_architecture_mental_model]] | downstream | 0.36 |
