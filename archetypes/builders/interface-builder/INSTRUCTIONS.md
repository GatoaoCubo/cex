---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for interface
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an interface

## Phase 1: DISCOVER
1. Identify the integration point: which two agents/systems need to communicate?
2. Check brain_query [IF MCP] for existing interfaces on this integration (avoid duplicates)
3. List the operations (methods) needed: what can the consumer request?
4. For each method, determine input and output types
5. Determine versioning needs: is this a new interface or evolution of existing?
6. Check backward compatibility requirements

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 20+ fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Contract Definition section: what this interface enables between parties
6. Write Methods section: table of name/input/output/description for each method
7. Write Versioning section: version history, backward_compatible flag, migration notes
8. Write Mock Specification section: test doubles and example payloads

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p06_iface_ pattern, kind == interface, methods list non-empty, quality == null
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still bilateral? Not drifting into unilateral input_schema? Not drifting into runtime signal?
5. If score < 8.0: revise in same pass before outputting
