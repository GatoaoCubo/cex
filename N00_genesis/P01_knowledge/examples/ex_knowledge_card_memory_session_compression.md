---
id: p01_kc_memory_session_compression
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Session Compression via Agent SDK for LLM Memory Decay"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: llm_memory
quality: 9.1
tags: [compression, memory-decay, agent-sdk, session-resume, memory-systems]
tldr: "Observations accumulate per-session; Stop hook compresses them into a summary via Agent SDK resume sessions, using dual session IDs"
when_to_use: "Building memory systems where raw observations grow unboundedly and need end-of-session compression"
keywords: [session-compression, memory-decay, agent-sdk, dual-session-id, observation-summary]
long_tails:
  - "How to compress LLM agent session observations into summaries"
  - "How to use dual session IDs for memory and content separation"
axioms:
  - "SEMPRE compress at Stop (once/session), never at PostToolUse"
  - "NUNCA resume SDK session with contentSessionId"
  - "NUNCA delete raw observations after compression"
linked_artifacts:
  primary: p01_kc_memory_privacy_controls
  related: [p01_kc_cex_function_inject]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
related:
  - p10_ax_session_compression
  - bld_memory_session_state
  - p01_kc_session_state
  - p01_kc_session_backend
  - kc_sdk_example
  - bld_architecture_session_backend
  - p01_kc_memory_summary
  - bld_collaboration_session_backend
  - p03_sp_session_state_builder
  - bld_tools_session_state
---

## Summary

Session compression solves unbounded context growth in LLM memory systems. Raw observations accumulate during a session via PostToolUse hooks, stored in SQLite with tool name, input, output, and title. When the Stop hook fires, the worker loads all observations for the session, builds a compression prompt, and calls the Claude Agent SDK to produce a narrative summary.

The compressed summary (~100 tokens) replaces verbose observations at session start. Next session loads the summary plus recent relevant observations as context, achieving progressive disclosure: minimal tokens for continuity, full observations available on demand via citation links.

Two session IDs prevent a critical confusion. The contentSessionId is stable across the session lifetime and used as the foreign key for observation storage. The memorySessionId is an SDK-internal identifier captured lazily from the first system init message and used exclusively for SDK resume calls. Mixing them causes either lost observations or broken resumes.

The Agent SDK v2 uses `await using` (Explicit Resource Management) for automatic session cleanup. First call creates a fresh session; subsequent calls resume with the captured memorySessionId. NULL check on memorySessionId is mandatory: NULL means the SDK session has not been initialized yet.

## Spec

| Component | Value | Detail |
|-----------|-------|--------|
| Compression trigger | Stop hook | Once per session, not per tool |
| SDK API | unstable_v2 | createSession / resumeSession |
| contentSessionId | Stable | DB foreign key, never for resume |
| memorySessionId | Lazy-captured | From system init msg, SDK only |
| Storage | SQLite | summaries + observations tables |
| Summary size | ~100 tokens | Injected at next SessionStart |
| Raw observations | Kept | Citation links remain valid |
| Resource mgmt | `await using` | Auto-closes SDK session |

## Patterns

| Trigger | Action |
|---------|--------|
| Stop hook fires | Load observations, compress via SDK |
| memorySessionId is NULL | Create fresh SDK session (no resume) |
| memorySessionId is set | Resume existing SDK session |
| New session starts | Inject summary + recent observations |
| Need full observation | Fetch via citation link on demand |

## Anti-Patterns

- Compressing at PostToolUse (fires per tool, cost explosion)
- Resuming with contentSessionId (resumes wrong session)
- Skipping NULL check on memorySessionId (crash on resume)
- Deleting raw observations post-compression (breaks citations)
- Growing context unboundedly without compression (token cost)

## Code

<!-- lang: typescript | purpose: Agent SDK session compression -->
```typescript
import {
  unstable_v2_createSession,
  unstable_v2_resumeSession
} from '@anthropic-ai/claude-agent-sdk';

// First call: fresh session
await using session = unstable_v2_createSession({
  model: 'sonnet'
});

// Resume: use memorySessionId (NEVER contentSessionId)
await using session = unstable_v2_resumeSession(
  memorySessionId, { model: 'sonnet' }
);

// NULL-based resume detection
const hasReal = session.memorySessionId !== null;
const options = {
  ...(hasReal && { resume: session.memorySessionId })
};
// hasReal=false -> fresh SDK session
// hasReal=true  -> resume existing session
```

## References

- source: https://github.com/thedotmack/claude-mem
- source: https://docs.anthropic.com/en/docs/agents
- related: p01_kc_memory_privacy_controls
- related: p01_kc_cex_function_inject

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_ax_session_compression]] | downstream | 0.44 |
| [[bld_memory_session_state]] | downstream | 0.40 |
| [[p01_kc_session_state]] | sibling | 0.38 |
| [[p01_kc_session_backend]] | sibling | 0.35 |
| [[kc_sdk_example]] | sibling | 0.29 |
| [[bld_architecture_session_backend]] | downstream | 0.29 |
| [[p01_kc_memory_summary]] | sibling | 0.29 |
| [[bld_collaboration_session_backend]] | downstream | 0.29 |
| [[p03_sp_session_state_builder]] | downstream | 0.28 |
| [[bld_tools_session_state]] | downstream | 0.28 |
