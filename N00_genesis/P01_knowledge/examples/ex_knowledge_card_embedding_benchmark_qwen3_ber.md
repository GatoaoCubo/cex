---
id: p01_kc_embedding_benchmark_qwen3_bertimbau
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Embedding Benchmark: Qwen3 vs BERTimbau para PT-BR E-Commerce"
version: 2.0.0
created: 2026-01-17
updated: 2026-03-25
author: research_agent
domain: research
quality: 9.1
tags: [embedding, benchmark, qwen3, bertimbau, pt-br, rag, ecommerce]
tldr: "Qwen3 primary (120ms P95) + BERTimbau fallback (91% PT-BR) = hybrid otimo. Ambos local a $0 vs $16K/ano API."
when_to_use: "Escolher modelo de embedding para RAG em portugues ou comparar custo local vs API"
keywords: [embedding_benchmark, qwen3, bertimbau, hybrid_routing, latency_sla]
long_tails:
  - "Qual melhor modelo embedding para portugues brasileiro"
  - "Quanto custa embedding local vs OpenAI API por ano"
axioms:
  - "SEMPRE priorizar latency SLA sobre accuracy marginal"
  - "NUNCA usar API paga quando modelo local atinge target"
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals]
density_score: 1.0
data_source: "Benchmark proprio: 50 queries x 30 docs, metricas Recall/MRR/NDCG/Latency"
related:
  - spec_local_model_per_nucleus
  - p01_kc_vector_embedding_model_selection
  - kc_test_ollama_wrapper
  - p01_kc_llm_benchmark_ecommerce_copy
  - p09_kc_retriever_domain
  - bld_knowledge_card_embedding_config
  - bld_examples_embedder_provider
  - claude_vs_free_decision_matrix
  - p01_emb_openai_text_embedding_3_small
  - atom_33_nucleus_model_strategy
---

## Quick Reference

topic: embedding model selection | scope: PT-BR e-commerce RAG | criticality: high
dataset: 50 queries, 30 documentos (product search, competitor, pricing, compliance)
decisao: Qwen3 primary + BERTimbau fallback (hybrid)

## Conceitos Chave

- Qwen3: 768-dim, multilingual, 120ms P95, 76% PT-BR
- BERTimbau: PT-BR specialist, 91% accuracy, 320ms P95
- Hybrid: regulatorio -> BERTimbau, resto -> Qwen3
- Custo local: $0/ano (Docker) vs $16K/ano (OpenAI API)

## Comparativo

| Metrica | Target | Qwen3 | BERTimbau | Vencedor |
|---------|--------|-------|-----------|----------|
| Recall@5 | >= 0.75 | 0.780 | 0.820 | BERTimbau |
| MRR | >= 0.85 | 0.820 | 0.880 | BERTimbau |
| NDCG@5 | >= 0.80 | 0.810 | 0.850 | BERTimbau |
| Latency P95 | <= 200ms | **120ms** | 320ms | **Qwen3** |
| PT-BR Accuracy | >= 0.80 | 76% | **91%** | **BERTimbau** |
| Targets met | 5/5 | 3/5 | 4/5 | — |

| Custo | Mensal | Anual |
|-------|--------|-------|
| Qwen3 local | $0 modelo | $0 |
| BERTimbau local | $0 modelo | $0 |
| Infra Docker | ~$50 | ~$600 |
| **Total local** | **~$50** | **~$600** |
| OpenAI API | $1,333 | **$16,000** |
| **Economia** | **$1,283/mes** | **$15,400/ano** |

## Regras de Ouro

- SEMPRE usar Qwen3 como default (120ms atende SLA de UX)
- SEMPRE rotear queries regulatorias para BERTimbau
- NUNCA pagar API embedding quando modelo local atinge targets
- SEMPRE re-benchmarkar mensalmente (modelos driftam)

## Code

<!-- lang: python | purpose: hybrid embedding routing -->
```python
PT_BR_TRIGGERS = ["anvisa", "inmetro", "conar", "registro", "certificacao"]

def embed_hybrid(texts):
    use_bertimbau = any(t in text.lower() for text in texts for t in PT_BR_TRIGGERS)
    return bertimbau_embed(texts) if use_bertimbau else qwen3_embed(texts)
# 90% -> Qwen3 (120ms) | 10% -> BERTimbau (320ms) | Blended P95: ~140ms
```

## References

- external: https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct
- external: https://huggingface.co/neuralmind/bert-base-portuguese-cased
- deepens: p01_kc_rag_fundamentals (arquitetura RAG completa)
- deepens: /skill embedding_evaluation (como benchmarkar — a ser criada)


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_local_model_per_nucleus]] | downstream | 0.29 |
| [[p01_kc_vector_embedding_model_selection]] | sibling | 0.21 |
| [[kc_test_ollama_wrapper]] | related | 0.21 |
| [[p01_kc_llm_benchmark_ecommerce_copy]] | sibling | 0.19 |
| [[p09_kc_retriever_domain]] | sibling | 0.19 |
| [[bld_knowledge_card_embedding_config]] | sibling | 0.16 |
| [[bld_examples_embedder_provider]] | downstream | 0.16 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.16 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.16 |
| [[atom_33_nucleus_model_strategy]] | sibling | 0.15 |
