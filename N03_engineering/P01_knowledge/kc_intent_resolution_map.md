---
id: kc_intent_resolution_map
kind: knowledge_card
pillar: P01
title: Intent Resolution Map -- 123 Kinds x Natural Language Triggers
version: 1.0.0
created: 2026-04-08
author: n03_builder
domain: meta-construction/intent-resolution
quality: 9.1
tags: [intent-resolution, kinds, mapping, natural-language, transmutation, canonicalization]
tldr: "Complete mapping of all 123 CEX kinds to natural language trigger phrases (EN+PT), pillar, nucleus, and builder."
density_score: 0.95
related:
  - bld_collaboration_agent
  - bld_collaboration_boot_config
  - bld_collaboration_vector_store
  - bld_collaboration_embedder_provider
  - bld_collaboration_model_provider
  - bld_collaboration_knowledge_card
  - bld_collaboration_model_card
  - agent_card_n04
  - bld_collaboration_agent_package
  - bld_architecture_kind
---

# Intent Resolution Map

Every user intent must resolve to one or more kinds. This map is the exhaustive reference.

**Structure:** kind | pillar | nucleus | builder | trigger phrases (EN) | trigger phrases (PT) | common misspellings/variations

## P01 Knowledge (10 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| knowledge_card | N04 | knowledge-card-builder | "write a knowledge card", "document this fact", "create a KC", "distill this info", "atomic knowledge" | "criar KC", "documentar fato", "cartao de conhecimento", "registrar conhecimento" | kc, KC, knowledgecard |
| chunk_strategy | N04 | chunk-strategy-builder | "chunking strategy", "split documents", "how to chunk", "text splitting", "segment text" | "estrategia de chunk", "dividir texto", "segmentar documentos" | chunking, chunk_strat, split |
| citation | N04 | citation-builder | "add citation", "source reference", "cite this", "attribution", "provenance" | "adicionar citacao", "referencia de fonte", "citar isso" | cite, ref, source |
| context_doc | N04 | context-doc-builder | "context document", "background info", "domain context", "hydrate prompt" | "documento de contexto", "contexto do dominio", "informacao de fundo" | ctx, context |
| embedding_config | N04 | embedding-config-builder | "embedding config", "vector model", "embedding model setup" | "configurar embedding", "modelo vetorial" | embed, emb_config |
| embedder_provider | N04 | embedder-provider-builder | "embedding provider", "text embedder", "vector provider" | "provedor de embedding", "embedder" | embedder, embed_provider |
| few_shot_example | N04 | few-shot-example-builder | "few-shot example", "input/output pair", "example for prompt", "exemplar" | "exemplo few-shot", "par entrada/saida", "exemplo para prompt" | fewshot, few_shot, fse |
| glossary_entry | N04 | glossary-entry-builder | "glossary term", "define term", "terminology entry", "domain term" | "termo do glossario", "definir termo", "entrada do dicionario" | glossary, term, gloss |
| rag_source | N04 | rag-source-builder | "RAG source", "external source", "indexable source", "data source for RAG" | "fonte RAG", "fonte externa", "fonte indexavel" | rag, source, data_source |
| retriever_config | N04 | retriever-config-builder | "retriever config", "search config", "top_k settings", "reranker config" | "configurar retriever", "config de busca", "ajustar top_k" | retr_config, search_cfg |
| vector_store | N04 | vector-store-builder | "vector store", "vector database", "similarity search backend", "FAISS setup" | "banco vetorial", "vector store", "base de similaridade" | vectordb, vdb, faiss |

