---
id: p01_kc_handoff_protocol
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P02
title: "Handoff Protocol — Deep Knowledge for handoff_protocol"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: handoff_protocol
quality: 9.1
tags: [handoff_protocol, p02, COLLABORATE, kind-kc]
tldr: "Agent-to-agent transfer protocol — defines what context passes between agents and what the receiving agent must return"
when_to_use: "Building, reviewing, or reasoning about handoff_protocol artifacts"
keywords: [handoff, agent-transfer, a2a, context-passing, collaboration]
feeds_kinds: [handoff_protocol]
density_score: null
related:
  - bld_knowledge_card_handoff_protocol
  - handoff-protocol-builder
  - p03_sp_handoff_protocol_builder
  - p01_kc_agent
  - bld_collaboration_handoff_protocol
  - p10_lr_handoff_protocol_builder
  - handoff-builder
  - bld_collaboration_handoff
  - bld_examples_handoff_protocol
  - p01_kc_handoff
---

# Handoff Protocol

## Spec
```yaml
kind: handoff_protocol
pillar: P02
llm_function: COLLABORATE
max_bytes: 2048
naming: p02_handoff.md
core: true
```

## What It Is
A handoff_protocol defines how one agent transfers control to another — what context is passed, what the receiving agent must return, and what triggers the transfer. It is the contract between agents in a multi-agent system. It is NOT a dispatch_rule (P12, which maps keywords to agent_groups) nor a router (which selects the target). Handoff protocols answer "what do I send and what do I get back?" — dispatch rules answer "who gets this task?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `AgentExecutor` tool delegation | Agent calls another agent as a tool |
| LlamaIndex | `SubQuestionQueryEngine` | Decomposes and delegates sub-queries |
| CrewAI | `allow_delegation=True` + task context | Built-in delegation with context propagation |
| DSPy | Module composition / `dspy.ChainOfThought` | Modules pass typed signatures between steps |
| Haystack | Pipeline node connections | Output of one node = input of next |
| OpenAI | Assistants handoff (Swarm pattern) | `transfer_to_agent()` tool pattern from Swarm |
| Anthropic | Tool use for agent dispatch | Agent A calls tool that triggers Agent B |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| trigger | string | required | More specific = fewer false handoffs but may miss edge cases |
| context_passed | list | required | More context = better informed target but higher token cost |
| return_contract | schema | required | Strict contract = reliable integration but less flexible |
| timeout | int | 300s | Longer = more patient but blocks caller |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| File-based handoff | Async multi-terminal agents | orchestrator writes `.claude/handoffs/task_edison.md`, spawns builder_agent |
| Signal-based return | Async completion notification | builder_agent writes signal JSON on completion; orchestrator polls |
| Tool-based handoff | Synchronous agent delegation | Agent A calls `delegate_to(agent_b, context)` tool |
| Queue-based handoff | High-volume multi-agent | Tasks pushed to queue; workers pull and process |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No return contract | Caller doesn't know if handoff succeeded | Define explicit return schema with status codes |
| Passing entire context | Token explosion; target overwhelmed | Pass only relevant context; use seeds/keywords |
| No timeout | Caller blocks forever on hung target | Always set timeout; implement fallback |

## Integration Graph
```
[agent, router] --> [handoff_protocol] --> [agent (target)]
                          |
                   [dispatch_rule (P12), signal_writer]
```

## Decision Tree
- IF agents run in same process THEN tool-based synchronous handoff
- IF agents run in separate terminals THEN file-based async handoff with signals
- IF high volume, many concurrent agents THEN queue-based handoff
- IF simple keyword routing without context THEN dispatch_rule (P12) instead
- DEFAULT: file-based handoff for organization agent_group architecture

## Quality Criteria
- GOOD: Trigger defined; context_passed listed; return_contract specified
- GREAT: Timeout set; error handling for failed handoffs; tested end-to-end across agents
- FAIL: No return contract; passes entire context; no timeout; no error handling

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_handoff_protocol]] | sibling | 0.36 |
| [[handoff-protocol-builder]] | related | 0.36 |
| [[p03_sp_handoff_protocol_builder]] | related | 0.35 |
| [[p01_kc_agent]] | sibling | 0.34 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.34 |
| [[p10_lr_handoff_protocol_builder]] | downstream | 0.33 |
| [[handoff-builder]] | downstream | 0.33 |
| [[bld_collaboration_handoff]] | downstream | 0.32 |
| [[bld_examples_handoff_protocol]] | downstream | 0.31 |
| [[p01_kc_handoff]] | sibling | 0.31 |
