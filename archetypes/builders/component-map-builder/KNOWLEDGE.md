---
id: component-map-builder-knowledge
kind: knowledge
parent: component-map-builder
version: 2.0.0
sources: [systems engineering, microservice registries, real agent architectures, builder architectures, dependency graph theory]
---

# Knowledge -- component-map-builder

## Foundational
Component maps are structured decompositions: WHAT exists and HOW pieces connect. From systems engineering (CMDB, service registries). Key insight: **a map is DATA, not a picture.** The builder produces queryable records, not diagrams.

## Topology Patterns

```text
Layered:   [UI] -> [Logic/Routing] -> [Infra/Data]
Hub-Spoke: [Spoke A/B/C/D] -- [HUB] (router/gateway)
Pipeline:  [Parser] -> [Classifier] -> [Executor] -> [Validator]
```
- Layered: multi-tier, agent pipelines. Top-down navigation.
- Hub-Spoke: router/dispatcher architectures. Shows bottleneck + spoke independence.
- Pipeline: sequential chains. Each node has one upstream, one downstream.

## Dependency Notation

| Notation | Meaning | Example |
|----------|---------|---------|
| `A --> B` | Data flow | Parser --> Classifier |
| `A --depends--> B` | A requires B | Search --depends--> Embeddings |
| `A --signals--> B` | Event/notification | Worker --signals--> Monitor |
| `A --produces--> B` | A generates B | Indexer --produces--> VectorIndex |
| `A <--> B` | Bidirectional | Cache <--> Database |

Every connection MUST have a type. Untyped arrows are forbidden.

Per component, document `receives` (from whom, what data) and `produces_for` (to whom, what data).

## Boundary Definition

**IS/IS NOT table**:

| component_map IS | component_map IS NOT |
|------------------|---------------------|
| Structured inventory of parts | Diagram (visual, not data) |
| Typed connections between parts | Specification (one component deep) |
| Ownership + status tracking | Workflow (execution order) |

Scope in one sentence. If you can't, split the map.

## LLM Format Guide

| Format | Comprehension | Use |
|--------|--------------|-----|
| ASCII box diagrams | HIGH | Architecture overviews |
| Markdown tables | HIGH | Inventories, connections |
| Text arrows (A-->B) | HIGH | Dependencies, flows |
| Mermaid | MODERATE | When renderer available |
| SVG/images | LOW | Never for LLM maps |

Best combo: **tables for inventory** + **ASCII for topology**.

## Concrete Examples

**Example 1 -- Agent Router**:
```
Components: Router, Executor, Fallback
Topology: [Input] --> [Router] --> [Executor] --> [Output]
                         |
                    [Fallback]
Router receives: raw request from Input
Router produces_for: classified task to Executor, unmatched to Fallback
```

**Example 2 -- Build Pipeline**:
```
Components: Scanner, Builder, Validator, Publisher
Topology: [Scanner] --> [Builder] --> [Validator] --> [Publisher]
Scanner receives: source files from trigger
Publisher produces_for: artifact to registry
```

## Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Orphan components (zero connections) | Remove or add connections |
| Circular dependencies (A->B->C->A) | Break with queue/event |
| Implicit dependencies | Audit all imports/calls/reads |
| Vague scope ("the system") | Narrow to one layer/domain |
| Missing ownership | Assign owner to every component |
| Diagram without data tables | Tables first, diagram second |
| Untyped connections | Label every connection with type |

## Boundary vs Nearby Types

| Type | Why NOT component_map |
|------|----------------------|
| diagram | Diagrams SHOW; maps INVENTORY |
| component_spec | Specs DEFINE one; maps COVER many |
| workflow | Workflows define WHEN; maps define WHAT |
| DAG | DAGs define RUN ORDER; maps describe STRUCTURE |
| interface | Interfaces ENFORCE contracts; maps CATALOG connections |

## Key Principles
1. Data first, diagram second
2. Type every connection
3. Scope in one sentence
4. IS/IS NOT boundary table
5. Every component has owner + status
6. ASCII + tables for LLMs
