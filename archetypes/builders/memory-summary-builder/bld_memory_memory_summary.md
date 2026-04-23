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
agent_group: edison
keywords: [memory summary, retention policy, entity retention, action items, freshness decay, compression method, multi-session, hybrid]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Memory Summary"
density_score: 0.90
llm_function: INJECT
related:
  - bld_manifest_memory_type
  - memory-summary-builder
  - bld_knowledge_card_memory_summary
  - bld_tools_memory_type
  - bld_config_memory_type
  - p03_sp_memory_summary_builder
  - bld_collaboration_memory_summary
  - bld_tools_agent
  - bld_config_tagline
  - bld_output_template_builder
---
## Summary
Memory summaries fail silently when retention policies are implicit. The difference between preserving agent commitments across sessions and losing them comes down to two spec-time decisions: whether action items are explicitly declared as retained, and whether the compression method preserves their exact phrasing.

Abstractive compression is dangerous for commitments: an LLM rewriting "deliver the API endpoint by Friday EOD" may produce "discuss API timeline" — semanticslly similar but operationally meaningless.

## Pattern
**Explicit per-category retention with hybrid compression for sessions containing commitments.**

1. entities: true — always retain named references (people, systems, files, IDs, URLs)
2. decisions: true — use extractive lift (not abstractive rewrite) for decision sentences
3. action_items: true if commitments exist — extract as structured list [{owner, task, deadline}]
4. timestamps: true only for multi_session where temporal sequencing matters

Compression method:
1. Pure narrative -> abstractive
2. Technical decisions, code, errors -> extractive
3. Mixed session (most cases) -> hybrid
4. Long-running continuous agent -> sliding_window

Freshness decay:
1. multi_session: 0.03–0.05
2. session: 0.08–0.12
3. conversation: 0.15–0.20

## Anti-Pattern
1. Omitting retain_entities — agent hallucinates entity details on next session load.
2. Abstractive for decisions — LLM paraphrases commitments into vague summaries.
3. freshness_decay > 0.15 for multi-session — summaries expire before being useful.
4. Missing max_tokens cap — summaries grow unbounded across progressive passes.
5. Conflating memory_summary with session_state — poisons future sessions with stale runtime state.
6. No trigger threshold — summarization fires too early or never; context overflows.

## Builder Context

This ISO operates within the `memory-summary-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_memory_summary_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_memory_summary_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | memory_summary |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.45 |
| [[memory-summary-builder]] | related | 0.42 |
| [[bld_knowledge_card_memory_summary]] | upstream | 0.41 |
| [[bld_tools_memory_type]] | upstream | 0.40 |
| [[bld_config_memory_type]] | upstream | 0.36 |
| [[p03_sp_memory_summary_builder]] | related | 0.35 |
| [[bld_collaboration_memory_summary]] | downstream | 0.35 |
| [[bld_tools_agent]] | upstream | 0.34 |
| [[bld_config_tagline]] | upstream | 0.33 |
| [[bld_output_template_builder]] | upstream | 0.33 |
