---
id: p01_kc_chinese_llm_ecosystem
kind: knowledge_card
type: domain
pillar: P01
title: 'Chinese LLM Ecosystem: Agent Frameworks and Patterns'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: agent_frameworks
origin: src_standards_global
quality: 9.1
tags:
- chinese-llm
- qwen-agent
- deepseek
- metagpt
- agentscope
- chatglm
tldr: Chinese LLM agent frameworks (Qwen-Agent, lagent, AgentScope, MetaGPT, ChatDev) universally adopt Western English vocabulary
  while contributing MacNet, SOP, reasoning_content, and Puppeteer as original abstractions.
when_to_use: When evaluating Chinese-origin agent frameworks, comparing Eastern/Western ecosystem convergence, or integrating
  Chinese LLM tools into multi-agent systems.
keywords:
- qwen-agent
- metagpt
- agentscope
- lagent
- chatdev
- chinese-ai
long_tails:
- chinese llm agent frameworks comparison
- metagpt sop workflow pattern
axioms:
- Chinese and Western agent frameworks share identical core vocabulary — divergence is in topology and orchestration, not
  terminology
linked_artifacts:
  adw: null
  agent: null
  hop: null
feeds_kinds:
- agent
- function_def
- mcp_server
- workflow
- plugin
- director
density_score: 0.9
---

# Knowledge Card: Chinese LLM Ecosystem

## Quick Reference
```yaml
topic: Chinese LLM Agent Frameworks
scope: Qwen-Agent, lagent, AgentScope, MetaGPT, ChatDev, DeepSeek, ChatGLM3
owner: Alibaba, Shanghai AI Lab, Tsinghua/OpenBMB, DeepSeek AI
criticality: high
finding: Universal English vocabulary adoption — no Chinese-exclusive terms
```

## Framework Profiles

### Qwen-Agent (Alibaba, ~22K stars)
- **Core**: Agent, Tool, Function Calling, MCP integration
- **Differentiator**: `reasoning_content` field for chain-of-thought scratchpad
- **Built-in**: Code Interpreter, RAG pipeline, Memory for multi-turn
- **Note**: First Chinese framework with native MCP support

### lagent (Shanghai AI Lab, ~7K stars)
- **Core**: Agent, AgentMessage, Memory, Action, Tool
- **Differentiator**: PyTorch-inspired layer analogy; `pre_hooks`/`post_hooks` lifecycle
- **AgentStatusCode**: END, STREAM, ERROR enum for execution state
- **Design**: Memory auto-populated on forward pass (neural network metaphor)

### AgentScope (Alibaba/ModelScope, ~9K stars)
- **Core**: Agent, Tool, Skill, Memory, Planning
- **Differentiator**: `message hub` (central bus for multi-agent communication)
- **Built-in**: ReAct agent, workflow graphs, human-in-the-loop
- **Strength**: Flexible multi-agent communication patterns

### MetaGPT (Independent, ~55K stars)
- **Core**: Role, Action, Message, Environment, Memory, Team
- **Differentiator**: `SOP` (Standard Operating Procedure) as formal agent concept
- **Pattern**: Role-based personas (ProductManager, Architect, Engineer)
- **Strength**: Structured multi-role software development simulation

### ChatDev (Tsinghua/OpenBMB, ~27K stars)
- **Core**: Agent, Role, Workflow, Task
- **Differentiator**: `MacNet` (DAG topology for communicative agents), `Puppeteer` (RL-trained orchestrator)
- **Pattern**: Virtual company simulation (CEO, CTO, Programmer roles)
- **Strength**: Novel orchestration topology beyond linear pipelines

### DeepSeek-V3 (~100K stars)
- Base model only — no framework abstractions
- Powers downstream applications through API

### ChatGLM3 (Tsinghua, ~14K stars)
- Bilingual (Chinese/English) LLM with Tool Use / Function Calling
- No agent framework — provides model-level capabilities

## Shared Vocabulary (Universal Across All)

| Term | Used By | Notes |
|------|---------|-------|
| Agent | All 5 frameworks | Core abstraction everywhere |
| Tool | All 5 frameworks | Callable external function |
| Memory | All 5 frameworks | State persistence mechanism |
| Action | lagent, AgentScope, MetaGPT, ChatDev | Executable unit |
| Role | MetaGPT, ChatDev, CrewAI-influenced | Agent identity/persona |
| Message | lagent, AgentScope, MetaGPT | Inter-agent communication |
| Workflow | AgentScope, ChatDev, MetaGPT | Execution graph |

## Original Chinese Contributions

| Innovation | Framework | Description |
|------------|-----------|-------------|
| `reasoning_content` | Qwen-Agent | Dedicated field for chain-of-thought content |
| `MacNet` | ChatDev | Directed acyclic graph for multi-agent communication |
| `SOP` | MetaGPT | Standard Operating Procedure as first-class concept |
| `Puppeteer` | ChatDev | RL-trained central orchestrator pattern |
| `pre_hooks`/`post_hooks` | lagent | Neural-net-inspired lifecycle hooks |
| `message hub` | AgentScope | Central bus for flexible agent communication |

## Flow
```text
[Western Vocabulary] -> [Chinese Framework Adoption] -> [Original Topology/Orchestration Innovations] -> [Convergent Ecosystem]
```

## Golden Rules
- Evaluate Chinese frameworks using the same criteria as Western ones — vocabulary is identical
- Look for innovation in orchestration topology (MacNet, SOP) rather than terminology
- MCP integration is spreading rapidly — Qwen-Agent already native, AgentScope following

## References
- Source: src_standards_global.md (Section 2: Chinese Ecosystem)
- Repos: QwenLM/Qwen-Agent, InternLM/lagent, modelscope/agentscope, geekan/MetaGPT, OpenBMB/ChatDev
