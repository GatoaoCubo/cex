---
id: kc_pillar_brief_p03_prompt_pt
kind: knowledge_card
pillar: P01
title: "P03 Prompt — Prompts Sao Programas (21 kinds, 3 camadas)"
version: 1.1.0
created: "2026-04-22"
updated: "2026-04-22"
author: n04_knowledge
quality: 7.8
language: pt-br
domain: pillar_architecture
tier: mechanic
tags: [p03, prompt-engineering, system-prompt, chain, reasoning-strategy, knowledge-card]
tldr: "P03 tem 21 kinds cobrindo templates, chains, CoT/ToT/ReAct e context_window_config; prompt_compiler resolve 284 patterns para {kind,pillar,nucleus,verb}."
when_to_use: "Ao engenheirar prompts, construir chains multi-passo ou configurar janelas de contexto em qualquer runtime LLM."
keywords: [prompt-engineering, chain, system-prompt, prompt-compiler, reasoning]
long_tails:
  - Como construir chains de prompts multi-passo no CEXAI
  - Diferenca entre system_prompt e context_file no P03
axioms:
  - SEMPRE separe identidade (system_prompt) de tarefa (action_prompt) e restricoes (constraint_spec)
  - NUNCA envie um prompt complexo sem estrategia de raciocinio explicita (CoT/ToT/ReAct)
  - SEMPRE versione prompts que funcionam; descarte nada que gere saida excelente
  - NUNCA empilhe contexto irrelevante; cada token compete pela atencao do modelo
linked_artifacts:
  primary: null
  related: [kc_pillar_brief_p03_prompt_en, kc_pillar_brief_p02_model_pt]
density_score: 0.91
data_source: "N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md"
source_concepts: [kc_lens_index, mentor_context, p03_pc_cex_universal]
---

# P03 Prompt — Prompts Sao Programas

## Quick Reference

```yaml
topic: P03_prompt_pillar
scope: 21 kinds cobrindo toda a camada de linguagem LLM
owner: n04_knowledge
criticality: high
```

## Os 21 Kinds do P03

| Camada | Kind | Funcao |
|--------|------|--------|
| Identidade | `system_prompt` | Quem a IA e nesta sessao (persona, regras) |
| Identidade | `context_file` | Instrucoes permanentes de workspace |
| Identidade | `constraint_spec` | O que NAO fazer (espaco negativo) |
| Template | `prompt_template` | Prompt salvo com variaveis `[PARA PREENCHER]` |
| Template | `action_prompt` | Tarefa especifica de cada invocacao |
| Template | `prompt_version` | Versao congelada do melhor prompt |
| Template | `instruction` | Guia procedural referenciado por includes |
| Orquestracao | `chain` | Sequencia multi-passo; saida A -> entrada B |
| Orquestracao | `planning_strategy` | Como a IA planeja antes de agir |
| Orquestracao | `prompt_compiler` | Mapeia 284 patterns para `{kind,pillar,nucleus,verb}` |
| Orquestracao | `multimodal_prompt` | Prompts cross-modal (texto+imagem+audio) |
| Raciocinio | `reasoning_strategy` | CoT, ToT, ReAct, self-consistency, reflexion |
| Raciocinio | `reasoning_trace` | Registro auditavel do raciocinio passo a passo |
| Raciocinio | `prompt_technique` | Tecnicas nomeadas (few-shot, role, self-ask) |
| Raciocinio | `prompt_optimizer` | Analise sistematica de fraquezas de prompt |
| Config | `context_window_config` | Particiona orcamento de tokens entre fontes |
| Cross | `tagline`+`webinar_script`+`sales_playbook`+... | 5 kinds de linguagem de marca/vendas |

## Estrategias de Raciocinio

| Estrategia | Quando Usar | Ganho Tipico |
|------------|-------------|--------------|
| CoT (chain-of-thought) | Qualquer pergunta analitica complexa | +20-40% precisao |
| ToT (tree-of-thought) | Decisoes com multiplos caminhos validos | Reduz vieses de caminho unico |
| ReAct (reason+act) | Agentes com ferramentas, fluxos multi-etapa | Menos alucinacoes em acoes |
| Self-consistency | Perguntas factuais que exigem alta confianca | Convergencia por votacao |
| Few-shot | Tarefas sensiveis a formato/tom/estilo | Supera instrucoes descritivas |

## P03 no Pipeline 8F

| Estagio 8F | Artefatos P03 |
|------------|---------------|
| F1 CONSTRAIN | `prompt_compiler` + `constraint_spec` + `context_window_config` |
| F2 BECOME | `system_prompt` (identidade) + `context_file` (workspace) |
| F3 INJECT | `action_prompt` + `prompt_technique` + `instruction` |
| F4 REASON | `reasoning_strategy` + `planning_strategy` |
| F5 CALL | `chain` (sequencia de prompts multi-passo) |
| F6 PRODUCE | `prompt_template` hidratado com variaveis |
| F7 GOVERN | `prompt_version` + `prompt_optimizer` |
| F8 COLLABORATE | `reasoning_trace` (registro auditavel) |

## Padroes-Chave

- **3 camadas**: `system_prompt` (quem) + `action_prompt` (o que) + `constraint_spec` (limites)
- **chain vs workflow**: chain=sequencia de prompts; workflow (P12)=agentes+ferramentas
- **prompt_compiler**: unico artefato P03 que roda antes do 8F (em F1 CONSTRAIN)
- **context_window_config**: define slots (system 8K, inject 60K, history 100K, generate 32K)
- **Orçamento de tokens**: identidade > tarefa > dominio > historico; descartar pelo final

## Anti-Padroes

| Anti-Padrao | Correcao |
|-------------|----------|
| Amnesia de prompt | Versionar em `prompt_version` |
| Prompt monolito | Quebrar em `chain` de passos focados |
| Sem system_prompt | Escrever system_prompt por tarefa recorrente |
| Criatividade sem restricoes | Adicionar `constraint_spec` explicita |
| Empilhar contexto | Curar: incluir so o necessario |
| Raciocinio implicito | Especificar `reasoning_strategy` (CoT/ToT) |

## Vocabulario Tecnico

| Termo CEXAI | Equivalente Industria |
|-------------|----------------------|
| `prompt_compiler` | Intent resolver (DSPy, Amazon Lex) |
| `system_prompt` | System message (OpenAI, Anthropic) |
| `chain` | Sequential chain (LangChain, DSPy) |
| `reasoning_strategy` | CoT/ToT/ReAct (Wei, Yao, Shinn) |

## Golden Rules

- SEPARE system_prompt / action_prompt / constraint_spec em arquivos distintos
- APLIQUE CoT em toda decisao com "pense passo a passo"
- VERSIONE todo prompt que gere saida excelente com `prompt_version`
- CURATE contexto: so injete o que o modelo precisa para esta tarefa

## References

- Canonical: `p03_pc_cex_universal.md` (284 kinds, PT+EN)
- CoT: https://arxiv.org/abs/2201.11903
- ToT: https://arxiv.org/abs/2305.10601

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p03_prompt_en]] | translation | 1.00 |
| [[kc_pillar_brief_p02_model_pt]] | sibling | 0.85 |
| [[kc_pillar_brief_p04_tools_pt]] | sibling | 0.85 |
| [[p03_pc_cex_universal]] | upstream | 0.75 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.55 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[p01_kc_8f_pipeline]] | upstream | 0.42 |
| [[mentor_context]] | upstream | 0.38 |
| [[kc_pillar_brief_p01_knowledge_pt]] | sibling | 0.35 |
| [[kc_pillar_brief_p12_orchestration_pt]] | sibling | 0.32 |
