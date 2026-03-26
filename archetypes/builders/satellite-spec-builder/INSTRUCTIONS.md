---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for satellite_spec
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a satellite_spec

## Phase 1: RESEARCH
1. Identify the satellite: name, primary domain, and role
2. Check brain_query [IF MCP] for existing satellite_specs (avoid duplicates)
3. Determine the LLM model requirement (opus for complex, sonnet for standard)
4. List required MCP servers and their purposes
5. Map boot sequence from PRIME file or design doc
6. Identify dispatch keywords that route tasks to this satellite
7. List dependencies on other satellites or external services

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 26 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Role section: primary function and responsibilities
6. Write Model & MCPs section: model choice rationale and MCP specs
7. Write Boot Sequence section: ordered init steps
8. Write Dispatch section: keywords and routing rules
9. Write Constraints section: operational limits
10. Write Dependencies section: required services
11. Write Scaling & Monitoring section: concurrency and health checks

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p08_sat_ pattern, kind == satellite_spec, model is valid, quality == null, name non-empty
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still a satellite spec? Not drifting into agent identity? Not drifting into boot_config detail?
5. If score < 8.0: revise in same pass before outputting
