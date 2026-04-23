---
kind: schema
id: bld_schema_eval_framework
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for eval_framework artifacts
quality: 9.2
title: "Schema Eval Framework"
version: "1.1.0"
author: n03_hybrid_review4
tags: [eval_framework, builder, schema]
tldr: "Schema for a named eval framework -- aligned with EleutherAI lm-eval-harness, OpenAI Evals, HELM, BIG-Bench, DeepEval canonical patterns."
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.92
related:
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_eval_metric
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_customer_segment
  - bld_schema_nps_survey
---

## Frontmatter Fields

### Required

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | -- | Must match ID Pattern below |
| kind | string | yes | "eval_framework" | Must equal "eval_framework" |
| pillar | string | yes | "P07" | Must equal "P07" |
| title | string | yes | -- | Descriptive name |
| version | string | yes | "1.0.0" | Semantic version |
| created | date | yes | -- | ISO 8601 |
| updated | date | yes | -- | ISO 8601 |
| author | string | yes | -- | Owner |
| domain | string | yes | -- | Application domain (NLP, code, safety, reasoning, RAG, agent) |
| quality | null | yes | null | NEVER self-score; peer review assigns |
| tags | array | yes | [] | Keywords |
| tldr | string | yes | -- | One-sentence summary |
| framework_type | enum | yes | -- | One of: benchmark, task_suite, red_team, rag_eval, agent_eval, judge_eval |
| tasks | array | yes | [] | Task ids or dataset refs (lm-eval-harness task names, HELM scenarios, etc.) |
| metrics | array | yes | [] | Metric names (exact_match, f1, rouge_l, pass_at_k, bleu, accuracy, g_eval_score, faithfulness) |
| runner | string | yes | -- | Execution backend (lm-eval-harness, openai-evals, helm, deepeval, custom) |

### Recommended

| Field | Type | Notes |
|-------|------|-------|
| adapter | string | Model I/O adapter (chat, completion, logprobs, tool_use) |
| fewshot_k | integer | Number of few-shot examples; 0 for zero-shot |
| sample_size | integer | Items sampled from each task; null for full |
| seed | integer | Reproducibility seed |
| prompt_template_ref | string | Reference to prompt_template artifact id |
| dependencies | array | Required libraries with versions |
| references | array | Citations (papers, leaderboards) |

## ID Pattern

Regex: `^p07_efw_[a-z][a-z0-9_]+\.md$`

Examples: `p07_efw_mmlu_core.md`, `p07_efw_helm_nlp.md`, `p07_efw_rag_ragas.md`

## Body Structure (required sections)

1. **Overview** -- purpose, target capability, canonical reference.
2. **Tasks** -- each task: id, dataset source, size, example item.
3. **Metrics** -- each metric: name, formula or reference, aggregation (mean/macro/micro).
4. **Runner & Adapter** -- execution stack, input/output format, model requirements.
5. **Reproducibility** -- seed, version pins, prompt template reference.
6. **References** -- papers, leaderboards, prior implementations.

## Constraints

- framework_type is an enum; no free-form values.
- tasks array MUST be non-empty.
- metrics array MUST be non-empty AND contain at least one metric name recognized by the runner.
- If runner == "lm-eval-harness", tasks must reference real task registry names.
- If framework_type == "rag_eval", metrics SHOULD include faithfulness or answer_relevance.
- File size must not exceed 5120 bytes.
- quality is assigned by peer review; always null at authoring time.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_benchmark_suite]] | sibling | 0.64 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.62 |
| [[bld_schema_reranker_config]] | sibling | 0.62 |
| [[bld_schema_usage_report]] | sibling | 0.62 |
| [[bld_schema_integration_guide]] | sibling | 0.60 |
| [[bld_schema_eval_metric]] | sibling | 0.59 |
| [[bld_schema_quickstart_guide]] | sibling | 0.59 |
| [[bld_schema_pitch_deck]] | sibling | 0.58 |
| [[bld_schema_customer_segment]] | sibling | 0.58 |
| [[bld_schema_nps_survey]] | sibling | 0.58 |
