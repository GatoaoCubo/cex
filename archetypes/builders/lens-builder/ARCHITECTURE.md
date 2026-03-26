---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of lens in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: lens in the CEX

## Boundary
lens EH: perspectiva analitica declarativa aplicada como filtro a artefatos CEX.

lens NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| agent (P02) | agent TEM capabilities e tools. lens FILTRA sem executar. | P02 agent |
| mental_model (P02) | mental_model ROTEIA decisoes. lens INTERPRETA artefatos. | P02 mental_model |
| model_card (P02) | model_card DESCREVE um LLM. lens APLICA perspectiva a qualquer artefato. | P02 model_card |
| boot_config (P02) | boot_config INICIALIZA provider. lens NAO configura runtime. | P02 boot_config |
| router (P02) | router DESPACHA task para satellite. lens NAO roteia. | P02 router |
| fallback_chain (P02) | fallback_chain DEGRADA entre modelos. lens NAO faz fallback. | P02 fallback_chain |
| iso_package (P02) | iso_package EMPACOTA agente. lens NAO empacota. | P02 iso_package |
| axiom (P02) | axiom GOVERNA com regra imutavel. lens FILTRA com perspectiva. | P02 axiom |
| scoring_rubric (P07) | rubric PONTUA com dimensoes. lens FILTRA sem scoring. | P07 scoring_rubric |

Regra: "por qual perspectiva devo analisar este artefato?" -> lens.

## Position in Analysis Flow

```text
artifact produced -> [lens] filters/emphasizes -> analyst/agent interprets -> decision
                          |
                    perspective: focus + filters + bias
```

lens is the INTERPRETATION LAYER — shapes how artifacts are read.

## Dependency Graph

```text
lens <--consumed_by-- agent (P02) — agent applies lens to filter analysis
lens <--consumed_by-- scoring_rubric (P07) — rubric may use lens as dimension
lens --receives-- knowledge_card (P01) — domain knowledge informs perspective
lens --independent-- signal, workflow, validator, boot_config
```

## Fractal Position
Pillar: P02 (Model — who the entity IS)
Function: INJECT (provide analytical perspective into context)
Scale: L0 (content layer — lenses are lightweight perspective definitions)
Lenses are the only P02 content-layer kind — all others are spec or runtime.
