---
id: bench_c
kind: knowledge_card
title: LLM Eval Metrics
version: 1.0.0
quality: null
---

# LLM Evaluation Metrics

**Evaluation metrics** quantify model performance in tasks like translation, summarization, and generation. Here's a comparison of key metrics:

| Metric         | Description                              | When to Use                          |
|----------------|------------------------------------------|--------------------------------------|
| **BLEU**       | Measures n-gram overlap with references  | Machine translation, text generation |
| **ROUGE**      | Focuses on recall of key phrases         | Summarization, text compression     |
| **BERTScore**  | Uses semantic similarity via BERT        | Semantic equivalence checks         |
| **Human Eval** | Expert ratings for fluency/accuracy      | Subjective quality assessment       |
| **LLM-as-Judge** | Uses another LLM to score outputs     | Scalable quality assessment         |

**Best Practices**:  
- Use BLEU/ROUGE for objective benchmarks  
- Combine with human evaluation for subjective tasks  
- BERTScore complements traditional metrics  
- LLM-as-Judge enables scalable quality checks  
- Always validate metrics against task-specific goals
