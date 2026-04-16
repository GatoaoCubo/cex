---
kind: memory
id: p10_mem_consolidation_policy_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for consolidation_policy construction
quality: 8.9
title: "Memory: consolidation_policy-builder patterns"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, memory]
tldr: "Key lessons: domain is LLM agent memory lifecycle (not OS GC), always async, consolidation_async: true required, enterprise needs compliance section"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Observation

The most common defect in consolidation_policy artifacts is **domain confusion**: generators
default to OS/GC memory management (garbage collection, slab allocation, heap compaction,
TLB shootdown) instead of LLM agent memory lifecycle (working->episodic->semantic promotion,
importance scoring, sleep-time consolidation). Every ISO must be checked for GC terminology.

A second common defect is **missing consolidation_async: true** -- synchronous consolidation
blocks agent response time. This is always a defect regardless of tier.

## Pattern

High-quality consolidation_policy artifacts share four traits:
1. Clear promotion rules: which layers are active, what triggers promotion, what condition.
2. Eviction strategy per layer with concrete triggers (not just "when memory is full").
3. Importance scoring: formula or model reference that quantifies memory value.
4. Commercial tier matrix: FREE (no consolidation), PRO (TTL + importance), ENTERPRISE
   (full compliance + audit trail + data residency).

## Evidence

Wave 3 generation (qwen3:14b) produced OS-focused ISOs for consolidation_policy:
- knowledge_card cited Java G1GC, POSIX memory management, Linux slab allocation
- system_prompt described heap fragmentation control and GC hooks
- quality_gate tested memory leak rate, deallocation latency, heap fragmentation ratio
- schema required `consolidation_criteria: array` (generic policy, not memory lifecycle)

None of these are relevant to LLM agent memory consolidation.

## Recommendations

- On every read of an existing consolidation_policy ISO, grep for: GC, garbage, slab,
  heap, fragmentation, compaction, TLB, deallocation, malloc, free(). Any match = domain
  contamination.
- The parent memory_architecture artifact defines which layers exist; consolidation_policy
  defines the lifecycle rules for those layers. Always read the parent first.
- Free tier: consolidation_policy is trivially empty (no persistent memory to consolidate).
  Document this explicitly rather than leaving empty sections.
- Enterprise compliance is non-trivial: GDPR Art. 17 hard-delete must be verifiable.
  Never use soft-delete alone for enterprise compliance artifacts.
