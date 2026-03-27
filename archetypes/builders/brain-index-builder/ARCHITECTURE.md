---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of brain_index in the CEX fractal
---

# Architecture: brain_index in the CEX

## Boundary
brain_index EH: indice de busca semantica que configura como conteudo eh encontrado via BM25, FAISS, ou hybrid search.

brain_index NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| embedding_config (P01) | embedding_config define o MODELO de embedding (dimensoes, chunk_size). brain_index define o INDICE construido a partir dos embeddings. | P01 embedding_config |
| rag_source (P01) | rag_source define ONDE os dados vem (URL, crawl). brain_index define COMO os dados sao buscados. | P01 rag_source |
| knowledge_card (P01) | knowledge_card eh o CONTEUDO indexado. brain_index eh o INDICE sobre o conteudo. | P01 knowledge_card |
| runtime_state (P10) | runtime_state define DECISOES de routing do agente. brain_index define INFRAESTRUTURA de busca. | P10 runtime_state |
| session_state (P10) | session_state eh SNAPSHOT efemero. brain_index eh indice PERSISTENTE. | P10 session_state |
| learning_record (P10) | learning_record armazena O QUE foi aprendido. brain_index armazena COMO encontrar informacao. | P10 learning_record |
| axiom (P10) | axiom eh regra FUNDAMENTAL imutavel. brain_index eh INDICE tecnico de busca. | P10 axiom |

Regra: "como o conteudo eh indexado e buscado para retrieval?" -> brain_index.

## Position in Retrieval Flow

```text
rag_source (data origin) -> embedding_config (vectorization) -> brain_index (indexing + search) -> knowledge_card (result)
```

brain_index is SEARCH LAYER — the engine that makes content findable.

## Dependency Graph

```text
brain_index <--fed_by-- rag_source (P01 provides raw content)
brain_index <--configured_by-- embedding_config (P01 provides vector model)
brain_index --indexes--> knowledge_card (P01 content is indexed)
brain_index --queried_by--> runtime_state (P10 agents query the index)
brain_index --independent-- permission, guardrail, signal
```

## Fractal Position
Pillar: P10 (Memory — what the system remembers)
Function: INJECT
Scale: L1 (runtime infrastructure)
brain_index is unique in P10 because it is INFRASTRUCTURE — it does not store knowledge itself but makes knowledge FINDABLE through search algorithms.
