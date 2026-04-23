---
id: p03_pc_cex_universal
kind: prompt_compiler
pillar: P03
version: 1.1.0
created: "2026-04-12"
updated: "2026-04-22"
author: n03_builder
title: "CEX Universal Prompt Compiler"
domain: intent_resolution
coverage: 300
languages: [en]
community_languages: [pt-br]
quality: 9.2
canonical_for: [n07-input-transmutation, F1_CONSTRAIN]
referenced_by:
  - .claude/rules/n07-input-transmutation.md
  - .claude/rules/n07-technical-authority.md
  - CLAUDE.md
role: "N07's transmutation brain -- maps every user phrase (any language) to {kind, pillar, nucleus, verb} before 8F starts. EN-first, multilingual-extensible. Source of CEX's 'senior AI engineer' leverage."
tags: [prompt_compiler, intent-resolution, cex, multilingual, transmutation, n07-canonical, f1-constrain]
tldr: "Source of truth for intent transmutation: maps natural-language input into {kind, pillar, nucleus, verb} for all 300 CEX kinds. EN-first; community-contributed language patterns welcome (PT-BR seeded). Loaded BEFORE every 8F run (F1 CONSTRAIN)."
density_score: 0.93
related:
  - kc_intent_resolution_map
  - p12_dr_software_project
  - quality_gate_intent_resolution
  - p12_dr_builder_nucleus
  - bld_sp_collaboration_software_project
  - p12_dispatch_rule_supabase
  - bld_collaboration_supabase_data_layer
  - spec_seed_words
  - p02_nd_n03.md
  - agent_card_n03
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
| agentic_rag | N04 | agentic rag | agentic rag | create |
| changelog | N04 | changelog | changelog | create |
| competitive_matrix | N01 | competitive matrix | competitive matrix | create |
| dataset_card | N04 | dataset card | dataset card | create |
| discovery_questions | N04 | discovery questions | discovery questions | create |
| domain_vocabulary | N04 | domain vocabulary | domain vocabulary | create |
| ecommerce_vertical | N04 | ecommerce vertical | ecommerce vertical | create |
| edtech_vertical | N04 | edtech vertical | edtech vertical | create |
| faq_entry | N04 | faq entry | faq entrada | create |
| fintech_vertical | N04 | fintech vertical | fintech vertical | create |
| govtech_vertical | N04 | govtech vertical | govtech vertical | create |
| graph_rag_config | N04 | graph rag config | grafo rag configuracao | create |
| healthcare_vertical | N04 | healthcare vertical | saude vertical | create |
| knowledge_graph | N04 | knowledge graph | knowledge grafo | create |
| legal_vertical | N04 | legal vertical | juridico vertical | create |
| lineage_record | N04 | lineage record | lineage registro | create |
| ontology | N04 | ontology | ontology | configure |
| repo_map | N04 | repo map | repo mapa | create |
| query_optimizer | N03 | query rewrite, query expansion, multi-hop query, query optimizer | reescrever query, expansao query, query multi-hop | create |
| reranker_config | N04 | reranker config | reranker configuracao | create |
| synthetic_data_config | N03 | synthetic data, generate training data, data augmentation | dados sinteticos, gerar dados treino, data augmentation | create |

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
| personality | N03 | personality, swap persona, hot-swap persona, soul.md | personalidade, trocar persona, persona hot-swap | create |
| router | N03 | router, route table, task routing | roteador, tabela rotas | create |
| agent_profile | N03 | agent profile | agente perfil | create |
| agents_md | N03 | agents md | agents md | configure |
| customer_segment | N03 | customer segment | cliente segmento | configure |
| finetune_config | N03 | finetune config | finetune configuracao | configure |
| model_architecture | N03 | model architecture | modelo arquitetura | create |
| nucleus_def | N03 | nucleus def | nucleus def | configure |
| rl_algorithm | N03 | rl algorithm | rl algorithm | create |
| role_assignment | N03 | role assignment | role assignment | configure |
| distillation_config | N03 | distillation, teacher student, model compression, knowledge distillation | destilacao, teacher student, compressao modelo | create |
| training_method | N03 | training method | training metodo | create |

