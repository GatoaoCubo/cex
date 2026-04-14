---
kind: schema
id: bld_schema_memory_benchmark
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for memory_benchmark
quality: null
title: "Schema Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for memory_benchmark"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes |  
|-----------|--------|----------|---------|-------|  
| id        | string | yes      |         |       |  
| kind      | string | yes      |         |       |  
| pillar    | string | yes      |         |       |  
| title     | string | yes      |         |       |  
| version   | string | yes      | 1.0     |       |  
| created   | date   | yes      |         |       |  
| updated   | date   | yes      |         |       |  
| author    | string | yes      |         |       |  
| domain    | string | yes      | memory  |       |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | list   | yes      |         |       |  
| tldr      | string | yes      |         |       |  
| capacity  | number | yes      |         | MB    |  
| latency   | number | yes      |         | ms    |  

### Recommended  
| Field      | Type   | Notes |  
|------------|--------|-------|  
| accuracy   | number | %     |  
| workload   | string |       |  

## ID Pattern  
^p07_mb_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Description of the memory benchmark purpose and scope.  
2. **Metrics**  
   - Key performance indicators (e.g., throughput, error rate).  
3. **Workload**  
   - Data patterns, access types, and stress scenarios.  
4. **Constraints**  
   - Hardware, software, and environmental limitations.  
5. **Results**  
   - Expected output format and validation criteria.  
6. **Notes**  
   - Additional context, caveats, or references.  

## Constraints  
- All metrics must be measurable and repeatable.  
- Capacity must not exceed 5120 MB.  
- Latency thresholds must align with industry standards.  
- Workloads must be defined in ASCII-compatible formats.  
- Results must include statistical confidence intervals.  
- Tags must use lowercase alphanumeric characters and underscores.
