---
id: self_audit_n01_codex_2026_04_11
kind: self_audit
title: N01 Intelligence Self-Audit
version: 1.0
quality: null
tags: [audit, self_review, n01, intelligence]
created: 2026-04-11
nucleus: n01
pillar: P07
---

## 1. Estado Atual
Varredura manual (excluindo `compiled/`) encontrou 65 arquivos `.md` ativos, superando os 53 citados no card (N01_intelligence/agent_card_n01.md:45). O único arquivo que ainda reprova cex_score é o README sem frontmatter (N01_intelligence/README.md:1); todos os demais trazem conteúdo especializado ≥9.0 ou `quality: null` aguardando atualização.

### 1.1 Artefatos por kind
| Kind | Count | Evidência |
|------|------:|----------|
| knowledge_card | 12 | `N01_intelligence/knowledge/kc_benchmark_tool_vs_llm.md:3` |
| output | 9 | `N01_intelligence/output/output_benchmark_report.md:3` |
| schema | 6 | `N01_intelligence/schemas/citation_format_contract.md:3` |
| agent | 3 | `N01_intelligence/agents/agent_competitor_tracker.md:3` |
| context_doc | 3 | `N01_intelligence/agent_card_n01.md:3` |
| tool_config | 3 | `N01_intelligence/tools/mcp_server_config_intelligence.md:3` |
| dispatch_rule | 2 | `N01_intelligence/orchestration/dispatch_rule_intelligence.md:3` |
| embedding_config | 2 | `N01_intelligence/knowledge/embedding_config_intelligence.md:3` |
| output_template | 2 | `N01_intelligence/output/output_monetization_research.md:3` |
| quality_gate | 2 | `N01_intelligence/feedback/quality_gate_intelligence.md:3` |
| rag_source | 2 | `N01_intelligence/knowledge/rag_source_intelligence.md:3` |
| scoring_rubric | 2 | `N01_intelligence/quality/p07_scoring_rubric_create_a_scoring_rubric_for_intelligence.md:3` |
| workflow | 2 | `N01_intelligence/orchestration/workflow_intelligence.md:3` |
| agent_card | 1 | `N01_intelligence/architecture/agent_card_intelligence.md:3` |
| benchmark | 1 | `N01_intelligence/quality/p07_benchmark_research_quality.md:3` |
| chain | 1 | `N01_intelligence/prompts/chain_kc_to_notebooklm.md:3` |
| checkpoint | 1 | `N01_intelligence/memory/checkpoint_intelligence.md:4` |
| cli_tool | 1 | `N01_intelligence/tools/research_pipeline_intelligence.md:3` |
| competitive_analysis | 1 | `N01_intelligence/output/output_competitive_landscape.md:3` |
| context-doc | 1 | `N01_intelligence/output/self_review_2026-04-02.md:3` |
| eval_dataset | 1 | `N01_intelligence/quality/p07_eval_dataset_research_outputs.md:3` |
| knowledge_index | 1 | `N01_intelligence/memory/knowledge_index_intelligence.md:3` |
| learning_record | 1 | `N01_intelligence/memory/learning_record_research_sessions.md:3` |
| prompt_template | 1 | `N01_intelligence/prompts/prompt_template_intelligence.md:3` |
| research_output | 1 | `N01_intelligence/output/output_content_factory_landscape.md:3` |
| self_audit | 1 | `N01_intelligence/reports/self_audit_2026_04_11.md:3` |
| system_prompt | 1 | `N01_intelligence/prompts/system_prompt_intelligence.md:3` |
| unknown | 1 | `N01_intelligence/README.md:1` |

### 1.2 Distribuição de qualidade
| Faixa | Qtde | Evidência |
|-------|-----:|----------|
| ≥9.0 definido | 43 | `N01_intelligence/output/output_competitive_landscape.md:5` |
| 8.0-8.9 | 0 | `N01_intelligence/output/output_market_snapshot.md:5` (nenhuma linha `quality: 8.x` encontrada na árvore) |
| <8.0 | 0 | `N01_intelligence/output/output_swot_analysis.md:5` (nenhuma linha `quality: 7.x` encontrada na árvore) |
| null | 22 | `N01_intelligence/knowledge/kc_token_optimization_map.md:10` |
| Sem frontmatter | 1 | `N01_intelligence/README.md:1` |

