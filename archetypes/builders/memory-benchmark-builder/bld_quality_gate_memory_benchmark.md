---
kind: quality_gate
id: p07_qg_memory_benchmark
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for memory_benchmark
quality: null
title: "Quality Gate Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for memory_benchmark"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric         | threshold     | operator | scope        |  
|----------------|---------------|----------|--------------|  
| memory latency | <= 100ns      | <=       | per test case|  
| bandwidth      | >= 50GB/s     | >=       | system wide  |  
| error rate     | <= 0.01%      | <=       | per cycle    |  

## HARD Gates  
| ID           | Check                  | Fail Condition                          |  
|--------------|------------------------|-----------------------------------------|  
| H01          | YAML frontmatter valid | Invalid YAML syntax or missing fields   |  
| H02          | ID matches pattern     | ID does not match ^p07_mb_[a-z][a-z0-9_]+.md$ |  
| H03          | kind field matches     | kind != 'memory_benchmark'              |  
| H04          | latency threshold met  | latency > 100ns for any test case       |  
| H05          | bandwidth threshold met| bandwidth < 50GB/s system wide          |  
| H06          | error rate threshold   | error rate > 0.01% per cycle            |  
| H07          | allocation success     | <99% allocation success rate            |  

## SOFT Scoring  
| Dim | Dimension        | Weight | Scoring Guide                          |  
|-----|------------------|--------|----------------------------------------|  
| D01 | Latency          | 0.15   | 0.0 (100ns+) to 1.0 (<=50ns)           |  
| D02 | Bandwidth        | 0.20   | 0.0 (25GB/s) to 1.0 (>=75GB/s)         |  
| D03 | Error Rate       | 0.15   | 0.0 (1%+) to 1.0 (<=0.001%)            |  
| D04 | Allocation       | 0.10   | 0.0 (50%) to 1.0 (>=99.9%)             |  
| D05 | Stability        | 0.10   | 0.0 (crash) to 1.0 (no crashes)        |  
| D06 | Scalability      | 0.10   | 0.0 (100GB) to 1.0 (>=500GB)           |  
| D07 | Consistency      | 0.10   | 0.0 (5% drift) to 1.0 (<=0.1% drift)   |  
| D08 | Security         | 0.10   | 0.0 (vulnerability) to 1.0 (none)      |  

## Actions  
| Score   | Action       |  
|---------|--------------|  
| >=9.5   | GOLDEN       |  
| >=8.0   | PUBLISH      |  
| >=7.0   | REVIEW       |  
| <7.0    | REJECT       |  

## Bypass  
| conditions                          | approver         | audit trail              |  
|------------------------------------|------------------|--------------------------|  
| Critical production issue          | CTO              | documented in JIRA       |  
| Third-party hardware limitation    | Hardware Lead    | signed waiver            |  
| Regulatory override                | Compliance Head  | legal review record      |
