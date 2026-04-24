---
id: p01_kc_bm25_search
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "BM25 Search — Keyword Retrieval for Local Knowledge Bases"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [bm25, keyword-search, retrieval, offline-search, knowledge-base]
tldr: "BM25 busca keyword-based em CSVs/docs locais: ~10ms, offline, sem embeddings — ideal para dados estruturados"
when_to_use: "Implementar busca rapida em knowledge bases locais sem dependencia de embeddings ou servidor"
keywords: [bm25, okapi-bm25, keyword-retrieval, text-search]
long_tails:
  - "Como implementar BM25 search em Python para knowledge base local"
  - "Quando usar BM25 ao inves de embeddings para busca"
axioms:
  - "SEMPRE cachear instancia BM25 fitted em producao"
  - "NUNCA usar BM25 para busca semantica — nao entende sinonimos"
linked_artifacts:
  primary: null
  related: [p01_kc_csv_as_knowledge]
density_score: null
data_source: "https://en.wikipedia.org/wiki/Okapi_BM25"
related:
  - p01_kc_csv_as_knowledge
  - p01_rc_hybrid_rag
  - bld_knowledge_card_knowledge_index
  - p04_plug_brain_search
  - leverage_map_v2_n04_verify_legacy_2026_04_15
  - p10_bi_organization_brain
  - leverage_map_v2_n04_verify
  - p10_lr_knowledge-index-builder
  - p10_bi_intelligence_outputs
  - leverage_map_v2_verify_n04
---

## TL;DR

BM25 (Okapi Best Match 25) e um algoritmo de ranking baseado em frequencia de termos que busca em documentos locais sem embeddings, sem servidor, sem GPU. Processa 161 linhas em ~10ms e 1000 linhas em ~50ms usando apenas Python stdlib.

## Conceito Central

BM25 calcula relevancia usando TF-IDF probabilistico: termos raros em um documento que sao raros no corpus recebem score alto. Dois parametros controlam o comportamento: k1 (saturacao de frequencia, tipicamente 1.2-2.0) e b (normalizacao por comprimento, tipicamente 0.75). O algoritmo tokeniza queries e documentos, constroi indice invertido e rankeia por score.

A forca do BM25 e simplicidade: nenhuma dependencia externa, funciona offline, resultado deterministico e interpretavel. A fraqueza e que opera exclusivamente em keywords — "carro" nao encontra "veiculo". Para buscas conceituais, embeddings sao necessarios. BM25 e ideal como primeiro estagio de retrieval ou como unico estagio para dados estruturados com keywords bem definidas.

Em sistemas hibridos (BM25 + embeddings), BM25 serve como recall rapido e embeddings como reranker semantico. Isso combina velocidade com compreensao conceitual.

## Arquitetura/Patterns

| Aspecto | Valor | Nota |
|---------|-------|------|
| Complexidade | O(n) por query | n = documentos no corpus |
| Latencia 161 docs | ~10ms | Sem cache, rebuild por query |
| Latencia 1000 docs | ~50ms | Sem cache, rebuild por query |
| Dependencias | Zero | Python stdlib apenas |
| Parametro k1 | 1.2-2.0 | Saturacao de frequencia |
| Parametro b | 0.75 | Normalizacao por tamanho |

Pattern de implementacao:

```python
from rank_bm25 import BM25Okapi

corpus = [doc.split() for doc in documents]
bm25 = BM25Okapi(corpus)  # fit once, query many
scores = bm25.get_scores(query.split())
top_n = sorted(range(len(scores)),
    key=lambda i: scores[i], reverse=True)[:5]
```

Para producao: instanciar BM25 uma vez no startup e reutilizar. Rebuild apenas quando corpus muda. Separar search_cols (indexados) de output_cols (retornados) para precisao.

Hibrido BM25 + embeddings (reranking pipeline):
```
Query -> BM25 recall (top 20, ~10ms)
  -> embedding rerank (top 5, ~200ms)
  -> LLM context injection
```

BM25 como primeiro estagio garante velocidade. Embeddings como segundo estagio adicionam compreensao semantica. Custo total: ~210ms vs ~500ms com embeddings puro. Fallback: se embedding service cai, BM25 sozinho ainda funciona.

## Exemplos Praticos

| Cenario | search_cols | Resultado |
|---------|------------|-----------|
| Produto por tipo | keywords, category | Top 3 matches com score |
| Guideline UX | rule_name, description | Regras aplicaveis |
| Font pairing | style, mood, use_case | Pares tipograficos |
| Skill discovery | name, description | Skills relevantes |

Fluxo tipico:
1. Carregar CSV com pandas
2. Concatenar search_cols em campo unico
3. Tokenizar e construir indice BM25
4. Query retorna top-N com score > threshold
5. Filtrar output_cols dos resultados

Threshold recomendado: descartar resultados com score < 1.0 (muito generico). Limitar a 3-5 resultados para contexto LLM.

## Anti-Patterns

- Buscar em muitas colunas verbosas (degrada precisao)
- Retornar todos os resultados sem threshold de score
- Assumir que BM25 entende sinonimos ou conceitos
- Rebuild do indice a cada query em producao (cachear!)
- Um CSV gigante multi-dominio ao inves de CSVs focados
- Usar BM25 como unica busca para perguntas abertas

## Referencias

- source: https://en.wikipedia.org/wiki/Okapi_BM25
- related: p01_kc_csv_as_knowledge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_csv_as_knowledge]] | sibling | 0.36 |
| [[p01_rc_hybrid_rag]] | related | 0.34 |
| [[bld_knowledge_card_knowledge_index]] | sibling | 0.34 |
| [[p04_plug_brain_search]] | downstream | 0.29 |
| [[leverage_map_v2_n04_verify_legacy_2026_04_15]] | related | 0.29 |
| [[p10_bi_organization_brain]] | downstream | 0.29 |
| [[leverage_map_v2_n04_verify]] | related | 0.26 |
| [[p10_lr_knowledge-index-builder]] | downstream | 0.25 |
| [[p10_bi_intelligence_outputs]] | downstream | 0.24 |
| [[leverage_map_v2_verify_n04]] | sibling | 0.24 |
