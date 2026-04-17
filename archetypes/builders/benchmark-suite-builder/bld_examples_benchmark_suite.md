---
kind: examples
id: bld_examples_benchmark_suite
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of benchmark_suite artifacts
quality: 8.9
title: "Examples Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, examples]
tldr: "Golden and anti-examples of benchmark_suite artifacts"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
name: "MMLU_Benchmark_Suite"
kind: benchmark_suite
description: "A comprehensive benchmark suite evaluating language models on 10+ academic disciplines"
tasks:
  - name: "Natural_Language_Reasoning"
    description: "Tests logical reasoning in natural language tasks"
    metrics: ["accuracy", "F1_score"]
    models: ["HuggingFace/T5", "Meta/Llama-2", "Anthropic/Claude-2"]
  - name: "Mathematical_Reasoning"
    description: "Evaluates mathematical problem-solving capabilities"
    metrics: ["accuracy", "perplexity"]
    models: ["Google/PaLM-2", "Anthropic/Claude-2", "HuggingFace/CodeLlama"]
  - name: "Code_Execution"
    description: "Assesses code generation and execution accuracy"
    metrics: ["execution_success", "code_quality"]
    models: ["HuggingFace/CodeLlama", "Anthropic/Claude-2", "Meta/Llama-2"]
```

## Anti-Example 1: Single Task Benchmark
```markdown
---
name: "SingleTaskBenchmark"
kind: benchmark_suite
description: "Evaluates text generation quality on a single task"
tasks:
  - name: "Text_Generation"
    description: "Tests model ability to generate coherent text"
    metrics: ["perplexity", "human_rating"]
    models: ["HuggingFace/GPT-2"]
```
## Why it fails
This is not a benchmark suite but a single benchmark. The 'benchmark_suite' kind requires multiple distinct tasks with different objectives and evaluation metrics.

## Anti-Example 2: Evaluation Framework Confusion
```markdown
---
name: "MLPerf_Evaluation"
kind: benchmark_suite
description: "MLPerf benchmarking framework for AI performance evaluation"
tasks:
  - name: "Inference_Speed"
    description: "Measures model inference throughput"
    metrics: ["queries_per_second", "latency"]
    models: ["MLPerf_Reference_Implementations"]
```
## Why it fails
This is an evaluation framework (MLPerf) not a benchmark suite. The 'benchmark_suite' kind should define specific tasks to evaluate model capabilities, not general-purpose evaluation infrastructure.