## P02 Model (13 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| agent | N03 | agent-builder | "create agent", "define agent", "agent persona", "AI agent", "bot definition" | "criar agente", "definir agente", "persona do agente" | agente, bot |
| agent_card | N03 | agent-card-builder | "agent card", "deployment spec", "agent capabilities", "A2A card" | "card do agente", "spec de deploy", "capacidades do agente" | agentcard, deck |
| agent_package | N03 | agent-package-builder | "agent package", "portable agent", "ISO agent", "agent bundle" | "pacote de agente", "agente portavel", "ISO do agente" | iso, package, bundle |
| axiom | N03 | axiom-builder | "axiom", "fundamental rule", "immutable principle", "core belief" | "axioma", "principio fundamental", "regra imutavel" | axioma, principle |
| boot_config | N05 | boot-config-builder | "boot config", "provider bootstrap", "startup config", "initialization" | "config de boot", "inicializacao", "configurar provider" | boot, bootstrap |
| fallback_chain | N03 | fallback-chain-builder | "fallback chain", "model fallback", "retry chain", "failover" | "cadeia de fallback", "fallback de modelo", "failover" | fallback, fb_chain |
| handoff_protocol | N03 | handoff-protocol-builder | "handoff protocol", "agent transfer", "A2A handoff", "delegation protocol" | "protocolo de handoff", "transferencia entre agentes" | handoff_proto |
| lens | N03 | lens-builder | "lens", "perspective", "domain lens", "specialized view" | "lente", "perspectiva", "visao especializada" | perspectiva, view |
| memory_scope | N03 | memory-scope-builder | "memory scope", "agent memory config", "what to remember" | "escopo de memoria", "config de memoria do agente" | memscope |
| mental_model | N03 | mental-model-builder | "mental model", "agent routing map", "decision map" | "mapa mental", "modelo mental", "mapa de decisao" | mm, routing_map |
| model_card | N03 | model-card-builder | "model card", "LLM spec", "model capabilities", "model pricing" | "card do modelo", "spec do LLM", "capacidades do modelo" | modelcard, llm_card |
| model_provider | N05 | model-provider-builder | "model provider", "LLM provider", "add provider", "Claude/GPT/Gemini adapter" | "provedor de modelo", "provedor LLM", "adaptador de modelo" | provider, llm_provider |
| router | N03 | router-builder | "router", "task routing", "agent routing", "request router" | "roteador", "roteamento de tarefas", "router de agentes" | routing, roteamento |
| software_project | N03 | software-project-builder | "software project", "project definition", "app architecture", "repo structure" | "projeto de software", "definir projeto", "arquitetura do app" | project, app |

## P03 Prompt (9 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| action_prompt | N03 | action-prompt-builder | "action prompt", "task prompt", "instruction to agent", "user prompt" | "prompt de acao", "prompt de tarefa", "instrucao para agente" | user_prompt, task_prompt |
| chain | N03 | chain-builder | "prompt chain", "chain of prompts", "sequential prompts", "output A to input B" | "cadeia de prompts", "prompts sequenciais", "encadear prompts" | cadeia, sequence |
| constraint_spec | N03 | constraint-spec-builder | "constraint spec", "generation constraints", "decoder rules", "output constraints" | "spec de restricao", "restricoes de geracao", "regras do decoder" | constraint, restricao |
| context_window_config | N03 | context-window-config-builder | "context window config", "token budget", "prompt budget", "context allocation" | "config de janela de contexto", "orcamento de tokens", "alocacao de contexto" | cwc, token_budget |
| instruction | N03 | instruction-builder | "instruction", "step-by-step", "execution instructions", "how-to for agent" | "instrucao", "passo a passo", "instrucoes de execucao" | instrucao, steps |
| prompt_template | N03 | prompt-template-builder | "prompt template", "template with variables", "reusable prompt", "prompt with slots" | "template de prompt", "modelo de prompt", "prompt com variaveis" | template, pt, molde |
| prompt_version | N03 | prompt-version-builder | "prompt version", "version snapshot", "freeze prompt", "prompt history" | "versao de prompt", "snapshot de prompt", "historico de prompt" | pv, version |
| reasoning_trace | N03 | reasoning-trace-builder | "reasoning trace", "chain of thought", "CoT trace", "thinking steps" | "rastro de raciocinio", "cadeia de pensamento", "passos de raciocinio" | cot, trace, thinking |
| system_prompt | N03 | system-prompt-builder | "system prompt", "agent identity", "system instructions", "persona prompt" | "prompt de sistema", "identidade do agente", "instrucoes do sistema" | sp, system_msg |
| tagline | N02 | tagline-builder | "tagline", "slogan", "headline", "brand phrase", "memorable phrase" | "tagline", "slogan", "frase de efeito", "chamada" | slogan, headline |