### 1.3 Maiores artefatos
| Artifact | Kind | Size (bytes) |
|----------|------|-------------:|
| `N01_intelligence/output/output_content_factory_landscape.md:3` | research_output | 35118 |
| `N01_intelligence/output/intent_resolution_benchmark.md:3` | knowledge_card | 33079 |
| `N01_intelligence/output/report_input_intent_resolution.md:3` | knowledge_card | 24720 |
| `N01_intelligence/reports/self_audit_2026_04_11.md:3` | self_audit | 19292 |
| `N01_intelligence/output/output_competitive_landscape.md:3` | competitive_analysis | 13458 |

### 1.4 Commits mais recentes
| Artifact | Commit (date) | Mensagem |
|----------|----------------|---------|
| `N01_intelligence/reports/self_audit_2026_04_11.md:3` | e53669a (2026-04-11T12:27:07-03:00) | [N01] self-audit report: state, gaps, wishlist (SELF_AUDIT mission) |
| `N01_intelligence/knowledge/kc_benchmark_tool_vs_llm.md:3` | 17bdf83 (2026-04-08T16:26:52-03:00) | [N01] research: token optimization audit -- 89 tools mapped, 3 KCs + benchmark |
| `N01_intelligence/knowledge/kc_token_optimization_map.md:3` | 17bdf83 (2026-04-08T16:26:52-03:00) | [N01] research: token optimization audit -- 89 tools mapped, 3 KCs + benchmark |
| `N01_intelligence/knowledge/kc_tool_first_patterns.md:3` | 17bdf83 (2026-04-08T16:26:52-03:00) | [N01] research: token optimization audit -- 89 tools mapped, 3 KCs + benchmark |
| `N01_intelligence/output/intent_resolution_benchmark.md:3` | 755cae0 (2026-04-08T14:09:18-03:00) | [N01] research: confidence scoring + clarification patterns + query decomposition + benchmark dataset (50 cases) |

### 1.5 Cobertura P01 (kinds prioritários)
| Kind P01 | Instâncias | Cobertura | Evidência / Observação |
|----------|-----------:|-----------|------------------------|
| knowledge_card | 12 | Sim | `N01_intelligence/knowledge/kc_benchmark_tool_vs_llm.md:3` |
| rag_source | 2 | Sim | `N01_intelligence/knowledge/rag_source_intelligence.md:3` |
| embedding_config | 2 | Sim | `N01_intelligence/knowledge/embedding_config_intelligence.md:3` |
| chunk_strategy | 0 | Não | `N01_intelligence/agent_card_n01.md:55` (ainda marcado como "Available, none built") |
| citation | 0 | Não | `N01_intelligence/schemas/citation_format_contract.md:3` (único item relacionado tem `kind: schema`) |
| glossary_entry | 0 | Não | `N01_intelligence/agent_card_n01.md:59` |
## 2. Regras e Compliance
As regras abaixo vêm de `.claude/rules/n01-intelligence.md`. Score 0-10 indica aderência observada.

| Regra | Score (0-10) | Evidência | Observação |
|-------|-------------:|----------|------------|
| Role = Research & Intelligence (.claude/rules/n01-intelligence.md:22) | 9 | `N01_intelligence/output/output_competitive_landscape.md:3` | Portfólio majoritariamente competitivo/mercado respeita o mandato. |
| CLI = Claude Code (.claude/rules/n01-intelligence.md:23) | 5 | `N01_intelligence/agent_card_n01.md:21` | Card ainda aponta exclusivamente para Claude, mas esta missão roda via Codex; documentação precisa refletir a exceção. |
| Domain = research/market analysis (.claude/rules/n01-intelligence.md:24) | 9 | `N01_intelligence/output/output_monetization_research.md:3` | Entregáveis continuam focados em pesquisa aplicada. |
| Artefatos devem viver em `N01_intelligence/` (.claude/rules/n01-intelligence.md:27) | 10 | `N01_intelligence/knowledge/knowledge_card_intelligence.md:1` | Não há arquivos fora do diretório do núcleo. |
| Especialização em pesquisa profunda (.claude/rules/n01-intelligence.md:28) | 9 | `N01_intelligence/orchestration/workflow_intelligence.md:21` | Workflow em 8 etapas segue ativo e descrito. |
| Outputs = briefs/análises (.claude/rules/n01-intelligence.md:29) | 9 | `N01_intelligence/output/output_research_brief.md:16` | Templates de briefing continuam no formato exigido. |
| Usar embedding_config + rag_source (.claude/rules/n01-intelligence.md:30) | 7 | `N01_intelligence/knowledge/embedding_config_intelligence.md:3` / `N01_intelligence/knowledge/rag_source_intelligence.md:3` | Configurações existem, porém falta `chunk_strategy` para fechar o pipeline RAG. |
| 8F obrigatório (.claude/rules/n01-intelligence.md:33) | 7 | `N01_intelligence/orchestration/workflow_intelligence.md:21` | Processo está documentado, mas outputs não registram o log F1-F8, dificultando auditoria. |
| Conteúdo precisa ser específico (.claude/rules/n01-intelligence.md:36) | 8 | `N01_intelligence/output/output_market_snapshot.md:15` | Entregáveis seguem densos; o único genérico é o README sem frontmatter. |
| `quality` deve ficar null (.claude/rules/n01-intelligence.md:37) | 2 | `N01_intelligence/output/output_competitive_landscape.md:5` / `N01_intelligence/knowledge/kc_token_optimization_map.md:10` | Metade do acervo mantém notas 9.x no frontmatter e outra metade permanece null: falta padronização. |
| Compilar após salvar (.claude/rules/n01-intelligence.md:38) | 9 | `N01_intelligence/compiled/output_competitive_landscape.yaml:1` | Compilados sincronizados; exceção é o README que não compila por falta de frontmatter. |

