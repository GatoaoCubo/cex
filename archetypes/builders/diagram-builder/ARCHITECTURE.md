---
id: diagram-builder-architecture
kind: architecture
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — ARCHITECTURE

## Boundary Definition

diagram EH: representacao visual de arquitetura — mostra componentes, conexoes, e camadas em formato grafico (ASCII ou Mermaid). Responde: "como este sistema se parece visualmente?"

## diagram NAO EH

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| component_map (P08) | component_map INVENTARIA dados estruturados. diagram VISUALIZA. | P08 component_map |
| pattern (P08) | pattern PRESCREVE solucao. diagram MOSTRA estrutura. | P08 pattern |
| law (P08) | law GOVERNA comportamento. diagram ILUSTRA arquitetura. | P08 law |
| satellite_spec (P08) | satellite_spec DEFINE um componente. diagram MOSTRA sistema. | P08 satellite_spec |
| dag (P12) | dag define ORDEM de execucao. diagram mostra ESTRUTURA visual. | P12 dag |
| workflow (P12) | workflow EXECUTA sequencia. diagram REPRESENTA visualmente. | P12 workflow |

## Decision Rule

"Como este sistema se parece visualmente?" -> diagram.
"Quais partes existem e quais sao seus atributos?" -> component_map.
"Qual solucao reutilizavel resolver este problema?" -> pattern.
"O que e obrigatorio neste dominio?" -> law.

## Position in Documentation Flow

```text
[component_map] --provides data--> [diagram] --communicates--> [documentation]
                                        |
                    [pattern] --may be illustrated by--> [diagram]
                                        |
                    [brain_index] <--stores-- [diagram]
```

## Dependency Graph

```text
diagram <--data_from-- component_map (P08)
diagram <--illustrates-- pattern (P08)
diagram <--illustrates-- law (P08)
diagram --produces_for--> documentation (external)
diagram <--queried_by-- brain_query (BM25 + FAISS)
diagram --independent-- signal
diagram --independent-- connector
diagram --independent-- quality_gate
diagram --independent-- scoring_rubric
diagram --referenced_by-- satellite_spec (P08)
diagram --referenced_by-- law-builder (P08)
```

## Fractal Position

| Attribute | Value |
|-----------|-------|
| Pillar | P08 — Architecture (how the system SCALES) |
| llm_function | INJECT — provides visual knowledge |
| Scale | L0 — content artifact |
| Layer | content |
| core | false |

diagram is the VISUAL kind of P08. While pattern prescribes and component_map inventories, diagram SHOWS.

## Sibling Kinds in P08

| Sibling | Role | Relationship to diagram |
|---------|------|------------------------|
| component_map | Structured inventory | Provides data to visualize |
| pattern | Reusable solution | May be illustrated by diagram |
| law | Operational mandate | Enforcement flow may be diagrammed |
| satellite_spec | Component definition | May include reference to diagram |
