---
kind: knowledge_card
id: bld_knowledge_card_agent
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for agent artifact production
sources: CEX P02 schema, agent_package pattern, agentic AI literature (Anthropic, OpenAI, LangChain)
quality: 9.1
title: "Knowledge Card Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - agent-builder
  - bld_collaboration_agent
  - bld_architecture_agent
  - p01_kc_agent
  - bld_instruction_agent
  - p03_sp_agent_builder
  - bld_collaboration_system_prompt
  - agent-profile-builder
  - agent-package-builder
  - p10_lr_agent-builder
---

# Domain Knowledge: agent
## Executive Summary
An agent is the core runtime identity in an agentic AI system — a persistent persona with scoped capabilities, assigned tools, and a structured file package (agent_package) that makes it portable and searchable. The agent kind defines WHO the LLM becomes when loaded. Every agent requires 10+ spec files covering identity, instructions, examples, error handling, and deployment.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (identity/model) |
| llm_function | BECOME (identity assumption) |
| Required builder specs | 10 minimum (MANIFEST through SYSTEM_INSTRUCTION) |
| Frontmatter fields | 10 required |
| Quality gates | 7 HARD + 10 SOFT |
| Capability bullets | 4-8 concrete, no vague entries |
| Naming | SPEC_{AGENT_UPPER}_{NNN}_{TYPE}.md |
## Patterns
- **BECOME function**: the LLM reads the agent definition and assumes that identity — persona, constraints, and voice
- **agent package structure**: 10 standardized files per agent enable consistent discovery, loading, and auditing
| Spec File | Purpose |
|----------|---------|
| 001_MANIFEST | Identity, version, capabilities |
| 002_QUICK_START | 5-minute onboarding |
| 003_PRIME | Entry point prompt |
| 004_INSTRUCTIONS | Step-by-step execution |
| 005_ARCHITECTURE | Boundary, dependencies |
| 006_OUTPUT_TEMPLATE | Output format with vars |
| 007_EXAMPLES | Golden + anti-examples |
| 008_ERROR_HANDLING | Failure modes |
| 009_UPLOAD_KIT | Deployment guide |
| 010_SYSTEM_INSTRUCTION | Full system prompt |
- **Capability scoping**: 4-8 concrete bullets describing what the agent CAN do — no vague "helps with" entries
- **Boundary discipline**: every agent explicitly lists what it does NOT handle, preventing overlap
- **Routing keywords**: 4-8 specific terms that activate this agent via semantic search
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague capabilities ("can help with tasks") | No routing signal; brain search returns wrong agent |
| Missing boundary list | Agent scope creep; overlaps with siblings |
| Incomplete agent_package (<10 files) | Agent cannot be fully loaded or audited |
| Identity mixed with task instructions | Conflates WHO (agent) with WHAT (action_prompt) |
| Over-scoped (>8 capabilities) | Agent does too much; should be split |
## Application
1. Define persona: name, domain expertise, voice, constraints
2. Scope capabilities: 4-8 concrete, verifiable bullets
3. Map boundaries: 3-5 sibling types this agent does NOT handle
4. Generate agent_package skeleton (10 files minimum)
5. Write routing keywords for semantic discovery
6. Validate: every capability is testsble, every boundary names a real sibling
## References
- Anthropic: System prompt and identity design patterns
- OpenAI: Assistant API — agent definition and tool assignment
- LangChain: Agent classes — ReAct, tool-using, conversational agents
- CEX P02 schema: canonical agent field definitions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | downstream | 0.59 |
| [[bld_collaboration_agent]] | downstream | 0.55 |
| [[bld_architecture_agent]] | downstream | 0.52 |
| [[p01_kc_agent]] | sibling | 0.49 |
| [[bld_instruction_agent]] | downstream | 0.43 |
| [[p03_sp_agent_builder]] | downstream | 0.42 |
| [[bld_collaboration_system_prompt]] | downstream | 0.38 |
| [[agent-profile-builder]] | downstream | 0.37 |
| [[agent-package-builder]] | downstream | 0.36 |
| [[p10_lr_agent-builder]] | downstream | 0.34 |
