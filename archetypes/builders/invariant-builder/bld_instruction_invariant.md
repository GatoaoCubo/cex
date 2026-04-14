---
id: p03_ins_law
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Invariant Builder Execution Protocol
target: invariant-builder agent
phases_count: 4
prerequisites:
  - A candidate rule statement or behavioral pattern to formalize is available
  - The domain scope is identifiable (which system or component the rule governs)
  - Rule intent is classifiable as mandate, not recommendation, safety restriction, or abstract truth
validation_method: checklist
domain: law
quality: 9.1
tags: [instruction, law, governance, P08, mandate, enforcement]
idempotent: true
atomic: false
rollback: "Discard generated artifact; source pattern or failure remains unchanged"
dependencies: []
logging: true
tldr: Formalize an inviolable operational rule into a complete invariant artifact with statement, rationale, enforcement, and exception protocol.
density_score: 0.91
llm_function: REASON
---
## Context
The invariant-builder produces `law` artifacts (P08) — inviolable operational mandates the system must always follow. Laws differ from instructions (flexible guides), guardrails (safety restrictions), and axioms (abstract truths): an invariant is an operational rule with enforcement consequences and a defined exception protocol.
**Inputs:**
- `$rule_trigger (required) - string - "Pattern, failure, or explicit mandate that motivates this law"`
- `$scope (required) - string - "System component or domain this law governs (e.g. 'agent spawning', 'file writes', 'auth flows')"`
- `$enforcement_context (optional) - string - "How violations are detected or prevented (hook, linter, human review, automated gate)"`
- `$exceptions (optional) - list[string] - "Known legitimate scenarios where the invariant does not apply"`
**Output:** A single `law` artifact file with frontmatter (15 required + 4 extended fields) and 8 body sections covering statement, rationale, enforcement, exceptions, examples, violations, and history.
**Boundary check before proceeding:**
- Rule merely recommends a better approach → route to pattern-builder
- Rule restricts for safety → route to guardrail-builder
- Rule expresses an abstract truth → route to axiom-builder
- Rule is a non-negotiable operational mandate → proceed
## Phases
### Phase 1: Classify
**Action:** Verify the rule qualifies as an invariant and define its exact scope.
1. Extract the core behavioral requirement from `$rule_trigger`.
2. Apply classification test:
   - Is it ALWAYS required with no optional path? → Law candidate
   - Does violation cause measurable harm or system failure? → Law candidate
   - Is it a recommendation or best forctice? → STOP, route to pattern-builder
   - Is it a safety boundary? → STOP, route to guardrail-builder
3. Define scope boundary: identify which agents, components, or workflows the rule governs.
4. Check for existing laws covering the same scope to avoid number collision.
5. Assign candidate law identifier: `p08_law_{N}` where N is the next available positive integer.
6. Select `enforcement` from: `pre_commit_hook`, `ci_gate`, `runtime_assertion`, `review_required`, `automated_linter`.
7. Identify `severity`: `critical` (system breaks), `high` (data loss possible), `medium` (quality degraded).
**Verification:** You can complete this sentence without hedging: "If this rule is violated, [specific failure] occurs because [reason]."
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections.
1. Read `SCHEMA.md` — source of truth for all 15 required + 4 extended fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Set `id`: pattern `p08_law_{number}` (must equal the output filename stem).
4. Set `kind`: literal string `law` — never "rule", "mandate", or any other value.
5. Set `quality`: literal `null` — never a number.
6. Set `number`: the integer assigned in Phase 1.
7. Set `statement`: one imperative sentence using MUST, SHALL, NEVER, or ALWAYS — no conditionals.
8. Set `rationale`: 2-4 sentences explaining WHY (not restating the statement).
9. Set `enforcement`: the mechanism name from Phase 1.
10. Fill extended fields: `scope`, `exceptions` (list or empty list), `priority` (1–10), `keywords`.
11. Write `## Statement` — full imperative form of the law.
12. Write `## Rationale` — why this law exists with concrete justification.
13. Write `## Enforcement` — mechanism, detection method, consequence of violation.
14. Write `## Exceptions` — each exception with approval criteria, or "None".
15. Write `## Examples` — at least 2 concrete correct applications.
16. Write `## Violations` — at least 2 concrete breach scenarios with consequences.
17. Write `## History` — when and why established, any revisions.
18. Write `## References` — governance sources or upstream documents that support this law.
**Verification:** Statement contains one of: MUST, SHALL, NEVER, ALWAYS. No section is empty.
### Phase 3: Validate
**Action:** Run all 9 HARD gates. Fix any failure before proceeding to output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches pattern `^p08_law_[0-9]+$` |
| H03 | `id` equals filename stem exactly |
| H04 | `kind` is literal string `law` |
| H05 | `quality` is `null` |
| H06 | All 15 required fields present and non-empty |
| H07 | `tags` is a list with length >= 3 |
| H08 | `number` is a positive integer |
| H09 | `statement` uses imperative mood (MUST / SHALL / NEVER / ALWAYS) |
Then score all 10 SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass before outputting.
**Cross-check:** Is this truly a mandate? Is it a single rule, not a bundle of rules?
### Phase 4: Output
**Action:** Emit the final artifact at the correct path.
1. Write file to: `cex/P08_architecture/examples/p08_law_{number}.md`
2. Confirm filename stem matches `id` field.
3. Confirm 8 body sections all present and non-empty.
4. Confirm total body size is within `CONFIG.md` size limit.
## Output Contract
```
id: p08_law_`{{number}}`
kind: invariant
pillar: P08
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
