---
kind: quality_gate
id: p07_qg_eval_framework
pillar: P11
llm_function: GOVERN
purpose: Quality gate for eval_framework ARTIFACTS (structure/metadata, not runtime eval throughput)
quality: 9.0
title: "Quality Gate Eval Framework"
version: "1.1.0"
author: n03_hybrid_review4
tags: [eval_framework, builder, quality_gate]
tldr: "Tests the eval_framework artifact structure. Runtime eval correctness is tested by the framework itself at execution time, not here."
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_eval_framework
  - p07_qg_benchmark_suite
  - p12_qg_workflow_node
  - bld_schema_eval_framework
  - p07_qg_memory_benchmark
  - bld_examples_benchmark_suite
  - p07_qg_eval_metric
  - eval-framework-builder
  - bld_knowledge_card_eval_framework
  - bld_examples_playground_config
---

## Quality Gate

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| ID pattern match | ^p07_efw_[a-z][a-z0-9_]+\.md$ | matches | frontmatter.id |
| Max bytes | 5120 | <= | file size |
| Required sections | 6 | >= | body |
| Metric list present | 1 | >= | body: Metrics |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Valid YAML frontmatter | YAML parse error or missing frontmatter |
| H02 | ID matches ^p07_efw_[a-z][a-z0-9_]+\.md$ | ID does not match pattern |
| H03 | kind == "eval_framework" | kind field missing or != "eval_framework" |
| H04 | pillar == "P07" | pillar != "P07" |
| H05 | quality == null | quality self-scored (must be null) |
| H06 | framework_type declared | framework_type field missing or empty |
| H07 | evaluation_criteria non-empty | evaluation_criteria array missing or [] |
| H08 | Body has "## Tasks" or "## Datasets" section | No task/dataset declaration |
| H09 | Body has "## Metrics" section with >= 1 metric | Metrics section missing or empty |
| H10 | References at least one canonical framework | No reference to lm-eval-harness, OpenAI Evals, HELM, BIG-Bench, DeepEval, Ragas, or Giskard |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Schema compliance | 0.25 | All required frontmatter fields present, correct types |
| D2 | Metric specification | 0.20 | Metrics named, formulas or references provided |
| D3 | Task/dataset grounding | 0.20 | Dataset source, version, and sample size declared |
| D4 | Reproducibility | 0.20 | Seed, version, prompt template, and adapter declared |
| D5 | Industry alignment | 0.15 | Uses EleutherAI/HELM/OpenAI-Evals/DeepEval terminology correctly |

Weight check: 0.25 + 0.20 + 0.20 + 0.20 + 0.15 = 1.00

## Actions

| Score | Action |
|-------|--------|
| GOLDEN (>= 9.5) | Auto-approve, promote to examples library |
| PUBLISH (>= 8.0) | Approve as-is |
| REVIEW (>= 7.0) | Peer review required before publish |
| REJECT (< 7.0) | Rework; fix all HARD failures and re-submit |

## Bypass

| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Legacy framework port with known gap | Pillar owner (P07) | Log bypass with migration plan + target version |

## Examples

## Golden Example
---
kind: eval_framework
name: HuggingFaceTransformersEvaluation
description: End-to-end evaluation using Hugging Face Transformers and MLflow
tools: ["Hugging Face Transformers", "MLflow", "Datasets"]
metrics: ["accuracy", "F1 score", "perplexity"]
workflow:
  - data_loading: "Load dataset from Hugging Face Datasets"
  - model_inference: "Run inference with Hugging Face Transformers model"
  - metric_calculation: "Compute metrics using evaluate library"
  - logging: "Log results to MLflow tracking server"
---

Hugging Face Transformers provides a unified API for model evaluation. The framework integrates with MLflow for experiment tracking and leverages the Hugging Face Datasets library for data loading. It supports multiple metrics and ensures reproducibility through versioned model and dataset references.

## Anti-Example 1: Benchmark Suite Confusion
---
kind: eval_framework
name: GLUEBenchmark
description: Evaluation using GLUE benchmark tasks
tools: ["GLUE benchmark"]
metrics: ["accuracy"]
workflow:
  - data_loading: "Load GLUE tasks"
  - model_inference: "Run model on tasks"
  - metric_calculation: "Compute accuracy"
---

## Why it fails
This is a benchmark collection (GLUE), not an evaluation framework. It lacks integration tools, metric diversity, and workflow automation required for end-to-end evaluation.

## Anti-Example 2: Single Metric Focus
---
kind: eval_framework
name: AccuracyOnly
description: Evaluation framework focusing on accuracy
tools: ["Custom script"]
metrics: ["accuracy"]
workflow:
  - data_loading: "Load data"
  - model_inference: "Run model"
  - metric_calculation: "Compute accuracy"
---

## Why it fails
An evaluation framework must support multiple metrics and comprehensive analysis. Focusing on a single metric (accuracy) ignores critical aspects like fairness, robustness, and error analysis.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
