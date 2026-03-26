---
id: diagram-builder-instructions
kind: instructions
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — INSTRUCTIONS

## Phase 1: DISCOVER

1. Identify the architecture scope to visualize
2. Determine zoom level: system, subsystem, or component
3. List components within scope
4. Map connections between components (data flow, dependencies, signals)
5. brain_query [IF MCP] for existing diagrams — avoid duplicates
6. Choose notation: ASCII (portable) or Mermaid (renderable)
7. Identify layers to represent (infra, runtime, content, governance)

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 15 required fields + 4 extended (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Scope section: what system/subsystem is visualized and its boundaries
6. Write Components section: labeled boxes/nodes with brief descriptions
7. Write Connections section: labeled arrows showing relationships
8. Write Diagram section: the actual ASCII or Mermaid visualization
9. Write Legend section: explanation of all symbols and arrow types
10. Write Annotations section: non-obvious design decisions

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md manually (no automated validator)
2. HARD gates: YAML parses, id pattern `^p08_diag_[a-z][a-z0-9_]+$`, kind literal "diagram", quality null, 15 required fields present, notation specified, diagram contains actual visual
3. SOFT gates: check each S01-S10 against QUALITY_GATES.md
4. Cross-check: is it purely visual? Not drifting into component inventory or pattern?
5. If score < 8.0: revise in same pass before output

## Step Constraints

- Phase 1 Step 5: brain_query only if MCP available — skip gracefully if not
- Phase 2 Step 4: quality MUST be null — any number fails H05
- Phase 2 Step 8: diagram must contain actual visual characters, not prose
- Phase 3 Step 5: never output below 8.0 — revise until gates pass

## Output Location

`cex/P08_architecture/examples/p08_diag_{scope_slug}.md`
