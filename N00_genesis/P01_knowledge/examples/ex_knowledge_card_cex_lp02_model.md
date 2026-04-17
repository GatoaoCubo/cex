---
id: p01_kc_cex_lp02_model
kind: knowledge_card
pillar: P01
title: "CEX LP02 Model — Quem a LLM Eh (9 Tipos de Identidade)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp02, model, become, agent, persona, identity, lens]
tldr: "P02 Model define identidade do LLM via 9 tipos — de agent a lens — usando funcao BECOME antes de qualquer input"
when_to_use: "Classificar artefatos de identidade ou entender como P02 configura quem o LLM eh"
keywords: [agent, mental-model, persona, boot-config, model-card, lens, agent-package]
long_tails:
  - "Quais tipos de identidade existem no CEX"
  - "Diferenca entre agent e persona no CEX"
axioms:
  - "SEMPRE executar BECOME antes de INJECT"
  - "NUNCA misturar identidade (P02) com conhecimento (P01)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_lp01_knowledge, p01_kc_cex_lp03_prompt]
density_score: 1.0
data_source: "https://arxiv.org/abs/2308.00352"
---

## Quick Reference

topic: LP02 Model | scope: 9 tipos de artefato | criticality: high
funcao_llm: BECOME | analogia: DNA + personalidade

## Conceitos Chave

- P02 responde: "quem eh esta entidade?"
- agent eh o tipo core (identidade completa + capabilities)
- Funcao dominante BECOME: identidade configurada no boot
- lens eh perspectiva cognitiva que colore toda percepcao
- mental_model mapeia routing, decisoes e vieses produtivos
- agent_package eh bundle portable de agente (LLM-agnostic)
- axiom eh principio imutavel da identidade profunda
- P02 define COMO P01 eh interpretado e P05 formatado
- boot_config inicializa por provider (modelo, temp, MCPs)
- model_card especifica LLM: pricing, context window, limites
- router traduz task em agent_group (regra de roteamento)
- fallback_chain sequencia modelos A -> B -> C com timeout
- Ordem boot: system_prompt -> mental_model -> persona -> agent
- P02 eh o LP mais diverso: 9 tipos para facetas de identidade
- Mesma task + lens diferente = output radicalmente diferente

## Fases

1. Definicao: escolher papel, dominio e perspectiva (lens)
2. Composicao: montar agent com persona + mental_model + tools
3. Boot: carregar boot_config + model_card (infra pre-requisito)
4. Ativacao: BECOME executa system_prompt -> mental_model -> agent
5. Operacao: identidade ativa constrange todos os outros LPs

## Regras de Ouro

- SEMPRE definir identidade ANTES de injetar contexto
- SEMPRE criar mental_model para agentes com 5+ tools
- NUNCA definir identidade no user prompt (volatil)
- NUNCA confundir quem SOU (P02) com o que SEI (P01)
- SEMPRE usar agent_package para agentes que migram entre LLMs

## Comparativo

| Tipo | Proposito | Tamanho | Core |
|------|-----------|---------|------|
| agent | Identidade completa + capabilities | <= 5120B | sim |
| lens | Perspectiva cognitiva especializada | <= 2048B | nao |
| mental_model | Mapa de routing e decisoes | <= 2048B | sim |
| boot_config | Inicializacao por provider | <= 2048B | nao |
| model_card | Spec do LLM (pricing, limites) | <= 2048B | nao |
| router | Regra task -> agent_group | <= 1024B | sim |
| fallback_chain | Sequencia fallback entre modelos | <= 512B | nao |
| agent_package | Bundle portable de agente | <= 4096B | sim |
| axiom | Principio fundamental imutavel | <= 3072B | sim |

## Flow

```
[boot_config + model_card]
          |
    [system_prompt]
          |
    [mental_model]
          |
      [persona]
          |
       [agent]  <-- BECOME completo
          |
  [lens colore percepcao]
          |
  [P01/P03/P04 operam sob identidade]
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- deepens: p01_kc_cex_function_become
- related: p01_kc_cex_lp01_knowledge


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
