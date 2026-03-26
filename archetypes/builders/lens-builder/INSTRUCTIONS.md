---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for lens
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a lens

## Phase 1: DISCOVER
1. Identify the perspective: what analytical viewpoint is needed?
2. Check brain_query [IF MCP] for existing lenses (avoid duplicates)
3. Determine which artifact kinds this lens applies to
4. List the specific attributes (filters) the lens highlights
5. Declare the bias direction (neutral or directional)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 20 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Perspective section: what the lens sees and emphasizes
6. Write Filters section: concrete attributes highlighted or suppressed
7. Write Application section: how to use this lens on artifacts
8. Write Limitations section: what the lens misses

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p02_lens_ pattern, kind == lens, quality == null, perspective non-empty, applies_to non-empty
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still a filter? Not drifting into agent capabilities? Not drifting into mental_model routing?
5. If score < 8.0: revise in same pass before outputting
