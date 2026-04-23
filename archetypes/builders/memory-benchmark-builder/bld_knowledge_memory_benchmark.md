---
kind: knowledge_card
id: bld_knowledge_card_memory_benchmark
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for memory_benchmark production
quality: 9.2
title: "Knowledge Card Memory Benchmark"
version: "1.1.0"
author: n05_operations
tags: [memory_benchmark, builder, knowledge_card, ai_memory, evaluation]
tldr: "Domain knowledge for benchmarking AI agent memory systems: retention, recall, multi-turn consistency"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - memory-benchmark-builder
  - p03_sp_memory_benchmark_builder
  - bld_instruction_memory_benchmark
  - bld_knowledge_card_memory_architecture
  - p01_kc_memory_scope
  - atom_22_memory_taxonomy
  - bld_knowledge_card_memory_scope
  - p10_rs_conversation
  - memory-architecture-builder
  - ex_context_session_memory
---

## Domain Overview

Memory benchmarking for AI agents evaluates how well language models retain, recall, and
reason over information across multi-turn conversations, long contexts, and sessions.
Unlike hardware memory benchmarks (DRAM/JEDEC), this domain targets the semantic memory
capacity of LLM-based agents: do they remember what was said? Can they answer questions
about prior context accurately? Does retrieval quality degrade over distance?

Key evaluation axes: (1) retention -- is the fact present in the agent's effective context?
(2) recall -- can the agent surface the fact when queried? (3) consistency -- does the agent
contradict itself across turns? (4) hallucination rate -- does the agent fabricate memories?

## Key Concepts

| Concept              | Definition                                                                      | Source                                    |
|----------------------|---------------------------------------------------------------------------------|-------------------------------------------|
| Retention rate       | % of facts from prior turns correctly recalled when queried later               | LOCOMO (Maharana et al., 2024)            |
| Recall accuracy      | Exact-match or F1 on memory retrieval questions                                 | LongMemEval (Wu et al., 2024)             |
| Hallucination rate   | % of recalled claims not grounded in prior context                              | MemGPT (Packer et al., 2023)              |
| Needle-in-a-Haystack | Synthetic test: single fact buried in long context; measures retrieval at depth | Kamradt (2023), various LLM leaderboards  |
| Multi-turn coherence | Consistency of agent answers across N follow-up turns                           | MT-Bench-101 (Bai et al., 2024)          |
| Memory scope         | Effective distance (tokens/turns) over which facts remain retrievable           | NarrativeQA long-context (Kocisk 2017)    |
| Proactive retrieval  | Agent surfaces relevant past facts without explicit prompting                   | MemGPT, Goodfire MemBench                 |
| Temporal ordering    | Correctly sequencing recalled events by time                                    | LOCOMO Section 4.3                        |

## Industry Standards and Benchmarks

- **LOCOMO** (Maharana et al., 2024): Long-conversation memory benchmark; 50 sessions, 300 turns avg
- **LongMemEval** (Wu et al., 2024): Single/multi-session memory; QA over stored conversation history
- **MemGPT evals** (Packer et al., 2023): Tiered memory (in-context vs. external store) recall accuracy
- **MT-Bench-101** (Bai et al., 2024): Multi-turn chat evaluation; tests coherence across 101 topics
- **Needle-in-a-Haystack** (Kamradt, 2023): Synthetic needle placement at varying depths/positions
- **NarrativeQA long-context** (Kocisk et al., 2017): Reading comprehension over book-length documents
- **Goodfire MemBench**: Proactive memory retrieval without user prompting

## Common Patterns

1. Generate synthetic conversation with planted facts at specific turn depths.
2. Query facts at varying distances (5, 20, 50, 100 turns later) to measure decay.
3. Use exact-match and F1 as primary metrics; ROUGE-L for partial recall.
4. Run hallucination detector (LLM-as-judge or NLI model) on all recalled claims.
5. Test both RAG-augmented and pure in-context memory variants separately.

## Pitfalls

- Confusing hardware memory (DRAM latency) with AI agent memory evaluation.
- Using only short-context tests that do not stress real-world multi-session recall.
- Omitting hallucination measurement -- recall rate alone is misleading.
- Failing to test temporal ordering (facts from earlier vs. later turns).
- Not separating retrieval accuracy from generation quality in the evaluation.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[memory-benchmark-builder]] | downstream | 0.56 |
| [[p03_sp_memory_benchmark_builder]] | downstream | 0.44 |
| [[bld_instruction_memory_benchmark]] | downstream | 0.35 |
| [[bld_knowledge_card_memory_architecture]] | sibling | 0.35 |
| [[p01_kc_memory_scope]] | sibling | 0.34 |
| [[atom_22_memory_taxonomy]] | sibling | 0.33 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.32 |
| [[p10_rs_conversation]] | downstream | 0.31 |
| [[memory-architecture-builder]] | downstream | 0.29 |
| [[ex_context_session_memory]] | related | 0.27 |
