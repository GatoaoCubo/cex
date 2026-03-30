---
id: p03_cot_competitor_analysis
kind: chain_of_thought
pillar: P03
title: Chain-of-Thought Competitor Analysis with Metacognitive Stages
reasoning_type: metacognitive_5stage
quality: 9.0
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
- Posicionamento: [resumo]
- Publico-alvo: [segmento]
- Faixa de preco: [range]
- Pontos fortes: [top 3]
- Pontos fracos: [top 3]

### Estrategia Recomendada
1. [Acao 1 — curto prazo (1-2 semanas)]
2. [Acao 2 — medio prazo (1-2 meses)]
3. [Acao 3 — longo prazo (3-6 meses)]

### Metricas de Sucesso
- [KPI 1]: [meta]
- [KPI 2]: [meta]

### Confianca
Score: [0.0-1.0] | Premissa mais fragil: [qual]
```

## Answer Extract
A resposta final (apos "## Final Answer") deve ser autonoma — legivel sem os estagios de raciocinio. O trace existe para auditoria e debug, nao para o consumidor final da analise.

## Research Base
- Metacognitive 5-stage CoT: +26.9% task performance (KC_builder_agent_024)
- Separar reasoning de answer_extract previne "reasoning leak" na resposta final
- XML tags permitem parsing automatico dos estagios
