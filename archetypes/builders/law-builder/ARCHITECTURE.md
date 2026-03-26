---
id: law-builder-architecture
kind: architecture_doc
pillar: P08
parent: law-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [architecture, law-builder, boundary, dependency, P08]
---

# law-builder — ARCHITECTURE

## Boundary

law EH: regra operacional inviolavel do sistema — define o que DEVE acontecer, com enforcement explicito e consequencias documentadas.

## law NAO EH

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| instruction (P03) | instruction GUIA com flexibilidade; violacao gera correcao, nao consequencia. law MANDA sem excecao. | P03 instruction |
| guardrail (P11) | guardrail RESTRINGE por seguranca (previne dano). law GOVERNA operacoes (garante consistencia). | P11 guardrail |
| axiom (P10) | axiom AFIRMA verdade abstrata permanente ("verdade existe"). law IMPOE regra operacional concreta. | P10 axiom |
| lifecycle_rule (P11) | lifecycle_rule GERENCIA transicoes de estado. law GOVERNA comportamento continuo. | P11 lifecycle_rule |
| pattern (P08) | pattern RECOMENDA solucao reutilizavel. law MANDA obediencia sem opcao. | P08 pattern |
| diagram (P08) | diagram VISUALIZA estrutura. law CONSTRANGE comportamento. | P08 diagram |
| component_map (P08) | component_map INVENTARIA partes do sistema. law GOVERNA como partes operam. | P08 component_map |
| satellite_spec (P08) | satellite_spec DEFINE capacidades de um componente. law GOVERNA o sistema inteiro. | P08 satellite_spec |

Regra de decisao: "que regra operacional DEVE ser seguida sem excecao e tem consequencia documentada?" -> law.

## Position in Governance Flow

```text
[pattern] proves solution --> [law] codifies mandate --> [guardrail] enforces safety
                                       |
                              [quality_gate] validates compliance
                                       |
                              [brain_index] --> [system_prompt] --> [agent obeys]
```

law is GOVERNANCE LAYER. Injected into system behavior as mandatory constraints that all agents internalize.

## Dependency Graph

```text
pattern (P08)        --informed_by--> law
learning_record (P10) --informed_by--> law
law                  --enforced_by--> quality_gate (P11)
law                  --injected_in--> system_prompt (P03)
law                  --referenced_by--> satellite_spec (P08)
law                  --referenced_by--> diagram (P08)
law                  --independent-- component_map (P08)
law                  --independent-- connector
law                  --independent-- signal
```

Explanations:
- `pattern --informed_by--> law`: proven patterns may be elevated to mandatory laws
- `learning_record --informed_by--> law`: repeated failures documented in learning records prompt new laws
- `law --enforced_by--> quality_gate`: gates check artifact compliance with laws (e.g., H05 enforces Law 5)
- `law --injected_in--> system_prompt`: agents internalize laws as behavioral constraints
- `law --referenced_by--> satellite_spec`: specs list which laws govern each satellite

## Fractal Position

```
Pillar: P08 (Architecture — how the system SCALES and CONSTRAINS)
Function: CONSTRAIN (imposes inviolable operational rules on all actors)
Scale: L0 (governance artifact — system-wide mandatory behavioral constraint)
Layer: governance
```

P08 kind hierarchy by function:
| Kind | Function | Mandates? |
|------|----------|-----------|
| law | CONSTRAIN | YES — inviolable |
| pattern | RECOMMEND | NO — reusable solution |
| diagram | VISUALIZE | NO — structural representation |
| component_map | INVENTORY | NO — parts catalog |
| satellite_spec | DEFINE | NO — component definition |

law is the GOVERNANCE kind of P08 — while pattern recommends and diagram visualizes, law mandates.

## Evolution Path

```text
observed_failure --> learning_record (P10)
                          |
                          v
               pattern (P08) [if solution found]
                          |
                          v
                  law (P08) [if mandate needed]
                          |
                          v
               quality_gate (P11) [enforcement]
```

Laws typically evolve from: (1) repeated failures documented in learning records, (2) proven patterns that warrant system-wide mandate, or (3) explicit governance decisions from operators.
