---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of interface in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: interface in the CEX

## Boundary
interface EH: contrato bilateral de integracao entre agentes, definindo methods com input/output tipados.

interface NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| input_schema (P06) | input_schema define SHAPE de entrada unilateral. interface define CONTRATO bilateral. | P06 input_schema |
| signal (P12) | signal reporta EVENTO runtime. interface define o que PODE acontecer. | P12 signal |
| connector (P04) | connector IMPLEMENTA comunicacao. interface ESPECIFICA o contrato. | P04 connector |
| validation_schema (P06) | validation_schema eh aplicado silenciosamente. interface eh ACORDO explicito. | P06 validation_schema |
| router (P02) | router decide PARA ONDE rotear. interface define COMO comunicar. | P02 router |

Regra: "qual o contrato formal entre estes dois agentes?" -> interface.

## Position in Integration Flow

```text
agent A needs data -> [interface] defines contract -> agent B implements -> [signal] confirms execution
                          |
                    methods: input/output typed
```

interface is a DESIGN-TIME artifact. It defines what CAN happen between two agents.

## Dependency Graph

```text
interface <--implements-- connector (P04, runtime adapter)
interface <--validates-- validator (P06, checks compliance)
interface <--references-- system_prompt (P03, mentions available methods)
interface --consumes--> input_schema (P06, for method input shapes)
interface --independent-- signal, dispatch_rule, quality_gate
```

## Fractal Position
Pillar: P06 (Schema — CONTRACTS and validation)
Function: CONSTRAIN (define integration boundaries)
Scale: L0 (spec layer — interfaces define how agents communicate before runtime)
Interfaces are the bilateral contract kind in P06 — complementing unilateral input_schema.
