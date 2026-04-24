---
quality: 9.1
quality: 8.0
id: kc_bilingual_term_map
kind: knowledge_card
8f: F3_inject
kc_type: meta_kc
pillar: P01
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Multilingual Term Map -- CEX Canonical Translations (EN-first)"
domain: didactic_engine
subdomain: multilingual_layer
tags: [multilingual, translation, ptbr, english, terms, mentor, canonical, taxonomy]
tldr: "Canonical multilingual term translations for CEX concepts (EN-first): 8F steps, 12 pillars, 8 nuclei, top 50 kinds, and operational vocabulary. PT-BR is the first community-contributed language layer."
density_score: null
related:
  - bld_schema_kind
  - kc_intent_resolution_map
  - bld_schema_nucleus_def
  - p01_kc_cex_project_overview
  - bld_collaboration_kind
  - bld_schema_context_window_config
  - bld_knowledge_card_nucleus_def
  - bld_schema_reranker_config
  - bld_examples_kind
  - p01_ctx_cex_project
---

# Bilingual Term Map

> Canonical EN <-> PT-BR translation for all major CEX concepts. These are NOT word-for-word translations -- they are culturally appropriate equivalents used by the /mentor engine to produce native PT-BR content.

## System Concepts

| EN Term | PT-BR Canonical | Notes |
|---------|----------------|-------|
| CEXAI (Cognitive Exchange AI) | CEXAI (Cognitive Exchange AI) | Never translate; CEX short form stays everywhere; X = exchange |
| AI brain | cerebro de IA | or "ativo de conhecimento" in technical context; avoid "enterprise brain" |
| kind | kind | Technical term; keep in EN. In narrative: "tipo de artefato" |
| artifact | artefato | Standard PT-BR tech term |
| pillar | pilar | Exact cognate |
| nucleus / nuclei | nucleo / nuclei | "nucleos" acceptable in very informal text |
| builder | builder | Keep EN; "construtor" in narrative context only |
| ISO (builder config) | ISO (config do builder) | Acronym stays; full form "arquivo de configuracao do builder" |
| pipeline | pipeline | Standard in BR tech; never "tubulacao" |
| sin lens | lente do pecado | Or just "lente" in context where "pecado" is established |
| orchestrator | orquestrador | Standard PT-BR |
| dispatch | dispatch | Keep EN; "despachar" as verb in narrative |
| handoff | handoff | Keep EN; "entrega de tarefa" in narrative |
| wave | onda | In deployment/mission context: "fase" also acceptable |
| grid | grid | Keep EN; "grade" only in visual/spatial context |
| signal | sinal | Standard PT-BR |

## 8F Pipeline Steps

| EN | PT-BR | Verb form (PT-BR) |
|----|-------|------------------|
| F1 CONSTRAIN | F1 RESTRINGIR | "Constrange o escopo" |
| F2 BECOME | F2 TORNAR-SE | "Carrega identidade de builder" |
| F3 INJECT | F3 INJETAR | "Injeta contexto" |
| F4 REASON | F4 RACIOCINAR | "Planeja abordagem" |
| F5 CALL | F5 CHAMAR | "Aciona ferramentas" |
| F6 PRODUCE | F6 PRODUZIR | "Gera o artefato" |
| F7 GOVERN | F7 GOVERNAR | "Valida qualidade" |
| F8 COLLABORATE | F8 COLABORAR | "Salva, compila, commita, sinaliza" |

## 12 Pillars

| EN | PT-BR | Domain translation |
|----|-------|-------------------|
| P01 Knowledge | P01 Conhecimento | Base de conhecimento, RAG, KCs |
| P02 Model | P02 Modelo | Definicoes de agente, provedores |
| P03 Prompt | P03 Prompt | Templates, cadeia de prompts |
| P04 Tools | P04 Ferramentas | Ferramentas externas, APIs, MCP |
| P05 Output | P05 Saida | Formatos de output, landing pages |
| P06 Schema | P06 Schema | Contratos de dados, validacao |
| P07 Evaluation | P07 Avaliacao | Qualidade, benchmarks, scoring |
| P08 Architecture | P08 Arquitetura | Diagramas, decisoes, convencoes |
| P09 Config | P09 Configuracao | Ambiente, segredos, feature flags |
| P10 Memory | P10 Memoria | Estado, contexto, indices |
| P11 Feedback | P11 Feedback | Aprendizado, correcoes, qualidade |
| P12 Orchestration | P12 Orquestracao | Workflows, dispatch, agendamento |

## 8 Nuclei

| EN | PT-BR | Sin Lens (PT-BR) |
|----|-------|-----------------|
| N00 Genesis | N00 Genesis | Arquetipo pre-pecado |
| N01 Intelligence | N01 Inteligencia | Inveja Analitica |
| N02 Marketing | N02 Marketing | Luxuria Criativa |
| N03 Engineering | N03 Engenharia | Soberba Inventiva |
| N04 Knowledge | N04 Conhecimento | Gula do Conhecimento |
| N05 Operations | N05 Operacoes | Ira da Qualidade |
| N06 Commercial | N06 Comercial | Avareza Estrategica |
| N07 Orchestrator | N07 Orquestrador | Preguica Orquestradora |

