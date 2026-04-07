---
kind: collaboration
id: bld_collaboration_session_backend
pillar: P12
llm_function: COLLABORATE
purpose: How session-backend-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: session-backend-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "where and how should this agent persist its session state between turns?"
I do not reduce context tokens. I do not decide what to remember long-term.
I specify session storage so agents maintain state across turns and restarts.
## Crew Compositions
### Crew: "Context Management"
```
  1. token-budget-builder -> "total token allocation per section"
  2. compression-config-builder -> "compression strategy when budget is exhausted"
  3. session-backend-builder -> "where to persist compressed state"
```
### Crew: "Full Agent Infrastructure"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "provider startup configuration"
  3. env-config-builder -> "environment variables"
  4. session-backend-builder -> "state persistence backend"
  5. compression-config-builder -> "context compression strategy"
  6. trace-config-builder -> "execution tracing and observability"
```
## Handoff Protocol
### I Receive
- seeds: target scope, expected concurrency, data sensitivity level, infrastructure availability
- optional: backend preference, TTL override, encryption level, serialization format
### I Produce
- session_backend artifact (.md + .yaml frontmatter)
- committed to: `cex/P10/examples/p10_sb_{backend}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- env-config-builder: provides connection_string variables for redis/postgres backends
- boot-config-builder: reveals when sessions are created/loaded during boot
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| compression-config-builder | Needs to know where compressed state is persisted |
| memory-builder | Long-term memory writes to the session backend |
| coordinator config | Cross-nucleus handoffs route through session storage |
