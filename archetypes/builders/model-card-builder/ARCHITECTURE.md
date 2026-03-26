---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of model_card in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: model_card in the CEX

## Boundary
model_card EH: spec tecnica de LLM (capacidades, custos, limites, status lifecycle).
model_card NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| boot_config | boot_config INICIALIZA (temp, MCPs). model_card DESCREVE. | P02 boot_config |
| agent | agent eh identidade completa. model_card eh spec de infra. | P02 agent |
| persona | persona define tom. model_card eh tecnico, sem personalidade. | P02 persona |
| benchmark | benchmark AVALIA performance. model_card DOCUMENTA specs declaradas. | P07 benchmark |
| router | router MAPEIA task→sat. model_card INFORMA, nao roteia. | P02 router |

Regra: "o que este LLM PODE e quanto CUSTA?" → model_card.

## Position in Boot Flow

```
[boot_config + model_card]   ← layer 0: infrastructure
          |
    [system_prompt]           ← layer 1: role
          |
    [mental_model]            ← layer 2: cognition
          |
       [agent]                ← layer 3: full identity (BECOME complete)
```

model_card is INFRASTRUCTURE. Loaded BEFORE any identity.
4 other P02 types depend on it: boot_config, router, fallback_chain, iso_package.

## Dependency Graph

```
model_card ←─used_by─── boot_config (selects model)
model_card ←─queried_by── router (cost/capability routing)
model_card ←─ordered_by── fallback_chain (A→B→C priority)
model_card ←─bundled_in── iso_package (deploy dependency)
model_card ──independent── persona, lens, axiom, mental_model
```

## Fractal Position
LP: P02 (Model — "who the entity IS")
Function: GOVERN (documents and constrains model selection)
Scale: L0 (infrastructure artifact, no agent identity)
The only P02 type that is purely DESCRIPTIVE (all others are prescriptive).
