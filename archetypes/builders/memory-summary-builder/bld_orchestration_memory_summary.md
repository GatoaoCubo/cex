---
kind: collaboration
id: bld_collaboration_memory_summary
pillar: P12
llm_function: COLLABORATE
purpose: How memory-summary-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_memory_scope
  - memory-summary-builder
  - bld_collaboration_compression_config
  - bld_collaboration_session_backend
  - bld_collaboration_builder
  - bld_collaboration_session_state
  - bld_collaboration_knowledge_card
  - bld_collaboration_runtime_state
  - bld_collaboration_learning_record
  - p03_sp_memory_summary_builder
---

# Collaboration: memory-summary-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this conversation or session be compressed, when should it fire, and what information must survive?"
I do not build ephemeral runtime snapshots. I do not define persistent learned patterns. I do not retrieve or embed summaries.
I specify memory compression artifacts so agents can extend their effective context window without ballooning token costs.

## Crew Compositions
### Crew: "Memory Stack"
```
  1. memory-summary-builder -> "compression spec (method, trigger, retention)"
  2. session-state-builder   -> "ephemeral runtime cursor (current task, tool state)"
  3. learning-record-builder -> "persistent behavioral patterns extracted from sessions"
```
### Crew: "Long-Running Agent Memory"
```
  1. memory-summary-builder  -> "sliding_window compression spec for continuous agent"
  2. retrieval-builder        -> "vector index and semantic search over stored summaries"
  3. injection-builder        -> "runtime context assembly — where and how to prepend summary"
```
### Crew: "Multi-Session Knowledge"
```
  1. memory-summary-builder  -> "cross-session compression spec (multi_session source_type)"
  2. knowledge-card-builder  -> "stable domain knowledge that never needs recompression"
  3. learning-record-builder -> "patterns extracted from compressed summaries over time"
```

## Handoff Protocol
### I Receive
- seeds: source_type, content volume estimate, fidelity requirements, retention needs
- optional: existing session_state for boundary clarification, max token budget for output
### I Produce
- memory_summary artifact (.md + .yaml frontmatter)
- committed to: `cex/P10_memory/examples/p10_summary_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None — independent builder (layer 0). Memory summaries can be defined standalone without other artifacts.

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| injection-builder | Injection specs reference memory_summary artifacts as the content to prepend |
| retrieval-builder | Retrieval indexes are built over stored memory_summary outputs |
| session-state-builder | Session state may reference active memory_summary id for context chain |
| agent-builder | Agents declare which memory_summary spec governs their context compression |

## Boundary Contracts
| I hand off to | When | What I pass |
|---------------|------|-------------|
| session-state-builder | Requester needs ephemeral runtime cursor, not compression spec | Scope description + runtime fields needed |
| learning-record-builder | Requester needs to persist a behavioral pattern, not compress conversation | Pattern description + evidence |
| knowledge-card-builder | Requester needs static domain knowledge artifact, not session compression | Domain topic + knowledge type |
| retrieval-builder | Requester needs semantic search over summaries, not the summary spec itself | Summary id + embedding requirements |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | sibling | 0.46 |
| [[memory-summary-builder]] | upstream | 0.46 |
| [[bld_collaboration_compression_config]] | sibling | 0.43 |
| [[bld_collaboration_session_backend]] | sibling | 0.41 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_collaboration_session_state]] | sibling | 0.36 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.35 |
| [[bld_collaboration_runtime_state]] | sibling | 0.35 |
| [[bld_collaboration_learning_record]] | sibling | 0.34 |
| [[p03_sp_memory_summary_builder]] | upstream | 0.33 |