## 3. Lacunas (o que falta)
| Gap | Prioridade | Esforço estimado | Evidência |
|-----|-----------|------------------|----------|
| Sem `chunk_strategy` para RAG | Normal | 0,5 dia | `N01_intelligence/agent_card_n01.md:55` |
| Sem `embedder_provider` configurado | Normal | 0,5 dia | `N01_intelligence/agent_card_n01.md:56` |
| Sem `few_shot_example` para pesquisas | Baixa | 0,5 dia | `N01_intelligence/agent_card_n01.md:58` |
| Sem `glossary_entry` para terminologia | Baixa | 0,5 dia | `N01_intelligence/agent_card_n01.md:59` |
| Sem `retriever_config` | Normal | 0,5 dia | `N01_intelligence/agent_card_n01.md:61` |
| Sem `vector_store` documentado | Normal | 1 dia | `N01_intelligence/agent_card_n01.md:62` |
| Sem tool `retriever` (P04) | Normal | 1 dia | `N01_intelligence/agent_card_n01.md:77` |
| Sem `search_tool` dedicado | Normal | 1 dia | `N01_intelligence/agent_card_n01.md:78` |
| Sem `document_loader` | Normal | 1 dia | `N01_intelligence/agent_card_n01.md:79` |
| Ausência de artifacts `citation` (apenas schema) | Normal | 0,5 dia | `N01_intelligence/schemas/citation_format_contract.md:3` |
| Card ainda marca 0 benchmark/eval apesar dos arquivos existentes | Normal | 0,25 dia | `N01_intelligence/agent_card_n01.md:68` / `N01_intelligence/quality/p07_benchmark_research_quality.md:13` |
| Card reporta total 53 vs. inventário real 65 | Normal | 0,25 dia | `N01_intelligence/agent_card_n01.md:45` |

## 4. Correções necessárias (artefatos existentes)
| Issue | Impacto | Ação sugerida | Evidência |
|-------|---------|---------------|----------|
| README sem frontmatter | cex_score = 0 impede compilação | Adicionar YAML mínimo (`id`, `kind`, `quality: null`) e reexecutar cex_score | `N01_intelligence/README.md:1` |
| Agents ainda com `quality: null` | Falta sinal claro de revisão para sub-agentes críticos | Aplicar cex_score com `--apply` em `agent_competitor_tracker` e `agent_paper_reviewer` | `N01_intelligence/agents/agent_competitor_tracker.md:25` / `N01_intelligence/agents/agent_paper_reviewer.md:26` |
| Estudos de intent resolution sem nota | Benchmarks recentes não entram no gate automático | Atualizar `quality` em `intent_resolution_benchmark` e `report_input_intent_resolution` após revisão | `N01_intelligence/output/intent_resolution_benchmark.md:13` / `N01_intelligence/output/report_input_intent_resolution.md:13` |
| Tool configs sem nota | Configs MCP não passam por score histórico | Rodar cex_score `--apply` em `mcp_server`, `scraping` e `search` configs | `N01_intelligence/tools/mcp_server_config_intelligence.md:12` / `N01_intelligence/tools/scraping_config_intelligence.md:12` / `N01_intelligence/tools/search_config_intelligence.md:12` |
| Benchmark + eval_dataset com `quality: null` | P07 não comprova qualidade própria | Atualizar as notas após revisão cruzada | `N01_intelligence/quality/p07_benchmark_research_quality.md:13` / `N01_intelligence/quality/p07_eval_dataset_research_outputs.md:13` |
| Densidade real <0,85 em quatro outputs segundo cex_feedback | Metadados de densidade (1.0) divergem dos cálculos recentes | Reaferir e comprimir `output_competitive_landscape`, `output_content_factory_landscape`, `output_monetization_research`, `output_readme_comparison` para fechar a lacuna | `_docs/FEEDBACK_REPORT.md:203` / `_docs/FEEDBACK_REPORT.md:204` / `_docs/FEEDBACK_REPORT.md:2603` / `_docs/FEEDBACK_REPORT.md:2604` |