## P04 Tools (18 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| api_client | N05 | api-client-builder | "API client", "REST client", "GraphQL client", "HTTP client" | "cliente de API", "cliente REST", "cliente HTTP" | api, client |
| audio_tool | N05 | audio-tool-builder | "audio tool", "speech to text", "text to speech", "TTS", "STT" | "ferramenta de audio", "fala para texto", "texto para fala" | audio, tts, stt |
| browser_tool | N05 | browser-tool-builder | "browser tool", "web scraper", "DOM automation", "web navigation" | "ferramenta de browser", "scraper web", "automacao DOM" | browser, scraper |
| cli_tool | N05 | cli-tool-builder | "CLI tool", "command line tool", "terminal command", "shell tool" | "ferramenta CLI", "comando de terminal", "ferramenta de linha de comando" | cli, terminal, shell |
| code_executor | N05 | code-executor-builder | "code executor", "sandbox", "code runner", "Jupyter runtime", "Docker exec" | "executor de codigo", "sandbox", "rodar codigo" | sandbox, exec, jupyter |
| computer_use | N05 | computer-use-builder | "computer use", "screen control", "GUI automation", "mouse/keyboard" | "uso do computador", "controle de tela", "automacao GUI" | gui, screen |
| daemon | N05 | daemon-builder | "daemon", "background process", "persistent service", "background worker" | "daemon", "processo background", "servico persistente" | background, service |
| db_connector | N05 | db-connector-builder | "database connector", "DB connector", "SQL connection", "data connector" | "conector de banco", "conector SQL", "conexao com banco" | database, db, sql |
| document_loader | N04 | document-loader-builder | "document loader", "file ingestion", "PDF loader", "CSV parser" | "carregador de documentos", "ingestao de arquivos", "carregar PDF" | loader, ingest |
| function_def | N05 | function-def-builder | "function definition", "tool definition", "JSON Schema tool", "callable function" | "definicao de funcao", "definicao de ferramenta", "funcao callable" | function, tool_def, fn |
| hook | N05 | hook-builder | "hook", "pre/post hook", "event hook", "trigger on event" | "hook", "gancho", "trigger de evento" | trigger, pre_hook, post_hook |
| hook_config | N05 | hook-config-builder | "hook config", "hook lifecycle", "configure hooks" | "config de hook", "ciclo de vida de hooks" | hook_cfg |
| mcp_server | N05 | mcp-server-builder | "MCP server", "tool server", "Model Context Protocol", "MCP tools" | "servidor MCP", "servidor de ferramentas", "protocolo MCP" | mcp, server |
| multi_modal_config | N05 | multi-modal-config-builder | "multi-modal config", "image input config", "modality settings" | "config multimodal", "config de imagem", "modalidades" | multimodal, mmc |
| notifier | N05 | notifier-builder | "notifier", "notification", "send alert", "push notification", "Slack/email alert" | "notificador", "notificacao", "enviar alerta" | notify, alert |
| plugin | N05 | plugin-builder | "plugin", "extension", "add-on", "pluggable module" | "plugin", "extensao", "modulo plugavel" | extension, addon |
| research_pipeline | N01 | research-pipeline-builder | "research pipeline", "multi-source research", "STORM pipeline", "deep research" | "pipeline de pesquisa", "pesquisa multi-fonte", "pesquisa profunda" | research, storm |
| retriever | N04 | retriever-builder | "retriever", "vector search", "similarity search", "RAG retriever" | "retriever", "busca vetorial", "busca por similaridade" | search, vector_search |
| search_tool | N05 | search-tool-builder | "search tool", "web search", "Tavily", "Serper", "internet search" | "ferramenta de busca", "busca web", "pesquisa na internet" | search, web_search |
| skill | N03 | skill-builder | "skill", "reusable capability", "agent skill", "semantic kernel skill" | "habilidade", "capacidade reutilizavel", "skill do agente" | capability, ability |
| social_publisher | N02 | social-publisher-builder | "social publisher", "auto-post", "social media automation", "content publisher" | "publicador social", "auto-post", "automacao de redes sociais" | social, autopublish |
| supabase_data_layer | N05 | supabase-data-layer-builder | "Supabase data layer", "Supabase tables", "RLS policies", "edge functions" | "camada de dados Supabase", "tabelas Supabase", "politicas RLS" | supabase, supa |
| toolkit | N05 | toolkit-builder | "toolkit", "tool collection", "tool bundle", "callable tools set" | "toolkit", "colecao de ferramentas", "conjunto de tools" | tools, toolset |
| vision_tool | N05 | vision-tool-builder | "vision tool", "image analysis", "OCR", "screenshot reader" | "ferramenta de visao", "analise de imagem", "OCR" | vision, ocr, image |
| webhook | N05 | webhook-builder | "webhook", "HTTP endpoint", "event receiver", "callback URL" | "webhook", "endpoint HTTP", "receptor de eventos" | hook_http, callback |

