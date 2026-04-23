---
kind: quality_gate
id: p07_qg_benchmark_suite
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for benchmark_suite
quality: 9.1
title: "Quality Gate Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for benchmark_suite"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_benchmark_suite
  - p09_qg_marketplace_app_manifest
  - p07_qg_eval_metric
  - p07_qg_memory_benchmark
  - p07_qg_cohort_analysis
  - p11_qg_roi_calculator
  - p05_qg_github_issue_template
  - p04_qg_stt_provider
  - p11_qg_safety_policy
  - p01_qg_reranker_config
---

## Quality Gate

## Definition
| metric          | threshold | operator | scope        |
|-----------------|-----------|----------|--------------|
| frontmatter     | valid     | ==       | artifact     |
| task_count      | >=3       | >=       | body         |
| section_count   | >=4       | >=       | body         |
| id_pattern      | matches   | ==       | frontmatter  |

## HARD Gates
| ID         | Check                  | Fail Condition                                      |
|------------|------------------------|-----------------------------------------------------|
| H01        | YAML frontmatter valid | Invalid YAML syntax or missing required fields      |
| H02        | ID matches pattern     | ID does not match ^p07_bs_[a-z][a-z0-9_]+.md$      |
| H03        | kind field matches     | kind is not 'benchmark_suite'                       |
| H04        | All tasks defined      | Missing task definition in benchmark suite          |
| H05        | Unique benchmark ID    | Duplicate ID across benchmark suite components      |
| H06        | Description present    | Missing or empty description field                  |
| H07        | Version specified      | No version field or invalid semantic versioning     |

## SOFT Scoring
| Dim | Dimension       | Weight | Scoring Guide                                      |
|-----|------------------|--------|----------------------------------------------------|
| D01 | Completeness     | 0.15   | 100% complete = 1.0; missing tasks = 0.5             |
| D02 | Accuracy         | 0.15   | 95%+ accuracy = 1.0; <90% = 0.0                      |
| D03 | Consistency      | 0.10   | All tasks aligned = 1.0; partial alignment = 0.5      |
| D04 | Scalability      | 0.10   | Handles 1000+ tasks = 1.0; <500 = 0.5                |
| D05 | Usability        | 0.12   | Clear documentation = 1.0; ambiguous = 0.5           |
| D06 | Documentation    | 0.10   | Full API docs = 1.0; partial = 0.5                   |
| D07 | Alignment        | 0.10   | Matches business goals = 1.0; partial = 0.5          |
| D08 | Innovation       | 0.18   | Novel metrics = 1.0; standard = 0.5                  |

## Actions
| Score     | Action         |
|-----------|----------------|
| GOLDEN    | >=9.5          | Auto-publish to production                              |
| PUBLISH   | >=8.0          | Publish to staging with QA review                       |
| REVIEW    | >=7.0          | Require peer review and documentation update            |
| REJECT    | <7.0           | Reject; rework required before resubmission             |

## Bypass
| conditions                | approver   | audit trail                          |
|---------------------------|------------|--------------------------------------|
| Emergency system fix      | CTO        | Emergency bypass logged with reason  |
| Legacy system exemption   | QA Lead    | Legacy system approval record        |
| Experimental feature      | CTO        | Experimental flag set in metadata    |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
