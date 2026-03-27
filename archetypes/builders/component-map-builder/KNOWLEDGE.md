---
id: component-map-builder-knowledge
kind: knowledge
parent: component-map-builder
version: 2.0.0
sources: [systems engineering, microservice registries, real agent architectures, builder architectures, dependency graph theory]
---

# Knowledge — component-map-builder

## Foundational

Component maps are structured decompositions showing WHAT exists in a system and HOW pieces connect. They originate from systems engineering (CMDB, service registries, infrastructure inventories) and serve a single purpose: make the invisible visible.

The key insight: **a map is DATA, not a picture.** A diagram shows relationships visually; a component map inventories them as structured, queryable records. Both are useful — but the builder produces the data layer, not the visual layer.

## Industry Implementations

| Source | What it defines | Alignment |
|--------|----------------|-----------|
| Microservice Registry | Service inventory + endpoints | Components + interfaces |
| AWS Resource Map | Infrastructure inventory + ownership | Components + ownership |
| API Catalog (Backstage) | Endpoint + owner inventory | Structured data inventory |
| CMDB (ITIL) | Configuration items + relations | Components + connections |
| Dependency Graph (npm/pip) | Package dependencies | Directed connections |
| Architecture Decision Records | Decision + context + consequences | Boundary definitions |

## Component Mapping Patterns

### Pattern 1: Layered Decomposition

Systems naturally organize into layers. Map each layer, then map connections between layers.

```text
Layer 3: [User Interface]
    |
Layer 2: [Business Logic / Routing]
    |
Layer 1: [Infrastructure / Data]
```

Each component belongs to exactly one layer. Cross-layer connections represent the system's data flow.

**When to use**: Multi-tier architectures, agent pipelines, request-processing stacks.
**Why it works**: Layers provide natural scope boundaries. Readers navigate top-down.

### Pattern 2: Hub-and-Spoke

One central component routes to multiple specialists. The hub is the only component with connections to all spokes.

```text
            [Spoke A]
               |
[Spoke D] -- [HUB] -- [Spoke B]
               |
            [Spoke C]
```

**When to use**: Router/gateway architectures, orchestrators, dispatcher systems.
**Why it works**: Clearly shows the routing bottleneck and spoke independence.

### Pattern 3: Pipeline

Linear flow where each component's output feeds the next component's input.

```text
[Parser] --> [Classifier] --> [Executor] --> [Validator] --> [Formatter]
```

**When to use**: Data processing chains, build pipelines, sequential workflows.
**Why it works**: Direction is unambiguous. Each node has exactly one upstream and one downstream.

## Dependency Graph Notation

### Arrow Conventions

Production systems use consistent arrow notation to distinguish relationship types:

| Notation | Meaning | Example |
|----------|---------|---------|
| `A --> B` | A sends data to B (data_flow) | `Parser --> Classifier` |
| `A --depends--> B` | A requires B to function (dependency) | `Search --depends--> Embeddings` |
| `A --signals--> B` | A sends event/notification to B | `Worker --signals--> Monitor` |
| `A --produces--> B` | A generates B as output (produces) | `Indexer --produces--> VectorIndex` |
| `A <--consumes-- B` | B reads/uses A (consumes) | `Index <--consumes-- QueryEngine` |
| `A <--> B` | Bidirectional flow | `Cache <--> Database` |

**Rule**: Every connection MUST have a type. Untyped arrows (`A -- B`) are ambiguous and forbidden in component maps.

### The `receives / produces_for` Pattern

For each component, document what it receives and what it produces:

```yaml
component: Intent Classifier
receives:
  - from: Request Parser
    data: structured intent object
produces_for:
  - to: Delegation Router
    data: operation type + execution path
```

This pattern makes data contracts explicit without requiring a full interface specification.

## Boundary Definition

### The IS / IS NOT Table

The most effective boundary definition pattern observed across production architectures:

```markdown
## Boundary

component_map IS:
- structured inventory of system parts
- typed connections between parts
- ownership and status tracking

component_map IS NOT:
| Confusion | Why NOT | Correct type |
|-----------|---------|-------------|
| diagram | Diagrams SHOW visually; maps INVENTORY as data | diagram |
| specification | Specs DEFINE one component deeply; maps COVER many | component_spec |
| workflow | Workflows define EXECUTION order; maps describe STRUCTURE | workflow |
```

**Why this pattern works**: The table forces explicit disambiguation against every neighboring type. LLMs and humans both benefit from knowing what something is NOT.