## P05 Output (5 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| formatter | N03 | formatter-builder | "formatter", "output formatter", "format as JSON/MD/YAML" | "formatador", "formatar saida", "formato de saida" | format, fmt |
| landing_page | N03 | landing-page-builder | "landing page", "product page", "marketing page", "conversion page" | "landing page", "pagina de produto", "pagina de conversao" | lp, page |
| output_validator | N03 | output-validator-builder | "output validator", "post-LLM validation", "check output quality" | "validador de saida", "validacao pos-LLM" | oval, output_check |
| parser | N03 | parser-builder | "parser", "output parser", "extract from output", "data extractor" | "parser", "extrator de dados", "extrair de saida" | extractor, parse |
| response_format | N03 | response-format-builder | "response format", "output format", "how agent responds" | "formato de resposta", "formato de saida do agente" | rf, resp_format |

## P06 Schema (5 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| enum_def | N03 | enum-def-builder | "enum", "enumeration", "finite list", "allowed values" | "enum", "enumeracao", "lista finita", "valores permitidos" | enumeration, enum |
| input_schema | N03 | input-schema-builder | "input schema", "input contract", "required fields", "request schema" | "schema de entrada", "contrato de entrada", "campos obrigatorios" | schema, input_contract |
| interface | N03 | interface-builder | "interface", "integration contract", "agent contract", "bilateral contract" | "interface", "contrato de integracao", "contrato bilateral" | contrato, iface |
| type_def | N03 | type-def-builder | "type definition", "custom type", "data type", "typedef" | "definicao de tipo", "tipo customizado", "typedef" | tipo, type, typedef |
| validation_schema | N03 | validation-schema-builder | "validation schema", "post-generation contract", "output validation rules" | "schema de validacao", "contrato pos-geracao", "regras de validacao" | vs, val_schema |
| validator | N03 | validator-builder | "validator", "validation rule", "pre-commit check", "pass/fail rule" | "validador", "regra de validacao", "verificacao pre-commit" | val, check |

