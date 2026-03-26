---
lp: P07
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_card artifacts
pattern: few-shot learning — LLM reads these before producing
source: P01_knowledge/examples/ex_knowledge_card_rag_fundamentals.md (real golden)
---

# Examples: knowledge-card-builder

## Golden Example

INPUT: "Destila conhecimento sobre RAG fundamentals"

OUTPUT:
```yaml
---
id: p01_kc_rag_fundamentals
type: knowledge_card
lp: P01
title: "RAG Fundamentals - Retrieval-Augmented Generation"
version: "1.0.0"
created: "2026-03-23"
updated: "2026-03-23"
author: "EDISON"
domain: "knowledge_engineering"
quality: null
tags: [rag, embeddings, chunking, retrieval, vector_search]
tldr: "RAG combina retrieval (BM25/FAISS) com generation (LLM) para respostas grounded em fontes reais"
when_to_use: "Quando LLM precisa de conhecimento atualizado ou verificavel"
keywords: [retrieval-augmented-generation, semantic-search, hybrid-search]
long_tails:
  - "Como escolher chunk size ideal para RAG"
  - "Diferenca entre BM25 e busca semantica em RAG"
axioms:
  - "SEMPRE chunk com overlap >= 10% para preservar contexto"
  - "NUNCA embeddar documentos inteiros acima de 512 tokens"
linked_artifacts:
  primary: null
  related: [p01_emb_nomic_embed_text]
density_score: 0.92
data_source: "https://arxiv.org/abs/2005.11401"
---

# RAG Fundamentals - Retrieval-Augmented Generation

## Quick Reference
```yaml
topic: retrieval-augmented-generation
scope: LLM knowledge pipelines
owner: PYTHA
criticality: high
```

## Key Concepts
- **Chunking**: fragmentacao de docs em blocos semanticos
- **Embedding**: projecao de texto em vetor denso N-dimensional
- **Hybrid Search**: BM25 (lexical) + FAISS (semantico) combinados
- **Context Injection**: chunks recuperados inseridos no prompt
- **Grounding**: ancoragem da resposta em evidencias reais

## Strategy Phases
1. **Ingest**: docs -> chunking -> embedding -> vector store
2. **Retrieve**: query -> embed -> similarity search -> rerank
3. **Generate**: LLM processa contexto augmentado -> resposta

## Golden Rules
- NUNCA confie em chunk size unico — teste 256/512/1024
- SEMPRE use hybrid search (BM25+semantic)
- SE retrieval score < 0.7 ENTAO fallback "nao sei"

## Flow
```text
[Docs] -> [Chunker] -> [Embedder] -> [Vector DB]
[Query] -> [Embed] -> [Search] -> [Rerank] -> [LLM] -> [Answer]
```

## Comparativo
| Abordagem | Vantagem | Desvantagem |
|-----------|----------|-------------|
| BM25 only | Rapido, sem GPU | Perde sinonimos |
| FAISS only | Captura significado | Falha em acronimos |
| Hybrid | Melhor recall, robusto | 2x custo indexacao |

## References
- https://arxiv.org/abs/2005.11401 (Lewis et al. 2020)
```

WHY THIS IS GOLDEN:
- quality: null (never self-scored)
- All 13 required frontmatter fields present
- tldr < 160 chars, no self-reference
- keywords (3), long_tails (2), axioms (2) present
- Bullets under 80 chars
- 7 body sections with tables + code blocks
- density_score 0.92 (no filler)
- id matches p01_kc_ pattern
- Linked artifact references real CEX artifact

## Anti-Example

INPUT: "Cria KC sobre Python"

BAD OUTPUT:
```yaml
---
id: python_knowledge
type: knowledge_card
title: Python Programming Language
quality: 9.0
tags: "python, programming"
---
Python is a versatile programming language. It was created by Guido van Rossum.
This document describes the main features of Python.
In summary, Python is great for many tasks.
```

FAILURES:
1. id: no `p01_kc_` prefix -> H03 FAIL
2. quality: self-assigned 9.0 -> H05 FAIL
3. tags: string not list -> H07 FAIL
4. lp: missing -> H06 FAIL
5. author: missing -> H06 FAIL
6. domain: missing -> H06 FAIL
7. when_to_use: missing -> H06 FAIL
8. tldr: missing -> H06 FAIL
9. body: filler ("this document describes", "in summary") -> S09 FAIL
10. body: self-reference ("this document") -> S02 FAIL
11. body: no sections, no tables, no code blocks -> S06/S11/S12
12. topic too broad: "Python" is not atomic -> split needed
