---
kind: quality_gate
id: p07_qg_eval_metric
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for eval_metric
quality: 9.1
title: "Quality Gate Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for eval_metric"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_eval_metric
  - p03_qg_prompt_technique
  - p03_qg_multimodal_prompt
  - p11_qg_usage_report
  - p01_qg_graph_rag_config
  - p05_qg_product_tour
  - p07_qg_memory_benchmark
  - p07_qg_benchmark_suite
  - p03_qg_prompt_optimizer
  - p05_qg_integration_guide
---

## Quality Gate

## Definition
| metric          | threshold | operator | scope        |
|-----------------|-----------|----------|--------------|
| frontmatter     | valid     | ==       | artifact     |
| section_count   | >=4       | >=       | body         |
| metric_type     | defined   | ==       | frontmatter  |
| id_pattern      | matches   | ==       | frontmatter  |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID       | Check                  | Fail Condition                                      |
|----------|------------------------|-----------------------------------------------------|
| H01      | YAML frontmatter valid | Invalid YAML syntax or missing fields               |
| H02      | ID matches pattern     | ID does not match ^p07_em_[a-z][a-z0-9_]+.md$      |
| H03      | kind field matches     | kind is not 'eval_metric'                           |
| H04      | metric defined         | metric field is missing or empty                    |
| H05      | threshold numeric      | threshold is not a number                           |
| H06      | operator valid         | operator is not in [<=, >=, ==, !=]                |
| H07      | scope defined          | scope field is missing or empty                     |

## SOFT Scoring
| Dim | Dimension     | Weight | Scoring Guide                                      |
|-----|---------------|--------|----------------------------------------------------|
| D1  | Clarity       | 0.15   | Clear definition (1.0) vs ambiguous (0.0)          |
| D2  | Relevance     | 0.20   | Directly tied to task goal (1.0) vs irrelevant     |
| D3  | Precision     | 0.15   | Measurable with formula (1.0) vs vague (0.0)       |
| D4  | Consistency   | 0.10   | Aligns with existing metrics (1.0) vs conflicting  |
| D5  | Documentation | 0.10   | Full context provided (1.0) vs incomplete          |
| D6  | Uniqueness    | 0.10   | No duplication (1.0) vs redundant (0.0)            |
| D7  | Scope         | 0.10   | Covers critical use case (1.0) vs limited          |
| D8  | Alignment     | 0.10   | Supports evaluation goals (1.0) vs misaligned      |

## Actions
(Table: Score | Action)
| Score     | Action         |
|-----------|----------------|
| >=9.5     | GOLDEN         |
| >=8.0     | PUBLISH        |
| >=7.0     | REVIEW         |
| <7.0      | REJECT         |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                  | approver       | audit trail              |
|-----------------------------|----------------|--------------------------|
| Critical business exception | CTO            | Signed waiver, timestamp |

## Examples

## Golden Example
```yaml
---
metric_name: "BLEU Score"
vendor: "Hugging Face"
version: "1.0.0"
description: "Measures the quality of machine translation by comparing generated text to reference translations."
---
**Definition**:
The BLEU (Bilingual Evaluation Understudy) score evaluates generated text by computing precision at the n-gram level (typically 4-grams) and applying a brevity penalty for shorter outputs.

**Calculation**:
1. Compute precision for each n-gram (n=1 to 4).
2. Geometric mean of precision scores.
3. Apply brevity penalty if generated text is shorter than the reference.

**Use Case**:
Assessing machine translation models in multilingual NLP tasks.

**Example**:
Generated: "The cat is on the mat."
Reference: "The cat sits on the mat."
Score: 0.85 (high precision, minor brevity penalty).
```

## Anti-Example 1: Vague Metric Definition
```yaml
---
metric_name: "Quality Check"
vendor: "ExampleCorp"
version: "0.1"
description: "Measures how good something is."
---
**Definition**:
"Quality Check" evaluates outputs based on unspecified criteria.

**Calculation**:
"Calculated using internal methods."

**Use Case**:
"Used for everything."
```
## Why it fails
Lacks specificity in calculation, use case, and criteria. No reproducibility or clarity for users.

## Anti-Example 2: Composite Metric
```yaml
---
metric_name: "Overall Model Performance"
vendor: "MLVendor"
version: "2.0"
description: "Combines accuracy, F1, and BLEU into a single score."
---
**Definition**:
Weighted average of accuracy (40%), F1 score (30%), and BLEU (30%).

**Calculation**:
(0.4 * accuracy) + (0.3 * F1) + (0.3 * BLEU).

**Use Case**:
"General-purpose model evaluation."
```
## Why it fails
Violates the boundary of being a *single* metric. Combines multiple metrics into a composite, making it unsuitable for focused evaluation.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
