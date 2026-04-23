---
kind: schema
id: bld_schema_judge_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for judge_config artifacts
quality: 9.2
title: "Schema Judge Config"
version: "1.1.0"
author: n03_hybrid_review4
tags: [judge_config, builder, schema]
tldr: "Schema for an LLM-as-judge configuration -- aligned with MT-Bench, Chatbot-Arena, G-Eval, Prometheus, PandaLM canonical patterns."
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.92
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_multimodal_prompt
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_sandbox_spec
  - bld_schema_search_strategy
---

## Frontmatter Fields

### Required

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | -- | Must match ID Pattern below |
| kind | string | yes | "judge_config" | Must equal "judge_config" |
| pillar | string | yes | "P07" | Must equal "P07" |
| title | string | yes | -- | Descriptive name |
| version | string | yes | "1.0.0" | Semantic version |
| created | date | yes | -- | ISO 8601 |
| updated | date | yes | -- | ISO 8601 |
| author | string | yes | -- | Owner |
| domain | string | yes | -- | Judging domain (factuality, safety, style, pairwise_chat, rag_faithfulness) |
| quality | null | yes | null | NEVER self-score; peer review assigns |
| tags | array | yes | [] | Keywords |
| tldr | string | yes | -- | One-sentence summary |
| judge_type | enum | yes | -- | One of: pairwise, rubric, reference_based, direct |
| judge_model | object | yes | -- | {provider, model, temperature} e.g. {provider: openai, model: gpt-4-turbo, temperature: 0} |
| scoring_scale | string | yes | -- | "1-5", "1-10", "binary", "pairwise_ab_tie", or custom |
| judgment_criteria | array | yes | [] | Named criteria (relevance, faithfulness, coherence, harmlessness, ...) |
| prompt_template_ref | string | yes | -- | Reference to prompt_template artifact id |

### Recommended

| Field | Type | Notes |
|-------|------|-------|
| rubric | object | Anchored descriptors per scale level (Prometheus-style) |
| reference_answer_ref | string | Required for judge_type == "reference_based" |
| position_bias_mitigation | enum | "swap_order", "randomize", "none" -- for pairwise |
| length_bias_mitigation | string | e.g., "normalize_by_token_count" |
| calibration_examples | array | Few-shot exemplars with gold scores |
| self_consistency_n | integer | Number of judge samples to aggregate |

## ID Pattern

Regex: `^p07_jc_[a-z][a-z0-9_]+\.md$`

Examples: `p07_jc_mtbench_gpt4.md`, `p07_jc_prometheus_rubric5.md`, `p07_jc_pairwise_arena.md`

## Body Structure (required sections)

1. **Overview** -- what this judge evaluates, when to invoke it.
2. **Criteria** -- each criterion: name, definition, observable signals.
3. **Rubric** -- for each scale level, a descriptor and a worked example.
4. **Judge Model** -- provider, model, temperature, decoding parameters; rationale for choice.
5. **Bias Controls** -- position, length, self-enhancement, verbosity mitigations.
6. **Example** -- input -> judge prompt -> sample output with parsed score.

## Constraints

- judge_type is an enum; no free-form values.
- For judge_type == "reference_based", reference_answer_ref MUST be set.
- For judge_type == "pairwise", position_bias_mitigation MUST be declared (non-null).
- judge_model.temperature SHOULD be 0 for deterministic scoring unless self_consistency_n > 1.
- scoring_weights (if present in body) MUST sum to 1.00.
- File size must not exceed 4096 bytes.
- quality is assigned by peer review; always null at authoring time.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_usage_report]] | sibling | 0.66 |
| [[bld_schema_benchmark_suite]] | sibling | 0.65 |
| [[bld_schema_pitch_deck]] | sibling | 0.64 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.64 |
| [[bld_schema_integration_guide]] | sibling | 0.64 |
| [[bld_schema_quickstart_guide]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
| [[bld_schema_sandbox_spec]] | sibling | 0.62 |
| [[bld_schema_search_strategy]] | sibling | 0.62 |
