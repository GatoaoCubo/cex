---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of learning_record in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: learning_record in the CEX

## Boundary
learning_record EH: registro persistente de experiencia — o que deu certo/errado, com score, contexto, e reproducibilidade.

learning_record NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| knowledge_card (P01) | KC DESTILA fato externo. LR CAPTURA experiencia interna. | P01 knowledge_card |
| session_state (P10) | session_state eh EFEMERO (morre com sessao). LR PERSISTE. | P10 session_state |
| mental_model (P10) | mental_model DECIDE routing. LR REGISTRA outcomes. | P10 mental_model |
| axiom (P10) | axiom eh IMUTAVEL. LR EVOLUI com cada experiencia. | P10 axiom |
| golden_test (P07) | golden_test VALIDA qualidade. LR DOCUMENTA o que aconteceu. | P07 golden_test |
| scoring_rubric (P07) | rubric DEFINE criterios. LR REGISTRA resultados. | P07 scoring_rubric |

Regra: "o que aprendemos com esta experiencia?" -> learning_record.

## Position in Memory Flow

```text
[Execution] -> [Signal complete] -> [learning_record] captures experience
                                           |
                              [memory_bridge] -> [routing intelligence]
                                           |
                              [brain_index] -> [future prompt hydration]
```

learning_record is CONTENT LAYER. Feeds routing intelligence and future decisions.
It transforms ephemeral execution outcomes into persistent organizational memory.

## Dependency Graph

```text
learning_record <--triggered_by-- signal (P12) — completion signals trigger capture
learning_record <--context_from-- session_state (P10) — session provides raw data
learning_record --produces_for--> mental_model (P10) — learning informs decision maps
learning_record --produces_for--> axiom (P10) — repeated learning may crystallize into axiom
learning_record <--queried_by-- brain_query (BM25 + FAISS)
learning_record <--validated_by-- scoring_rubric (P07)
learning_record --independent-- knowledge_card, boot_config, workflow
```

## Fractal Position
Pillar: P10 (Memory — what the system REMEMBERS from experience)
Function: INJECT (provides experiential context to routing and decisions)
Scale: L0 (content artifact — the evolving layer of system experience)
learning_record bridges ephemeral execution (P12 signals) with persistent memory (P10).