### P03 Prompt
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| action_prompt | N03 | task prompt, user message, action | prompt tarefa, mensagem usuario | create |
| chain | N03 | prompt chain, sequential chain | cadeia prompts, chain sequencial | create |
| context_file | N03 | context file, workspace instructions, CLAUDE.md, AGENTS.md, project instructions | arquivo contexto, instrucoes projeto, instrucoes workspace | create |
| constraint_spec | N03 | constraint, decoder rules | restricao, regras geracao | create |
| context_window_config | N03 | token budget, context window | orcamento tokens, janela contexto | configure |
| instruction | N03 | instructions, step-by-step, guide | instrucoes, passo-a-passo | create |
| prompt_compiler | N03 | intent resolution, prompt compiler | resolucao intencao, compilador | create |
| prompt_template | N03 | prompt template, template with vars | template prompt, template vars | create |
| prompt_version | N03 | version prompt, freeze prompt | versionar prompt, snapshot | create |
| reasoning_trace | N03 | reasoning trace, chain-of-thought | trace raciocinio, cadeia pensamento | create |
| system_prompt | N03 | system prompt, agent identity, persona | prompt sistema, identidade agente | create |
| churn_prevention_playbook | N03 | churn prevention playbook | churn prevention playbook | create |
| expansion_play | N03 | expansion play | expansao play | create |
| multimodal_prompt | N03 | multimodal prompt | multimodal prompt | create |
| planning_strategy | N03 | planning strategy | planning estrategia | create |
| prompt_optimizer | N03 | prompt optimizer | prompt otimizador | validate |
| prompt_technique | N03 | prompt technique | prompt technique | create |
| reasoning_strategy | N03 | reasoning strategy | reasoning estrategia | create |
| sales_playbook | N06 | sales playbook | sales playbook | create |
| webinar_script | N02 | webinar script | webinar script | create |

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
| messaging_gateway | N05 | messaging gateway, multi-platform bot, telegram/discord/slack integration | gateway de mensagem, bot multiplataforma, integracao telegram/discord/slack | create |
| webhook | N05 | webhook, HTTP callback | webhook, callback HTTP | create |
| action_paradigm | N05 | action paradigm | action paradigm | create |
| agent_name_service_record | N05 | agent name service record | agente name service registro | create |
| diff_strategy | N05 | diff strategy | diff estrategia | create |
| event_stream | N05 | event stream | evento fluxo | create |
| mcp_app_extension | N05 | mcp app extension | mcp app extension | create |
| sdk_example | N05 | sdk example | sdk example | create |
| search_strategy | N05 | search strategy | busca estrategia | create |
| stt_provider | N05 | stt provider | stt provedor | create |
| tts_provider | N05 | tts provider | tts provedor | create |
| voice_pipeline | N05 | voice pipeline | voz pipeline | create |

### P05 Output
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| formatter | N03 | formatter, format as JSON/CSV | formatador, formatar JSON | create |
| landing_page | N03 | landing page, web page | landing page, pagina web | create |
| output_validator | N03 | output validator, check output | validador saida, validar saida | create |
| parser | N03 | parser, extract data, parse output | parser, extrair dados | create |
| response_format | N03 | response format, output format | formato resposta, formato saida | create |
| analyst_briefing | N01 | analyst briefing | analyst briefing | create |
| app_directory_entry | N03 | app directory entry | app directory entrada | create |
| case_study | N03 | case study | case study | create |
| code_of_conduct | N03 | code of conduct | code of conduct | create |
| contributor_guide | N03 | contributor guide | contributor guia | create |
| course_module | N03 | course module | curso modulo | create |
| github_issue_template | N03 | github issue template | github issue template | create |
| integration_guide | N03 | integration guide | integration guia | create |
| interactive_demo | N03 | interactive demo | interactive demo | create |
| onboarding_flow | N03 | onboarding flow | onboarding flow | create |
| partner_listing | N03 | partner listing | partner listing | create |
| pitch_deck | N03 | pitch deck | pitch deck | create |
| press_release | N02 | press release | press release | create |
| pricing_page | N06 | pricing page | precificacao pagina | create |
| product_tour | N03 | product tour | product tour | create |
| quickstart_guide | N03 | quickstart guide | quickstart guia | create |
| streaming_config | N03 | streaming config | streaming configuracao | create |
| user_journey | N03 | user journey | user journey | create |

