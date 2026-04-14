---
kind: instruction
id: bld_instruction_memory_benchmark
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for memory_benchmark
quality: null
title: "Instruction Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, instruction]
tldr: "Step-by-step production process for memory_benchmark"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Define memory evaluation criteria: latency, throughput, error rates, and consistency.  
2. Identify target memory systems (e.g., DRAM, SSD, persistent memory).  
3. Review existing benchmarks (e.g., STREAM, MEMBENCH) for methodology gaps.  
4. Analyze hardware/software requirements for test environments.  
5. Select memory workloads (e.g., random access, sequential writes).  
6. Document risks: false positives, environmental interference, scalability limits.  

## Phase 2: COMPOSE  
1. Set up development environment with SCHEMA.md constraints.  
2. Define benchmark structure: test cases, metrics, and reporting formats.  
3. Write test cases for memory access patterns (sequential, random, burst).  
4. Implement memory stress tests (e.g., sustained writes, read-modify-write cycles).  
5. Integrate OUTPUT_TEMPLATE.md for result formatting (CSV, JSON, HTML).  
6. Add metadata: test version, hardware specs, OS details.  
7. Write documentation for usage, configuration, and interpretation.  
8. Conduct code review for compliance with SCHEMA.md and P07 standards.  
9. Finalize artifact with version control and release notes.  

## Phase 3: VALIDATE  
- [ ] Run unit tests for all memory operations (pass/fail).  
- [ ] Cross-validate results against industry benchmarks.  
- [ ] Test on 3+ hardware platforms (e.g., x86, ARM, FPGA).  
- [ ] Verify output matches OUTPUT_TEMPLATE.md structure.  
- [ ] Confirm governance compliance (P07, GOVERN function).
