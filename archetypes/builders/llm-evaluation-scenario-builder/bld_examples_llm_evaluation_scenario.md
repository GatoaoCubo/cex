---
kind: examples
id: bld_examples_llm_evaluation_scenario
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of llm_evaluation_scenario artifacts
quality: 9.1
title: "Examples LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, examples, helm]
tldr: "Golden and anti-examples of llm_evaluation_scenario artifacts"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example

```markdown
---
id: p07_evs_medical_clinical_mcq.md
kind: llm_evaluation_scenario
pillar: P07
subject_area: knowledge
capability: clinical_diagnosis_mcq
task_format: mcq
primary_metric: exact_match
num_instances: 1089
num_few_shot: 5
adapter_ref: p03_pt_helm_mcq_standard.md
dataset_source: "MedQA-USMLE (MIT License)"
canonicalization_fn: "helm_normalize_mcq_letter"
token_cost_estimate: "~2.1M tokens for 1089 instances at 5-shot"
quality: null
---

## Scenario Overview
**Subject Area**: knowledge (HELM taxonomy)
**Capability Tested**: Clinical diagnosis from patient vignettes (USMLE Step 1-3 style)

| Field | Value |
|-------|-------|
| HELM Taxonomy | knowledge > medicine |
| IBM Extension | N/A |
| Upstream Dataset | MedQA-USMLE |
| License | MIT |

## Adapter Configuration
| Parameter | Value |
|-----------|-------|
| num_train_trials | 1 |
| num_test_instances | 1089 |
| max_tokens | 5 |
| temperature | 0.0 |
| stop_sequences | ["\n"] |

## Canonicalization Rules
1. Strip leading/trailing whitespace from model output.
2. Extract first letter character (A-E) from output string.
3. Uppercase extracted letter for comparison.

**Normalization Function**: `helm_normalize_mcq_letter`
```

## Anti-Example 1: Mixed Task Format

```markdown
---
id: p07_evs_reasoning_general.md
subject_area: reasoning
capability: general_reasoning
task_format: mixed  <!-- INVALID -->
primary_metric: accuracy
---
Some tasks are MCQ, others require a 3-sentence explanation.
```

**Why it fails**: Mixed task formats violate H06. Canonicalization becomes impossible -- MCQ needs letter extraction while open-ended needs ROUGE scoring. Single scenarios must be homogeneous.

## Anti-Example 2: Vague Capability

```markdown
---
id: p07_evs_knowledge_intelligence.md
subject_area: knowledge
capability: intelligence  <!-- INVALID: not falsifiable -->
task_format: open_ended
primary_metric: bleu
---
Tests how "intelligent" the model is at answering questions.
```

**Why it fails**: "Intelligence" is not a falsifiable cognitive function (H05). A valid capability must be specific: "factual_recall_world_events_2020_2024" or "multi_step_math_word_problems".

## Anti-Example 3: Missing Canonicalization

```markdown
---
id: p07_evs_code_python_generation.md
subject_area: code
capability: python_function_generation
task_format: generation
primary_metric: pass_at_k
---
Model generates Python functions. We check if they pass unit tests.
```

**Why it fails**: Missing canonicalization_fn (H08). Code evaluation requires explicit normalization: strip markdown code fences, normalize whitespace, specify execution sandbox. Without it, metric computation is nondeterministic across runners.
