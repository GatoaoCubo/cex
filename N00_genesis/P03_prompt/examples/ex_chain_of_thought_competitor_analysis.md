---
id: p03_cot_competitor_analysis
kind: chain_of_thought
pillar: P03
title: Chain-of-Thought Competitor Analysis with Metacognitive Stages
reasoning_type: metacognitive_5stage
quality: 9.2
updated: "2026-04-07"
domain: "prompt engineering"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.92
tldr: "Defines chain of thought for chain-of-thought competitor analysis with metacognitive stages, with validation gates and integration points."
related:
  - p10_lr_e2e_eval_builder
  - bld_instruction_e2e_eval
  - bld_instruction_research_pipeline
---

# Chain-of-Thought: Competitor Analysis

## Task
Analisar um concorrente direto no marketplace e recomendar estrategia de diferenciacao. O modelo deve raciocinar explicitamente por 5 estagios metacognitivos antes de produzir a resposta final.

## Reasoning Cue
Antes de responder, passe por EXATAMENTE 5 estagios de raciocinio. Cada estagio deve ser explicito e rotulado. NAO pule estagios. NAO combine estagios. O raciocinio deve ser visivel para auditoria.

### Metacognitive 5-Stage Protocol (KC_builder_agent_024)

**Stage 1 — UNDERSTAND**: Decomponha o problema
```text
<understand>
O que sei sobre o concorrente: [fatos concretos]
O que NAO sei e preciso inferir: [gaps]
Qual o objetivo real do usuario: [goal reformulado]
Restricoes: [budget, timeline, mercado]
</understand>
```

**Stage 2 — PLAN**: Defina abordagem
```text
<plan>
Abordagem escolhida: [metodo]
Metricas que vou analisar: [lista]
Fontes de evidencia: [dados disponiveis]
Riscos da minha analise: [vieses possiveis]
</plan>
```

**Stage 3 — MONITOR**: Execute com checkpoints
```text
<monitor>
Checkpoint 1 - Posicionamento: [analise de preco, publico, proposta de valor]
Checkpoint 2 - Forcas/Fraquezas: [SWOT resumido]
Checkpoint 3 - Gaps exploraveis: [oportunidades concretas]
Minha confianca ate aqui: [0.0-1.0] — se < 0.6, revisitar PLAN
</monitor>
```

**Stage 4 — EVALUATE**: Valide conclusoes
```text
<evaluate>
Conclusao principal: [1 frase]
Evidencias a favor: [lista]
Evidencias contra: [lista]
Confianca final: [0.0-1.0]
Vieses identificados: [confirmation bias, recency bias, etc.]
</evaluate>
```

**Stage 5 — REFLECT**: Meta-avaliacao
```text
<reflect>
Qualidade do meu raciocinio: [auto-score 1-10]
O que faria diferente: [melhorias]
Premissa mais fragil: [qual suposicao pode estar errada]
</reflect>
```

## Format
```text
# Competitor Analysis: {{competitor_name}}

## Reasoning Trace
[5 estagios completos com tags XML]

## Final Answer
### Perfil do Concorrente
1. Posicionamento: [resumo]
2. Publico-alvo: [segmento]
3. Faixa de preco: [range]
4. Pontos fortes: [top 3]
5. Pontos fracos: [top 3]

### Estrategia Recomendada
1. [Acao 1 — curto prazo (1-2 semanas)]
2. [Acao 2 — medio prazo (1-2 meses)]
3. [Acao 3 — longo prazo (3-6 meses)]

### Metricas de Sucesso
1. [KPI 1]: [meta]
2. [KPI 2]: [meta]

### Confianca
Score: [0.0-1.0] | Premissa mais fragil: [qual]
```

## Answer Extract
A resposta final (apos "## Final Answer") deve ser autonoma — legivel sem os estagios de raciocinio. O trace existe para auditoria e debug, nao para o consumidor final da analise.

## Research Base
1. Metacognitive 5-stage CoT: +26.9% task performance (KC_builder_agent_024)
2. Separar reasoning de answer_extract previne "reasoning leak" na resposta final
3. XML tags permitem parsing automatico dos estagios

## Properties

| Property | Value |
|----------|-------|
| Kind | `chain_of_thought` |
| Pillar | P03 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_e2e_eval_builder]] | downstream | 0.19 |
| [[bld_instruction_e2e_eval]] | related | 0.16 |
| [[bld_instruction_research_pipeline]] | related | 0.15 |
