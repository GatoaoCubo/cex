---
kind: quality_gate
id: bld_eval_retrieval_evaluator
pillar: P07
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for retrieval_evaluator
quality: null
title: "Retrieval Evaluator Builder - Eval ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, quality_gate]
tldr: "Quality gate for retrieval evaluator artifacts: validates metric definition, judgment scale, query set, and baseline."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_retrieval_evaluator
  - bld_model_retrieval_evaluator
---

## Quality Gate

## Definition

| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| frontmatter | valid | == | artifact |
| section_count | >=5 | >= | body |
| primary_metric | defined | == | frontmatter |
| id_pattern | matches | == | frontmatter |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern | ID does not match ^p07_re_[a-z][a-z0-9_]+$ |
| H03 | kind field matches | kind is not 'retrieval_evaluator' |
| H04 | primary_metric defined | primary_metric field missing or empty |
| H05 | quality is null | quality must be null at authoring time |
| H06 | Required fields present | Missing: id, kind, pillar, primary_metric, k_values, judgment_scale, baseline |
| H07 | judgment_scale valid | judgment_scale not in [binary, graded] |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Metric clarity | 0.20 | Formula provided (1.0) vs vague description (0.0) |
| D2 | Query set spec | 0.15 | Size, construction, domain coverage documented |
| D3 | Baseline defined | 0.15 | Reference system with expected scores (1.0) vs absent (0.0) |
| D4 | Threshold precision | 0.15 | Numeric pass/fail criteria (1.0) vs qualitative (0.0) |
| D5 | Judgment protocol | 0.10 | Annotator guidelines documented (1.0) vs missing (0.0) |
| D6 | Statistical rigor | 0.10 | Confidence intervals, significance tests mentioned |
| D7 | Regression detection | 0.10 | Automated regression criteria defined |
| D8 | Documentation | 0.05 | tldr captures key info in <= 160 characters |

## Actions

| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Golden Example

```yaml
---
id: p07_re_rag_retrieval_v1
kind: retrieval_evaluator
primary_metric: ndcg
k_values: [1, 5, 10]
judgment_scale: graded
min_query_set_size: 100
baseline: bm25_default
quality: null
---
## Metrics
NDCG@k = (DCG@k / IDCG@k). DCG@k = sum(rel_i / log2(i+1)) for i=1..k.
Secondary: MRR = 1/rank_of_first_relevant.
## Query Set
100 queries across 5 domains. Constructed from real user queries with manual relevance annotation.
## Judgment Protocol
Graded scale: 0=irrelevant, 1=marginally relevant, 2=relevant, 3=highly relevant.
Inter-annotator agreement: Cohen's kappa >= 0.7 required.
```

## Anti-Example

```yaml
id: eval_retrieval
kind: evaluator
primary_metric: "good results"
quality: 9.0
```

FAILURES: id pattern wrong, kind wrong, metric not measurable, quality not null.
