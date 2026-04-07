# GLOSSARIO: 68 Tipos de Artefato x 12 LPs

---

## CORE (peso 1.0)

### P01 Knowledge (6 tipos)
- knowledge_card: fato atomico pesquisavel (max 2KB)
- rag_source: fonte externa indexavel
- glossary_entry: definicao de termo
- context_doc: contexto de dominio
- embedding_config: configuracao de embedding
- few_shot_example: exemplo pra prompt

### P02 Model (7 tipos)
- agent: definicao de agente (persona + capabilities)
- lens: perspectiva especializada sobre dominio
- boot_config: configuracao de inicializacao
- mental_model: mapa mental do agente
- model_card: spec do LLM usado
- router: regra de roteamento
- fallback_chain: sequencia de fallback

### P03 Prompt (5 tipos)
- system_prompt: prompt de sistema
- action_prompt: prompt de acao especifica
- prompt_template: template com {{vars}}
- instruction: instrucao operacional
- chain: sequencia de prompts

### P04 Tools (9 tipos)
- mcp_server: servidor MCP
- hook: pre/post processing hook
- skill: habilidade reutilizavel
- plugin: extensao plugavel
- client: cliente de API
- cli_tool: ferramenta CLI
- scraper: extrator de dados
- connector: conector de servico
- daemon: processo background

---

## QUALITY (peso 0.8)

### P05 Output (4 tipos)
- output_schema: formato de saida
- parser: extrator de dados de saida
- formatter: formatador de saida
- naming_rule: regra de nomenclatura

### P06 Schema (5 tipos)
- input_schema: contrato de entrada
- output_schema: contrato de saida
- type_def: definicao de tipo customizado
- validator: regra de validacao
- interface: contrato de integracao

### P07 Evals (6 tipos)
- unit_eval: teste unitario de agente
- smoke_eval: teste rapido de sanidade
- e2e_eval: teste end-to-end
- benchmark: medicao de performance
- golden_test: caso de teste referencia (9.5+)
- scoring_rubric: criterio de avaliacao

### P11 Feedback (5 tipos)
- quality_gate: barreira de qualidade
- bugloop: ciclo de correcao automatica
- lifecycle_rule: regra de ciclo de vida
- guardrail: restricao de seguranca
- optimizer: otimizador de processo

---

## SCALE (peso 0.6)

### P08 Architecture (5 tipos)
- agent_card: especificacao de agent_group
- pattern: pattern reutilizavel
- law: lei operacional
- diagram: diagrama de arquitetura
- component_map: mapa de componentes

### P09 Config (5 tipos)
- env_config: variaveis de ambiente
- path_config: caminhos do sistema
- permission: regra de permissao
- feature_flag: flag de feature
- runtime_rule: regra de runtime

### P10 Memory (5 tipos)
- mental_model: modelo mental persistente
- knowledge_index: indice de busca
- learning_record: registro de aprendizado
- session_state: estado de sessao
- axiom: regra fundamental

### P12 Orchestration (6 tipos)
- workflow: fluxo de trabalho
- dag: grafo aciclico de dependencias
- spawn_config: configuracao de spawn
- signal: sinal de comunicacao entre agentes
- handoff: instrucao de handoff
- dispatch_rule: regra de despacho

---

TOTAL: 68 tipos CORE fixos + _custom/ por LP
Promocao: usado 10x + quality > 8.0 = vira CORE

---
*GLOSSARIO v1.0 | 2026-03-22*