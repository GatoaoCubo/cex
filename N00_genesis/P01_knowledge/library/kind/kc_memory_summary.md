---
id: p01_kc_memory_summary
kind: knowledge_card
type: kind
pillar: P10
title: "Memory Summary — Deep Knowledge for memory_summary"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: memory_summary
quality: 9.1
tags: [memory_summary, P10, INJECT, kind-kc]
tldr: "LLM-compressed digest of prior session memories, injected to bootstrap context without raw history verbosity"
when_to_use: "Building, reviewing, or reasoning about memory_summary artifacts"
keywords: [compression, summary, context-window]
feeds_kinds: [memory_summary]
density_score: null
aliases: ["compressed memory", "session digest", "context summary", "memory compression", "conversation summary"]
user_says: ["compress memory", "comprimir memoria", "summarize past sessions", "reduce context size", "make a memory digest"]
long_tails: ["I need to compress past conversation history to fit the context window", "summarize what happened in previous sessions for the next session", "create a compact digest of prior sessions to bootstrap context cheaply", "reduce memory token usage by compressing old sessions into summaries"]
cross_provider:
  langchain: "ConversationSummaryMemory"
  llamaindex: "ResponseSynthesizer (tree mode)"
  crewai: "Memory LTM + LLM compression"
  dspy: "ChainOfThought summarization module"
  openai: "Thread summarization via gpt-4o"
  anthropic: "System prompt injection of compressed prior"
  haystack: "PromptBuilder + summarization pipeline"
related:
  - p01_kc_session_state
  - p10_memory_summary
  - memory-summary-builder
  - bld_collaboration_memory_summary
  - p01_kc_memory_persistence
  - bld_memory_session_state
  - p01_kc_memory_scope
  - p01_kc_learning_record
  - bld_knowledge_card_memory_summary
  - bld_examples_memory_summary
---

# Memory Summary

## Spec
```yaml
kind: memory_summary
pillar: P10
llm_function: INJECT
max_bytes: 2048
naming: p10_summary.md
core: true
```

## What It Is
A memory summary is a compressed, LLM-generated digest of prior session memories that fits within a tight context budget. It is written at session end and injected at session start as a compact briefing. Unlike session_state (ephemeral snapshot of current run), a memory summary persists across sessions and is intentionally lossy — trading completeness for token efficiency.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ConversationSummaryMemory` | Native summary memory — LLM compresses chat history on overflow |
| LlamaIndex | `ResponseSynthesizer` (tree mode) | Hierarchical synthesis can compress large doc sets to summaries |
| CrewAI | `Memory` LTM + LLM compression pass | Long-term memory uses embedding store; summary is a retrieval digest |
| DSPy | `ChainOfThought` summarization module | Custom module wrapping history compression |
| Haystack | `PromptBuilder` + summarization pipeline | No native; build summarize pipeline component |
| OpenAI | Thread summarization via gpt-4o | Periodic summarize-and-truncate pattern for long threads |
| Anthropic | System prompt injection of compressed prior | Compress via claude-haiku, inject in next session system block |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| max_bytes | int | 2048 | Lower = less context cost; higher = more fidelity |
| compression_ratio | float | 0.15 | 15% of source = aggressive; 30% = balanced fidelity |
| sections | list | [decisions, failures, state] | Include only actionable sections; drop narrative |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Rolling summary | Long-running agents (>10 sessions) | Summarize last 5 sessions, drop older; keep last 2 raw |
| Section-structured digest | Multi-domain agents with varied context | Split into `decisions:`, `failures:`, `open_items:` sections |
| Score-filtered injection | Only inject if summary score >= 7.0 | Low-quality sessions generate noise, skip injection |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Injecting full raw history | Context window overflow; LLM buries key facts | Compress to 2048 bytes max before injection |
| Summarizing single session | Not enough signal; creates administrative overhead | Accumulate 3+ sessions before writing summary |
| Lossy compression of critical state | Active task state corrupted by summarization | Keep active session_state separate; never summarize in-progress work |

## Integration Graph
```
[session_state] --> [memory_summary] --> [action_prompt]
[learning_record] ----^
```

## Decision Tree
- IF context budget < 20% remaining THEN trigger memory summary compression
- IF session count >= 3 THEN write rolling summary replacing oldest entries
- IF session is in-progress THEN do NOT summarize; use session_state instead
- DEFAULT: Write summary at session end; inject at next session start

## Quality Criteria
- GOOD: Under 2048 bytes; covers decisions, failures, open items; readable by LLM
- GREAT: Section headers; scored entries prioritized; compression ratio documented
- FAIL: Raw dump of messages; >2048 bytes; no structure; summarizes single low-value session

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_session_state]] | sibling | 0.43 |
| [[p10_memory_summary]] | related | 0.42 |
| [[memory-summary-builder]] | related | 0.40 |
| [[bld_collaboration_memory_summary]] | downstream | 0.39 |
| [[p01_kc_memory_persistence]] | sibling | 0.36 |
| [[bld_memory_session_state]] | related | 0.34 |
| [[p01_kc_memory_scope]] | sibling | 0.34 |
| [[p01_kc_learning_record]] | sibling | 0.33 |
| [[bld_knowledge_card_memory_summary]] | sibling | 0.33 |
| [[bld_examples_memory_summary]] | upstream | 0.31 |
