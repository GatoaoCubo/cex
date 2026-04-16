---
kind: memory
id: p10_mem_memory_architecture_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for memory_architecture construction
quality: 8.9
title: "Memory: memory_architecture-builder patterns"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, memory]
tldr: "Key lessons: domain is LLM agent memory (not hardware), always include tier matrix, cite MemGPT/Zep/mem0, define eviction policy per layer"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Observation

The most common defect in memory_architecture artifacts is **domain confusion**:
generators trained on broad corpora default to hardware memory architecture (DRAM,
cache hierarchies, MESI coherence) instead of LLM agent memory systems. Every ISO
in this builder must be checked for hardware terminology and corrected.

## Pattern

High-quality memory_architecture artifacts share three traits:
1. Explicit four-layer model (working/episodic/semantic/procedural) with backend per layer.
2. Commercial tier matrix distinguishing FREE (context-only) from PRO (episodic) from
   ENTERPRISE (full graph + compliance).
3. Industry grounding: reference MemGPT/Letta (2023), Zep (2024), or mem0 (2024) as
   architectural precedent -- not computer architecture textbooks.

## Evidence

Wave 3 generation (qwen3:14b) produced hardware-focused ISOs for memory_architecture:
- knowledge_card cited JEDEC DDR5, CXL 3.0, AMD Infinity Fabric
- system_prompt described cache hierarchy design and MESI protocol
- schema required `memory_type: RAM/ROM`, `capacity: bytes`, `access_time: nanoseconds`
- quality_gate tested latency <10ns and error rate 0.01% (hardware metrics)

These are all correct for computer architecture but wrong for LLM agent memory.

## Recommendations

- On every read of an existing memory_architecture ISO, grep for: DRAM, DDR, SRAM,
  cache, coherence, ECC, CXL, bandwidth, nanosecond. Any match = domain contamination.
- When referencing memory latency, use agent-relevant units: milliseconds for
  retrieval, seconds for consolidation -- not nanoseconds for hardware access.
- The consolidation_policy and procedural_memory kinds are siblings in P10: cross-reference
  them rather than re-specifying their content.
- Tier matrix is mandatory per N06 commercial lens. Free tier = no persistent memory;
  pro tier = episodic + semantic; enterprise = full graph + compliance + team sharing.
