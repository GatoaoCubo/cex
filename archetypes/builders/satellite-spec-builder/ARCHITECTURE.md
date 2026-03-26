---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of satellite_spec in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: satellite_spec in the CEX

## Boundary
satellite_spec EH: especificacao completa de um satelite autonomo (role, model, MCPs, boot, constraints, scaling).

satellite_spec NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| agent (P02) | agent DEFINE identidade individual. satellite_spec ESPECIFICA o satelite inteiro. | P02 agent |
| boot_config (P02) | boot_config CONFIGURA init por provider. satellite_spec DEFINE a arquitetura. | P02 boot_config |
| pattern (P08) | pattern DOCUMENTA design reutilizavel. satellite_spec INSTANCIA um satelite concreto. | P08 pattern |
| law (P08) | law GOVERNA com regra inviolavel. satellite_spec DESCREVE um componente. | P08 law |
| diagram (P08) | diagram VISUALIZA arquitetura. satellite_spec ESPECIFICA componente. | P08 diagram |
| component_map (P08) | component_map MAPEIA conexoes entre componentes. satellite_spec DEFINE um componente. | P08 component_map |
| spawn_config (P12) | spawn_config PARAMETRIZA o lancamento runtime. satellite_spec DEFINE o que eh lancado. | P12 spawn_config |
| dispatch_rule (P12) | dispatch_rule ROTEIA uma keyword. satellite_spec CONTEM todas as dispatch rules do satelite. | P12 dispatch_rule |

Regra: "qual o role, model, tools e constraints deste satelite?" -> satellite_spec.

## Position in Architecture Flow

```text
system design -> [satellite_spec] defines satellite -> boot_config inits -> spawn_config launches -> signal monitors
                        |
                  role + model + MCPs + constraints
```

satellite_spec is the BLUEPRINT LAYER — defines what a satellite IS before it runs.

## Dependency Graph

```text
satellite_spec <--instantiated_by-- spawn_config (P12) — spawn reads spec to launch
satellite_spec <--constrained_by-- law (P08) — laws apply to all satellites
satellite_spec --receives-- component_map (P08) — architecture context informs spec
satellite_spec --produces_for--> boot_config (P02) — boot_config implements spec's init
satellite_spec --produces_for--> dispatch_rule (P12) — dispatch derives from spec's keywords
satellite_spec --independent-- knowledge_card, signal, quality_gate
```

## Fractal Position
Pillar: P08 (Architecture — how the system SCALES)
Function: BECOME (defines what a satellite IS)
Scale: L0 (spec layer — satellite_spec is the primary P08 architecture artifact)
satellite_spec is the most complex P08 kind — it bridges identity (P02) with orchestration (P12).
