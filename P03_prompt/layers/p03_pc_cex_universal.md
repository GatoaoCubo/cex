---
id: p03_pc_cex_universal
kind: prompt_compiler
pillar: P03
version: 1.1.0
created: "2026-04-12"
updated: "2026-04-16"
author: n03_builder
title: "CEX Universal Prompt Compiler"
domain: intent_resolution
coverage: 257
languages: [pt-br, en]
quality: null
canonical_for: [n07-input-transmutation, F1_CONSTRAIN]
referenced_by:
  - .claude/rules/n07-input-transmutation.md
  - .claude/rules/n07-technical-authority.md
  - CLAUDE.md
role: "N07's transmutation brain -- maps every user phrase (PT/EN) to {kind, pillar, nucleus, verb} before 8F starts. Source of CEX's 'senior AI engineer' leverage."
tags: [prompt_compiler, intent-resolution, cex, bilingual, transmutation, n07-canonical, f1-constrain]
tldr: "Source of truth for intent transmutation: maps natural-language input (PT/EN) into {kind, pillar, nucleus, verb} for all 257 CEX kinds. Loaded BEFORE every 8F run (F1 CONSTRAIN). Quality:null per CLAUDE.md rule -- peer review assigns score."
density_score: 0.93
---

## Preamble

You are a **prompt compiler**. Resolve user input into `{kind, pillar, nucleus, verb}` BEFORE executing. This is F1 CONSTRAIN in every 8F pipeline. Protocol: (1) Match Kind Table. (2) Resolve verb. (3) If ambiguous, disambiguate. (4) If no match, fallback. (5) Feed tuple to pipeline.

## Kind Resolution Table

Key: EN=English patterns, PT=Portuguese patterns, N=nucleus, V=verb

### P01 Knowledge
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| knowledge_card | N04 | KC, knowledge card, document this | KC, documentar, criar KC | create |
| chunk_strategy | N04 | chunking, split docs, chunk size | chunking, dividir docs | configure |
| citation | N04 | cite, citation, reference source | citacao, referenciar | create |
| context_doc | N04 | context doc, background doc, long-form | documento contexto, doc longo | create |
| embedding_config | N04 | embedding config, vector settings | config embedding, config vetorial | configure |
| embedder_provider | N04 | embedding provider, vector provider | provedor embedding | configure |
| few_shot_example | N04 | few-shot, example pair, demo | few-shot, par exemplo | create |
| glossary_entry | N04 | glossary, define term, terminology | glossario, definir termo | create |
| rag_source | N04 | RAG source, retrieval source | fonte RAG, fonte recuperacao | configure |
| retriever_config | N04 | retriever config, search settings | config retriever, config busca | configure |
| vector_store | N04 | vector store, vector DB, embedding store | vector store, banco vetorial | configure |

### P02 Model
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| agent | N03 | create agent, agent definition | criar agente, definir agente | create |
| agent_package | N03 | agent package, portable agent | pacote agente, agente portable | create |
| axiom | N03 | axiom, fundamental rule, immutable | axioma, regra fundamental | create |
| boot_config | N05 | boot config, startup, provider init | config boot, inicializacao | configure |
| fallback_chain | N03 | fallback chain, model fallback | cadeia fallback, fallback modelo | create |
| handoff_protocol | N03 | handoff protocol, transfer rules | protocolo handoff, transferencia | create |
| lens | N03 | lens, perspective, viewpoint | lente, perspectiva | create |
| memory_scope | N04 | memory scope, context boundary | escopo memoria, limite contexto | configure |
| mental_model | N03 | mental model, cognitive map | modelo mental, mapa cognitivo | create |
| model_card | N03 | model card, LLM spec, capabilities | model card, spec modelo | create |
| model_provider | N05 | model provider, LLM provider | provedor modelo, provedor LLM | configure |
| router | N03 | router, route table, task routing | roteador, tabela rotas | create |

