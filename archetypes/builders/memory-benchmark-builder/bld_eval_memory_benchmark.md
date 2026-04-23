---
kind: quality_gate
id: p07_qg_memory_benchmark
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for memory_benchmark
quality: 9.0
title: "Quality Gate Memory Benchmark"
version: "1.1.0"
author: n05_operations
tags: [memory_benchmark, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for memory_benchmark"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_examples_memory_benchmark
  - p03_sp_memory_benchmark_builder
  - bld_instruction_memory_benchmark
  - memory-benchmark-builder
  - p07_qg_benchmark_suite
  - hybrid_review4_n05
  - benchmark-builder
  - p11_qg_benchmark
  - p07_qg_eval_metric
  - bld_architecture_benchmark
---

## Quality Gate

## Definition

| metric           | threshold | operator | scope        |
|------------------|-----------|----------|--------------|
| frontmatter      | valid     | ==       | artifact     |
| section_count    | >=4       | >=       | body         |
| metric_count     | >=2       | >=       | body         |
| id_pattern       | matches   | ==       | frontmatter  |

## HARD Gates

| ID  | Check                     | Fail Condition                                        |
|-----|---------------------------|-------------------------------------------------------|
| H01 | YAML frontmatter valid    | Invalid YAML syntax or missing required fields        |
| H02 | ID matches pattern        | ID does not match ^p07_mb_[a-z][a-z0-9_]+.md$        |
| H03 | kind field matches        | kind != 'memory_benchmark'                            |
| H04 | At least 2 metrics        | Fewer than 2 evaluation metrics defined in body       |
| H05 | Metric formula present    | No formula or calculation method specified per metric |
| H06 | Real benchmark reference  | No reference to LOCOMO, LongMemEval, MemGPT, or equiv |
| H07 | No hardware metrics       | Body contains DRAM/SRAM/bandwidth/ECC references      |

## SOFT Scoring

| Dim | Dimension           | Weight | Scoring Guide                                            |
|-----|---------------------|--------|----------------------------------------------------------|
| D01 | Metric completeness | 0.20   | retention+recall+hallucination (1.0) vs partial (0.5)    |
| D02 | Formula precision   | 0.20   | Exact formula cited (1.0) vs vague description (0.0)     |
| D03 | Benchmark grounding | 0.15   | 3+ real benchmarks cited (1.0) vs 1 (0.5) vs 0 (0.0)    |
| D04 | Distance coverage   | 0.15   | Tests at 3+ turn distances (1.0) vs single depth (0.3)   |
| D05 | Hallucination check | 0.15   | Hallucination metric required (1.0) vs absent (0.0)      |
| D06 | Reproducibility     | 0.10   | Dataset + prompt templates specified (1.0) vs none (0.0) |
| D07 | Domain accuracy     | 0.05   | AI memory domain only (1.0) vs hardware contamination (0)|

## Actions

| Score  | Action   |
|--------|----------|
| >=9.5  | GOLDEN   |
| >=8.0  | PUBLISH  |
| >=7.0  | REVIEW   |
| <7.0   | REJECT   |

## Bypass

| conditions                   | approver   | audit trail                      |
|------------------------------|------------|----------------------------------|
| Novel benchmark not yet named | Tech Lead  | Citation pending; flag for update |

## Examples

## Golden Example
```markdown
---
title: "DDR4 Memory Latency Evaluation"
description: "Benchmark for assessing latency in DDR4 memory modules under varying load conditions"
authors: ["A. Smith", "J. Lee"]
date: "2023-11-15"
version: "1.2"
keywords: ["memory benchmark", "latency", "DDR4", "server CPU", "memory test tool"]
---

**Objective**: Measure random access latency in DDR4-3200 modules across 4K-16MB data sizes.

**Methodology**:
- Hardware: Server-class CPU, 2x DDR4-3200 32GB ECC
- Tools: Memory test suite v8.1, memory bandwidth benchmark v4.0
- Workloads: 100% random read/write, 10% sequential, 50% mixed

**Metrics**:
- Average latency (ns)
- Latency variance (%)
- Bandwidth (GB/s)

**Setup**:
- OS: Ubuntu 22.04 LTS
- Kernel: 5.15.0
- Memory configuration: 2x 16GB (non-ECC) vs 2x 16GB (ECC)

**Results**:
- ECC modules showed 12% higher latency under 16MB load
- Memory test suite detected 3 errors in non-ECC configuration
```

## Anti-Example 1: General Benchmark Confusion
```markdown
---
title: "System Performance Test"
description: "Evaluates overall system performance"
authors: ["B. Taylor"]
date: "2023-11-10"
version: "0.5"
keywords: ["benchmark", "system", "CPU", "GPU"]
---

**Objective**: Measure system performance across multiple workloads.

**Methodology**:
- Tools: Geekbench 6, 3DMark
- Workloads: CPU, GPU, storage

**Metrics**:
- Overall score (points)
- CPU score
- GPU score

**Setup**:
- OS: Windows 11
- Hardware: Generic "ProviderA" system
```
## Why it fails: Focuses on general system performance rather than memory-specific metrics. Uses vague vendor names and lacks memory-related workloads or evaluation criteria.

## Anti-Example 2: Architecture Specification
```markdown
---
title: "Memory Controller Design"
description: "Specification for a high-performance memory controller"
authors: ["C. Park"]
date: "2023-11-12"
version: "1.0"
keywords: ["memory architecture", "controller", "DDR5"]
---

**Objective**: Define a memory controller for DDR5-6000 modules.

**Methodology**:
- Design: 8-channel interleaving
- Features: ECC support, error correction

**Metrics**:
- Bandwidth (GB/s)
- Latency (cycles)

**Setup**:
- Target: 128GB system with 8x DDR5-6000
```
## Why it fails: Describes memory architecture design rather than evaluation. Focuses on system specifications, not benchmarking methodology or results.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
