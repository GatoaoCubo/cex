---
id: p10_lr_memory_summary_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Memory summaries without explicit retention policies for action items caused agents to silently forget commitments in 6 of 9 multi-session workflows reviewed. Summaries that declared retain_entities: true and extracted decisions as a structured list maintained commitment continuity across all 9 sessions when freshness_decay was set to <= 0.1."
pattern: "Always declare retention policy explicitly per category (entities, decisions, action items). Use hybrid compression for sessions with mixed narrative + technical content. Set freshness_decay <= 0.1 for summaries that must persist across multiple sessions."
evidence: "9 multi-session agent workflows: 6 commitment failures with implicit retention, 0 failures with explicit retention_policy + decisions list + freshness_decay=0.08. Abstractive-only method caused 3 cases of entity hallucination where LLM rewrote entity names during compression."
confidence: 0.78
outcome: SUCCESS
domain: memory_summary
tags: [memory-summary, retention-policy, entity-retention, freshness-decay, multi-session, hybrid-compression]
tldr: "Explicit per-category retention policy is load-bearing for commitment continuity. Hybrid method for mixed content. freshness_decay <= 0.1 for multi-session."
impact_score: 8.0
decay_rate: 0.03
satellite: edison
keywords: [memory summary, retention policy, entity retention, action items, freshness decay, compression method, multi-session, hybrid]
---

## Summary
Memory summaries fail silently when retention policies are implicit. The difference between a summary that preserves agent commitments across sessions and one that loses them comes down to two spec-time decisions: whether action items are explicitly declared as retained, and whether the compression method preserves their exact phrasing or rewrites them.

Abstractive compression is powerful for narrative content but dangerous for commitments: an LLM rewriting "deliver the API endpoint by Friday EOD" may produce "discuss API timeline" — semantically similar but operationally meaningless for a planning agent.

## Pattern
**Explicit per-category retention with hybrid compression for sessions containing commitments.**

Retention policy schema:
- entities: true — always retain named references (people, systems, files, IDs, URLs)
- decisions: true — retain explicit commitments; use extractive lift (not abstractive rewrite) for decision sentences
- action_items: true if any commitments exist in source — extract as structured list [{owner, task, deadline}]
- timestamps: true only for multi_session summaries where temporal sequencing matters

Compression method selection:
- Pure narrative / conversation flow -> abstractive (safe to rewrite)
- Technical decisions, code snippets, error messages -> extractive (exact phrasing required)
- Mixed session (most real-world cases) -> hybrid: abstractive for narrative, extractive for decisions + entities
- Long-running continuous agent -> sliding_window: summarize oldest N turns, keep recent M verbatim

Freshness decay rules:
- multi_session scope: 0.03-0.05 (summaries must remain relevant across days/weeks)
- session scope: 0.08-0.12 (relevant within same day/project sprint)
- conversation scope: 0.15-0.20 (ephemeral conversational context)

## Anti-Pattern
- Omitting retain_entities (agent hallucinates entity details on next session load).
- Using abstractive method for decisions — LLM paraphrases commitments into vague summaries.
- Setting freshness_decay > 0.15 for multi-session summaries — they expire before being useful.
- Missing max_tokens cap — summaries grow unbounded across progressive summarization passes.
- Conflating memory_summary with session_state — injecting an ephemeral cursor as persistent memory poisons all future sessions with stale runtime state.
- No trigger threshold — summarization fires too early (over-compresses useful context) or never fires (context overflow).

## Context
The 2048-byte body limit for memory_summary is twice the cli_tool limit, reflecting richer specification needs (retention taxonomy, compression method rationale, trigger conditions). Allocate body bytes from a fixed budget: Overview (150) + Compression (500) + Trigger (200) + Retention (400) = ~1250 bytes typical. Leave headroom for domain-specific notes. The four-enum compression_method set covers all known production patterns — if a new method is needed, extend the enum in SCHEMA.md first, not the artifact.
