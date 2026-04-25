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
tldr: "Qwen3 primary (120ms P95) + BERTimbau fallback (91% PT-BR) = optimal hybrid. Both local at $0 vs $16K/year API."
when_to_use: "Choose embedding model for Portuguese RAG or compare local vs API cost"
keywords: [embedding_benchmark, qwen3, bertimbau, hybrid_routing, latency_sla]
long_tails:
  - "Best embedding model for Brazilian Portuguese"
  - "How much does local embedding cost vs OpenAI API per year"
axioms:
  - "ALWAYS prioritize latency SLA over marginal accuracy"
  - "NEVER use paid API when local model meets target"
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals]
density_score: 1.0
data_source: "Internal benchmark: 50 queries x 30 docs, metrics Recall/MRR/NDCG/Latency"
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
dataset: 50 queries, 30 documents (product search, competitor, pricing, compliance)
decision: Qwen3 primary + BERTimbau fallback (hybrid)

## Key Concepts

- Qwen3: 768-dim, multilingual, 120ms P95, 76% PT-BR
- BERTimbau: PT-BR specialist, 91% accuracy, 320ms P95
- Hybrid: regulatory -> BERTimbau, rest -> Qwen3
- Local cost: $0/year (Docker) vs $16K/year (OpenAI API)

## Comparison

| Metric | Target | Qwen3 | BERTimbau | Winner |
|---------|--------|-------|-----------|----------|
| Recall@5 | >= 0.75 | 0.780 | 0.820 | BERTimbau |
| MRR | >= 0.85 | 0.820 | 0.880 | BERTimbau |
| NDCG@5 | >= 0.80 | 0.810 | 0.850 | BERTimbau |
| Latency P95 | <= 200ms | **120ms** | 320ms | **Qwen3** |
| PT-BR Accuracy | >= 0.80 | 76% | **91%** | **BERTimbau** |
| Targets met | 5/5 | 3/5 | 4/5 | — |

| Cost | Monthly | Annual |
|------|---------|--------|
| Qwen3 local | $0 model | $0 |
| BERTimbau local | $0 model | $0 |
| Docker infra | ~$50 | ~$600 |
| **Total local** | **~$50** | **~$600** |
| OpenAI API | $1,333 | **$16,000** |
| **Savings** | **$1,283/month** | **$15,400/year** |

## Golden Rules

- ALWAYS use Qwen3 as default (120ms meets UX SLA)
- ALWAYS route regulatory queries to BERTimbau
- NEVER pay for embedding API when local model meets targets
- ALWAYS re-benchmark monthly (models drift)

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
- deepens: p01_kc_rag_fundamentals (complete RAG architecture)
- deepens: /skill embedding_evaluation (how to benchmark — to be created)


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
