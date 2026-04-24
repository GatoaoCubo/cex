---
id: memory_architecture_n01
kind: memory_architecture
8f: F3_inject
pillar: P10
nucleus: n01
title: "N01 Intelligence Memory Architecture"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [memory_architecture, n01, memory_layers, persistence, retrieval, analytical_envy]
tldr: "4-layer memory architecture for N01: working (session context), episodic (research sessions), semantic (KCs + entities), procedural (methods). Maps storage, retrieval, and decay rules for each layer."
density_score: 0.91
updated: "2026-04-17"
related:
  - p01_kc_memory_scope
  - bld_knowledge_card_memory_architecture
  - bld_collaboration_memory_type
  - bld_output_template_memory_architecture
  - bld_examples_memory_scope
  - memory-architecture-builder
  - bld_collaboration_memory_scope
  - atom_22_memory_taxonomy
  - p01_kc_session_state
  - bld_memory_session_state
---

<!-- 8F: F1 constrain=P10/memory_architecture F2 become=memory-architecture-builder F3 inject=knowledge_index_n01+entity_memory_n01+mem_memory_summary_n01+mem_runtime_state_n01 F4 reason=Analytical Envy compounding requires a memory architecture, not just ad-hoc storage -- the structure IS the strategic advantage F5 call=cex_compile F6 produce=memory_architecture_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P10_memory/ -->

## Purpose

Four types of memory serve different N01 research needs:
1. What am I doing RIGHT NOW? (working memory)
2. What did I find LAST TIME? (episodic memory)
3. What do I KNOW? (semantic memory)
4. HOW do I do this? (procedural memory)

Without explicit architecture, N01 conflates these -- slow, expensive, error-prone.
With explicit layers, each memory type has optimal storage, retrieval, and decay.

## Memory Layer Architecture

### Layer 1: Working Memory (Session Context)

| Property | Value |
|----------|-------|
| Storage | in-context (no disk write during session) |
| Scope | current session only |
| Capacity | ~100K tokens (Claude context window subset) |
| Content | task goal, active sources, interim findings, chain-of-thought |
| Decay | session end = total loss |
| Persistence | summarize to L2 at session end |

Key contents:
- Current research goal and atomic questions (from DSTCS Step 1)
- Source pool being triangulated (from search_strategy_n01.md)
- Interim confidence scores and findings
- Tool call results not yet synthesized

### Layer 2: Episodic Memory (Research Sessions)

| Property | Value |
|----------|-------|
| Storage | `N01_intelligence/P10_memory/sessions/{date}_{mission}.yaml` |
| Scope | per-session research record |
| Capacity | unlimited (disk) |
| Content | session goal, key findings, entities discovered, quality score |
| Decay | 90 days retention; archive at 365 days |
| Persistence | written by cex_hooks_native.py on session end |

Schema:
```yaml
session_id: "{date}_{mission_slug}"
goal: "string"
duration_minutes: int
sources_consulted: int
entities_discovered: ["string"]
key_findings: [{finding, confidence, sources}]
quality_score: float
artifacts_created: ["string"]
next_session_context: "string"
```

### Layer 3: Semantic Memory (Persistent Knowledge)

| Property | Value |
|----------|-------|
| Storage | `N01_intelligence/P01_knowledge/*.md` + entity files |
| Scope | permanent (until explicitly updated or archived) |
| Capacity | unlimited |
| Content | knowledge_cards, entity profiles, market data |
| Decay | manual review trigger at 90-day staleness |
| Retrieval | `knowledge_index_n01.md` + `retriever_n01.md` |

Sub-types:
- Declarative: facts about the world (KCs)
- Entity: profiles of companies, people, products
- Structural: taxonomy, glossary, ontology

### Layer 4: Procedural Memory (Methods)

| Property | Value |
|----------|-------|
| Storage | `N01_intelligence/P03_prompt/*.md` + `P04_tools/*.md` |
| Scope | permanent (versioned) |
| Capacity | unlimited |
| Content | reasoning strategies, search strategies, evaluation protocols |
| Decay | version bump when superseded |
| Retrieval | direct path reference (not indexed search) |

Sub-types:
- Search: `search_strategy_n01.md`
- Reasoning: `reasoning_strategy_n01.md`
- Evaluation: `eval_framework_n01.md`
- Quality: `quality_gate_intelligence.md`

## Memory Lifecycle

```
SESSION START:
  L4 (procedural) -> load always (fast, deterministic)
  L3 (semantic) -> query retriever for relevant context
  L2 (episodic) -> check for recent sessions on same topic
  L1 (working) -> initialize empty

DURING SESSION:
  L1 -> accumulate findings, chain-of-thought

SESSION END:
  L1 -> summarize to L2 (session record)
  L1 -> update L3 (KCs, entities if new knowledge found)
  L2 -> archive if > 90 days

STALENESS CHECK (weekly):
  L3 -> scan for entities/KCs > 90 days -> flag for refresh
  L2 -> archive sessions > 90 days
```

## Retrieval Priority (by task type)

| Task | L1 | L2 | L3 | L4 |
|------|----|----|----|-----|
| New research topic | empty | check recent | query KCs+entities | load all |
| Follow-up research | session context | load previous session | load related KCs | load strategy |
| Entity lookup | check in-context | no | load entity profile | no |
| Method question | no | no | no | load relevant method |

## Comparison vs. Alternatives

| Architecture | Layers | Retrieval Speed | Staleness Control | N01 Fit |
|-------------|--------|----------------|-----------------|---------|
| No architecture (ad-hoc) | 1 | O(n) scan | none | fail |
| Session-only (no persistence) | 1 | N/A | N/A | loses compounding |
| External vector DB | 2-3 | fast | manual | requires cloud |
| This 4-layer | 4 | L3/L4 fast | built-in decay rules | optimal |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_scope]] | upstream | 0.41 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.37 |
| [[bld_collaboration_memory_type]] | downstream | 0.37 |
| [[bld_output_template_memory_architecture]] | upstream | 0.36 |
| [[bld_examples_memory_scope]] | upstream | 0.36 |
| [[memory-architecture-builder]] | related | 0.35 |
| [[bld_collaboration_memory_scope]] | downstream | 0.34 |
| [[atom_22_memory_taxonomy]] | related | 0.33 |
| [[p01_kc_session_state]] | related | 0.32 |
| [[bld_memory_session_state]] | related | 0.32 |