### P06 Schema
| Kind | N | EN | PT | V |
|------|---|----|----|---|
| enum_def | N03 | enum, enumeration, value list | enum, enumeracao, lista valores | create |
| input_schema | N03 | input schema, validate input | schema entrada, validar entrada | create |
| interface | N03 | interface, API contract | interface, contrato integracao | create |
| type_def | N03 | type def, custom type, data type | definicao tipo, tipo custom | create |
| validation_schema | N03 | validation schema, rules | schema validacao, regras validacao | create |
| validator | N03 | validator, field validator | validador, validador campo | create |
| aggregate_root | N03 | aggregate root | aggregate root | configure |
| api_reference | N03 | api reference | api reference | configure |
| data_contract | N03 | data contract | data contract | configure |
| edit_format | N03 | edit format | edit formato | configure |
| event_schema | N03 | event schema | evento esquema | configure |
| openapi_spec | N03 | openapi spec | openapi especificacao | configure |
| value_object | N03 | value object | value object | configure |

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
| curriculum_config | N05 | curriculum, training schedule, data ordering, difficulty schedule | curriculo, agenda treino, ordenacao dados | create |
| retrieval_evaluator | N05 | retrieval eval, RAG eval, MRR, NDCG, retrieval quality | avaliacao retrieval, qualidade RAG, qualidade recuperacao | test |
| benchmark_suite | N05 | benchmark suite | benchmark suite | validate |
| bias_audit | N05 | bias audit | bias auditoria | validate |
| cohort_analysis | N05 | cohort analysis | cohort analise | validate |
| eval_framework | N05 | eval framework | avaliacao framework | validate |
| eval_metric | N05 | eval metric | avaliacao metric | validate |
| experiment_tracker | N05 | experiment tracker | experimento rastreador | validate |
| judge_config | N05 | judge config | judge configuracao | validate |
| llm_evaluation_scenario | N05 | llm evaluation scenario | llm evaluation scenario | validate |
| memory_benchmark | N05 | memory benchmark | memoria benchmark | validate |
| reward_model | N05 | reward model | reward modelo | validate |
| trajectory_eval | N05 | trajectory eval | trajectory avaliacao | validate |
| usage_report | N05 | usage report | usage relatorio | validate |

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
| agent_computer_interface | N03 | agent computer interface | agente computer interface | create |
| bounded_context | N03 | bounded context | bounded contexto | configure |
| capability_registry | N03 | capability registry | capability registro | configure |
| context_map | N03 | context map | contexto mapa | configure |
| dual_loop_architecture | N03 | dual loop architecture | dual loop arquitetura | create |
| fhir_agent_capability | N03 | fhir agent capability | fhir agente capability | configure |

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
| terminal_backend | N05 | terminal backend, execution environment, execution target, backend switch, local docker ssh daytona modal singularity | backend de terminal, ambiente de execucao, alvo execucao, trocar backend | configure |
| hibernation_policy | N05 | hibernation, idle policy, sleep when idle, scale to zero, hibernate, daytona pause, modal hibernate, serverless idle | hibernacao, politica de hibernar, hibernar, dormir quando ocioso, idle cost, custo ociosidade | configure |
| inference_config | N05 | inference params, temperature, sampling, top_p config, generation config | parametros inferencia, temperatura, amostragem, config geracao | configure |
| tokenizer_config | N05 | tokenizer, BPE, sentencepiece, tiktoken, tokenizer config | tokenizador, BPE, sentencepiece, tiktoken, config tokenizador | configure |
| alert_rule | N05 | alert rule | alerta regra | validate |
| backpressure_policy | N05 | backpressure policy | backpressure politica | validate |
| batch_config | N05 | batch config | lote configuracao | create |
| canary_config | N05 | canary config | canary configuracao | validate |
| circuit_breaker | N05 | circuit breaker | circuit breaker | validate |
| cost_budget | N05 | cost budget | cost orcamento | validate |
| data_residency | N05 | data residency | data residency | configure |
| deployment_manifest | N05 | deployment manifest | implantacao manifesto | create |
| experiment_config | N05 | experiment config | experimento configuracao | validate |
| kubernetes_ai_requirement | N05 | kubernetes ai requirement | kubernetes ai requirement | configure |
| marketplace_app_manifest | N05 | marketplace app manifest | marketplace app manifesto | configure |
| oauth_app_config | N05 | oauth app config | oauth app configuracao | configure |
| playground_config | N05 | playground config | playground configuracao | configure |
| prosody_config | N05 | prosody config | prosody configuracao | configure |
| quantization_config | N05 | quantization config | quantization configuracao | configure |
| rbac_policy | N05 | rbac policy | rbac politica | configure |
| realtime_session | N05 | realtime session | realtime sessao | create |
| retry_policy | N05 | retry policy | retry politica | validate |
| sandbox_config | N05 | sandbox config | sandbox configuracao | configure |
| sandbox_spec | N05 | sandbox spec | sandbox especificacao | configure |
| slo_definition | N05 | slo definition | slo definicao | validate |
| sso_config | N05 | sso config | sso configuracao | configure |
| thinking_config | N05 | thinking config | thinking configuracao | configure |
| transport_config | N05 | transport config | transport configuracao | configure |
| usage_quota | N05 | usage quota | usage cota | configure |
| vad_config | N05 | vad config | vad configuracao | configure |
| white_label_config | N05 | white label config | white label configuracao | configure |

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
| user_model | N04 | model the user, user profile, remember preferences, track working style | modelar o usuario, perfil do usuario, lembrar preferencias, estilo de trabalho | create |
| agent_grounding_record | N04 | agent grounding record | agente grounding registro | create |
| c2pa_manifest | N04 | c2pa manifest | c2pa manifesto | configure |
| consolidation_policy | N04 | consolidation policy | consolidation politica | validate |
| episodic_memory | N04 | episodic memory | episodic memoria | create |
| memory_architecture | N04 | memory architecture | memoria arquitetura | create |
| model_registry | N04 | model registry | modelo registro | validate |
| procedural_memory | N04 | procedural memory | procedural memoria | create |
| prospective_memory | N04 | prospective memory | prospective memoria | create |
| vc_credential | N04 | vc credential | vc credential | configure |
| workflow_run_crate | N04 | workflow run crate | fluxo run crate | create |
| working_memory | N04 | working memory | working memoria | create |

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
| ab_test_config | N05 | ab test config | ab teste configuracao | validate |
| ai_rmf_profile | N05 | ai rmf profile | ai rmf perfil | validate |
| audit_log | N05 | audit log | auditoria log | validate |
| compliance_checklist | N05 | compliance checklist | conformidade checklist | validate |
| compliance_framework | N05 | compliance framework | conformidade framework | configure |
| conformity_assessment | N05 | conformity assessment | conformity assessment | validate |
| constitutional_rule | N05 | constitutional rule | constitutional regra | configure |
| content_filter | N05 | content filter | content filtro | validate |
| drift_detector | N05 | drift detector | drift detector | validate |
| enterprise_sla | N05 | enterprise sla | enterprise sla | validate |
| gpai_technical_doc | N05 | gpai technical doc | gpai technical doc | create |
| hitl_config | N05 | hitl config | hitl configuracao | validate |
| incident_report | N05 | incident report | incidente relatorio | validate |
| nps_survey | N05 | nps survey | nps survey | validate |
| preference_dataset | N05 | preference dataset | preference dataset | validate |
| referral_program | N05 | referral program | indicacao program | configure |
| roi_calculator | N06 | roi calculator | roi calculator | validate |
| safety_hazard_taxonomy | N05 | safety hazard taxonomy | seguranca hazard taxonomy | configure |
| safety_policy | N05 | safety policy | seguranca politica | configure |
| self_improvement_loop | N05 | self improvement loop | self improvement loop | validate |
| subscription_tier | N06 | subscription tier | assinatura plano | configure |
| threat_model | N05 | threat model | ameaca modelo | validate |

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
| pipeline_template | N07 | pipeline, scenario pipeline, scenario-indexed flow, opencode pipeline | pipeline, fluxo por cenario, pipeline cenario, pipeline opencode | create |
| revision_loop_policy | N05 | revision policy, max retries, iteration budget, escalation policy | politica de revisao, max tentativas, orcamento iteracao, politica escalacao | create |
| curation_nudge | N04 | memory nudge, persist reminder, proactive memory, curation prompt | nudge de memoria, lembrete persistir, memoria proativa, nudge curacao | create |
| workflow | N03 | workflow, orchestration flow | workflow, fluxo orquestracao | create |
| workflow_primitive | N03 | workflow primitive, basic step | primitiva workflow, etapa basica | create |
| collaboration_pattern | N07 | collaboration pattern | collaboration padrao | create |
| crew_template | N07 | crew template | crew template | create |
| domain_event | N07 | domain event | domain evento | create |
| process_manager | N07 | process manager | process manager | create |
| renewal_workflow | N07 | renewal workflow | renovacao fluxo | create |
| saga | N07 | saga | saga | create |
| state_machine | N07 | state machine | estado machine | create |
| team_charter | N07 | team charter | team charter | create |
| visual_workflow | N07 | visual workflow | visual fluxo | create |
| workflow_node | N07 | workflow node | fluxo node | create |

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_intent_resolution_map]] | upstream | 0.43 |
| [[p12_dr_software_project]] | downstream | 0.36 |
| [[quality_gate_intent_resolution]] | downstream | 0.34 |
| [[p12_dr_builder_nucleus]] | downstream | 0.33 |
| [[bld_sp_collaboration_software_project]] | downstream | 0.28 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.28 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.26 |
| [[spec_seed_words]] | upstream | 0.25 |
| [[p02_nd_n03.md]] | upstream | 0.24 |
| [[agent_card_n03]] | upstream | 0.24 |
