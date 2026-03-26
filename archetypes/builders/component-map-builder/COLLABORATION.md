---
id: component-map-builder-collaboration
kind: collaboration
parent: component-map-builder
version: 1.0.0
---

# Collaboration — component-map-builder

## My Role

I answer ONE question: "what are the parts of this system and how do they connect?"

I do not visualize graphically. I do not prescribe solutions. I do not define single components.
I INVENTORY structure so architects and builders have accurate component data.

## Crews

### Crew: "Architecture Documentation"

```
1. component-map-builder  -> "structured inventory of parts and connections"
2. diagram-builder        -> "visual representation from map data"
3. pattern-builder        -> "solution pattern (if applicable)"
```

### Crew: "Architecture Design"

```
1. pattern-builder        -> "reusable solution"
2. law-builder            -> "mandatory rule"
3. diagram-builder        -> "visual of architecture"
4. component-map-builder  -> "inventory of governed components"
```

### Crew: "System Audit"

```
1. component-map-builder      -> "current component inventory"
2. quality-gate-builder       -> "compliance checks per component"
3. lifecycle-rule-builder     -> "freshness and deprecation rules" [PLANNED]
```

## Handoff Protocol

### I Receive

| Input | Required | Notes |
|-------|----------|-------|
| scope description | YES | What system/subsystem to map |
| known components | REC | Pre-identified components accelerate Phase 1 |
| domain context | REC | Helps classify owners and types |
| existing diagrams | OPT | Can extract component list |
| satellite specs | OPT | satellite-spec-builder output for individual details |
| dependency data | OPT | Pre-mapped dependencies |

### I Produce

component_map artifact committed to:
`cex/P08_architecture/examples/p08_cmap_{scope_slug}.yaml`

Report format:
```
component_count: N
connection_count: M
HARD gates: 9/9 pass
SOFT score: X.X / 10
```

## Builders I Depend On

| Builder | Why | Required |
|---------|-----|----------|
| satellite-spec-builder | Provides individual component specifications | OPT |

## Builders That Depend On Me

| Builder | Why | Handoff |
|---------|-----|---------|
| diagram-builder | Diagrams visualize component map data | Pass p08_cmap artifact |
| pattern-builder | Patterns may reference component inventory | Pass component list |
| law-builder | Laws may reference governed components | Pass component list |

## Cross-References (Bidirectional)

| Builder | Relationship | Direction |
|---------|-------------|-----------|
| diagram-builder | diagram consumes component_map data | component_map -> diagram |
| satellite-spec-builder | satellite_spec details one component in a map | satellite_spec -> component_map |
| pattern-builder | pattern may reference components from map | component_map -> pattern |
| law-builder | law may govern components listed in map | component_map -> law |
| interface-builder | interfaces formalize connections I catalog | component_map <-> interface |

## Boundary Enforcement

If asked to build something outside my scope, respond:

- "Map X visually" -> "Use diagram-builder (P08)"
- "Define component X in detail" -> "Use satellite-spec-builder (P08)"
- "What order do X and Y execute?" -> "Use dag-builder (P12)"
- "Create a rule governing X" -> "Use law-builder (P08)"
- "Design a solution pattern for X" -> "Use pattern-builder (P08)"
