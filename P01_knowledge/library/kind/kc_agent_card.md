---
id: p01_kc_agent_card
kind: knowledge_card
type: kind
pillar: P08
title: "Agent Card — Deep Knowledge for agent_card"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: agent_card
quality: null
tags: [agent_card, P08, BECOME, kind-kc]
tldr: "agent_card is the deployment spec for an autonomous agent — encoding identity, model, tools, boot sequence, dispatch scope, and operational constraints in one versioned artifact."
when_to_use: "Building, reviewing, or reasoning about agent_card artifacts"
keywords: [agent_spec, deployment, autonomous_agent]
feeds_kinds: [agent_card]
density_score: null
---

# Agent Card

## Spec
```yaml
kind: agent_card
pillar: P08
llm_function: BECOME
max_bytes: 4096
naming: p08_ac_{{agent_name}}.yaml
core: false
```

## What It Is
An agent_card is the versioned deployment spec for one autonomous agent — it encodes identity (name, role), model selection, tool allowlist, boot sequence (files to read before first LLM call), dispatch scope, and hard constraints. It is NOT an agent instance at runtime (P02 persona only), NOT a boot_config (P02, provider startup), and NOT a spawn_config (P12, runtime launch parameters).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `AgentExecutor` config | Defines tools, llm, memory, max_iterations |
| LlamaIndex | `AgentWorkflow` config | Model, tools, step execution spec |
| CrewAI | `Agent` (role/goal/backstory/llm/tools) | Most direct: structured identity + tool fields |
| DSPy | `Module` + `LM` config | Module class with LM binding and tool decorators |
| Haystack | Pipeline YAML config | Component wiring + OpenAIChatGenerator config |
| OpenAI | `Assistant` resource | Persistent agent with model, tools, instructions |
| Anthropic | system prompt + tools array | Model, tool list, system spec per-request |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| model | string | sonnet | Larger = smarter but slower and costlier |
| tools | list[str] | [] | More tools = more latency + hallucination surface |
| max_iter | int | 10 | Higher = handles complexity but risks runaway loops |
| boot_sequence | list[path] | [] | More files = richer context but slower cold start |
| scope_fence | list[path] | [] | Tighter = safer; too tight = agent can't complete task |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Minimal spec | Single-purpose agent with 3-5 tools | p08_ac_scout.yaml: tools: [glob, grep, read] |
| Scoped boot | Agent pre-loads knowledge before tasks | boot_sequence: [PRIME.md, mental_model.yaml] |
| Model tiering | Route by task complexity | opus for build, sonnet for research |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| God-agent | All tools + wide scope causes context bloat and drift | Split into specialized agents per domain |
| No constraints | Agent without scope_fence drifts into forbidden paths | Always define scope_fence + forbidden_paths |
| Inline prompts >200 chars | Long inline prompts hang TSP non-interactive spawn | Write prompts to handoff files |

## Integration Graph
```
boot_config, persona --> [agent_card] --> spawn_config, workflow
                              |
                         law, permission, path_config
```

## Decision Tree
- IF single agent_node domain THEN solo agent_card per agent_node
- IF cross-domain orchestration THEN director + multiple agent_cards
- IF ephemeral one-shot task THEN inline spec (no persistent card needed)
- DEFAULT: dedicated agent_card per agent_node role, versioned in P08

## Quality Criteria
- GOOD: model, tools, boot_sequence, scope_fence all present and non-empty
- GREAT: scope fence tight, model choice has explicit rationale, dispatch constraints documented
- FAIL: missing model or tools, no constraints, inline prompt >200 chars, no version
