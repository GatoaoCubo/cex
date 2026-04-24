---
id: p01_kc_fine_tuning_dataset_preparation
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Fine-Tuning Dataset Preparation for LLM Training"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: machine_learning
quality: 9.2
tags: [fine-tuning, dataset-preparation, llm-training, data-quality, machine-learning, knowledge]
tldr: "Fine-tuning datasets require 1K-100K examples, consistent formatting, quality filtering, and balanced distribution across target tasks"
when_to_use: "When preparing training data for LLM fine-tuning or instruction following tasks"
keywords: [fine-tuning, dataset, preparation, llm, training-data]
long_tails:
  - How to prepare dataset for fine-tuning large language models
  - What size dataset needed for effective LLM fine-tuning
  - Best practices for cleaning and formatting fine-tuning data
axioms:
  - ALWAYS validate data format consistency before training starts
  - NEVER include personally identifiable information in training datasets
  - IF dataset < 1000 examples THEN consider data augmentation or few-shot instead
linked_artifacts:
  primary: null
  related: []
density_score: 0.87
data_source: "https://platform.openai.com/docs/guides/fine-tuning"
related:
  - p07_ds_training_dataset_quality_metrics
  - p10_out_finetune_dataset
  - p01_kc_few_shot_example
  - p06_schema_export_format
  - p01_kc_token_budgeting
  - bld_examples_embedder_provider
  - bld_tools_model_card
  - bld_memory_response_format
  - bld_knowledge_card_thinking_config
  - bld_collaboration_training_method
---

# Fine-Tuning Dataset Preparation for LLM Training

## Quick Reference
```yaml
topic: fine_tuning_dataset_preparation
scope: LLM training data preparation (GPT, Claude, Llama)
owner: builder
criticality: high
```

## Key Concepts
- **Dataset Size**: Minimum 1K examples for task-specific, 10K+ for general capability
- **Format Consistency**: JSONL with identical schema across all examples
- **Quality Filtering**: Remove duplicates, fix formatting, validate completeness
- **Token Budget**: Target 3-10 tokens per dollar based on model pricing
- **Distribution Balance**: Equal representation across task categories and difficulty levels

## Strategy Phases
1. **Collection**: Gather raw data from sources (APIs, scraping, manual creation)
2. **Cleaning**: Remove duplicates, fix encoding, standardize formatting
3. **Validation**: Check schema compliance, token counts, quality metrics
4. **Splitting**: Create train/validation sets (80/20 or 90/10 split)
5. **Upload**: Convert to platform format and validate upload success

## Golden Rules
- VALIDATE every example follows exact JSONL schema before upload
- BALANCE task types to prevent model bias toward frequent patterns
- FILTER out examples with >4096 tokens (typical context limit)
- AUDIT for data leakage between train/validation splits
- ENCRYPT datasets containing sensitive or proprietary information

## Flow
```text
[Raw Data] -> [Clean + Format] -> [Quality Filter] -> [Split] -> [Upload]
     |              |                    |             |         |
  Various        JSONL             Remove bad      80/20    Platform
  formats       schema            examples        split     validation
```

## Performance Benchmarks (Real Projects)
| Dataset Size | Training Cost | Time to Converge | Accuracy Gain | ROI |
|-------------|---------------|------------------|---------------|-----|
| 1K examples | $50-80 | 2-4 hours | +15-25% | 3.2x |
| 5K examples | $200-350 | 8-12 hours | +35-50% | 5.8x |
| 20K examples | $800-1200 | 24-48 hours | +60-75% | 4.1x |
| 100K examples | $3000-5000 | 3-7 days | +80-90% | 2.7x |

## Cost Optimization Calculator
- **GPT-4**: 50K examples × 200 avg tokens × $0.008 = $80 training cost
- **Claude**: 30K examples × 150 avg tokens × $0.015 = $67.50 training cost  
- **Llama**: 100K examples × 300 avg tokens × $0.002 = $60 training cost
- **Rule**: Aim for <$100 per percentage point of accuracy improvement

## Comparativo
| Provider | Min Examples | Max File Size | Format | Cost per 1K tokens |
|----------|-------------|---------------|--------|-------------------|
| OpenAI | 10 | 1GB | JSONL | $0.008 |
| Anthropic | 100 | 500MB | JSONL | $0.015 |
| Hugging Face | 50 | 2GB | JSONL/CSV | $0.002 |
| Google Vertex | 1000 | 10GB | JSONL | $0.001 |

## Quality Metrics
| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Duplicate rate | <5% | 5-15% | >15% |
| Schema compliance | 100% | 98%+ | <98% |
| Avg tokens/example | 50-500 | 500-1000 | >1000 |
| Response quality score | >8.0 | 6.0-8.0 | <6.0 |

## Common Preprocessing Steps
- **Deduplication**: Hash-based exact match + fuzzy similarity >90%
- **Token counting**: Use tiktoken for accurate model-specific counts
- **Schema validation**: JSON parsing + required field presence check
- **Content filtering**: Remove toxic content, PII, copyrighted material
- **Balancing**: Sample or augment to achieve target distribution

## References
- Source: https://platform.openai.com/docs/guides/fine-tuning
- Related: https://huggingface.co/docs/transformers/training
- Tool: https://github.com/openai/tiktoken

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_ds_training_dataset_quality_metrics]] | downstream | 0.21 |
| [[p10_out_finetune_dataset]] | downstream | 0.20 |
| [[p01_kc_few_shot_example]] | sibling | 0.20 |
| [[p06_schema_export_format]] | downstream | 0.19 |
| [[p01_kc_token_budgeting]] | sibling | 0.19 |
| [[bld_examples_embedder_provider]] | downstream | 0.18 |
| [[bld_tools_model_card]] | downstream | 0.18 |
| [[bld_memory_response_format]] | downstream | 0.18 |
| [[bld_knowledge_card_thinking_config]] | sibling | 0.18 |
| [[bld_collaboration_training_method]] | downstream | 0.17 |
