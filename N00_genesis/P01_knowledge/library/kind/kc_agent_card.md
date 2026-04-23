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
quality: 9.1
tags: [agent_card, P08, BECOME, kind-kc]
tldr: "agent_card is the deployment spec for an autonomous agent — encoding identity, model, tools, boot sequence, dispatch scope, and operational constraints in one versioned artifact."
when_to_use: "Building, reviewing, or reasoning about agent_card artifacts"
keywords: [agent_spec, deployment, autonomous_agent]
feeds_kinds: [agent_card]
density_score: null
related:
  - p01_kc_agent
  - p01_kc_mental_model
  - bld_collaboration_agent
  - agent-builder
  - agent-card-builder
  - p01_kc_boot_config
  - bld_knowledge_card_agent
  - bld_collaboration_agent_card
  - bld_architecture_agent
  - bld_collaboration_model_card
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
- IF single agent_group domain THEN solo agent_card per agent_group
- IF cross-domain orchestration THEN director + multiple agent_cards
- IF ephemeral one-shot task THEN inline spec (no persistent card needed)
- DEFAULT: dedicated agent_card per agent_group role, versioned in P08

## Quality Criteria
- GOOD: model, tools, boot_sequence, scope_fence all present and non-empty
- GREAT: scope fence tight, model choice has explicit rationale, dispatch constraints documented
- FAIL: missing model or tools, no constraints, inline prompt >200 chars, no version

## Production Reference: OpenClaude Built-in Agents
OpenClaude defines 3 built-in agent types as typed deployment specs:

| Agent | Model | Background | Read-Only | Tool Denylist |
|-------|-------|-----------|-----------|---------------|
| Explore | haiku (speed) | no | yes | edit, write, spawn, plan-exit |
| Plan | inherit (depth) | no | yes | edit, write, spawn, plan-exit |
| Verification | inherit | yes | yes (except temp) | edit, write, spawn, plan-exit |

**Key architectural insight**: Agent cards define CONSTRAINTS, not capabilities.
The tool denylist is more important than the allowlist. An agent that can do
everything except X is more dangerous than one that can only do Y.

**Pattern: omit_project_rules**
Explore and Plan agents skip loading CLAUDE.md/project rules. Reasoning:
- They interpret results, not follow project conventions
- Loading project rules biases sub-agents toward implementer assumptions
- Main agent has full context and interprets sub-agent results
CEX equivalent: agent_card field `omit_project_rules: true`

**Pattern: model selection by purpose**
- Speed tasks (explore): cheapest model (haiku)
- Depth tasks (plan, verify): inherit parent model
- Creative tasks: highest model (opus)
CEX equivalent: router_config.yaml model tiers

## New Agent Card Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Tool denylist > allowlist | Define what's forbidden, not what's allowed | Verification agent |
| Background flag | Agent runs independently, caller continues | Verification agent |
| Model by purpose | haiku=speed, inherit=depth, opus=creative | Explore vs Plan |
| omit_project_rules | Sub-agents should not load project conventions | All 3 agents |
| Input/output contract | Typed input fields + typed output format | Verification agent |
| Dispatch command | Exact CLI invocation in the card | All 3 agents |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | sibling | 0.44 |
| [[p01_kc_mental_model]] | sibling | 0.39 |
| [[bld_collaboration_agent]] | downstream | 0.35 |
| [[agent-builder]] | upstream | 0.34 |
| [[agent-card-builder]] | related | 0.34 |
| [[p01_kc_boot_config]] | sibling | 0.33 |
| [[bld_knowledge_card_agent]] | sibling | 0.31 |
| [[bld_collaboration_agent_card]] | related | 0.31 |
| [[bld_architecture_agent]] | related | 0.31 |
| [[bld_collaboration_model_card]] | upstream | 0.29 |
