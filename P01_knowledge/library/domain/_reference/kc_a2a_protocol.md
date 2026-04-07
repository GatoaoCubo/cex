---
id: p01_kc_a2a_protocol
kind: knowledge_card
type: domain
pillar: P01
title: 'Google A2A Protocol: Agent-to-Agent Communication Standard'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: agent_interoperability
origin: src_standards_global
quality: 9.1
tags:
- a2a
- google
- agent-protocol
- interoperability
- standard
tldr: Google A2A defines Agent, Task, AgentCard, Artifact, and TaskState as the wire-level contract for autonomous agent-to-agent
  communication over HTTPS+SSE.
when_to_use: When designing multi-agent systems that need interoperability between independently deployed agents, or when
  implementing agent discovery and task delegation.
keywords:
- a2a
- agent-card
- task-state
- artifact
- agent-interoperability
long_tails:
- how does google a2a agent discovery work
- a2a task lifecycle states explained
axioms:
- Agents are opaque autonomous units — communicate via messages, never share internals
linked_artifacts:
  adw: null
  agent: null
  hop: null
feeds_kinds:
- agent
- handoff_protocol
- signal
- checkpoint
- mcp_server
density_score: 0.92
---

# Knowledge Card: Google A2A Protocol

## Quick Reference
```yaml
topic: Google Agent-to-Agent (A2A) Protocol
scope: Inter-agent communication standard (wire-level)
owner: Google DeepMind
criticality: high
spec_date: 2025
transport: HTTPS + SSE (Server-Sent Events)
message_format: JSON-RPC 2.0
```

## Core Entities

### Agent
- Autonomous opaque unit with skills and identity
- Discoverable via AgentCard at `/.well-known/agent.json`
- Exposes capabilities but never internal implementation

### Task
- Unit of work assigned to an agent; has full lifecycle
- Created by a client agent, executed by a remote agent
- Contains Messages (input) and produces Artifacts (output)

### AgentCard
- Metadata JSON describing agent capabilities, endpoint URL, supported skills
- Published at a well-known URL for discovery
- Contains: name, description, skills[], endpoint, authentication requirements

### Artifact
- Output produced by a completed or in-progress task
- Typed content: text, file, or structured data
- Composed of Parts (TextPart, FilePart, DataPart)

### TaskState
- Lifecycle enum governing task progression:
  - `submitted` — task created, not yet picked up
  - `working` — agent actively processing
  - `input-required` — agent needs more info from caller
  - `completed` — task finished successfully
  - `failed` — task terminated with error
  - `canceled` — task aborted by caller

## Supporting Concepts

| Concept | Role |
|---------|------|
| **AgentSkill** | Specific capability an agent advertises in its AgentCard |
| **Message** | Conversational exchange between user/client and agent |
| **Part** | Typed content unit: TextPart, FilePart, DataPart |
| **PushNotification** | Webhook callback for async task status updates |

## Flow
```text
[Discover AgentCard] -> [Create Task] -> [Send Messages] -> [Monitor TaskState] -> [Receive Artifacts]
```

## Key Design Decisions
- Agents are **opaque** — no shared memory, no internal state exposure
- Communication is **asynchronous** by default (SSE streaming + webhooks)
- Tasks have **first-class lifecycle** with explicit state machine
- Discovery is **decentralized** via well-known URLs (no central registry required)

## Comparison: A2A vs MCP
| Dimension | MCP (Anthropic) | A2A (Google) |
|-----------|-----------------|--------------|
| Focus | Client-to-server tool access | Agent-to-agent delegation |
| Core unit | Tool (function call) | Task (work unit with lifecycle) |
| Discovery | Server capabilities negotiation | AgentCard at well-known URL |
| Transport | stdio, SSE, HTTP | HTTPS + SSE |
| State | Session-scoped | Task lifecycle (6 states) |
| Complementary | Yes — MCP for tools, A2A for agent delegation |

## Adoption (as of 2025-2026)
- Integrated by: AgentScope, LangGraph, BeeAI
- Wire format: JSON-RPC 2.0 over HTTPS
- Growing ecosystem alongside MCP (complementary, not competing)

## Golden Rules
- Always publish an AgentCard with accurate skill descriptions
- Design for async-first: use PushNotification for long-running tasks
- Never expose agent internals — communicate only via Messages and Artifacts

## References
- Spec: github.com/google/A2A
- Source: src_standards_global.md (Section 1: Standards & Specs)
- Related: MCP (Anthropic), OpenAPI 3.1, JSON-LD 1.1
