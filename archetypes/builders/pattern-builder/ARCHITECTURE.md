---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of pattern in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: pattern in the CEX

## Boundary
pattern EH: solucao reutilizavel nomeada para um problema recorrente de arquitetura — descreve problem, forces, solution, consequences.

pattern NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| law (P08) | law GOVERNA com regra inviolavel. pattern RECOMENDA solucao. | P08 law |
| workflow (P12) | workflow EXECUTA sequencia de steps. pattern DESCREVE abordagem. | P12 workflow |
| diagram (P08) | diagram VISUALIZA arquitetura. pattern EXPLICA solucao. | P08 diagram |
| component_map (P08) | component_map INVENTARIA conexoes. pattern RESOLVE problemas. | P08 component_map |
| satellite_spec (P08) | satellite_spec DEFINE um componente. pattern RESOLVE problema recorrente. | P08 satellite_spec |
| instruction (P03) | instruction DIZ como fazer. pattern EXPLICA por que funciona. | P03 instruction |

Regra: "qual a solucao recorrente nomeada para este problema?" -> pattern.

## Position in Architecture Flow

```text
[Recurring Problem] -> [pattern] documents solution -> [law] may codify -> [workflow] implements
                            |
               [satellite_spec] may reference pattern
                            |
               [brain_index] -> [prompt injection] -> [agent applies]
```

pattern is CONTENT LAYER. Injected into decision-making as architectural knowledge.
It informs laws, workflows, and satellite specifications with proven solutions.

## Dependency Graph

```text
pattern <--informed_by-- learning_record (P10) — patterns emerge from repeated learning
pattern --produces_for--> law (P08) — proven patterns may become mandatory rules
pattern --produces_for--> workflow (P12) — workflows implement pattern steps
pattern --produces_for--> satellite_spec (P08) — specs reference applicable patterns
pattern <--queried_by-- brain_query (BM25 + FAISS)
pattern <--injected_in-- system_prompt (P03) via IHP
pattern --independent-- signal, connector, scoring_rubric
```

## Fractal Position
Pillar: P08 (Architecture — how the system SCALES)
Function: INJECT (provides reusable solutions to architecture decisions)
Scale: L0 (content artifact — architectural knowledge distilled into named solutions)
pattern is the KNOWLEDGE kind of P08 — while law governs and satellite_spec defines, pattern teaches.
