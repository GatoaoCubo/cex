---
id: law-builder-instructions
kind: instruction
pillar: P03
parent: law-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [instructions, law-builder, protocol, P08, governance]
---

# law-builder — INSTRUCTIONS

## Phase 1: CLASSIFY

1. Identify the operational rule to formalize as a law
2. Verify mandate: confirm this rule MUST be followed without exception (not a recommendation)
3. Confirm it is operational (not safety-focused -> guardrail, not abstract truth -> axiom, not flexible -> instruction)
4. Identify the enforcement mechanism: automated check, review gate, or runtime guard
5. Identify exceptions: conditions where the law legitimately does not apply
6. Check brain_query [IF MCP]: `brain_query("existing laws P08 governance")` to avoid number collision
7. Determine scope: system-wide, satellite-specific, or domain-specific
8. Assign number: next sequential positive integer not already used in P08 laws

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all 15 required + 4 extended fields
2. Read OUTPUT_TEMPLATE.md — fill every `{{var}}` following SCHEMA constraints
3. Fill frontmatter field `id`: pattern `p08_law_{number}` (must equal filename stem)
4. Fill frontmatter field `kind`: literal string `law` (never "rule", "mandate", or other)
5. Fill frontmatter field `quality`: literal `null` (NEVER a number)
6. Fill frontmatter field `number`: the integer assigned in Phase 1 Step 8
7. Fill frontmatter field `statement`: one imperative sentence using MUST/SHALL/NEVER/ALWAYS
8. Fill frontmatter field `rationale`: explain WHY (not just restate the statement)
9. Fill frontmatter field `enforcement`: name the detection mechanism explicitly
10. Fill all remaining required fields: pillar, version, created, updated, author, domain, tags, tldr
11. Fill extended fields: scope, exceptions (list or empty list), priority (1-10), keywords
12. Write `## Statement` section: full imperative form of the law
13. Write `## Rationale` section: why this law exists, with concrete justification
14. Write `## Enforcement` section: mechanism, detection method, consequence of violation
15. Write `## Exceptions` section: conditions where law does not apply, or "None"
16. Write `## Examples` section: at least 2 concrete correct applications
17. Write `## Violations` section: at least 2 concrete breach scenarios with consequences
18. Write `## History` section: when and why the law was established, any revisions
19. Write `## References` section: governance sources that support this law

## Phase 3: VALIDATE

1. Check H01: YAML frontmatter parses without error
2. Check H02: id matches pattern `^p08_law_[0-9]+$`
3. Check H03: id equals filename stem exactly
4. Check H04: kind is literal string `law`
5. Check H05: quality is `null`
6. Check H06: all 15 required fields are present and non-empty (quality: null is valid)
7. Check H07: tags is a list with length >= 3
8. Check H08: number is a positive integer
9. Check H09: statement uses imperative mood (contains MUST, SHALL, NEVER, or ALWAYS)
10. Check all 10 SOFT gates against QUALITY_GATES.md; score each
11. Cross-check: is this truly a law (mandate) and not drifting toward instruction or guideline?
12. If any HARD gate fails: fix before outputting
13. If SOFT score < 8.0: revise in same pass before outputting
14. Confirm number uniqueness against existing laws in CEX system

## Output

Produce a single `.md` file at: `cex/P08_architecture/examples/p08_law_{number}.md`
File content: YAML frontmatter block + body sections (8 required sections)
