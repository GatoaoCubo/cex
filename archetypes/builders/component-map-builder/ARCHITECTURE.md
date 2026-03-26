---
id: component-map-builder-architecture
kind: architecture
parent: component-map-builder
version: 1.0.0
---

# Architecture — component-map-builder

## Boundary

component_map EH: inventario estruturado de componentes e conexoes — dados tabulares de QUEM existe, O QUE faz, e COMO conecta.

### component_map NAO EH

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| diagram (P08) | diagram VISUALIZA graficamente. component_map INVENTARIA dados. | P08 diagram |
| satellite_spec (P08) | satellite_spec DEFINE um componente. component_map MAPEIA muitos. | P08 satellite_spec |
| pattern (P08) | pattern PRESCREVE solucao. component_map DESCREVE estrutura. | P08 pattern |
| law (P08) | law GOVERNA comportamento. component_map CATALOGA partes. | P08 law |
| dag (P12) | dag define ORDEM de execucao. component_map descreve ESTRUTURA estatica. | P12 dag |
| interface (P06) | interface DEFINE contrato bilateral. component_map CATALOGA todos os contratos. | P06 interface |

Regra: "quais sao as partes deste sistema e como conectam?" -> component_map.

## Position in Architecture Flow

```text
[survey] identifies components
         |
         v
[component_map] -- inventories structure --> [diagram] visualizes
         |
         +--> [satellite_spec] details individual component
         |
         +--> [brain_index] stores for retrieval
         |
         +--> [pattern] references component inventory
         |
         +--> [law] references governed components
```

component_map is SPEC LAYER (L0). Structured data that feeds diagrams and informs architecture decisions.

## Dependency Graph

```text
satellite_spec (P08)    -->  component_map      (fed_by: specs detail individual components)
component_map           -->  diagram (P08)       (produces_for: diagrams visualize map data)
component_map           -->  pattern (P08)       (produces_for: patterns may reference inventory)
component_map           -->  law (P08)           (produces_for: laws may reference governed components)
brain_query (BM25+FAISS) --> component_map      (queried_by: search retrieves maps)
component_map           --x  signal             (independent)
component_map           --x  connector          (independent)
component_map           --x  quality_gate       (independent)
component_map           --x  scoring_rubric     (independent)
```

## Fractal Position

```
Pillar:    P08 (Architecture — how the system SCALES)
Function:  INJECT (provides structured component knowledge)
Scale:     L0 (spec artifact — structured inventory of system parts)
```

component_map is the DATA kind of P08:
- diagram (P08) VISUALIZES
- pattern (P08) PRESCRIBES
- law (P08) GOVERNS
- satellite_spec (P08) DEFINES one
- component_map (P08) INVENTORIES many

## Builder Execution Flow

```text
Phase 1: SURVEY
  define_scope --> list_components --> map_owners --> map_connections
       |
       v [IF MCP]
  brain_query (check existing maps)
       |
       v
Phase 2: COMPOSE
  read_schema --> fill_frontmatter --> write_sections --> count_verify
       |
       v
Phase 3: VALIDATE
  hard_gates (9) --> soft_gates (10) --> orphan_check --> score
       |
       v [score < 8.0]
  revise (same pass)
       |
       v [score >= 8.0]
Phase 4: DELIVER
  write_yaml --> confirm_id_match --> report
```

## Quality Gate Architecture

```text
HARD gates (9): H01-H09 — any failure = REJECT
  H01 YAML parse
  H02 id pattern
  H03 id == filename
  H04 kind literal
  H05 quality null
  H06 required fields
  H07 tags len
  H08 scope non-empty
  H09 component_count >= 2

SOFT gates (10): S01-S10 — score = sum of weights
  S01 tldr length     (1.0)
  S02 connection_count (1.0)
  S03 direction present (1.0)
  S04 component fields (1.0)
  S05 no orphans      (1.0)
  S06 interfaces      (1.0)
  S07 body sections   (1.0)
  S08 density         (1.0)
  S09 dependencies    (0.5)
  S10 keywords        (0.5)
```
