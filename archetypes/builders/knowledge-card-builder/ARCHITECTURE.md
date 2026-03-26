---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of knowledge_card in the CEX
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: knowledge_card in the CEX

## Boundary
knowledge_card EH: fato atomico destilado, pesquisavel, versionado, com densidade >= 0.80.
knowledge_card NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| model_card | model_card eh spec de LLM. KC eh fato generico. | P02 model_card |
| context_doc | context_doc eh contexto amplo sem density gate. | P01 context_doc |
| glossary_entry | glossary_entry eh definicao curta (3 linhas). KC eh denso. | P01 glossary_entry |
| rag_source | rag_source eh ponteiro externo. KC eh conteudo destilado. | P01 rag_source |
| few_shot_example | few_shot eh par input/output. KC eh conhecimento. | P01 few_shot_example |

Regra: "qual o fato essencial sobre este topico?" -> knowledge_card.

## Position in Knowledge Flow

```
[Raw Source] -> [Research/Destilacao] -> [knowledge_card]
                                              |
                              [Brain Index] -> [Retrieval]
                                              |
                              [Prompt Hydration] -> [Agent]
```

knowledge_card is CONTENT LAYER. Injected into prompts via Brain search.
It feeds agents, skills, and workflows with factual context.

## Dependency Graph

```
knowledge_card <--queried_by-- brain_query (BM25 + FAISS)
knowledge_card <--injected_in-- system_prompt (via IHP)
knowledge_card <--referenced_by-- agent (linked_artifacts)
knowledge_card <--consumed_by-- skill (domain context)
knowledge_card --independent-- model_card, boot_config, persona
```

## Fractal Position
Pillar: P01 (Knowledge — "what the entity KNOWS")
Function: INJECT (provides factual context to other LPs)
Scale: L0 (content artifact, no identity or behavior)
The primary P01 kind — all other P01 kinds are simpler variants.
