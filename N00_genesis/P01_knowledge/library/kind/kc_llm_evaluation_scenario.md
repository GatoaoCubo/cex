---
id: kc_llm_evaluation_scenario
kind: knowledge_card
8f: F3_inject
title: LLM Evaluation Scenario
version: 1.0.0
quality: 8.9
pillar: P01
tldr: "Structured evaluation framework for LLM performance using HELM metrics, adapter configs, and few-shot pools"
when_to_use: "When defining repeatable test scenarios to benchmark LLM quality across fluency, relevance, and toxicity"
density_score: 1.0
related:
  - llm-evaluation-scenario-builder
  - p03_sp_llm_evaluation_scenario_builder
  - bld_knowledge_card_llm_evaluation_scenario
  - n01_atom_26_evaluation_taxonomy
  - bld_collaboration_llm_evaluation_scenario
  - eval-framework-builder
  - bld_instruction_llm_evaluation_scenario
  - kc_judge_config
  - p10_lr_llm_evaluation_scenario_builder
  - p01_kc_prompt_engineering_best_practices
---

# LLM Evaluation Scenario

## Overview
A structured framework for assessing large language model (LLM) performance using HELM (Human Evaluation of Machine Learning) and Stanford CRFM (Continuous Representation for Fine-tuning Models) methodologies. This scenario defines task instances, metric mapping, adapter configurations, and canonicalization protocols for consistent evaluation.

## Task Instances
- **Task Types**: Text generation, reasoning, code execution, multilingual translation
- **Input Formats**: JSON/CSV with prompt, context, and expected output fields
- **Execution Modes**: Single-turn, multi-turn, chain-of-thought

## Metric Mapping
| Metric              | Definition                          | Weight |
|---------------------|-------------------------------------|--------|
| Fluency             | Grammatical correctness and flow    | 0.35   |
| Relevance           | Alignment with expected output      | 0.25   |
| Coherence           | Logical consistency                 | 0.20   |
| Diversity           | Variation in generated responses    | 0.10   |
| Toxicity           | Presence of harmful content         | 0.10   |

## Adapter Configuration
- **Model Adapter**: HF Transformers (PyTorch) or GGUF (CUDA)
- **Batch Size**: 16-256 (depends on GPU memory)
- **Temperature**: 0.7-1.2 (controls creativity vs. consistency)
- **Top-p**: 0.95 (nucleus sampling)

## Few-Shot Pool
- **Training Data**: 1000 curated examples (500 validation, 500 test)
- **Prompt Templates**: 
  - `Question: {q} || Answer: {a} || Reasoning: {r}`
  - `Input: {input} || Output: {output} || Score: {score}`

## Canonicalization
1. **Normalization**: Remove extra whitespace, standardize capitalization
2. **Tokenization**: Use BPE (Byte Pair Encoding) for consistent tokenization
3. **Scoring**: 
   - Automatic: BLEU-4, ROUGE-L, perplexity
   - Human: 5-point Likert scale (1=poor, 5=excellent)
4. **Bias Mitigation**: 
   - Use demographic fairness metrics
   - Apply adversarial debiasing during training

## Implementation Notes
- Requires access to HELM evaluation dashboard
- Must include metadata: model version, dataset split, evaluation date
- Results should be stored in `.cex/evaluations/` with timestamped directories

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[llm-evaluation-scenario-builder]] | downstream | 0.36 |
| [[p03_sp_llm_evaluation_scenario_builder]] | downstream | 0.35 |
| [[bld_knowledge_card_llm_evaluation_scenario]] | sibling | 0.28 |
| [[n01_atom_26_evaluation_taxonomy]] | sibling | 0.24 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.23 |
| [[eval-framework-builder]] | downstream | 0.22 |
| [[bld_instruction_llm_evaluation_scenario]] | downstream | 0.22 |
| [[kc_judge_config]] | sibling | 0.22 |
| [[p10_lr_llm_evaluation_scenario_builder]] | downstream | 0.22 |
| [[p01_kc_prompt_engineering_best_practices]] | sibling | 0.22 |
