---
kind: collaboration
id: bld_collaboration_compression_config
pillar: P12
llm_function: COLLABORATE
purpose: How compression-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_session_backend
  - bld_collaboration_memory_summary
  - bld_collaboration_memory_scope
  - bld_collaboration_context_window_config
  - compression-config-builder
  - bld_collaboration_agent
  - bld_architecture_compression_config
  - bld_collaboration_boot_config
  - bld_collaboration_builder
  - p03_sp_compression_config_builder
---

# Collaboration: compression-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this agent compress its context when approaching the token limit?"
I do not allocate token budgets. I do not persist session state.
I specify compression strategies so agents degrade gracefully under token pressure.
## Crew Compositions
### Crew: "Context Management"
```
  1. token-budget-builder -> "total token allocation per section"
  2. compression-config-builder -> "compression strategy when budget is exhausted"
  3. session-backend-builder -> "where to persist compressed state"
```
### Crew: "Long-Running Agent Setup"
```
  1. agent-builder -> "agent definition"
  2. token-budget-builder -> "token allocation"
  3. compression-config-builder -> "context compression strategy"
  4. memory-builder -> "long-term memory policy"
  5. session-backend-builder -> "state persistence"
```
## Handoff Protocol
### I Receive
- seeds: target agent/scope, model context window size, message type catalog
- optional: trigger_ratio preference, preserve_types override, strategy preference
### I Produce
- compression_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P10/examples/p10_cc_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- token-budget-builder: reveals the total token budget that sets the compression ceiling
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| session-backend-builder | Needs to know what compressed state to persist |
| memory-builder | Needs compression policy to decide what survives long-term |
| crew-runner config | Reads compression_config before assembling prompts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_session_backend]] | sibling | 0.63 |
| [[bld_collaboration_memory_summary]] | sibling | 0.44 |
| [[bld_collaboration_memory_scope]] | sibling | 0.42 |
| [[bld_collaboration_context_window_config]] | sibling | 0.42 |
| [[compression-config-builder]] | upstream | 0.40 |
| [[bld_collaboration_agent]] | sibling | 0.37 |
| [[bld_architecture_compression_config]] | upstream | 0.36 |
| [[bld_collaboration_boot_config]] | sibling | 0.36 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[p03_sp_compression_config_builder]] | upstream | 0.34 |
