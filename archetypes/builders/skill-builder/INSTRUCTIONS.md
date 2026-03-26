---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for skill
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a skill

## Phase 1: RESEARCH
1. Identify the capability name and domain
2. Determine invocation pattern: slash command, keyword, event, or agent-invoked
3. Set user_invocable based on whether a human can trigger it directly
4. Search existing skills via brain_query [IF MCP] — avoid duplicates
5. List what the skill receives as input
6. List what the skill produces as output
7. Identify sub-skills this skill may delegate to
8. Determine platform constraints (if any)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill every {{var}} following SCHEMA constraints
3. Set id using pattern: `p04_skill_{name}` (underscores, lowercase)
4. Set quality: null (NEVER self-score)
5. Decompose into phases: minimum 2, maximum 6, each atomic
6. Write each phase with explicit Input / Action / Output
7. Ensure phases list in frontmatter matches ## Workflow Phases subsections exactly
8. Write when_to_use as list of conditions (parallel structure)
9. Write when_not_to_use as list of exclusions (same abstraction level as when_to_use)
10. Write at least 3 examples of concrete invocations
11. Write ## Anti-Patterns section with at least 3 named failures
12. Write ## Metrics section with at least 2 measurable success criteria
13. Check body <= 5120 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md (all HARD gates before publishing)
2. HARD gates: YAML parses, id matches pattern, kind == skill, quality == null, required fields present, phases match body sections
3. SOFT gates: check density, phase atomicity, trigger specificity, when_to_use contrast
4. Cross-check: no identity language in body? phases non-overlapping? trigger unambiguous?
5. If score < 7.0: revise before outputting
