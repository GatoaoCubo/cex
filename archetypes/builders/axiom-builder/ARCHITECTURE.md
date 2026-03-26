---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of axiom in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: axiom in the CEX

## Boundary
axiom EH: regra fundamental imutavel — verdade permanente que define identidade do sistema.

axiom NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| law (P08) | law GOVERNA operacao e pode evoluir. axiom DEFINE verdade permanente. | P08 law |
| guardrail (P11) | guardrail RESTRINGE comportamento. axiom DECLARA verdade. | P11 guardrail |
| lifecycle_rule (P11) | lifecycle_rule GERENCIA ciclo de vida. axiom eh atemporal. | P11 lifecycle_rule |
| learning_record (P10) | learning EVOLUI com experiencia. axiom nunca muda. | P10 learning_record |
| instruction (P03) | instruction EXECUTA passos. axiom DECLARA fato. | P03 instruction |

Regra: "qual a verdade permanente e imutavel deste dominio?" -> axiom.

## Position in Memory Flow

```text
[System Design] -> [axiom] defines truth -> [law] operationalizes -> [guardrail] restricts
                       |
              [learning_record] validates over time
                       |
              [brain_index] -> [prompt injection] -> [agent behavior]
```

axiom is CONTENT LAYER. Injected into prompts as foundational context.
It constrains laws, informs guardrails, and anchors learning records.

## Dependency Graph

```text
axiom <--constrained_by-- nothing (axioms are foundational)
axiom --produces_for--> law (P08) — laws operationalize axioms
axiom --produces_for--> guardrail (P11) — guardrails enforce axiom boundaries
axiom --produces_for--> learning_record (P10) — learning validates axioms
axiom <--queried_by-- brain_query (BM25 + FAISS)
axiom <--injected_in-- system_prompt (P03) via IHP
axiom --independent-- signal, workflow, skill, connector
```

## Fractal Position
Pillar: P10 (Memory — what the system REMEMBERS as permanent truth)
Function: INJECT (provides foundational constraints to other LPs)
Scale: L0 (content artifact — the deepest layer of system identity)
axiom is the only P10 kind that is truly immutable — all others evolve.
