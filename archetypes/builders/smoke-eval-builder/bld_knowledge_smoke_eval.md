---
kind: knowledge_card
id: bld_knowledge_card_smoke_eval
pillar: P07
llm_function: INJECT
purpose: Domain knowledge for smoke_eval production — atomic searchable facts
sources: smoke-eval-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_smoke_eval_builder
  - p03_ins_smoke_eval_builder
  - p11_qg_smoke-eval
  - bld_collaboration_smoke_eval
  - bld_memory_smoke_eval
  - bld_examples_smoke_eval
  - bld_schema_smoke_eval
  - bld_config_smoke_eval
  - bld_output_template_smoke_eval
  - p01_kc_smoke_eval
---

# Domain Knowledge: smoke_eval
## Executive Summary
Smoke evals are fast-fail sanity checks constrained to 30 seconds maximum — the lightest evaluation artifact in P07. Each smoke eval answers one question: "does this component work at all?" It validates the critical path only, not correctness or performance. Unlike unit_evals (deep correctness testing) or benchmarks (performance measurement), smoke evals abort on first failure and require minimal setup.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (evaluation) |
| Format | Markdown |
| Naming | `p07_se_{scope_slug}.md` |
| ID regex | `^p07_se_[a-z][a-z0-9_]+$` |
| Max body bytes | 3072 (smaller than unit_eval) |
| Required frontmatter fields | 17 |
| Recommended frontmatter fields | 6: prerequisites, environment, health_check, frequency, alerting, density_score |
| timeout | integer ≤ 30 seconds — hard constraint |
| fast_fail | `true` always — invariant |
| quality field | null always — invariant |
| tldr max | 160 characters |
| Assertion object shape | `check` + `expected` + `timeout_ms` |
## Patterns
| Pattern | Rule |
|---------|------|
| Critical path first | List minimum checks in strict dependency order |
| Binary assertions | Each assertion is pass/fail only — no partial credit |
| fast_fail: true | Abort on first assertion failure; never continue after failure |
| timeout discipline | Total eval ≤ 30s; `timeout_ms` per assertion sets individual ceiling |
| Scope = one component | One smoke_eval per deployable unit or service boundary |
| Prerequisites listed | Everything that must exist before the eval can run |
| On Failure section | Escalation path: who to alert, what to check next |
- **Body sections**: Critical Path → Assertions → Prerequisites → On Failure
- **Assertion example**: `check: "API /health"` / `expected: "200 OK"` / `timeout_ms: 5000`
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| timeout > 30 seconds | Hard schema rejection; smoke evals must complete fast |
| fast_fail: false | Defeats purpose; always abort on first failure |
| Deep logic or correctness assertions | Out of scope; use unit_eval for correctness |
| Performance measurement | Use benchmark; smoke is binary pass/fail only |
| Missing prerequisites section | Eval may run against absent dependencies |
| Missing On Failure guidance | Leaves operator without recovery path |
| Assertions without timeout_ms | Single slow check can block entire eval pipeline |
| Scope covering multiple services | Split into one smoke_eval per component |
## Application
1. Identify component scope (one deployable unit or integration boundary)
2. List critical path: minimum ordered checks that confirm the component is "alive"
3. Write each assertion: `check` (what to verify) + `expected` (pass condition) + `timeout_ms`
4. Set `timeout` ≤ 30 (total), set `fast_fail: true`
5. Write prerequisites: runtime dependencies, environment, credentials needed
6. Write On Failure: escalation path and first diagnostic steps
7. Set `quality: null`, verify body ≤ 3072 bytes
8. Name file `p07_se_{scope_slug}.md`
## References
- Schema: smoke_eval SCHEMA.md (P06)
- Pillar: P07 (evaluation)
- Boundary: unit_eval (deep correctness), benchmark (performance), e2e_eval (full pipeline)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_smoke_eval_builder]] | upstream | 0.51 |
| [[p03_ins_smoke_eval_builder]] | upstream | 0.49 |
| [[p11_qg_smoke-eval]] | downstream | 0.44 |
| [[bld_collaboration_smoke_eval]] | related | 0.41 |
| [[bld_memory_smoke_eval]] | downstream | 0.40 |
| [[bld_examples_smoke_eval]] | related | 0.40 |
| [[bld_schema_smoke_eval]] | upstream | 0.39 |
| [[bld_config_smoke_eval]] | downstream | 0.38 |
| [[bld_output_template_smoke_eval]] | upstream | 0.37 |
| [[p01_kc_smoke_eval]] | sibling | 0.37 |
