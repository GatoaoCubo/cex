---
lp: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of knowledge_card in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: knowledge_card in the CEX

## Boundary
knowledge_card EH: fato atomico pesquisavel (densidade > 0.80, max 5KB).
knowledge_card NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| glossary_entry | glossary define termo (max 3 linhas). KC tem profundidade. | P01 glossary_entry |
| context_doc | context_doc hidrasta prompts (sem density gate). KC eh denso. | P01 context_doc |
| rag_source | rag_source eh ponteiro pra fonte. KC eh conteudo destilado. | P01 rag_source |
| model_card | model_card eh spec de LLM. KC eh conhecimento de dominio. | P02 model_card |
| prompt_template | prompt_template eh instrucao. KC eh fato, nao diretiva. | P03 prompt_template |
| few_shot_example | few_shot eh par input/output. KC eh conhecimento standalone. | P01 few_shot_example |

Regra: "qual eh o fato essencial e pesquisavel sobre X?" -> knowledge_card.

## Position in Knowledge Flow

```
[Raw Sources]          <- layer 0: external docs, APIs, code
       |
[knowledge_card]       <- layer 1: destilacao atomica (THIS)
       |
[Brain Index]          <- layer 2: BM25 + FAISS indexing
       |
[brain_query]          <- layer 3: retrieval via MCP
       |
[Agent Context]        <- layer 4: injected into prompts
```

knowledge_card is CONTENT. Created AFTER research, consumed BY retrieval.

## Dependency Graph

```
knowledge_card <-indexed_by-- Brain (BM25 + FAISS)
knowledge_card <-queried_via-- brain_query MCP
knowledge_card <-hydrates---- agent prompts (context injection)
knowledge_card <-validated_by- validate_kc.py v2.0
knowledge_card --independent-- model_card, agent, workflow
knowledge_card --links_to---- other KCs via linked_artifacts
```

## Fractal Position
LP: P01 (Knowledge — "what the entity KNOWS")
Function: INJECT (provides knowledge to other artifacts)
Scale: L1 (content artifact, atomic grain)
The core content type of P01 — all other P01 types support it.
