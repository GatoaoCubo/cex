---
kind: architecture
id: bld_architecture_memory_benchmark
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of memory_benchmark -- inventory, dependencies
quality: 9.0
title: "Architecture Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, architecture]
tldr: "Component map of memory_benchmark -- inventory, dependencies"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name             | Role                           | Pillar | Status  |  
|----------------------|--------------------------------|--------|---------|  
| bld_manifest         | Builder identity and routing   | P07    | Active  |  
| bld_instruction      | Step-by-step production guide  | P03    | Active  |  
| bld_system_prompt    | Builder persona and rules      | P03    | Active  |  
| bld_schema           | Formal data contract (SSOT)    | P06    | Active  |  
| bld_quality_gate     | HARD/SOFT scoring gates        | P11    | Active  |  
| bld_output_template  | Output skeleton with vars      | P05    | Active  |  
| bld_examples         | Sample input/output pairs      | P07    | Active  |  
| bld_knowledge_card   | Domain knowledge injection     | P01    | Active  |  
| bld_architecture     | ISO inventory and deps         | P08    | Active  |  
| bld_collaboration    | Crew coordination protocol     | P12    | Active  |  
| bld_config           | Runtime configuration          | P09    | Active  |  
| bld_memory           | Learned patterns (memory ISO)  | P10    | Active  |  
| bld_tools            | Tool registry for F5 CALL      | P04    | Active  |  

## Dependencies  
| From              | To                  | Type         |  
|-------------------|---------------------|--------------|  
| bld_manifest      | bld_instruction     | Reference    |  
| bld_system_prompt | bld_output_template | Dependency   |  
| bld_schema        | bld_quality_gate    | Dependency   |  
| bld_config        | bld_memory          | Configuration|  
| bld_tools         | memory_profiler     | External     |  
| bld_examples      | bld_instruction     | Reference    |  

## Architectural Position  
memory_benchmark operates in CEX pillar P07 as a specialized evaluation builder targeting AI agent
memory quality: retention, recall, consistency, and hallucination rate across multi-turn
conversations. It integrates with eval-metric-builder (atomic metrics) and benchmark-suite-builder
(composite suite assembly), while drawing on bld_knowledge_card for grounding in real benchmarks
(LOCOMO, LongMemEval, MemGPT). Not to be confused with hardware memory profiling tools.
