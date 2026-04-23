---
kind: knowledge_card
id: bld_knowledge_card_handoff_protocol
pillar: P02
llm_function: INJECT
purpose: Domain knowledge for handoff_protocol production
sources: A2A protocol spec (Google), Swarm handoff patterns, multi-agent orchestration research, organization agent_group dispatch
quality: 9.0
title: "Knowledge Card Handoff Protocol"
version: "1.0.0"
author: n03_builder
tags: [handoff_protocol, builder, examples]
tldr: "Golden and anti-examples for handoff protocol construction, demonstrating ideal structure and common pitfalls."
domain: "handoff protocol construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_handoff_protocol_builder
  - handoff-protocol-builder
  - p01_kc_handoff_protocol
  - bld_collaboration_handoff_protocol
  - p03_sp_handoff_protocol_builder
  - bld_examples_handoff_protocol
  - bld_instruction_handoff_protocol
  - handoff-builder
  - bld_collaboration_handoff
  - p01_kc_handoff
---

# Domain Knowledge: handoff_protocol
## Executive Summary
Handoff protocol — trigger conditions, context passed, return contract between agents. Produced as P02 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 |
| llm_function | COLLABORATE |
| Max bytes | 2048 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Fire-and-forget | Source sends task, does not wait for result | Async logging, notifications, non-blocking side effects |
| Request-response | Source sends task and blocks until result returns | Sequential pipelines, dependent computations |
| Streaming | Target sends incremental results back to source | Long-running tasks with progress updates |
| Escalation | Target cannot complete, escalates back with partial context | Error recovery, human-in-the-loop |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No return contract | Caller cannot validate or use result — silent type mismatch |
| Passing full context | Token waste; pass only what target needs |
| No timeout | Hung handoff blocks entire pipeline indefinitely |
| Implicit trigger | Handoff fires on vague conditions, causing spurious delegations |
## Application
1. Identify the use case and constraints
2. Select apownte pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p02_handoff_[a-z][a-z0-9_]+$`
## References
- Google A2A Task lifecycle, OpenAI Swarm Handoff, Anthropic tool_use handoff, CrewAI delegation, AutoGen handoff
- A2A protocol spec (Google), Swarm handoff patterns, multi-agent orchestration research, organization agent_group dispatch

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_handoff_protocol_builder]] | downstream | 0.52 |
| [[handoff-protocol-builder]] | related | 0.45 |
| [[p01_kc_handoff_protocol]] | sibling | 0.40 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.37 |
| [[p03_sp_handoff_protocol_builder]] | related | 0.36 |
| [[bld_examples_handoff_protocol]] | downstream | 0.34 |
| [[bld_instruction_handoff_protocol]] | downstream | 0.33 |
| [[handoff-builder]] | downstream | 0.33 |
| [[bld_collaboration_handoff]] | downstream | 0.31 |
| [[p01_kc_handoff]] | sibling | 0.30 |