### P03 Prompt
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| action_prompt | N03 | task prompt, user message, action | prompt tarefa, mensagem usuario | create |
| chain | N03 | prompt chain, sequential chain | cadeia prompts, chain sequencial | create |
| constraint_spec | N03 | constraint, decoder rules | restricao, regras geracao | create |
| context_window_config | N03 | token budget, context window | orcamento tokens, janela contexto | configure |
| instruction | N03 | instructions, step-by-step, guide | instrucoes, passo-a-passo | create |
| prompt_compiler | N03 | intent resolution, prompt compiler | resolucao intencao, compilador | create |
| prompt_template | N03 | prompt template, template with vars | template prompt, template vars | create |
| prompt_version | N03 | version prompt, freeze prompt | versionar prompt, snapshot | create |
| reasoning_trace | N03 | reasoning trace, chain-of-thought | trace raciocinio, cadeia pensamento | create |
| system_prompt | N03 | system prompt, agent identity, persona | prompt sistema, identidade agente | create |

### P04 Tools
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| api_client | N05 | API client, REST client | cliente API, cliente REST | create |
| audio_tool | N05 | audio tool, STT, TTS | ferramenta audio, TTS | create |
| browser_tool | N05 | web scraper, browser automation | scraper web, automacao browser | create |
| cli_tool | N05 | CLI tool, command line tool | ferramenta CLI, linha comando | create |
| code_executor | N05 | code executor, sandbox, run code | executor codigo, sandbox | create |
| computer_use | N05 | computer use, desktop automation | uso computador, automacao desktop | create |
| daemon | N05 | daemon, background service | daemon, servico background | create |
| db_connector | N05 | DB connector, SQL client, database | conector banco, cliente SQL | create |
| document_loader | N05 | doc loader, file ingestion | carregador docs, ingestao | create |
| function_def | N05 | function def, callable, tool fn | definicao funcao, funcao tool | create |
| hook | N05 | hook, event hook, lifecycle hook | hook, hook evento | create |
| hook_config | N05 | hook config, hook settings | config hook, config hooks | configure |
| mcp_server | N05 | MCP server, model context protocol | servidor MCP, protocolo MCP | create |
| multi_modal_config | N05 | multimodal, vision+text config | multimodal, config multi-modal | configure |
| notifier | N05 | notifier, notification, alerts | notificador, notificacao, alertas | create |
| plugin | N05 | plugin, extension, add-on | plugin, extensao | create |
| research_pipeline | N01 | deep research, research pipeline | pesquisa profunda, pipeline pesquisa | create |
| retriever | N04 | retriever, search retriever | retriever, recuperador | create |
| search_tool | N05 | search tool, web search | ferramenta busca, busca web | create |
| skill | N03 | skill, executable skill | skill, habilidade executavel | create |
| social_publisher | N02 | social publisher, social post | publicador social, post social | create |
| supabase_data_layer | N05 | supabase, data layer | supabase, camada dados | create |
| toolkit | N05 | toolkit, tool collection | toolkit, colecao ferramentas | create |
| vision_tool | N05 | vision tool, image analysis, OCR | ferramenta visao, analise imagem | create |
| webhook | N05 | webhook, HTTP callback | webhook, callback HTTP | create |

### P05 Output
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| formatter | N03 | formatter, format as JSON/CSV | formatador, formatar JSON | create |
| landing_page | N03 | landing page, web page | landing page, pagina web | create |
| output_validator | N03 | output validator, check output | validador saida, validar saida | create |
| parser | N03 | parser, extract data, parse output | parser, extrair dados | create |
| response_format | N03 | response format, output format | formato resposta, formato saida | create |

### P06 Schema
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| enum_def | N03 | enum, enumeration, value list | enum, enumeracao, lista valores | create |
| input_schema | N03 | input schema, validate input | schema entrada, validar entrada | create |
| interface | N03 | interface, API contract | interface, contrato integracao | create |
| type_def | N03 | type def, custom type, data type | definicao tipo, tipo custom | create |
| validation_schema | N03 | validation schema, rules | schema validacao, regras validacao | create |
| validator | N03 | validator, field validator | validador, validador campo | create |

