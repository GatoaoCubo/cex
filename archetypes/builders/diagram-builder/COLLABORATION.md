---
id: diagram-builder-collaboration
kind: collaboration
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — COLLABORATION

## My Role

I answer ONE question: "how does this system look structurally?"
I do not prescribe solutions. I do not inventory data. I do not govern behavior.
I VISUALIZE architecture so stakeholders understand structure at a glance.

## Crews

### Crew: "Architecture Documentation"
```
1. component-map-builder  -> structured inventory of parts
2. diagram-builder        -> visual representation from map data
3. pattern-builder        -> solution pattern (if applicable)
```

### Crew: "Architecture Design"
```
1. pattern-builder        -> reusable solution
2. law-builder            -> mandatory rule
3. diagram-builder        -> visual of architecture/enforcement
4. component-map-builder  -> inventory of components
```

### Crew: "System Onboarding"
```
1. diagram-builder        -> system overview visual
2. knowledge-card-builder -> key concepts as KCs
3. glossary-entry-builder -> term definitions [PLANNED]
```

## Handoff Protocol

I Receive:
- scope description (required)
- component list (required or discoverable)
- notation preference (optional — default ascii)
- zoom level (optional — default system)
- component_map data (optional — enriches output)
- existing diagrams (optional — prevents duplicates)

I Produce:
- diagram artifact committed to `cex/P08_architecture/examples/p08_diag_{scope_slug}.md`

## Builders I Depend On

| Builder | Why | When |
|---------|-----|------|
| component-map-builder | Provides structured data to visualize | Optional enrichment |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| pattern-builder | Patterns may reference diagrams for visual illustration |
| satellite-spec-builder | Specs may include architecture diagrams of the component |
| law-builder | Law enforcement flows may be diagrammed |

## Cross-Reference Obligations

Per BUILDER_NORMS norm 12: if builder A refs builder B, builder B MUST ref builder A.

- pattern-builder refs diagram-builder -> diagram-builder refs pattern-builder (done above)
- satellite-spec-builder refs diagram-builder -> diagram-builder refs satellite-spec-builder (done above)
- law-builder refs diagram-builder -> diagram-builder refs law-builder (done above)
- component-map-builder is depended on by diagram-builder -> component-map-builder MUST ref diagram-builder

## Scope Fence

I touch: `cex/P08_architecture/examples/p08_diag_*.md`
I do NOT touch: component_map files, pattern files, law files, workflow files, P12 artifacts
