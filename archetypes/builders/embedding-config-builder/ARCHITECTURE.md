---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of embedding_config in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: embedding_config in the CEX

## Boundary
embedding_config EH: configuracao de modelo de embedding (dimensoes, chunking, distance metric) para RAG.

embedding_config NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| knowledge_card (P01) | KC DESTILA conhecimento. embedding_config CONFIGURA vetorizacao. | P01 knowledge_card |
| rag_source (P01) | rag_source APONTA para fonte externa. embedding_config DEFINE como vetorizar. | P01 rag_source |
| glossary_entry (P01) | glossary DEFINE termos. embedding_config CONFIGURA modelo. | P01 glossary_entry |
| context_doc (P01) | context_doc FORNECE background. embedding_config PROCESSA texto. | P01 context_doc |
| few_shot_example (P01) | example DEMONSTRA input/output. embedding_config PARAMETRIZA modelo. | P01 few_shot_example |
| brain_index (P10) | brain_index CONFIGURA o indice (BM25, FAISS). embedding_config CONFIGURA o modelo vetorial. | P10 brain_index |

Regra: "qual modelo de embedding usar, com quais parametros?" -> embedding_config.

## Position in RAG Flow

```text
raw text -> [embedding_config] defines vectorization -> brain_index indexes vectors -> retriever queries -> agent uses
                    |
              model + dimensions + chunk_size + distance_metric
```

embedding_config is the VECTORIZATION LAYER — defines how text becomes vectors.

## Dependency Graph

```text
embedding_config <--consumed_by-- brain_index (P10) — index uses embedding config
embedding_config <--consumed_by-- retriever agent (P02) — retriever needs vector params
embedding_config --receives-- rag_source (P01) — source characteristics inform chunk_size
embedding_config --independent-- signal, workflow, quality_gate, satellite_spec
```

## Fractal Position
Pillar: P01 (Knowledge — what the agent KNOWS)
Function: GOVERN (defines embedding model parameters)
Scale: L0 (spec layer — embedding_config is infrastructure for knowledge retrieval)
embedding_config is the bridge between raw content (P01) and searchable index (P10).
