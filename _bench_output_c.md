---
id: bench_c
kind: knowledge_card
title: LLM Eval Metrics
version: 1.0.0
quality: null
---

**Evaluation Metrics** are quantitative measures used to assess the performance of language models in tasks like translation, summarization, and generation.

| Metric         | Description                              | When to Use                          |
|----------------|------------------------------------------|--------------------------------------|
| **BLEU**       | Measures n-gram overlap with references  | Machine translation, text generation |
| **ROUGE**      | Focuses on recall of n-grams             | Summarization, text compression      |
| **BERTScore**  | Uses semantic similarity via BERT        | Semantic understanding, paraphrasing |
| **Human Eval** | Subjective assessment by human annotators| Quality judgment, creative tasks     |
| **LLM-as-Judge** | Uses another model to score outputs    | Quick validation, large-scale testing|

Use BLEU/ROUGE for objective comparisons, BERTScore for semantic alignment, and human eval/LLM-as-Judge for qualitative insights.
