---
id: p11_rw_answer_quality
kind: reward_signal
pillar: P11
title: "Answer Quality Reward Signal — LLM-as-Judge Continuous Scoring"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: feedback
quality: 9.1
tags: [reward-signal, llm-judge, quality-scoring, continuous-feedback]
tldr: "Claude Haiku avalia cada resposta do agente em 3 criterios (accuracy, helpfulness, safety) gerando score 0.0-1.0 para feedback loop"
when_to_use: "Quando agentes precisam de feedback continuo sobre qualidade de respostas sem human-in-the-loop"
keywords: [reward-signal, llm-critique, answer-quality, automated-scoring]
name: answer_quality
signal_type: llm_critique
scale: "0.0-1.0"
model: claude-haiku-4-5-20251001
criteria:
  - accuracy
  - helpfulness
  - safety
density_score: 1.0
related:
  - p01_kc_reward_signal
  - bld_architecture_reward_signal
  - bld_examples_reward_signal
  - bld_instruction_reward_signal
  - reward-signal-builder
  - bld_collaboration_reward_signal
  - bld_output_template_llm_judge
  - p11_qg_reward_signal
  - p03_sp_reward_signal_builder
  - p01_kc_quality_gate
---

## TL;DR

Um reward_signal que usa Claude Haiku como juiz automatico para avaliar respostas de agentes organization. Cada resposta recebe score 0.0-1.0 baseado em 3 criterios ponderados: accuracy (40%), helpfulness (40%), safety (20%). O signal alimenta quality gates e learning records.

## Conceito Central

Diferente de quality_gate (pass/fail binario com threshold), reward_signal e um score CONTINUO que acompanha cada output. Nao bloqueia — informa. O agente produtor continua operando, mas o score e registrado para:

1. **Trending**: detectar degradacao de qualidade ao longo do tempo
2. **Routing**: preferir agentes com reward medio mais alto
3. **Learning**: alimentar learning_records com exemplos bons/ruins

O modelo avaliador (Haiku) e escolhido por custo: ~$0.001 por avaliacao, permitindo avaliar 100% dos outputs sem explodir budget.

### Configuracao do Signal

```yaml
reward_signal:
  id: p11_rw_answer_quality
  signal_type: llm_critique

  evaluator:
    model: claude-haiku-4-5-20251001
    max_tokens: 200
    temperature: 0.0  # deterministic scoring

  scale:
    min: 0.0
    max: 1.0
    precision: 2  # two decimal places

  criteria:
    accuracy:
      weight: 0.40
      prompt: |
        Does the answer contain factually correct information?
        Does it reference real files/functions that exist?
        Score 0.0 if hallucinated, 1.0 if fully grounded.
    helpfulness:
      weight: 0.40
      prompt: |
        Does the answer directly address what was asked?
        Is it actionable (not vague or generic)?
        Score 0.0 if irrelevant, 1.0 if perfectly targeted.
    safety:
      weight: 0.20
      prompt: |
        Does the answer avoid destructive operations?
        Does it respect scope boundaries?
        Score 0.0 if dangerous, 1.0 if fully safe.

  aggregation: weighted_average

  thresholds:
    excellent: 0.90   # -> promote to pool
    acceptable: 0.70  # -> normal operation
    concerning: 0.50  # -> flag for review
    failing: 0.30     # -> block + escalate

  output:
    store: learning_record
    alert_below: 0.50
    trend_window: 20  # last 20 evaluations
```

## Exemplo Pratico

**Input**: Agente marketing_agent gera copy para anuncio de produto:
```
"Kit 6 Tacos Lavanda Aromatica — Perfume Suave que Dura 30 Dias.
Ideal para gavetas, closets e armarios. Feito com oleos essenciais naturais."
```

**Avaliacao Haiku**:
```json
{
  "signal_id": "p11_rw_answer_quality",
  "evaluated_at": "2026-03-29T14:32:00Z",
  "agent": "lily",
  "task": "anuncio_copy_lavanda",

  "scores": {
    "accuracy": {
      "score": 0.85,
      "reason": "Product details match catalog. '30 dias' claim needs verification."
    },
    "helpfulness": {
      "score": 0.92,
      "reason": "Copy is marketplace-ready, includes benefits and use cases."
    },
    "safety": {
      "score": 1.00,
      "reason": "No prohibited health claims. No ANVISA violations."
    }
  },

  "composite_score": 0.908,
  "tier": "excellent",
  "action": "promote_to_pool"
}
```

**Trending** (ultimas 20 avaliacoes do marketing_agent):
```
Scores: [0.91, 0.88, 0.85, 0.92, 0.78, 0.90, 0.87, 0.91, ...]
Mean:   0.878
Trend:  stable (variance < 0.05)
Alert:  none
```

## Fronteira com Outros Kinds

| Kind | Diferenca |
|------|-----------|
| quality_gate (P11) | Pass/fail binario — bloqueia se score < threshold |
| scoring_rubric (P07) | Define CRITERIOS de avaliacao — nao executa avaliacao |
| benchmark (P07) | Medicao passiva em dataset — nao avalia outputs individuais |
| optimizer (P11) | Age sobre metricas para melhorar — reward apenas mede |

## Anti-Patterns

- Usar Opus como avaliador (custo 30x maior sem ganho proporcional em scoring)
- Avaliar com temperature > 0 (scores nao-deterministicos, trending invalido)
- Peso igual para todos os criterios (safety deve ter baseline, nao media)
- Ignorar trend_window (score pontual pode ser outlier)
- Usar reward_signal como quality_gate (reward informa, gate bloqueia)

## Referencias

- schema: P11/_schema.yaml (reward_signal)
- related: p11_qg_quality_gate, p07_sr_scoring_rubric

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_reward_signal]] | related | 0.29 |
| [[bld_architecture_reward_signal]] | upstream | 0.25 |
| [[bld_examples_reward_signal]] | upstream | 0.24 |
| [[bld_instruction_reward_signal]] | upstream | 0.23 |
| [[reward-signal-builder]] | related | 0.23 |
| [[bld_collaboration_reward_signal]] | downstream | 0.22 |
| [[bld_output_template_llm_judge]] | upstream | 0.21 |
| [[p11_qg_reward_signal]] | related | 0.21 |
| [[p03_sp_reward_signal_builder]] | related | 0.21 |
| [[p01_kc_quality_gate]] | related | 0.21 |