### P07 Evaluation
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| benchmark | N05 | benchmark, perf test, latency | benchmark, teste performance | test |
| e2e_eval | N05 | e2e test, integration test | teste e2e, teste integracao | test |
| eval_dataset | N05 | eval dataset, test data | dataset avaliacao, dados teste | create |
| golden_test | N05 | golden test, reference test | teste golden, teste referencia | create |
| llm_judge | N05 | LLM judge, AI evaluator | juiz LLM, avaliador IA | create |
| red_team_eval | N05 | red team, adversarial test | red team, teste adversarial | test |
| regression_check | N05 | regression test, regression check | teste regressao, verificar regressao | test |
| scoring_rubric | N05 | scoring rubric, eval criteria | rubrica avaliacao, criterios | create |
| smoke_eval | N05 | smoke test, sanity check | teste smoke, verificacao rapida | test |
| trace_config | N05 | trace config, observability | config trace, observabilidade | configure |
| unit_eval | N05 | unit test, unit eval | teste unitario, avaliacao unit | test |

### P08 Architecture
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| agent_card | N03 | agent card, deploy spec | agent card, spec deploy | create |
| component_map | N03 | component map, system map | mapa componentes, mapa sistema | create |
| decision_record | N03 | ADR, decision record | ADR, registro decisao | create |
| diagram | N03 | diagram, architecture diagram | diagrama, diagrama arquitetura | create |
| invariant | N03 | invariant, system law | invariante, lei sistema | create |
| naming_rule | N03 | naming rule, naming convention | regra nomenclatura, convencao nomes | create |
| pattern | N03 | design pattern, architecture pattern | padrao design, padrao arquitetura | create |
| supervisor | N03 | supervisor, oversight agent | supervisor, agente supervisao | create |

### P09 Config
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| effort_profile | N03 | effort profile, complexity | perfil esforco, complexidade | configure |
| env_config | N05 | env config, env vars, environment | config ambiente, variaveis ambiente | configure |
| feature_flag | N05 | feature flag, toggle | flag feature, toggle | configure |
| path_config | N05 | path config, file paths | config caminhos, caminhos | configure |
| permission | N05 | permission, access control | permissao, controle acesso | configure |
| rate_limit_config | N05 | rate limit, throttle | limite taxa, throttle | configure |
| runtime_rule | N05 | runtime rule, execution rule | regra runtime, regra execucao | create |
| secret_config | N05 | secrets, credentials, keys | credenciais, segredos, chaves | configure |

### P10 Memory
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| compression_config | N04 | compression, memory compression | compressao, compressao memoria | configure |
| entity_memory | N04 | entity memory, remember entity | memoria entidade, lembrar entidade | create |
| knowledge_index | N04 | knowledge index, search index | indice conhecimento, indice busca | create |
| learning_record | N04 | learning record, lesson learned | registro aprendizado, licao | create |
| memory_summary | N04 | memory summary, compress memory | resumo memoria, comprimir memoria | create |
| memory_type | N04 | memory type, memory classification | tipo memoria, classificacao | configure |
| prompt_cache | N05 | prompt cache, caching config | cache prompts, config cache | configure |
| runtime_state | N05 | runtime state, current state | estado runtime, estado atual | create |
| session_backend | N05 | session backend, session storage | backend sessao, armazenamento | configure |
| session_state | N05 | session state, conversation state | estado sessao, estado conversa | create |

### P11 Feedback
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| bugloop | N05 | bugloop, auto-fix, detect-fix-verify | bugloop, correcao automatica | create |
| content_monetization | N06 | pricing, monetization, revenue | preco, monetizacao, receita | create |
| guardrail | N03 | guardrail, safety rail, filter | guardrail, limite seguranca | create |
| lifecycle_rule | N03 | lifecycle rule, artifact lifecycle | regra ciclo vida | create |
| optimizer | N05 | optimizer, optimize, tune | otimizador, otimizar, tunar | optimize |
| quality_gate | N03 | quality gate, quality check | gate qualidade, verificacao | create |
| reward_signal | N03 | reward signal, feedback signal | sinal recompensa, sinal feedback | create |