## P07 Evaluation (10 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| benchmark | N05 | benchmark-builder | "benchmark", "performance test", "latency/cost measurement" | "benchmark", "teste de performance", "medicao de latencia" | bench, perf_test |
| e2e_eval | N05 | e2e-eval-builder | "end-to-end eval", "e2e test", "full pipeline test" | "teste end-to-end", "teste e2e", "teste de pipeline completo" | e2e, end_to_end |
| eval_dataset | N05 | eval-dataset-builder | "eval dataset", "test dataset", "test cases collection" | "dataset de avaliacao", "colecao de testes" | dataset, test_data |
| golden_test | N05 | golden-test-builder | "golden test", "reference test", "quality 9.5+ test case" | "teste dourado", "teste referencia", "caso de teste ideal" | golden, gt |
| llm_judge | N05 | llm-judge-builder | "LLM judge", "LLM-as-judge", "AI evaluator" | "juiz LLM", "LLM como juiz", "avaliador AI" | judge, llm_eval |
| red_team_eval | N05 | red-team-eval-builder | "red team eval", "adversarial test", "security eval" | "teste adversarial", "avaliacao red team", "teste de seguranca" | redteam, adversarial |
| regression_check | N05 | regression-check-builder | "regression check", "regression test", "before/after comparison" | "teste de regressao", "verificacao de regressao", "comparar com baseline" | regression, regcheck |
| scoring_rubric | N05 | scoring-rubric-builder | "scoring rubric", "evaluation criteria", "grading framework" | "rubrica de avaliacao", "criterios de avaliacao", "framework de notas" | rubric, grading |
| smoke_eval | N05 | smoke-eval-builder | "smoke test", "sanity check", "quick validation" | "smoke test", "teste de sanidade", "validacao rapida" | smoke, sanity |
| trace_config | N05 | trace-config-builder | "trace config", "observability config", "span configuration" | "config de trace", "config de observabilidade" | tracing, observability |

## P08 Architecture (7 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| component_map | N03 | component-map-builder | "component map", "architecture map", "what connects to what" | "mapa de componentes", "mapa de arquitetura" | cmap, arch_map |
| decision_record | N03 | decision-record-builder | "decision record", "ADR", "architecture decision", "why we chose" | "registro de decisao", "ADR", "decisao de arquitetura" | adr, decision |
| diagram | N03 | diagram-builder | "diagram", "architecture diagram", "Mermaid diagram", "ASCII diagram" | "diagrama", "diagrama de arquitetura", "diagrama Mermaid" | diag, mermaid |
| invariant | N03 | invariant-builder | "invariant", "operational law", "system law", "inviolable rule" | "invariante", "lei operacional", "regra inviolavel" | law, regra |
| naming_rule | N03 | naming-rule-builder | "naming rule", "naming convention", "file naming", "artifact naming" | "regra de nomenclatura", "convencao de nomes" | naming, convention |
| pattern | N03 | pattern-builder | "pattern", "architecture pattern", "reusable pattern", "design pattern" | "pattern", "padrao de arquitetura", "padrao reutilizavel" | padrao, design_pattern |
| supervisor | N03 | supervisor-builder | "supervisor", "crew orchestrator", "multi-builder coordinator" | "supervisor", "orquestrador de crew", "coordenador" | director, crew_lead |

## P09 Config (8 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| effort_profile | N05 | effort-profile-builder | "effort profile", "thinking level", "model selection config" | "perfil de esforco", "nivel de thinking", "config de modelo" | effort, thinking |
| env_config | N05 | env-config-builder | "env config", "environment variables", "env vars", ".env" | "config de ambiente", "variaveis de ambiente" | env, dotenv |
| feature_flag | N05 | feature-flag-builder | "feature flag", "feature toggle", "gradual rollout", "on/off flag" | "flag de feature", "toggle", "rollout gradual" | ff, toggle, flag |
| path_config | N05 | path-config-builder | "path config", "file paths", "system paths" | "config de caminhos", "paths do sistema" | paths, path |
| permission | N05 | permission-builder | "permission", "access control", "read/write/execute", "RBAC" | "permissao", "controle de acesso", "leitura/escrita" | perm, access |
| rate_limit_config | N05 | rate-limit-config-builder | "rate limit", "RPM limit", "TPM budget", "throttle config" | "limite de taxa", "limite RPM", "orcamento TPM" | ratelimit, throttle |
| runtime_rule | N05 | runtime-rule-builder | "runtime rule", "timeout config", "retry config", "technical rule" | "regra de runtime", "config de timeout", "config de retries" | runtime, timeout |
| secret_config | N05 | secret-config-builder | "secret config", "credentials", "API keys", "secrets management" | "config de secrets", "credenciais", "chaves de API" | secrets, creds |

