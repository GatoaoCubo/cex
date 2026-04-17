---
kind: instruction
id: bld_instruction_memory_benchmark
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for memory_benchmark
quality: 8.9
title: "Instruction Memory Benchmark"
version: "1.1.0"
author: n05_operations
tags: [memory_benchmark, builder, instruction]
tldr: "Step-by-step production process for memory_benchmark"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Phase 1: RESEARCH

1. Define the memory evaluation goal: retention, recall, consistency, or hallucination rate?
2. Identify target agent architecture: pure in-context, RAG/external store, or hybrid?
3. Review real benchmarks for methodology: LOCOMO, LongMemEval, MemGPT evals, MT-Bench-101.
4. Select turn distance range: short (5-10 turns), medium (20-50), long (100+ or multi-session).
5. Choose primary metrics: exact-match, F1, ROUGE-L, or LLM-judge; define hallucination detector.
6. Document scope: what memory types are out of scope (hardware DRAM, caching layers, etc.).

## Phase 2: COMPOSE

1. Load bld_schema_memory_benchmark.md for required fields (memory_type, eval_distance).
2. Write frontmatter: id matching ^p07_mb_[a-z][a-z0-9_]+.md$, kind=memory_benchmark, pillar=P07.
3. Write Overview: target system, memory type, scope boundary.
4. Write Metrics section: for each metric, include name, formula, scale, and primary tool.
5. Write Test Protocol: conversation generation method, fact planting, query turn distances.
6. Write Reference Benchmarks: cite >= 1 real benchmark (LOCOMO, LongMemEval, MemGPT, NiH).
7. Write Evaluation Criteria: pass/fail thresholds, hallucination budget, baseline.
8. Add Notes: known failure modes, scope caveats.

## Phase 3: VALIDATE

- [ ] frontmatter YAML parses without error (H01).
- [ ] id matches ^p07_mb_[a-z][a-z0-9_]+.md$ (H02).
- [ ] kind == memory_benchmark (H03).
- [ ] >= 2 metrics defined with formulas (H04, H05).
- [ ] >= 1 real benchmark cited (H06) -- NOT hardware DRAM benchmarks.
- [ ] No DRAM/SRAM/bandwidth/ECC references in body (H07).
- [ ] Run: python _tools/cex_wave_validator.py --scope archetypes/builders/memory-benchmark-builder/
- [ ] Run: python _tools/cex_compile.py {path}
