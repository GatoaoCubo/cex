---
kind: instruction
id: bld_instruction_memory_architecture
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for memory_architecture
quality: null
title: "Instruction Memory Architecture"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_architecture, builder, instruction]
tldr: "Step-by-step production process for memory_architecture"
domain: "memory_architecture construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze memory hierarchy (cache, RAM, storage) for latency/throughput tradeoffs.  
2. Evaluate DRAM, SRAM, and non-volatile memory (NVM) technologies for use case compatibility.  
3. Study access patterns (sequential, random, burst) to define bandwidth requirements.  
4. Investigate error correction codes (ECC, parity) and reliability metrics.  
5. Benchmark existing architectures for performance bottlenecks.  
6. Document memory addressing schemes (linear, segmented, virtual).  

## Phase 2: COMPOSE  
1. Define memory layers per SCHEMA.md (e.g., L1/L2/L3 cache, main memory).  
2. Map components to OUTPUT_TEMPLATE.md’s structure (modules, interfaces, parameters).  
3. Outline data flow between memory controllers and processors.  
4. Specify cache coherence protocols (MESI, MOESI) in detail.  
5. Detail ECC implementation for error detection/correction.  
6. Integrate memory bandwidth calculations (transfer rate, latency).  
7. Write module descriptions using OUTPUT_TEMPLATE.md’s terminology.  
8. Align memory hierarchy with SCHEMA.md’s abstraction levels.  
9. Finalize artifact with cross-references to schema and template.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance: All modules match SCHEMA.md’s definitions.  
- [ ] ✅ Technical accuracy: Latency/bandwidth claims match research benchmarks.  
- [ ] ✅ Use case alignment: Memory design supports P10’s INJECT function.  
- [ ] ✅ Peer review: No logical inconsistencies in hierarchy or protocols.  
- [ ] ✅ Output format: OUTPUT_TEMPLATE.md’s structure fully implemented.
