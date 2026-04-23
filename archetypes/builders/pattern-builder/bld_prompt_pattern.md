---
id: p03_ins_pattern
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Pattern Builder Instructions
target: pattern-builder agent
phases_count: 3
prerequisites:
  - A recurring problem or architectural challenge is identified by name
  - At least 2 concrete instances where this solution was applied are known
  - The solution is reusable across contexts (not a one-time fix)
validation_method: checklist
domain: pattern
quality: 9.0
tags:
  - instruction
  - pattern
  - architecture
  - P08
idempotent: true
atomic: false
rollback: "Delete the produced pattern artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Discover recurring problem and forces, compose solution with consequences and anti-patterns, validate recurrence and gates, write a pattern artifact."
density_score: 0.86
llm_function: REASON
related:
  - bld_schema_pattern
  - p03_sp_pattern_builder
  - p11_qg_pattern
  - bld_knowledge_card_pattern
  - bld_memory_pattern
  - bld_collaboration_pattern
  - p01_kc_pattern
  - pattern-builder
  - bld_architecture_pattern
  - bld_tools_pattern
---
## Context
The pattern-builder receives a **recurring problem description** and produces a `pattern` artifact that formally encodes the named, reusable solution for that problem.
**Input variables**:
- `{{pattern_name}}` — a short, memorable name for the solution (e.g., "Circuit Breaker", "Retry with Backoff", "Fan-Out Aggregation")
- `{{problem}}` — the recurring situation in concrete terms: what goes wrong, under what conditions, how often
- `{{solution_sketch}}` — a brief description of the approach that resolves the problem
- `{{examples}}` — 2 or more concrete instances where this solution was applied (system name, context, outcome)
- `{{related}}` — optional list of known complementary, alternative, or prerequisite patterns
**Output**: a single `pattern` artifact at `p08_pat_{{pattern_slug}}.md` with problem, context, forces, solution, consequences, examples, anti-patterns, and related patterns.
**Boundaries**: documents recurring solutions only. Does NOT encode inviolable rules (use law), define executable multi-step workflows (use workflow), produce visual diagrams (use diagram), or map component relationships (use component_map).
## Phases
### Phase 1: DISCOVER
**Goal**: Confirm recurrence, extract forces, and gather examples before writing the solution.
1. Verify recurrence: confirm the problem in `{{problem}}` happens repeatedly across different contexts — not a one-off fix. If it cannot be confirmed as recurring, stop and route to bugloop or workflow instead.
2. State the problem in concrete terms: what fails, under what conditions, what the impact is. Avoid abstract language.
3. Identify forces — the competing tensions that make the problem hard to solve:
   - List at least 2 forces (e.g., "need fast response" vs "need reliable delivery")
   - Forces must be genuine tensions, not just desirable properties
4. Inspect `{{examples}}`. For each, record: system/context name, how the solution was applied, and what the measurable outcome was. Minimum 2 concrete examples required.
5. Search existing patterns via brain_query [IF MCP]: `pattern {{pattern_name}}`. If a duplicate exists, read it and determine whether an update or merge is needed rather than creating a new artifact.
6. Identify related patterns from `{{related}}` or by reasoning:
   - **Complementary**: patterns that are typically used alongside this one
   - **Alternative**: patterns that solve the same problem differently
   - **Prerequisite**: patterns that must be in place before applying this one
7. Identify anti-patterns: 1–3 common wrong approaches to the same problem, each with an explanation of why they fail.
**Exit**: recurrence confirmed, at least 2 forces identified, at least 2 concrete examples documented, at least 1 anti-pattern identified.
### Phase 2: COMPOSE
**Goal**: Produce all artifact fields and body sections following SCHEMA.md and OUTPUT_TEMPLATE.md.
8. Read SCHEMA.md — source of truth for all required fields (14 required + 7 extended).
9. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints exactly.
10. Generate `pattern_slug` in kebab-case (e.g., `circuit-breaker`, `retry-backoff`). Set `id = p08_pat_{{pattern_slug}}`.
11. Fill frontmatter: all 14 required + 7 extended fields. Set `quality: null` — never self-score. Set `null` for optional extended fields if not applicable.
12. Write **Problem** section: the recurring situation in concrete terms (2–4 sentences). Must describe recurrence explicitly.
13. Write **Context** section: environment where the problem occurs, frequency, severity, and applicable system types.
14. Write **Forces** section: list each competing tension as a bullet. Minimum 2 forces.
15. Write **Solution** section: the concrete reusable approach. Include an optional ASCII diagram or pseudocode if it clarifies the mechanism. Keep this section focused on the "how", not the "why".
16. Write **Consequences** section: both benefits AND costs. Never list benefits only. For each consequence, state whether it is a benefit or cost explicitly.
17. Write **Examples** section: 2+ concrete applications from Phase 1 step 4. Include system name, context, and outcome for each.
18. Write **Anti-Patterns** section: 1–3 wrong approaches with explanation of why each fails.
19. Write **Related Patterns** section: list complementary, alternative, and prerequisite patterns with one-line descriptions. Use artifact IDs where known.
20. Verify body <= 4096 bytes.
**Exit**: all sections present, consequences include both benefits and costs, examples are concrete (not hypothetical), anti-patterns are named.
### Phase 3: VALIDATE
**Goal**: Verify all quality gates before writing the final artifact.
21. Check QUALITY_GATES.md manually (no automated validator for patterns).
22. Verify all HARD gates pass: YAML parses, `id` matches pattern, `kind = pattern`, `quality = null`, all required fields present, `name` present, Problem section describes recurrence explicitly.
23. Cross-check: is this truly a pattern (recurring, reusable)? Confirm it is NOT drifting into:
    - law (inviolable rule) — route to invariant-builder
    - workflow (executable multi-step procedure) — route to workflow-builder


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pattern]] | downstream | 0.44 |
| [[p03_sp_pattern_builder]] | related | 0.43 |
| [[p11_qg_pattern]] | downstream | 0.43 |
| [[bld_knowledge_card_pattern]] | upstream | 0.42 |
| [[bld_memory_pattern]] | downstream | 0.42 |
| [[bld_collaboration_pattern]] | downstream | 0.38 |
| [[p01_kc_pattern]] | downstream | 0.38 |
| [[pattern-builder]] | downstream | 0.34 |
| [[bld_architecture_pattern]] | downstream | 0.33 |
| [[bld_tools_pattern]] | downstream | 0.30 |
