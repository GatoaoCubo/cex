---
id: p01_kc_cex_function_become
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function BECOME — Identity Configuration Before Processing"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, become, identity, system-prompt, persona]
tldr: "BECOME configura identidade do LLM (persona, regras, limites) via 6 tipos de artefato antes de qualquer input"
when_to_use: "Entender como LLMs assumem papeis e por que identidade precede contexto"
keywords: [become, identity, system-prompt, persona, agent-profile]
long_tails:
  - "Como configurar identidade de um agente LLM antes do processamento"
  - "Qual a diferenca entre BECOME e INJECT no CEX"
axioms:
  - "SEMPRE executar BECOME antes de INJECT"
  - "NUNCA misturar identidade (BECOME) com contexto (INJECT)"
linked_artifacts:
  primary: p01_kc_cex_function_inject
  related: [p01_kc_cex_function_reason]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_lp02_model
  - p01_kc_mental_model
  - p01_kc_agent
  - bld_architecture_agent
  - agent-builder
  - p01_kc_cex_llm_function_concept
  - bld_collaboration_agent
  - p01_kc_cex_pipeline_execution
  - bld_architecture_boot_config
  - p01_kc_boot_config
---

## Summary

BECOME configura a identidade, persona e papel do LLM antes de qualquer processamento. Define QUEM o modelo e para a sessao via system prompt, mental model e boot config. Mapeia ao "Role" do MetaGPT, "Agent Profile" do CrewAI e "InceptionPrompt" do CAMEL. Representa 8% dos tipos CEX (6 de 76).

## Spec

| Tipo | LP | Funcao | Detalhe |
|------|-----|--------|---------|
| agent | P02 | Identidade completa | Memoria, autonomia, tools, handoffs |
| mental_model | P02 | Mapa cognitivo | Dominios, vieses produtivos, restricoes |
| system_prompt | P03 | Papel persistente | Instrucao baseline pre-input |
| persona | P02 | Comunicacao | Tom, estilo, preferencias afetivas |
| boot_config | P02 | Inicializacao | Modelo, temperatura, max_tokens, MCPs |
| model_card | P02 | Especificacao LLM | Provider, versao, custos, limites |

Ordem de execucao: system_prompt → mental_model → persona → agent.
boot_config e model_card sao pre-requisitos de infraestrutura.
BECOME executa ANTES de qualquer INJECT — identidade precede contexto.

## Code

<!-- lang: python | purpose: agent identity via BECOME -->
```python
agent = Agent(
    name="shaka",
    instructions="Voce e um pesquisador de mercado brasileiro",
    model="sonnet",
    tools=[web_search, firecrawl],
    mental_model={"domain": "market_research", "bias": "quantitative"},
)
# system_prompt = instructions (BECOME)
# tools = CALL (configurado, nao executado)
# mental_model = restricoes cognitivas (BECOME)
```

## Patterns

| Trigger | Action |
|---------|--------|
| Agente precisa de identidade persistente | Usar tipo agent com memoria |
| Interacao direta com humanos | Adicionar persona ao agent |
| Decisao arquitetural de modelo | Criar model_card explicito |
| Multiplos agentes no sistema | Mental model por especialista |
| Parametros de boot especificos | Boot config com flags e MCPs |

## Anti-Patterns

- Definir identidade dentro do user prompt (volatil)
- Persona sem system prompt (tom sem papel = incoerente)
- Confundir BECOME com INJECT (quem SOU vs o que SEI)
- Agent com 20+ tools sem mental model (sobrecarga)
- Omitir boot_config (defaults implicitos = bugs)

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_function_inject
- related: p01_kc_cex_function_reason

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp02_model]] | sibling | 0.46 |
| [[p01_kc_mental_model]] | sibling | 0.36 |
| [[p01_kc_agent]] | sibling | 0.36 |
| [[bld_architecture_agent]] | downstream | 0.35 |
| [[agent-builder]] | downstream | 0.34 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.30 |
| [[bld_collaboration_agent]] | downstream | 0.30 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.29 |
| [[bld_architecture_boot_config]] | downstream | 0.28 |
| [[p01_kc_boot_config]] | sibling | 0.28 |