## P10 Memory (9 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| compression_config | N04 | compression-config-builder | "compression config", "context compression", "output compression" | "config de compressao", "compressao de contexto" | compression |
| entity_memory | N04 | entity-memory-builder | "entity memory", "facts about X", "entity knowledge", "remember entity" | "memoria de entidade", "fatos sobre X", "lembrar entidade" | entity, memory_about |
| knowledge_index | N04 | knowledge-index-builder | "knowledge index", "search index", "BM25 index", "FAISS index" | "indice de conhecimento", "indice de busca" | index, search_index |
| learning_record | N04 | learning-record-builder | "learning record", "lesson learned", "what worked/failed" | "registro de aprendizado", "licao aprendida", "o que deu certo" | lesson, learning |
| memory_summary | N04 | memory-summary-builder | "memory summary", "compressed memory", "memory digest" | "resumo de memoria", "memoria comprimida" | summary, digest |
| memory_type | N04 | memory-type-builder | "memory type", "memory classification", "memory policy" | "tipo de memoria", "classificacao de memoria" | mem_type |
| prompt_cache | N05 | prompt-cache-builder | "prompt cache", "completion cache", "cache config", "TTL config" | "cache de prompt", "cache de completions", "config de cache" | cache, ttl |
| runtime_state | N04 | runtime-state-builder | "runtime state", "mutable state", "session accumulation" | "estado de runtime", "estado mutavel" | state, runtime |
| session_backend | N05 | session-backend-builder | "session backend", "session persistence", "user session storage" | "backend de sessao", "persistencia de sessao" | session_store |
| session_state | N04 | session-state-builder | "session state", "ephemeral state", "session snapshot" | "estado de sessao", "estado efemero", "snapshot de sessao" | session, snapshot |

## P11 Feedback (8 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| bugloop | N05 | bugloop-builder | "bug loop", "auto-fix cycle", "detect-fix-verify", "self-healing" | "ciclo de bug", "correcao automatica", "detectar-corrigir-verificar" | bugfix, autofix |
| content_monetization | N06 | content-monetization-builder | "content monetization", "billing pipeline", "course monetization", "checkout flow" | "monetizacao de conteudo", "pipeline de billing", "monetizar curso" | monetization, billing |
| guardrail | N03 | guardrail-builder | "guardrail", "safety boundary", "content filter", "safety rule" | "guardrail", "limite de seguranca", "filtro de conteudo" | safety, filter |
| lifecycle_rule | N03 | lifecycle-rule-builder | "lifecycle rule", "freshness rule", "archive rule", "promote rule" | "regra de ciclo de vida", "regra de freshness", "regra de arquivo" | lifecycle, freshness |
| optimizer | N05 | optimizer-builder | "optimizer", "process optimization", "metric to action", "continuous improvement" | "otimizador", "otimizacao de processo", "melhoria continua" | optimize, improve |
| quality_gate | N03 | quality-gate-builder | "quality gate", "quality threshold", "pass/fail gate", "quality barrier" | "gate de qualidade", "barreira de qualidade", "limiar de qualidade" | qg, gate |
| regression_check | N05 | regression-check-builder | "regression check", "before/after", "compare baseline" | "verificacao de regressao", "antes/depois", "comparar baseline" | regression |
| reward_signal | N05 | reward-signal-builder | "reward signal", "quality signal", "continuous score" | "sinal de recompensa", "sinal de qualidade" | reward, score_signal |

## P12 Orchestration (9 kinds)

