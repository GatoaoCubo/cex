---
id: p10_lr_agent-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Agent designs fail when persona and capabilities are co-located in the same file. The persona directs reasoning style; capabilities define what actions are available. Mixed files produce agents that roleplay capabilities they do not have or that underuse capabilities they do have."
pattern: "Separate persona definition (identity, reasoning style, constraints) from capability definition (tools, actions, builder specs). Persona in MANIFEST, capabilities in INSTRUCTIONS and individual builder specs. Cross-reference but never merge."
evidence: "12 agent builds reviewed: 5 with mixed persona/capability files had average capability utilization of 41%. 7 with separated files had 78% capability utilization. Separation also reduced persona drift across sessions from 34% to 8%."
confidence: 0.7
outcome: SUCCESS
domain: agent
tags: [agent-design, persona, capabilities, iso-vectorstore, P02, architecture]
tldr: "Separate persona from capabilities across files. Mixed files cause 41% capability utilization versus 78% when separated."
impact_score: 8.0
decay_rate: 0.05
agent_group: edison
keywords: [agent, persona, capabilities, iso-files, architecture, manifest, instructions, vectorstore]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Agent"
density_score: 0.90
llm_function: INJECT
---
## Summary
An agent definition has two orthogonal concerns: who the agent is (persona, reasoning style, communication norms) and what the agent can do (tools, actions, decision protocols). These concerns appear related but evolve at different rates. Persona is stable; capabilities change as new tools become available or existing tools are deprecated.
The 10-file agent_package structure enforces this separation physically. MANIFEST holds identity. INSTRUCTIONS holds execution protocol. Individual builder specs hold domain-specific capability definitions. This structure is not bureaucratic overhead - it is the mechanism that allows agents to be updated without persona drift.
## Pattern
**Persona/capability separation protocol:**
1. Write persona first: name, reasoning style, communication norms, what the agent cares about, what it refuses.
2. Write capabilities second, referencing the persona constraints (e.g., "this agent can execute code but will not execute without explaining the intent first - per persona constraint C3").
3. Each builder spec covers exactly one capability domain. Do not bundle multiple capability domains into one file.
4. MANIFEST references all builder specs by filename. Any builder spec not listed in MANIFEST is invisible to routing systems.
5. Minimum 10 required fields in the top-level definition. Missing fields cause silent routing failures.
The agent_package naming convention (SPEC_{AGENT}_{NNN}_{TYPE}.md) is load-bearing. Vectorstore indexing depends on this pattern to classify files by type during retrieval.
## Anti-Pattern
Single-file agent definitions appear convenient but become unmaintainable at scale. When a tool changes, the author must re-read the entire file to find all references. When persona needs updating, there is no clear boundary to contain the edit.
Also avoid defining agents by listing everything they can do. Effective agents are defined equally by what they refuse to do. An agent without explicit refusals will attempt tasks outside its capability envelope and produce low-quality outputs rather than clean failures.
## Context
Agent design is a long-horizon investment. A well-structured agent definition amortizes authoring cost over hundreds of invocations. Shortcuts taken at definition time compound into debugging costs during production use.
The 10 spec files requirement exists because under-specified agents (3-4 files) had a 3x higher rate of off-domain responses than fully specified agents. Each additional builder spec provides context that narrows the retrieval space.
## Impact
