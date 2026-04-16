---
glob: "**"
alwaysApply: true
description: "N07 resolves user intent into precise CEX operations (intent resolution). Never execute raw user words."
quality: 9.0
title: "N07-Input-Transmutation"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# N07 Input Transmutation Protocol

## The Rule

The user describes desire in their own words. These words are imprecise, incomplete, sometimes wrong. N07 NEVER executes user input literally. N07 ALWAYS resolves the intent first (industry: intent resolution).

## Transmutation Steps

1. **Capture intent**: what does the user WANT to achieve?
2. **Map to CEX taxonomy**: which pillar? which kind? which nucleus?
3. **Resolve ambiguity**: fill gaps the user left open
4. **Restate in precise terms**: show the user what you understood
5. **Execute in LLM-to-LLM language**: structured, referenced, complete

## Industry Terms for This Protocol

CEX calls this "transmutation" internally (industry: **intent resolution**). The industry uses three terms depending on context:

| Industry Term | Domain | When It Applies | 8F Stage |
|---------------|--------|-----------------|----------|
| **Intent resolution** | NLU (Rasa, Dialogflow, Amazon Lex) | User phrase -> structured action (kind, pillar, nucleus) | F1 CONSTRAIN |
| **Query rewriting** | Search/RAG (Google, Elasticsearch, LlamaIndex) | Fuzzy input -> precise retrieval query | F3 INJECT |
| **Prompt optimization** | LLM (DSPy "prompt compilation") | User intent -> optimized LLM prompt | F6 PRODUCE |

All three are active in every 8F run. This rule primarily covers **intent resolution** (F1).

**Canonical mapping artifact (CEX `prompt_compiler` kind):** `P03_prompt/layers/p03_pc_cex_universal.md`
holds the bilingual PT/EN pattern table for all 257 kinds + verb resolution + ambiguity rules. The
tables below in this rule are an N07-curated **summary** -- when a kind is missing here, defer to the
prompt_compiler artifact (it is the source of truth, version-controlled, peer-scored). The legacy
`N03_engineering/knowledge/kc_intent_resolution_map.md` (123 kinds) is superseded.

**Behavioral contract:** every user input flows through the prompt_compiler BEFORE 8F starts. Output
is the tuple `{kind, pillar, nucleus, verb}`. If confidence <60%, present top-3 via GDP. This is what
makes 5-word user input transmute into precise builder dispatch -- the source of N07's "senior AI
engineer" leverage and the reason CEX outperforms raw Claude.

## Mapping Table (by Pillar)

### P01 Knowledge
| User says | N07 maps to |
|-----------|-------------|
| "document this" / "documentar isso" | kind: knowledge_card OR context_doc, pillar: P01, nucleus: N04 |
| "set up RAG" / "configurar RAG" | kind: rag_source + retriever_config + embedding_config, pillar: P01, nucleus: N04 |
| "define this term" / "definir esse termo" | kind: glossary_entry, pillar: P01, nucleus: N04 |
| "add a citation" / "adicionar citacao" | kind: citation, pillar: P01, nucleus: N04 |

### P02 Model
| User says | N07 maps to |
|-----------|-------------|
| "create agent" / "criar agente" | kind: agent, pillar: P02, nucleus: N03 |
| "agent deployment spec" / "spec de deploy" | kind: agent_card, pillar: P08, nucleus: N03 |
| "add a new LLM provider" / "adicionar provedor" | kind: model_provider, pillar: P02, nucleus: N05 |
| "model fallback chain" / "cadeia de fallback" | kind: fallback_chain, pillar: P02, nucleus: N03 |

### P03 Prompt
| User says | N07 maps to |
|-----------|-------------|
| "write a prompt template" / "criar template de prompt" | kind: prompt_template, pillar: P03, nucleus: N03 |
| "system prompt" / "prompt de sistema" | kind: system_prompt, pillar: P03, nucleus: N03 |
| "chain of prompts" / "cadeia de prompts" | kind: chain, pillar: P03, nucleus: N03 |
| "token budget" / "orcamento de tokens" | kind: context_window_config, pillar: P03, nucleus: N03 |
| "write a tagline" / "criar slogan" | kind: tagline, pillar: P03, nucleus: N02 |

### P04 Tools
| User says | N07 maps to |
|-----------|-------------|
| "MCP server" / "servidor MCP" | kind: mcp_server, pillar: P04, nucleus: N05 |
| "web scraper" / "scraper web" | kind: browser_tool, pillar: P04, nucleus: N05 |
| "API client" / "cliente de API" | kind: api_client, pillar: P04, nucleus: N05 |
| "webhook endpoint" / "endpoint webhook" | kind: webhook, pillar: P04, nucleus: N05 |
| "deep research" / "pesquisa profunda" | kind: research_pipeline, pillar: P04, nucleus: N01 |

