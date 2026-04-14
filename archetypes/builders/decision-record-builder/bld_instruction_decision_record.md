---
kind: instruction
id: bld_instruction_decision_record
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for decision_record
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Decision Record"
version: "1.0.0"
author: n03_builder
tags: [decision_record, builder, examples]
tldr: "Golden and anti-examples for decision record construction, demonstrating ideal structure and common pitfalls."
domain: "decision record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a decision_record
## Phase 1: RESEARCH
1. Identify the architectural decision to be documented (technology choice, structural pattern, process rule, etc.)
2. Determine the current status: is this a proposed decision (not yet ratified) or accepted (already in effect)?
3. Reconstruct the context: what problem, constraint, or force made this decision necessary? Who was affected?
4. Enumerate the options that were (or should be) considered — minimum 2, ideally 3+
5. For each option, gather pros and cons from the team's perspective at decision time
6. Identify the chosen option and the primary rationale for choosing it over alternatives
7. List known consequences: what becomes easier, harder, required, or at risk as a result of this decision
8. Check for existing ADRs in the same domain to avoid duplication and to identify supersession relationships
9. Confirm the slug for id: snake_case, lowercase, no hyphens — describe the decision topic concisely
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill required frontmatter fields: id, title, status, context (summary), decision (summary), version, created, updated, author
4. Set quality: null — never self-score
5. Populate tags: minimum 3, must include "decision_record" and the primary domain keyword
6. Write tldr: <= 160 chars summarizing what was decided and its primary consequence
7. Write ## Context section: describe the situation, forces, and constraints that made the decision necessary. Use present/past tense for circumstances, not for the decision itself
8. Write ## Options Considered section: for each option, include name, brief description, pros, and cons. Be honest — do not omit options that were rejected for valid reasons
9. Write ## Decision section: state the chosen option clearly in the first sentence. Follow with the primary rationale in 2-4 sentences
10. Write ## Consequences section: list positive effects, negative effects (technical debt, constraints introduced), and neutral effects. Include at least one negative consequence
11. If status == superseded: populate superseded_by with the replacing ADR's id
12. If this ADR supersedes another: populate supersedes with the older ADR's id
13. Verify body <= 4096 bytes
14. Verify id matches `^p08_adr_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p08_adr_` prefix and snake_case slug
4. Confirm kind == decision_record
5. Confirm status is one of: proposed, accepted, deprecated, superseded
6. Confirm context, decision fields are non-empty strings
7. Confirm ## Context, ## Options Considered, ## Decision, ## Consequences sections all present
8. Confirm at least 2 options documented in ## Options Considered
9. Confirm at least one negative consequence documented in ## Consequences
10. If status == superseded: confirm superseded_by field is populated
11. Cross-check boundary: is this truly a decision record (single past/proposed choice)? Not a law (inviolable rule)? Not a pattern (reusable prescription)? Not a diagram?
12. Score against SOFT gates in QUALITY_GATES.md
13. Revise if score < 8.0 before outputting
