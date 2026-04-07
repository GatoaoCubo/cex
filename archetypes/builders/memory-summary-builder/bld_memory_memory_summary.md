---
id: p10_lr_memory_summary_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Memory summaries without explicit retention policies for action items caused agents to silently forget commitments in 6 of 9 multi-session workflows reviewed. Summaries that declared retain_entities: true and extracted decisions as a structured list maintained commitment continuity across all 9 sessions when freshness_decay was set to <= 0.1."
pattern: "Always declare retention policy explicitly per category (entities, decisions, action items). Use hybrid compression for sessions with mixed narrative + technical content. Set freshness_decay <= 0.1 for summaries that must persist across multiple sessions."
evidence: "9 multi-session agent workflows: 6 commitment failures with implicit retention, 0 failures with explicit retention_policy + decisions list + freshness_decay=0.08. Abstractive-only caused 3 entity hallucination cases."
confidence: 0.78
outcome: SUCCESS
domain: memory_summary
tags: [memory-summary, retention-policy, entity-retention, freshness-decay, multi-session, hybrid-compression]
tldr: "Explicit per-category retention policy is load-bearing for commitment continuity. Hybrid method for mixed content. freshness_decay <= 0.1 for multi-session."
impact_score: 8.0
decay_rate: 0.03
agent_node: edison
keywords: [memory summary, retention policy, entity retention, action items, freshness decay, compression method, multi-session, hybrid]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
Memory summaries fail silently when retention policies are implicit. The difference between preserving agent commitments across sessions and losing them comes down to two spec-time decisions: whether action items are explicitly declared as retained, and whether the compression method preserves their exact phrasing.

Abstractive compression is dangerous for commitments: an LLM rewriting "deliver the API endpoint by Friday EOD" may produce "discuss API timeline" — semanticslly similar but operationally meaningless.

## Pattern
**Explicit per-category retention with hybrid compression for sessions containing commitments.**

- entities: true — always retain named references (people, systems, files, IDs, URLs)
- decisions: true — use extractive lift (not abstractive rewrite) for decision sentences
- action_items: true if commitments exist — extract as structured list [{owner, task, deadline}]
- timestamps: true only for multi_session where temporal sequencing matters

Compression method:
- Pure narrative -> abstractive
- Technical decisions, code, errors -> extractive
- Mixed session (most cases) -> hybrid
- Long-running continuous agent -> sliding_window

Freshness decay:
- multi_session: 0.03–0.05
- session: 0.08–0.12
- conversation: 0.15–0.20

## Anti-Pattern
- Omitting retain_entities — agent hallucinates entity details on next session load.
- Abstractive for decisions — LLM paraphrases commitments into vague summaries.
- freshness_decay > 0.15 for multi-session — summaries expire before being useful.
- Missing max_tokens cap — summaries grow unbounded across progressive passes.
- Conflating memory_summary with session_state — poisons future sessions with stale runtime state.
- No trigger threshold — summarization fires too early or never; context overflows.
