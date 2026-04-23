---
kind: knowledge_card
id: bld_knowledge_card_memory_summary
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for memory_summary production — memory compression specification
sources: LangChain ConversationSummaryMemory, Zep, Letta (MemGPT), progressive summarization literature
quality: 9.2
title: "Knowledge Card Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_memory_summary_builder
  - p03_sp_memory_summary_builder
  - memory-summary-builder
  - bld_examples_memory_summary
  - p01_kc_memory_summary
  - bld_collaboration_memory_summary
  - p01_kc_memory_persistence
  - bld_instruction_memory_summary
  - bld_config_memory_summary
  - ex_context_session_memory
---

# Domain Knowledge: memory_summary
## Executive Summary
Memory summaries are compressed representations of past context injected into LLM prompts to extend effective context beyond the model's raw window. They trade verbatim fidelity for token efficiency, preserving entities, decisions, and action items while dropping greetings, redundant clarifications, and filler. Unlike session_state (ephemeral cursor) and learning_record (persistent patterns), memory_summary is a reusable compression artifact consumed at injection time.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (Memory) |
| llm_function | INJECT |
| layer | runtime |
| machine_format | yaml |
| max_bytes | 2048 |
| naming | p10_summary_{scope}.md |
| id_prefix | p10_ms |

## Compression Methods
| Method | Ratio | Fidelity | Best For |
|--------|-------|----------|----------|
| abstractive | 5:1–20:1 | Semantic only | Long sessions, high turn count |
| extractive | 2:1–5:1 | High (exact phrasing) | Short windows, precise recall |
| hybrid | 4:1–10:1 | Moderate-high | General purpose sessions |
| sliding_window | Continuous | Progressive loss | Long-running continuous agents |

## Trigger Patterns
| Trigger | Condition | Typical Threshold |
|---------|-----------|------------------|
| token_threshold | Total context tokens >= N | 3000–6000 tokens |
| turn_count | Message count >= N | 10–20 turns |
| explicit | Caller invokes summarize() directly | N/A |
| time_based | Elapsed time >= N | Session-specific |

## Retention Taxonomy
Retain: entities (named people, systems, files, URLs, IDs), decisions (explicit commitments), action items (owner + due date), temporal markers (multi-session only).
Drop: greetings, filler, redundant clarification loops, tool call details when only result matters.

## Ecosystem Reference
- **LangChain ConversationSummaryMemory**: abstractive via LLM, progressive per turn
- **Zep**: async server-side summarization, entity extraction, temporal awareness
- **Letta (MemGPT)**: hierarchical — core / archival (vector) / recall (recent window)
- **OpenAI Assistants**: built-in thread summarization with automatic truncation

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No entity retention | Agent hallucinates entity details on reload |
| Over-compression | Action items lost; agent forgets commitments silently |
| No max_tokens cap | Summaries grow unbounded across progressive passes |
| Conflating with session_state | Injecting ephemeral cursor poisons future sessions |
| Lossy abstractive on code | LLM rewrites code incorrectly; use extractive |
| Missing trigger threshold | Context overflows without warning |

## Application
1. Identify source_type: conversation, session, multi-session, or document
2. Choose compression_method based on fidelity needs and turn count
3. Set trigger: token_threshold for budget management, turn_count for structured workflows
4. Define source_window: turns consumed per pass
5. Declare retention: entities (always), decisions (planning agents), action items (commitments)
6. Set freshness_decay: 0.05 long-lived, 0.1 typical session, 0.2+ ephemeral
7. Cap max_tokens to protect downstream context budget

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_memory_summary_builder]] | downstream | 0.44 |
| [[p03_sp_memory_summary_builder]] | downstream | 0.43 |
| [[memory-summary-builder]] | downstream | 0.42 |
| [[bld_examples_memory_summary]] | downstream | 0.38 |
| [[p01_kc_memory_summary]] | sibling | 0.36 |
| [[bld_collaboration_memory_summary]] | downstream | 0.35 |
| [[p01_kc_memory_persistence]] | sibling | 0.34 |
| [[bld_instruction_memory_summary]] | downstream | 0.32 |
| [[bld_config_memory_summary]] | downstream | 0.30 |
| [[ex_context_session_memory]] | related | 0.30 |
