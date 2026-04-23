---
kind: knowledge_card
id: bld_knowledge_card_unit_eval
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for unit_eval production — atomic searchable facts
sources: unit-eval-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Unit Eval"
version: "1.0.0"
author: n03_builder
tags: [unit_eval, builder, examples]
tldr: "Golden and anti-examples for unit eval construction, demonstrating ideal structure and common pitfalls."
domain: "unit eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_unit_eval
  - p03_sp_unit-eval-builder
  - p03_ins_unit_eval
  - bld_architecture_unit_eval
  - bld_examples_unit_eval
  - p11_qg_unit_eval
  - p01_kc_unit_eval
  - bld_instruction_golden_test
  - bld_output_template_unit_eval
  - bld_instruction_e2e_eval
---

# Domain Knowledge: unit_eval
## Executive Summary
A `unit_eval` (P07) is a deterministic test for a single agent or prompt in isolation — it answers "does this target produce the correct output for this exact input?" It differs from `smoke_eval` (shallow pass/fail sanity), `e2e_eval` (multi-agent pipeline), and `golden_test` (quality calibration reference) by requiring gate-mapped assertions tied to specific quality gates of the target artifact. Each unit_eval covers ONE target, ONE input scenario.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 |
| Kind | `unit_eval` |
| ID pattern | `^p07_ue_[a-z][a-z0-9_]+$` |
| Naming | `p07_ue_{target_slug}.md` + `.yaml` |
| Max body | 4096 bytes |
| Required frontmatter fields | 18 |
| Recommended fields | 6 |
| `timeout` default | 60 seconds |
| `quality` field | always `null` |
| `assertions` | non-empty list; each item must have `gate_ref` |
## Patterns
| Pattern | Rule |
|---------|------|
| Single responsibility | One unit_eval = one target + one input scenario |
| Concrete assertions | Exact expected values — never "should be good" or vague |
| Gate-mapped checks | Every assertion references a `gate_ref` (e.g. `"H01"`) from the target's quality gates |
| Setup isolation | `setup` section clears external state before test executes |
| Teardown cleanup | `teardown` section prevents pollution of subsequent tests |
| Edge cases separate | Each edge case gets its own unit_eval with `edge_case: true` |
| Timeout explicit | Set `timeout` per expected execution cost; default 60s |
| `score` field | Set expected minimum score when target has numeric quality gate |
**Assertion object structure**:
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `gate_ref` | string | YES | Maps to target's quality gate ID |
| `check` | string | YES | Human-readable description of what is checked |
| `expected` | any | YES | Exact expected value |
| `severity` | enum | YES | `HARD` or `SOFT` |
**Boundary — what unit_eval is NOT**:
| kind | Why NOT unit_eval |
|------|-----------------|
| `smoke_eval` | Shallow pass/fail only, no gate mapping, <30s |
| `e2e_eval` | Tests full pipeline with multiple agents together |
| `golden_test` | 9.5+ reference for calibration, not verification |
| `benchmark` | Measures latency/cost, not output correctness |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague `expected_output` ("looks good") | Assertion is unevaluable; test is meaningless |
| Missing `gate_ref` on assertions | Disconnects test from quality framework; ungated |
| Testing multiple behaviors in one file | Violates single responsibility; failures are ambiguous |
| No `setup` for stateful targets | External state bleeds in; flaky results |
| `quality` set to a score | Never self-score; governance assigns |
| `id` not matching filename stem | Schema constraint violated; indexing breaks |
| Empty `assertions` list | Schema HARD gate: assertions must be non-empty |
## Application
1. Identify `target` (agent/prompt ID) and `target_kind` (artifact kind)
2. Choose ONE input scenario — edge cases get separate files
3. Set `id` = `p07_ue_{target_slug}`, must equal filename stem
4. Write `input` as exact verbatim text to feed the target
5. Write `expected_output` as the correct, concrete expected result
6. Map assertions: for each gate in the target's quality gates, write one assertion object with `gate_ref`, `check`, `expected`, `severity`
7. Write `setup` section: preconditions, state initialization
8. Write `teardown` section: cleanup steps
9. Set `timeout` based on expected execution time; flag `edge_case: true` if applicable
10. Set `quality: null` — do not self-score
## References
- unit-eval-builder MANIFEST.md v1.0.0
- unit-eval-builder SCHEMA.md v1.0.0

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_unit_eval]] | downstream | 0.47 |
| [[p03_sp_unit-eval-builder]] | downstream | 0.45 |
| [[p03_ins_unit_eval]] | downstream | 0.45 |
| [[bld_architecture_unit_eval]] | downstream | 0.43 |
| [[bld_examples_unit_eval]] | downstream | 0.42 |
| [[p11_qg_unit_eval]] | downstream | 0.41 |
| [[p01_kc_unit_eval]] | sibling | 0.37 |
| [[bld_instruction_golden_test]] | downstream | 0.36 |
| [[bld_output_template_unit_eval]] | downstream | 0.36 |
| [[bld_instruction_e2e_eval]] | downstream | 0.35 |