## Top 50 Kinds: EN <-> PT-BR

| Kind (EN) | PT-BR Narrative Name | Keep EN? |
|-----------|---------------------|---------|
| `knowledge_card` | ficha de conhecimento | yes (kind name stays EN) |
| `agent` | agente | yes |
| `prompt_template` | template de prompt | yes |
| `system_prompt` | prompt de sistema | yes |
| `workflow` | fluxo de trabalho | yes |
| `quality_gate` | portao de qualidade | yes |
| `knowledge_index` | indice de conhecimento | yes |
| `embedding_config` | config de embedding | yes |
| `guardrail` | barreira de seguranca | yes |
| `env_config` | config de ambiente | yes |
| `api_client` | cliente de API | yes |
| `learning_record` | registro de aprendizado | yes |
| `entity_memory` | memoria de entidade | yes |
| `crew_template` | template de equipe | yes |
| `decision_record` | registro de decisao | yes |
| `benchmark` | benchmark | yes |
| `context_doc` | documento de contexto | yes |
| `chain` | cadeia | yes |
| `router` | roteador | yes |
| `scoring_rubric` | rubrica de avaliacao | yes |
| `landing_page` | landing page | yes |
| `model_card` | ficha do modelo | yes |
| `data_contract` | contrato de dados | yes |
| `chunk_strategy` | estrategia de chunking | yes |
| `retriever_config` | config de recuperacao | yes |
| `signal` | sinal | yes |
| `handoff` | handoff / entrega | yes (keep EN as noun) |
| `schedule` | agendamento | yes |
| `dispatch_rule` | regra de dispatch | yes |
| `taxonomy` | taxonomia | yes |
| `glossary_entry` | entrada de glossario | yes |
| `citation` | citacao | yes |
| `memory_summary` | resumo de memoria | yes |
| `user_model` | modelo de usuario | yes |
| `feature_flag` | feature flag | yes |
| `rate_limit_config` | config de rate limit | yes |
| `secret_config` | config de segredos | yes |
| `bugloop` | loop de correcao | yes |
| `reward_signal` | sinal de recompensa | yes |
| `regression_check` | verificacao de regressao | yes |
| `prompt_cache` | cache de prompt | yes |
| `context_window_config` | config de janela de contexto | yes |
| `diagram` | diagrama | yes |
| `naming_rule` | regra de nomenclatura | yes |
| `interface` | interface | yes |
| `type_def` | definicao de tipo | yes |
| `input_schema` | schema de entrada | yes |
| `output_validator` | validador de saida | yes |
| `code_executor` | executor de codigo | yes |
| `sandbox_config` | config de sandbox | yes |

## Operational Vocabulary

| EN | PT-BR | Context |
|----|-------|---------|
| "ship it" | "entregar / deployar" | Deployment context |
| "build" | "construir / buildar" | "buildar" is acceptable BR tech slang |
| "commit" | "commitar" | Standard BR dev slang |
| "review" | "revisar / fazer review" | PR context |
| "merge" | "mergear" | Standard BR dev slang |
| "deploy" | "deployar / subir" | "subir" = more natural PT-BR |
| "spin up" | "subir / iniciar" | Process context |
| "tear down" | "derrubar / matar" | Process termination |
| "score" | "pontuar / dar nota" | Quality scoring |
| "gate" | "portao / bloquear" | Quality gate context |
| "handoff" | "repassar / entregar" | Task transfer |
| "dispatch" | "despachar / disparar" | Agent launch |
| "signal" | "sinalizar / enviar sinal" | Completion notification |
| "synthesize" | "sintetizar / compilar" | Knowledge consolidation |
| "ingest" | "ingerir / importar" | Data/document loading |

## Translation Rules for /mentor

1. **Kind names always stay in EN** -- they are canonical identifiers, not prose words
2. **8F step labels** (F1-F8) stay as-is; the verb translations above are for narrative use only
3. **Pillar codes** (P01-P12) stay as-is
4. **Acronyms** (RAG, GDP, RAG, BM25) stay in EN; spell out on first use
5. **Technical slang** that is standard in BR dev culture: keep EN form (commit, deploy, merge, pipeline)
6. **Non-technical narrative**: full PT-BR, culturally appropriate

## Quick Reference

```yaml
topic: bilingual_term_map
scope: EN <-> PT-BR canonical translations for /mentor production
owner: n04_knowledge
criticality: high
audience: mentor_engine, mentor_locale_ptbr, /mentor_produce
languages: [en, pt-br]
kinds_covered: 50
concepts_covered: [8F_steps, 12_pillars, 8_nuclei, operational_vocab]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | downstream | 0.31 |
| [[kc_intent_resolution_map]] | sibling | 0.30 |
| [[bld_schema_nucleus_def]] | downstream | 0.29 |
| [[p01_kc_cex_project_overview]] | sibling | 0.28 |
| [[bld_collaboration_kind]] | downstream | 0.25 |
| [[bld_schema_context_window_config]] | downstream | 0.24 |
| [[bld_knowledge_card_nucleus_def]] | sibling | 0.24 |
| [[bld_schema_reranker_config]] | downstream | 0.24 |
| [[bld_examples_kind]] | downstream | 0.23 |
| [[p01_ctx_cex_project]] | related | 0.23 |
