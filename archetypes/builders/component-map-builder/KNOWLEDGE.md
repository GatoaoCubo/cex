---
id: component-map-builder-knowledge
kind: knowledge
parent: component-map-builder
version: 1.0.0
---

# Knowledge — component-map-builder

## Foundational

Component maps trace back to systems engineering — structured decompositions showing WHAT exists and HOW it connects. In software: dependency graphs, microservice registries, API catalogs, infrastructure inventories. The key insight: a map is DATA, not a picture.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Microservice Registry | Service inventory + endpoints | Components + interfaces |
| AWS Resource Map | Infrastructure inventory | Components + ownership |
| API Catalog (Backstage) | Endpoint + owner inventory | Structured data inventory |
| CMDB (ITIL) | Configuration items + relations | Components + connections |
| Dependency Graph (npm/pip) | Package dependencies | Directed connections |
| CEX Component Maps | Agent/satellite inventories | Domain: multi-agent system |

## Key Patterns

- SCOPE-BOUNDED: clear boundary of what is and isn't included
- EVERY-COMPONENT: no component in scope is omitted
- TYPED-CONNECTIONS: every connection has a type (data_flow, dependency, signal)
- DIRECTED: connections have direction (A -> B, not just "A relates to B")
- OWNED: every component has an owner (team, satellite, or system)
- VERSIONED: components track their current version
- INTERFACE-AWARE: boundaries between components are explicit
- HEALTH-TRACKED: current status (active, deprecated, planned)

## Connection Types

| Type | Meaning | Example |
|------|---------|---------|
| data_flow | Data moves from A to B | Pool -> Indexer |
| dependency | A requires B to function | FAISS -> Ollama |
| signal | A sends event/notification to B | satellite -> signal_writer |
| produces | A generates B as output | Indexer -> BM25 Index |
| consumes | A reads/uses B | brain_query -> BM25 Index |

## Boundary vs Nearby Types

| Type | What it is | Why NOT component_map |
|------|------------|----------------------|
| diagram (P08) | Visual representation | Diagrams SHOW; maps INVENTORY |
| satellite_spec (P08) | Single component spec | Specs DEFINE one; maps COVER many |
| pattern (P08) | Reusable solution | Patterns SOLVE; maps INVENTORY |
| law (P08) | Operational mandate | Laws GOVERN; maps DESCRIBE structure |
| dag (P12) | Execution dependency graph | DAGs define EXECUTION order; maps describe STRUCTURE |
| interface (P06) | Bilateral contract | Interfaces ENFORCE contracts; maps CATALOG connections |

## Decision Rule

Ask: "what are the parts of this system and how do they connect?"
If yes -> component_map.
If "show me a picture" -> diagram.
If "define this one component deeply" -> satellite_spec.
If "what order do things execute?" -> dag.

## CEX-Specific Notes

- Satellite network maps: cover STELLA, SHAKA, LILY, EDISON, PYTHA, ATLAS, YORK
- Brain infrastructure: BM25 + FAISS + Ollama + Pool
- API infrastructure: FastAPI routes + Railway + PostgreSQL
- Hook system: PostToolUse hooks + signal_writer + monitors
