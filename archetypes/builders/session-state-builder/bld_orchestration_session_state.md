---
kind: collaboration
id: bld_collaboration_session_state
pillar: P10
llm_function: COLLABORATE
purpose: How session-state-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Session State"
version: "1.0.0"
author: n03_builder
tags: [session_state, builder, examples]
tldr: "Golden and anti-examples for session state construction, demonstrating ideal structure and common pitfalls."
domain: "session state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - session-state-builder
  - p03_sp_session_state_builder
  - bld_collaboration_signal
  - bld_architecture_session_state
  - bld_memory_session_state
  - bld_collaboration_checkpoint
  - bld_collaboration_runtime_state
  - p01_kc_session_state
  - bld_collaboration_session_backend
  - runtime-state-builder
---

# Collaboration: session-state-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the agent's current session state right now?"
I capture ephemeral in-session snapshots — context window usage, active task, checkpoint progress, and recovery pointers. I do NOT handle persistent state across sessions (runtime-state-builder), accumulated learning over time (learning-record-builder), or search indexes.
## Crew Compositions
### Crew: "Agent Resilience System"
```
  1. session-state-builder  -> "snapshots ephemeral context: tokens used, current task, checkpoint"
  2. runtime-state-builder  -> "persists durable state that survives session boundaries"
  3. fallback-chain-builder -> "uses checkpoint data from session_state to define recovery paths"
```
### Crew: "Long-Running Task Coordination"
```
  1. session-state-builder -> "captures mid-execution checkpoint so work can resume after interruption"
  2. signal-builder        -> "emits a progress signal derived from the session_state checkpoint data"
  3. handoff-builder       -> "packages session state + progress signal into a resumable handoff"
```
### Crew: "Context Overflow Protection"
```
  1. session-state-builder -> "tracks tokens_used and context_window fields to detect overflow risk"
  2. skill-builder         -> "defines the overflow-protection skill that reads session state and compresses"
  3. lifecycle-rule-builder -> "establishes rules for when to checkpoint based on session state thresholds"
```
## Handoff Protocol
### I Receive
- seeds: agent ID, current task description, tokens used, active tool calls
- optional: checkpoint label, recovery pointer, priority queue of pending items
### I Produce
- session_state artifact (YAML, fields: agent_id, task, tokens_used, checkpoint, timestamp, max 80 lines)
- committed to: `cex/P10/examples/session-state-{agent}-{timestamp}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- None required. Session state is captured from live agent execution context.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| runtime-state-builder  | promotes durable fields from session_state into persistent storage |
| fallback-chain-builder | reads checkpoint data from session_state to define recovery entry points |
| signal-builder         | extracts progress percentage from session_state to populate progress signals |
| handoff-builder        | embeds session_state snapshot into handoff for cross-session resumption |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[session-state-builder]] | related | 0.54 |
| [[p03_sp_session_state_builder]] | upstream | 0.51 |
| [[bld_collaboration_signal]] | sibling | 0.49 |
| [[bld_architecture_session_state]] | upstream | 0.48 |
| [[bld_memory_session_state]] | related | 0.47 |
| [[bld_collaboration_checkpoint]] | sibling | 0.46 |
| [[bld_collaboration_runtime_state]] | sibling | 0.44 |
| [[p01_kc_session_state]] | related | 0.40 |
| [[bld_collaboration_session_backend]] | sibling | 0.40 |
| [[runtime-state-builder]] | related | 0.38 |