### P05 Output
| User says | N07 maps to |
|-----------|-------------|
| "make me a landing page" / "criar landing page" | kind: landing_page, pillar: P05, builder: landing-page-builder |
| "format as JSON" / "formatar como JSON" | kind: formatter, pillar: P05, nucleus: N03 |
| "parse the output" / "extrair dados da saida" | kind: parser, pillar: P05, nucleus: N03 |

### P06 Schema
| User says | N07 maps to |
|-----------|-------------|
| "validate the input" / "validar entrada" | kind: input_schema, pillar: P06, nucleus: N03 |
| "define a custom type" / "definir tipo customizado" | kind: type_def, pillar: P06, nucleus: N03 |
| "integration contract" / "contrato de integracao" | kind: interface, pillar: P06, nucleus: N03 |

### P07 Evaluation
| User says | N07 maps to |
|-----------|-------------|
| "fix the tests" / "consertar os testes" | nucleus: N05, domain: operations, tools: cex_e2e_test.py |
| "benchmark this" / "benchmark disso" | kind: benchmark, pillar: P07, nucleus: N05 |
| "scoring criteria" / "criterios de avaliacao" | kind: scoring_rubric, pillar: P07, nucleus: N05 |
| "LLM as judge" / "LLM como juiz" | kind: llm_judge, pillar: P07, nucleus: N05 |

### P08 Architecture
| User says | N07 maps to |
|-----------|-------------|
| "architecture diagram" / "diagrama de arquitetura" | kind: diagram, pillar: P08, nucleus: N03 |
| "decision record" / "registro de decisao" | kind: decision_record, pillar: P08, nucleus: N03 |
| "naming convention" / "convencao de nomes" | kind: naming_rule, pillar: P08, nucleus: N03 |

### P09 Config
| User says | N07 maps to |
|-----------|-------------|
| "environment config" / "config de ambiente" | kind: env_config, pillar: P09, nucleus: N05 |
| "rate limits" / "limites de taxa" | kind: rate_limit_config, pillar: P09, nucleus: N05 |
| "manage secrets" / "gerenciar credenciais" | kind: secret_config, pillar: P09, nucleus: N05 |
| "feature toggle" / "flag de feature" | kind: feature_flag, pillar: P09, nucleus: N05 |

### P10 Memory
| User says | N07 maps to |
|-----------|-------------|
| "remember this entity" / "lembrar essa entidade" | kind: entity_memory, pillar: P10, nucleus: N04 |
| "build search index" / "criar indice de busca" | kind: knowledge_index, pillar: P10, nucleus: N04 |
| "compress memory" / "comprimir memoria" | kind: memory_summary, pillar: P10, nucleus: N04 |
| "cache prompts" / "cache de prompts" | kind: prompt_cache, pillar: P10, nucleus: N05 |

### P11 Feedback
| User says | N07 maps to |
|-----------|-------------|
| "quality gate" / "gate de qualidade" | kind: quality_gate, pillar: P11, nucleus: N03 |
| "auto-fix bugs" / "correcao automatica" | kind: bugloop, pillar: P11, nucleus: N05 |
| "safety guardrail" / "limite de seguranca" | kind: guardrail, pillar: P11, nucleus: N03 |
| "pricing strategy" / "estrategia de preco" | kind: content_monetization, pillar: P11, nucleus: N06 |

### P12 Orchestration
| User says | N07 maps to |
|-----------|-------------|
| "workflow" / "fluxo de trabalho" | kind: workflow, pillar: P12, nucleus: N03 |
| "launch all nuclei" / "lancar todos nuclei" | dispatch: grid, 6 nuclei, handoffs required |
| "schedule a task" / "agendar tarefa" | kind: schedule, pillar: P12, nucleus: N07 |
| "overnight improvement" / "melhoria noturna" | tool: overnight.ps1, mode: evolve, target: 9.0 |

### Operational (no specific kind)
| User says | N07 maps to |
|-----------|-------------|
| "research competitors" / "pesquisar concorrentes" | nucleus: N01, kind: knowledge_card, domain: competitive |
| "content for instagram" / "conteudo pro insta" | kind: schedule + prompt_template, pillar: P03+P12, nucleus: N02 |
| "optimize the system" / "otimizar o sistema" | kind: optimizer, pillar: P11, nucleus: N05 |

## Verb Resolution (PT + EN)

N07 maps user verbs to canonical actions. These inform which 8F functions to emphasize.

