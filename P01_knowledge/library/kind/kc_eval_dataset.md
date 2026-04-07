---
id: p01_kc_eval_dataset
kind: knowledge_card
type: kind
pillar: P07
title: "Eval Dataset — Deep Knowledge for eval_dataset"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: eval_dataset
quality: 9.1
tags: [eval_dataset, P07, GOVERN, kind-kc]
tldr: "Versioned collection of test cases with inputs and expected outputs for systematic evaluation."
when_to_use: "Building, reviewing, or reasoning about eval_dataset artifacts"
keywords: [dataset, test-cases, eval, benchmark, versioned]
feeds_kinds: [eval_dataset]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Eval Dataset

## Spec
```yaml
kind: eval_dataset
pillar: P07
llm_function: GOVERN
max_bytes: 4096
naming: p07_dataset.md
core: true
```

## What It Is
A versioned, curated collection of test cases—each with an input, expected output, and metadata—used to drive unit_eval, e2e_eval, benchmark, and regression_check runs. A dataset is a CONTAINER; golden_tests are individual cases. NOT golden_test (one case with quality >= 9.5; eval_dataset contains many quality levels). NOT benchmark (dataset is the input; benchmark is the protocol that uses it).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | Dataset (LangSmith) | Evaluation dataset with input/output pairs |
| LlamaIndex | EmbeddingQAFinetuneDataset | QA pairs for retrieval eval |
| CrewAI | Manual test corpus | No native format; use JSON/CSV |
| DSPy | trainset / devset | List of dspy.Example objects |
| Haystack | EvaluationDataset | Haystack native eval dataset format |
| OpenAI | Evals data_source | JSONL file with {input, ideal} pairs |
| Anthropic | Custom eval JSONL | {prompt, expected_output} JSONL format |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| size | int | >= 30 | Larger = more coverage, higher eval cost |
| splits | dict | {test: 1.0} | train/dev/test splits for iterative dev |
| version | semver | 1.0.0 | Must increment when cases added/changed |
| distribution | dict | balanced | Imbalanced = biased metric reporting |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Balanced split | Iterative prompt optimization | 70% dev, 30% test, never mix |
| Golden subset | High-confidence regression guard | Include all golden_tests as subset |
| Adversarial mix | Robust eval including edge cases | 20% adversarial + 80% nominal |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No version tracking | Can't reproduce past eval results | Increment version on any case change |
| Test set contamination | Dev/test leak = inflated metrics | Hard split, never re-use test cases |
| Only happy-path cases | Misses edge cases and failures | Include 20%+ adversarial or edge cases |

## Integration Graph
```
[golden_test] -------> [eval_dataset] --> [unit_eval]
[few_shot_ex (P01)] -> [eval_dataset] --> [e2e_eval]
                           |-----------> [benchmark]
                           |-----------> [regression_check]
```

## Decision Tree
- IF single high-quality reference case THEN golden_test
- IF collection for running evals systematically THEN eval_dataset
- IF defining the measurement protocol THEN benchmark
- DEFAULT: eval_dataset for any systematic evaluation corpus

## Quality Criteria
- GOOD: Versioned, size >= 30, splits defined, source documented
- GREAT: Contains golden_test subset, adversarial cases labeled, distribution reported
- FAIL: Single case, no version, no splits, test/dev contaminated