### Scope Statement

Every map needs a one-line scope statement: "This map covers X and does NOT cover Y."

```markdown
## Scope
This map covers the request routing infrastructure from user input to agent handoff.
It does NOT cover individual agent internals or downstream execution pipelines.
```

**Rule**: If you can't write the scope in one sentence, the map covers too much. Split it.

## Diagram Representation for LLMs

### What LLMs Understand Best

| Format | LLM comprehension | When to use |
|--------|-------------------|-------------|
| ASCII box diagrams | HIGH — trained on millions of ASCII art examples | Architecture overviews, flow diagrams |
| Markdown tables | HIGH — structured, unambiguous | Component inventories, connection lists |
| Mermaid syntax | MODERATE — can parse but may hallucinate syntax | When rendering tool is available |
| Text arrows (`A --> B`) | HIGH — simple, unambiguous | Dependency graphs, data flows |
| Nested indentation | MODERATE — works for trees, fails for graphs | Hierarchical structures only |
| SVG/image references | LOW — cannot read embedded images | Never for LLM-consumed maps |

### Recommended Combination

Use **tables for inventory** (components, connections) and **ASCII diagrams for topology** (how pieces fit together). This gives both queryable data and spatial intuition:

```markdown
## Components
| Name | Role | Owner | Status |
|------|------|-------|--------|
| Router | Classify and route requests | platform | active |
| Executor | Run dispatched tasks | compute | active |

## Topology
```
```text
[Input] --> [Router] --> [Executor] --> [Output]
                |
           [Fallback]
```

## Connection Types

| Type | Meaning | Direction | Example |
|------|---------|-----------|---------|
| data_flow | Data moves from A to B | unidirectional | Request → Router |
| dependency | A requires B to function | unidirectional | Search → Index |
| signal | A sends event/notification to B | unidirectional | Worker → Monitor |
| produces | A generates B as output | unidirectional | Builder → Artifact |
| consumes | A reads/uses B as input | unidirectional | Reader → Database |
| bidirectional | Data flows both ways | bidirectional | Cache ↔ Store |

**Rule**: Every connection has exactly one type and one direction. If a connection is truly bidirectional, mark it explicitly — do not assume.

## Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|-------------|-------------|-----|
| Orphan components | Component with zero connections — why is it in the map? | Remove it or add its connections |
| Circular dependencies | A → B → C → A — creates deadlock risk, unclear data flow | Break the cycle with an intermediate queue or event |
| Implicit dependencies | Component uses another but connection not documented | Audit: for each component, list all imports/calls/reads |
| Vague boundaries | "This map covers the system" — scope too broad | Narrow scope to one layer, one domain, or one pipeline |
| Missing ownership | Components with no owner — nobody is responsible | Assign owner to every component (team, service, or "system") |
| Diagram without data | Pretty picture but no structured inventory underneath | Tables first, diagram second |
| Status-free components | No indication if component is active, deprecated, or planned | Add status field to every component |
| Untyped connections | Lines between boxes with no label — what flows? | Label every connection with type + data description |

## Decision Rule

Ask: "What are the parts of this system and how do they connect?"
If yes → component_map.
If "show me a picture" → diagram.
If "define this one component deeply" → component_spec.
If "what order do things execute?" → workflow or DAG.
If "what are the rules for routing?" → dispatch_rule.

## Boundary vs Nearby Types

| Type | What it is | Why NOT component_map |
|------|------------|----------------------|
| diagram (P08) | Visual representation | Diagrams SHOW; maps INVENTORY |
| component_spec (P08) | Single component definition | Specs DEFINE one; maps COVER many |
| pattern (P08) | Reusable solution template | Patterns SOLVE; maps INVENTORY |
| workflow (P12) | Step graph with execution order | Workflows define WHEN; maps define WHAT |
| DAG (P12) | Execution dependency graph | DAGs define RUN ORDER; maps describe STRUCTURE |
| interface (P06) | Bilateral contract | Interfaces ENFORCE contracts; maps CATALOG connections |

## Key Principles Summary

1. **Data first, diagram second**: Tables are queryable; pictures are not
2. **Type every connection**: Untyped arrows are ambiguous and useless
3. **Scope in one sentence**: If you can't, split the map
4. **IS/IS NOT boundary table**: Disambiguate against every neighboring type
5. **Every component has an owner and status**: No orphans, no ambiguity
6. **ASCII + tables for LLMs**: Highest comprehension combination
7. **receives/produces_for per component**: Makes data contracts explicit