### P12 Orchestration
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| checkpoint | N03 | checkpoint, save point | checkpoint, ponto salvamento | create |
| dag | N03 | DAG, dependency graph | DAG, grafo dependencias | create |
| dispatch_rule | N03 | dispatch rule, keyword dispatch | regra dispatch, dispatch keyword | create |
| handoff | N07 | handoff, task handoff | handoff, transferencia tarefa | create |
| schedule | N07 | schedule, cron, recurring task | agendar, cron, tarefa recorrente | schedule |
| signal | N07 | signal, completion signal | sinal, sinal conclusao | create |
| spawn_config | N05 | spawn config, launch config | config spawn, config lancamento | configure |
| workflow | N03 | workflow, orchestration flow | workflow, fluxo orquestracao | create |
| workflow_primitive | N03 | workflow primitive, basic step | primitiva workflow, etapa basica | create |

### Specialized (cross-pillar)
| Kind | P | N | EN | PT | V |
|------|---|---|----|----|---|
| software_project | P02 | N03 | software project, codebase spec | projeto software, definicao projeto | create |
| tagline | P03 | N02 | tagline, slogan, brand tagline | tagline, slogan, lema marca | create |

## Verb Resolution Table

| PT | EN | Action | 8F |
|----|-----|--------|-----|
| criar, crie, faz | create, build, make | create | F6 |
| melhorar, melhore | improve, enhance | improve | F7 |
| reconstruir | rebuild, recreate | rebuild | F6 |
| analisar, avaliar | analyze, review | analyze | F3 |
| validar, verificar | validate, check | validate | F7 |
| documentar | document, record | document | F6 |
| integrar, conectar | integrate, connect | integrate | F5 |
| testar | test, evaluate | test | F7 |
| implantar | deploy, ship, release | deploy | F8 |
| configurar | configure, setup | configure | F1 |
| otimizar | optimize, tune | optimize | F7 |
| auditar | audit, inspect | audit | F7 |
| agendar | schedule, cron | schedule | F8 |
| monitorar | monitor, watch | monitor | F5 |
| pesquisar | research, investigate | research | F3 |
| escrever | write, compose | create | F6 |
| deletar | delete, remove | delete | F8 |
| listar | list, enumerate | analyze | F3 |
| buscar | search, find | analyze | F3 |
| corrigir | fix, repair, patch | improve | F7 |
| migrar | migrate, convert | integrate | F5 |
| escalar | scale, expand | configure | F1 |
| proteger | secure, harden | configure | F1 |
| cachear | cache, store | configure | F5 |
| formatar | format, structure | create | F6 |
| debugar | debug, troubleshoot | analyze | F3 |
| versionar | version, snapshot | create | F8 |
| comparar | compare, diff | analyze | F3 |
| exportar | export, extract | create | F8 |
| importar | import, ingest | integrate | F5 |

## Ambiguity Resolution

When input matches multiple kinds, resolve in order:

1. **Context**: current nucleus narrows candidates (N04 prefers knowledge; N05 prefers ops)
2. **Specificity**: more specific kind wins (`mcp_server` > `api_client` when MCP mentioned)
3. **Boundary**: eliminate kinds whose boundary says "NOT this" for the input
4. **Core preference**: core kinds preferred over non-core for ambiguous input
5. **GDP trigger**: if 2+ candidates remain, present top options to user

**Common confusions**:
| Input | Looks like | Actually | Differentiator |
|-------|-----------|----------|---------------|
| route tasks | router | dispatch_rule | dispatch if keyword-only; router if confidence |
| validate data | validator | input_schema | input_schema=incoming; validator=outgoing |
| document this | knowledge_card | context_doc | KC=atomic fact; context_doc=long-form |
| test this | unit_eval | e2e_eval | unit=single; e2e=multi-component |
| set up RAG | rag_source | multi-kind | rag_source + retriever_config + embedding_config |

## Fallback Heuristics

When NO kind matches:
1. **TF-IDF**: search input against kind descriptions (cex_query.py)
2. **Semantic**: compare against kind KC summaries
3. **>= 60% confidence**: proceed with best match, flag: "Resolved as {kind} ({score}%)"
4. **< 60% confidence**: present top 3 candidates, ask user

## Behavioral Instructions

1. NEVER execute literally -- resolve intent first
2. ALWAYS produce {kind, pillar, nucleus, verb} before action
3. Teach when correcting (once, then silent)
4. Report confidence on fallback
5. Boundary notes eliminate candidates
6. Detect language; match detected first
7. Multi-kind valid: "set up RAG" = 3 kinds