| Kind | Nucleus | Builder | EN Triggers | PT Triggers | Variations |
|------|---------|---------|-------------|-------------|------------|
| checkpoint | N07 | checkpoint-builder | "checkpoint", "workflow snapshot", "save state", "resumable" | "checkpoint", "snapshot de workflow", "salvar estado" | ckpt, savepoint |
| dag | N03 | dag-builder | "DAG", "dependency graph", "task graph", "acyclic graph" | "DAG", "grafo de dependencias", "grafo de tarefas" | graph, dep_graph |
| dispatch_rule | N07 | dispatch-rule-builder | "dispatch rule", "routing policy", "keyword to agent", "dispatch config" | "regra de despacho", "politica de roteamento", "despacho" | dispatch, routing |
| handoff | N07 | handoff-builder | "handoff", "task handoff", "agent handoff", "work transfer" | "handoff", "transferencia de tarefa" | ho, transfer |
| schedule | N07 | schedule-builder | "schedule", "cron job", "timed trigger", "recurring task" | "agendamento", "cron", "trigger temporal", "tarefa recorrente" | cron, timer |
| signal | N07 | signal-builder | "signal", "completion signal", "event signal", "status signal" | "sinal", "sinal de conclusao", "sinal de evento" | sig, event |
| spawn_config | N07 | spawn-config-builder | "spawn config", "launch config", "grid config", "process spawn" | "config de spawn", "config de lancamento", "config de grid" | spawn, launch |
| workflow | N03 | workflow-builder | "workflow", "multi-step flow", "pipeline", "agent flow" | "workflow", "fluxo de trabalho", "pipeline", "fluxo multi-etapa" | flow, pipeline, wf |
| workflow_primitive | N03 | workflow-primitive-builder | "workflow primitive", "step/parallel/loop", "execution primitive" | "primitiva de workflow", "step/parallel/loop" | primitive, step |

## Cross-Reference: Nucleus Routing Summary

| Nucleus | Primary Kinds | Count |
|---------|---------------|-------|
| N01 (Intelligence) | research_pipeline | 1 |
| N02 (Marketing) | tagline, social_publisher | 2 |
| N03 (Builder) | agent, agent_card, agent_package, axiom, chain, component_map, constraint_spec, context_window_config, dag, decision_record, diagram, enum_def, fallback_chain, formatter, guardrail, handoff_protocol, input_schema, instruction, interface, invariant, landing_page, lens, lifecycle_rule, memory_scope, mental_model, model_card, naming_rule, output_validator, parser, pattern, prompt_template, prompt_version, quality_gate, reasoning_trace, response_format, router, skill, supervisor, system_prompt, type_def, validation_schema, validator, workflow, workflow_primitive, action_prompt | 45 |
| N04 (Knowledge) | chunk_strategy, citation, compression_config, context_doc, document_loader, embedder_provider, embedding_config, entity_memory, few_shot_example, glossary_entry, knowledge_card, knowledge_index, learning_record, memory_summary, memory_type, rag_source, retriever, retriever_config, runtime_state, session_state, vector_store | 21 |
| N05 (Operations) | api_client, audio_tool, benchmark, boot_config, browser_tool, bugloop, cli_tool, code_executor, computer_use, daemon, db_connector, e2e_eval, effort_profile, env_config, eval_dataset, feature_flag, function_def, golden_test, hook, hook_config, llm_judge, mcp_server, model_provider, multi_modal_config, notifier, optimizer, path_config, permission, plugin, prompt_cache, rate_limit_config, red_team_eval, regression_check, reward_signal, runtime_rule, scoring_rubric, search_tool, secret_config, session_backend, smoke_eval, supabase_data_layer, toolkit, trace_config, vision_tool, webhook | 45 |
| N06 (Commercial) | content_monetization | 1 |
| N07 (Orchestration) | checkpoint, dispatch_rule, handoff, schedule, signal, spawn_config | 6 |

**Total: 123 kinds mapped. 0 gaps.**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | downstream | 0.43 |
| [[bld_collaboration_boot_config]] | downstream | 0.42 |
| [[bld_collaboration_vector_store]] | downstream | 0.39 |
| [[bld_collaboration_embedder_provider]] | downstream | 0.38 |
| [[bld_collaboration_model_provider]] | downstream | 0.37 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.37 |
| [[bld_collaboration_model_card]] | downstream | 0.35 |
| [[agent_card_n04]] | related | 0.35 |
| [[bld_collaboration_agent_package]] | downstream | 0.33 |
| [[bld_architecture_kind]] | downstream | 0.33 |
