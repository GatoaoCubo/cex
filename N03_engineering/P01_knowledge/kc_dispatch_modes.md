---
id: kc_dispatch_modes
kind: knowledge_card
title: CEX Dispatch Modes Comparison
version: 1.0.0
quality: 8.9
pillar: P01
density_score: 1.0
---

# CEX Dispatch Modes Comparison

The CEX system supports multiple dispatch modes for task execution. Each mode has distinct characteristics that make them suitable for different workloads. Below is a comparison of key dispatch modes:

| Mode           | Concurrency | Model              | Cost       | Throughput | Best Use Case                          |
|----------------|-------------|--------------------|------------|------------|----------------------------------------|
| **Claude Grid** | Parallel    | Claude Opus        | High       | High       | Complex tasks requiring parallelism    |
| **Aider Grid**  | Parallel    | Aider              | Medium     | Medium     | Batch processing with moderate complexity |
| **Aider Crew**  | Parallel    | Aider              | Medium     | High       | Parallelizable tasks with shared context |
| **Aider Sweep** | Sequential  | Aider              | Low        | Medium     | Linear workflows with dependent steps  |
| **Aider Cascade** | Sequential | Aider              | Low        | Low        | Dependent tasks requiring strict order |

## Mode Details

### Claude Grid
- **Concurrency**: Full parallel execution across all available nuclei
- **Model**: Claude Opus (1M context window)
- **Cost**: High due to parallel resource allocation
- **Throughput**: High for complex, independent tasks
- **Best Use**: Research analysis, large-scale data processing

### Aider Grid
- **Concurrency**: Parallel execution with resource throttling
- **Model**: Aider (optimized for batch processing)
- **Cost**: Medium due to balanced resource allocation
- **Throughput**: Medium for moderate complexity workloads
- **Best Use**: Batch file processing, standard task queues

### Aider Crew
- **Concurrency**: Parallel execution with shared context
- **Model**: Aider (with context preservation)
- **Cost**: Medium with context maintenance overhead
- **Throughput**: High for parallelizable tasks
- **Best Use**: Documentation generation, multi-step workflows

### Aider Sweep
- **Concurrency**: Sequential execution
- **Model**: Aider (with memory retention)
- **Cost**: Low for linear processing
- **Throughput**: Medium for dependent task chains
- **Best Use**: Code review, sequential data processing

### Aider Cascade
- **Concurrency**: Strict sequential execution
- **Model**: Aider (with strict dependency tracking)
- **Cost**: Low for simple task chains
- **Throughput**: Low for dependent task sequences
- **Best Use**: Validation pipelines, step-by-step transformations
```

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
