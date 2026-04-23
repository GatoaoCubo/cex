---
id: p03_ins_lifecycle_rule
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Lifecycle Rule Builder Execution Protocol
target: lifecycle-rule-builder agent
phases_count: 4
prerequisites:
  - The artifact kind to govern is identified (e.g. knowledge_card, model_card, law)
  - A reason freshness matters for this artifact kind is articulable
  - No existing lifecycle rule covers this artifact kind and scope
validation_method: checklist
domain: lifecycle_rule
quality: 9.1
tags: [instruction, lifecycle-rule, freshness, P11, governance, state-machine]
idempotent: true
atomic: false
rollback: "Discard generated artifact; governed artifact kind is unaffected"
dependencies: []
logging: true
tldr: Define declarative lifecycle states, transitions, and review cycles for an artifact kind, with measurable triggers and clear ownership for each state change.
density_score: 0.89
llm_function: REASON
related:
  - p03_sp_lifecycle_rule_builder
  - bld_memory_lifecycle_rule
  - bld_knowledge_card_lifecycle_rule
  - p11_qg_lifecycle_rule
  - bld_schema_lifecycle_rule
  - bld_collaboration_lifecycle_rule
  - bld_architecture_lifecycle_rule
  - bld_examples_lifecycle_rule
  - bld_manifest_lifecycle_rule
  - bld_tools_lifecycle_rule
---
## Context
The lifecycle-rule-builder produces `lifecycle_rule` artifacts (P11) — declarative governance rules that define how artifacts of a given kind move through states (creation, review, promotion, deprecation, sunset). Lifecycle rules differ from hooks (executable triggers), runtime rules (behavior at execution time), and quality gates (scoring thresholds): a lifecycle rule defines when artifact state changes and who decides, not how the system executes.
**Inputs:**
- `$artifact_kind (required) - string - "The artifact type this rule governs (e.g. 'knowledge_card', 'model_card', 'learning_record')"`
- `$domain_volatility (required) - string - "How fast the artifact's domain changes: 'high' (weeks), 'medium' (months), 'low' (years)"`
- `$states (optional) - list[string] - "Named lifecycle states; defaults to: draft, active, stale, deprecated, archived"`
- `$review_owner (optional) - string - "Role or agent responsible for review decisions"`
- `$freshness_days (optional) - integer - "Days before an active artifact becomes stale; if omitted, derived from domain_volatility"`
**Output:** A single `lifecycle_rule` artifact with 16 required + 4 recommended frontmatter fields and body sections covering definition, states table, transitions table, review protocol, and automation plan.
**Boundary check before proceeding:**
- Need to execute a transition programmatically → route to hook-builder (planned)
- Need to score artifact quality → route to quality-gate-builder
- Need to restrict unsafe behavior → route to guardrail-builder
- Need to define when artifact state changes declaratively → proceed
## Phases
### Phase 1: Research
**Action:** Gather the parameters needed to define apownte states and transitions.
1. Identify the `artifact_kind`: the exact kind string used in frontmatter of the governed artifacts.
2. Determine why freshness matters: what goes wrong when an artifact of this kind becomes stale.
3. Find existing lifecycle rules for similar domains in `P11_feedback/examples/` — avoid duplicates.
4. Derive `freshness_days` from `domain_volatility` if not provided:
   - `high` volatility → 30–60 days
   - `medium` volatility → 90–180 days
   - `low` volatility → 365+ days
5. Identify the `review_cycle`: how often active artifacts are reviewed regardless of freshness trigger.
6. Identify the `review_owner`: the role, agent, or human responsible for state decisions.
7. Confirm the `review_cycle` value is a recognized period: `weekly`, `monthly`, `quarterly`, `semi-annual`, `annual`.
**Verification:** You can answer: "An artifact of kind [X] becomes stale after [N] days and [role] decides whether to renew, deprecate, or archive it."
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections.
1. Read `SCHEMA.md` — source of truth for all 16 required + 4 recommended fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Fill frontmatter: all 16 required fields + 4 recommended (`null` valid for recommended).
4. Set `quality`: literal `null` — never a number.
5. Set `freshness_days`: positive integer, derived or provided.
6. Set `review_cycle`: one of the recognized period values.
7. Write `## Definition` — what artifact kind this governs and why freshness matters for it.
8. Write `## States` — table with >= 3 states:
   | State | Entry Criteria | Max Duration | Exit Action |
   Each state must have a measurable entry criterion (not "when it feels outdated").
9. Write `## Transitions` — table with >= 3 transitions:
   | From | To | Trigger | Action | Owner |
   Each trigger must be measurable (time elapsed, score threshold, event occurred).
10. Write `## Review Protocol` — reviewer role, review cycle, checklist items (>= 3), possible outcomes.
11. Write `## Automation` — which transitions are automated vs manual, and the automation mechanism.
**Verification:** Every transition trigger is measurable. No trigger uses subjective language ("when it feels outdated", "when it seems wrong"). States count >= 3, transitions count >= 3.
### Phase 3: Validate
**Action:** Run all 9 HARD gates from `QUALITY_GATES.md`. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches expected pattern for lifecycle_rule |
| H03 | `kind` is literal string `lifecycle_rule` |
| H04 | `pillar` is `P11` |
| H05 | `quality` is `null` |
| H06 | `freshness_days` is a positive integer |
| H07 | `review_cycle` is one of the recognized period values |
| H08 | `## States` table has >= 3 rows |
| H09 | `## Transitions` table has >= 3 rows with measurable triggers |
Score SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass.
**Cross-check:** Are all transition triggers measurable (not subjective)? Does `## Automation` clearly separate automated from manual transitions?
### Phase 4: Output
**Action:** Emit the final artifact at the correct path.
1. Write file to the path defined in `CONFIG.md` for lifecycle_rule artifacts.
2. Confirm filename stem matches `id` field.
3. Confirm all 5 body sections present and non-empty.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_lifecycle_rule_builder]] | related | 0.45 |
| [[bld_memory_lifecycle_rule]] | downstream | 0.42 |
| [[bld_knowledge_card_lifecycle_rule]] | downstream | 0.40 |
| [[p11_qg_lifecycle_rule]] | downstream | 0.39 |
| [[bld_schema_lifecycle_rule]] | downstream | 0.38 |
| [[bld_collaboration_lifecycle_rule]] | downstream | 0.38 |
| [[bld_architecture_lifecycle_rule]] | downstream | 0.34 |
| [[bld_examples_lifecycle_rule]] | related | 0.34 |
| [[bld_manifest_lifecycle_rule]] | related | 0.33 |
| [[bld_tools_lifecycle_rule]] | downstream | 0.29 |