## 5. Wishlist de Ferramentas
### 5a Ferramentas existentes que continuarei usando
| Ferramenta | Uso em N01 | Fonte |
|------------|------------|-------|
| `cex_retriever.py` | Localiza artefatos análogos para cross-referenciar dados antes de cada brief. | `CLAUDE.md:117` |
| `cex_query.py` | Descobre rapidamente qual builder/kind deve ser acionado ao receber novos intents. | `CLAUDE.md:104` |
| `cex_token_budget.py` | Calcula orçamento de tokens para varreduras longas antes de abrir MCPs caros. | `CLAUDE.md:118` |
| `cex_memory_select.py` | Injeta memórias relevantes (aprendizados anteriores) em novos relatórios. | `CLAUDE.md:119` |
| `cex_doctor.py` | Verifica saúde estrutural após cada onda de pesquisa. | `CLAUDE.md:111` |

### 5b Ferramentas que deveriam existir
| Ferramenta proposta | Owner | Descrição | Evidência |
|---------------------|-------|-----------|----------|
| `cex_chunk_designer.py` | N05 | Gerar automaticamente `chunk_strategy` a partir de exemplos (tamanho, overlap, filtros) para alinhar RAG com embeddings existentes. | `N01_intelligence/agent_card_n01.md:55` |
| `cex_vector_guard.py` | N05 | Provisionar `retriever_config` + `vector_store` pareados (provider, índice, TTL) sem depender de edição manual. | `N01_intelligence/agent_card_n01.md:61` / `N01_intelligence/agent_card_n01.md:62` |
| `cex_citation_tracer.py` | N05 | Converter contratos de citação em artifacts vivos (listas de fontes + status) e validar links periodicamente. | `N01_intelligence/schemas/citation_format_contract.md:3` |
| `cex_quality_sync.py` | N05 | Consumir o output do `cex_score.py` e sincronizar `quality`/`density_score` automaticamente, evitando divergências. | `N01_intelligence/knowledge/kc_token_optimization_map.md:10` |

## 6. Dependências Cruzadas
| Eu preciso de | Outros precisam de mim |
|---------------|----------------------|
| N03 para implementar partes "build" do pipeline quando a requisição envolve código novo (N01_intelligence/orchestration/dispatch_rule_research_pipeline.md:61). | N03 consome especificações técnicas derivadas das pesquisas (`N01_intelligence/tools/research_pipeline_intelligence.md:87`). |
| N05 para empacotar/deployar crons de pesquisa após a fase de configuração (N01_intelligence/orchestration/dispatch_rule_research_pipeline.md:65). | N05 recebe cron configs e parâmetros gerados por N01 para execução operacional (N01_intelligence/orchestration/dispatch_rule_research_pipeline.md:74). |
| N02 para transformar achados em copy/design quando o escopo sai do domínio de pesquisa (N01_intelligence/prompts/system_prompt_intelligence.md:56). | N02 solicita briefs e consome os templates entregues (`N01_intelligence/output/output_research_brief.md:50`). |
| N06 para decisões de branding/comercial fora da alçada de pesquisa (N01_intelligence/prompts/system_prompt_intelligence.md:56). | N06 utiliza os pacotes de pricing/concorrência enviados após cada pesquisa (N01_intelligence/orchestration/dispatch_rule_research_pipeline.md:72). |
| N07 para despachar briefs claros e manter o grid (N01_intelligence/orchestration/dispatch_rule_research_pipeline.md:70). | N07 recebe relatórios completos/sinais quando o pipeline encerra (`N01_intelligence/tools/research_pipeline_intelligence.md:88`). |
