---
id: p01_kc_agent
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P02
title: "Agent — Deep Knowledge for agent"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: agent
quality: 9.1
tags: [agent, p02, BECOME, kind-kc]
tldr: "Complete agent definition — persona, capabilities, tools, and routing rules that make an LLM BECOME a specialist"
when_to_use: "Building, reviewing, or reasoning about agent artifacts"
keywords: [agent, persona, capabilities, specialist, identity]
feeds_kinds: [agent]
density_score: null
aliases: ["agent definition", "bot config", "assistant spec", "AI persona", "autonomous agent"]
user_says: ["create an agent", "build a bot", "make an assistant", "criar agente", "I need an AI that does X", "set up an autonomous worker"]
long_tails: ["I need an AI agent that can handle customer support", "set up a conversational bot for my product", "build an autonomous assistant that uses tools", "define a specialist persona with capabilities and routing"]
cross_provider:
  langchain: "AgentExecutor / create_react_agent"
  llamaindex: "AgentRunner / FunctionCallingAgent"
  crewai: "Agent(role, goal, backstory, tools)"
  dspy: "dspy.ReAct / dspy.Module subclass"
  openai: "Assistants API (assistant object)"
  anthropic: "Claude with tool_use + system prompt"
  haystack: "Agent (preview) / pipeline-as-agent"
related:
  - agent-builder
  - bld_collaboration_agent
  - bld_architecture_agent
  - bld_knowledge_card_agent
  - bld_instruction_agent
  - p03_ins_mental_model
  - p01_kc_mental_model
  - bld_collaboration_system_prompt
  - p01_kc_agent_card
  - agent-profile-builder
---

# Agent

## Spec
```yaml
kind: agent
pillar: P02
llm_function: BECOME
max_bytes: 5120
naming: p02_agent_{{name}}.md + .yaml
core: true
```

## What It Is
An agent is the complete identity specification that transforms a general LLM into a domain specialist. It defines persona (who the agent is), capabilities (what it can do), tools (what it has access to), and routing rules (when it activates). It is NOT a skill (P04, which is a single executable ability) nor a system_prompt (P03, which defines how the agent speaks). The agent kind answers "who am I?" — skills answer "what can I do?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `AgentExecutor` / `create_react_agent` | Agent = LLM + tools + prompt; executor runs the loop |
| LlamaIndex | `AgentRunner` / `FunctionCallingAgent` | Agents with step-wise execution and memory |
| CrewAI | `Agent(role, goal, backstory, tools)` | Most explicit agent definition; role-based |
| DSPy | `dspy.ReAct` / `dspy.Module` subclass | Agents as optimizable modules with signatures |
| Haystack | `Agent` (preview) / pipeline-as-agent | Pipeline with conditional routing acts as agent |
| OpenAI | Assistants API (`assistant` object) | name, instructions, tools, model, file_search |
| Anthropic | Claude with tool_use + system prompt | No native agent abstraction; built from primitives |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| agent_group | string | required | Determines runtime environment and MCPs available |
| domain | string | required | Scopes the agent's knowledge and tool access |
| quality | float | >= 7.0 | Higher quality = pool eligible (8.0+) or golden (9.5+) |
| iso_vectorstore | dir | required | Min 10 files; completeness determines agent reliability |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Specialist agent | Deep domain expertise needed | SEO agent with marketplace-specific tools |
| Orchestrator agent | Multi-step workflow coordination | orchestrator dispatching to agent nodes |
| Review agent | Quality validation | Code reviewer with read-only tool access |
| Builder agent | Code/content creation | builder_agent building components with write access |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| God agent (does everything) | Jack of all trades, master of none | Split into specialist agents per domain |
| Agent without tools | LLM can only talk, not act | Attach relevant tools; even read-only for reviewers |
| Copying agent for minor variant | Maintenance burden, version drift | Use lens (P02) for perspective shifts on same base agent |

## Integration Graph
```
[axiom, mental_model] --> [agent] --> [skill (P04), system_prompt (P03)]
                            |
                    [agent_package, boot_config]
```

## Decision Tree
- IF need a complete autonomous specialist THEN agent
- IF need a perspective shift on existing agent THEN lens
- IF need a single callable ability THEN skill (P04)
- IF need agent identity in portable format THEN agent_package
- DEFAULT: agent for any entity that needs to BECOME a specialist

## Quality Criteria
- GOOD: Persona defined; capabilities listed; tools specified; domain scoped
- GREAT: ISO vectorstore complete (10+ files); tested in agent_group; quality >= 8.0; routing registered
- FAIL: No clear boundary from other agents; missing capabilities; tools undefined; iso_vectorstore < 3 files

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | related | 0.57 |
| [[bld_collaboration_agent]] | downstream | 0.55 |
| [[bld_architecture_agent]] | downstream | 0.49 |
| [[bld_knowledge_card_agent]] | sibling | 0.43 |
| [[bld_instruction_agent]] | downstream | 0.40 |
| [[p03_ins_mental_model]] | downstream | 0.37 |
| [[p01_kc_mental_model]] | sibling | 0.36 |
| [[bld_collaboration_system_prompt]] | downstream | 0.35 |
| [[p01_kc_agent_card]] | sibling | 0.34 |
| [[agent-profile-builder]] | related | 0.34 |