| PT Verb | EN Verb | Canonical Action | Primary 8F Function |
|---------|---------|-----------------|---------------------|
| criar, crie, cria | create, build, make | create | F6 PRODUCE |
| melhorar, melhore | improve, enhance, evolve | improve | F7 GOVERN |
| reconstruir, reconstroi | rebuild, recreate | rebuild | F2 BECOME + F6 PRODUCE |
| analisar, analise | analyze, review, audit | analyze | F3 INJECT + F4 REASON |
| validar, valide | validate, verify, check | validate | F7 GOVERN |
| documentar, documente | document, describe | document | F6 PRODUCE (knowledge_card) |
| integrar, integre | integrate, connect | integrate | F5 CALL |
| testar, teste | test, evaluate | test | F7 GOVERN (eval kinds) |
| implantar, implante | deploy, ship, release | deploy | F8 COLLABORATE |
| configurar, configure | configure, setup | configure | F1 CONSTRAIN (config kinds) |
| otimizar, otimize | optimize, tune | optimize | F7 GOVERN (optimizer) |
| auditar, audite | audit, inspect | audit | F3 INJECT + F7 GOVERN |
| agendar, agende | schedule, plan, time | schedule | F8 COLLABORATE (schedule) |
| monitorar, monitore | monitor, watch, observe | monitor | F5 CALL (trace_config) |

## 8F Pipeline Mastery

N07 must know every step and apply it automatically:

| Function | What it does | N07's role |
|----------|-------------|-----------|
| F1 CONSTRAIN | Resolve kind, pillar, schema | Select from kinds_meta.json |
| F2 BECOME | Load builder (13 components) | Include builder path in handoff |
| F3 INJECT | Assemble context (KCs, examples, brand, memory) | List artifact references in handoff |
| F4 REASON | Plan approach | GDP if subjective, autonomous if technical |
| F5 CALL | Use tools for enrichment | Specify which tools are relevant |
| F6 PRODUCE | Generate with full context | Ensure nucleus has agent card + references |
| F7 GOVERN | Quality gate | Require signal with quality score |
| F8 COLLABORATE | Save, compile, commit, signal | Specify signal + commit message format |

## 12 Pillars Mastery

| Pillar | Domain | Example kinds |
|--------|--------|--------------|
| P01 Knowledge | Storage, retrieval, KCs | knowledge_card, chunk_strategy, embedding_config |
| P02 Model | Agent definitions, providers | agent, model_provider, boot_config |
| P03 Prompt | Templates, actions, chains | prompt_template, action_prompt, chain |
| P04 Tools | External capabilities | cli_tool, browser_tool, mcp_server |
| P05 Output | Production artifacts | landing_page, output_template, diagram |
| P06 Schema | Data contracts | schema, validation_schema, input_schema |
| P07 Evaluation | Quality, scoring, testing | quality_gate, scoring_rubric, benchmark |
| P08 Architecture | System structure | agent_card, component_map, interface |
| P09 Config | Runtime settings | env_config, path_config, secret_config |
| P10 Memory | State, context, indexing | knowledge_index, memory_scope, entity_memory |
| P11 Feedback | Learning, correction | bugloop, learning_record, regression_check |
| P12 Orchestration | Workflows, dispatch | workflow, dispatch_rule, schedule |

## Example Transmutation

User input: "quero melhorar os artefatos que estao ruins"

N07 resolves intent (industry: intent resolution):
- Intent: improve low-quality artifacts
- Map: cex_evolve.py sweep (tool), quality < 9.0 (threshold)
- Resolve: heuristic first (free), agent for stubborn (budget)
- Restate: "Evolve 1302 artifacts below 9.0 using heuristic pass then agent mode"
- Execute: overnight_h1.cmd or direct cex_evolve.py dispatch

User NEVER needs to know "cex_evolve.py" or "heuristic mode" or "quality threshold". User says what they want. N07 knows the system.

## Terminology Enforcement (MANDATORY)

Every N07 output — chat, handoff, artifact, commit message — uses industry terms.
Source of truth: `_docs/specs/spec_metaphor_dictionary.md` (Industry term column).

When user uses a metaphor:
1. Accept it (don't interrupt flow)
2. Respond using the industry term
3. If first time: add one-line teaching in parentheses
4. If already taught: just use the term, no explanation

Track taught terms in: `N07_admin/memory/user_directive_technical_authority.md`

## N07 Self-Check Before Every Action

Before executing anything, verify:
- [ ] Did I kill idle processes? (lesson #1)
- [ ] Did I map user intent to CEX taxonomy? (this rule)
- [ ] Does the handoff include artifact references? (dispatch-depth rule)
- [ ] Is the output format structured data? (core purpose)
- [ ] Am I using industry terms in ALL output? (terminology enforcement)
- [ ] Did I reason through 8F at depth, not surface? (1M token leverage)
- [ ] Did I teach when I corrected? (didactic protocol)
