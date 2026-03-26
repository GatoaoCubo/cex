---
pillar: P03
llm_function: REASON
purpose: Execution protocol for producing a context_doc artifact
---

# Instructions: context-doc-builder

## Phase 1: SCOPE

**Goal**: Establish precise domain boundaries before writing a single line.

1. Identify domain label (snake_case, e.g., `ecommerce_imports`, `api_auth_jwt`)
2. Write scope sentence: "This context covers [X] within [Y] for [Z] audience"
3. List what is explicitly OUT of scope (1-3 items minimum)
4. Enumerate stakeholders: who consumes this context_doc? (agent, human, both?)
5. Gather constraints: what cannot change? (regulatory, technical, organizational)
6. List assumptions: what is taken as given without proof?
7. List dependencies: what other artifacts, systems, or facts does this context reference?
8. Run `brain_query("context_doc [domain]")` — if existing doc found, update rather than duplicate

## Phase 2: COMPOSE

**Goal**: Produce the .md file with correct frontmatter and all required body sections.

1. Read SCHEMA.md — internalize all required/recommended fields and constraints
2. Read OUTPUT_TEMPLATE.md — use as the structural skeleton
3. Fill frontmatter:
   - id: `p01_ctx_{{topic_slug}}` (must equal filename stem)
   - kind: `context_doc` (literal, no variation)
   - domain: snake_case domain label from Phase 1
   - scope: scope sentence from Phase 1
   - quality: null (always — never self-score)
   - all other required fields from SCHEMA.md
4. Write `## Scope` section: restate scope, list in-scope and out-of-scope items
5. Write `## Background` section: domain background, history, rationale (no filler)
6. Write `## Stakeholders` section: who uses this context and why
7. Write `## Constraints & Assumptions` section: hard constraints + working assumptions
8. Write `## Dependencies` section: referenced artifacts, systems, external sources
9. Write `## References` section: source links, related artifacts, version history

## Phase 3: VALIDATE

**Goal**: Verify artifact passes all gates before marking ready.

1. Open QUALITY_GATES.md
2. Check all 7 HARD gates sequentially — any HARD fail = reject and fix
3. Check all 8 SOFT gates — note which pass/fail for scoring estimate
4. Cross-check boundary drift:
   - Is this still a context_doc? (not drifted into KC = no single-atomic-fact structure)
   - Is scope section present and >= 3 lines?
   - Body byte count <= 2048?
5. If body > 2048 bytes: trim Background section first, then Stakeholders
6. Set quality: null in frontmatter (not a score — external gate sets this)
7. Produce companion .yaml file with identical frontmatter fields
