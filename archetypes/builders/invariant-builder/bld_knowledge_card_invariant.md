---
kind: knowledge_card
id: bld_knowledge_card_invariant
pillar: P08
llm_function: INJECT
purpose: Domain knowledge for law production — atomic searchable facts
sources: invariant-builder MANIFEST.md + SCHEMA.md v1.0.0
quality: 9.1
title: "Knowledge Card Invariant"
version: "1.0.0"
author: n03_builder
tags: [invariant, builder, examples]
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: law
## Executive Summary
Laws are inviolable operational rules — the highest-authority governance artifacts in P08. Each law encodes ONE mandate in imperative mood (MUST/SHALL/NEVER/ALWAYS) with an explicit enforcement mechanism and exception list. Laws differ from instructions (flexible guides, P03), guardrails (safety restrictions, P11), and axioms (abstract truths, P10) by being operationally binding with named consequences for violation.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (governance) |
| Kind | `law` — exact literal, never "rule" / "mandate" / "policy" |
| ID pattern | `p08_law_{number}` — no leading zeros |
| Required frontmatter | 15 fields |
| Extended frontmatter | 4 fields (scope, exceptions, priority, keywords) |
| Required body sections | 8 |
| Max body bytes | 3072 |
| Density minimum | 0.80 |
| Quality field | always `null` — self-scoring prohibited (H05) |
| Statement mood | imperative: MUST / SHALL / NEVER / ALWAYS |
| Number | positive integer, unique + sequential across all P08 laws |
| Scope values | `system`, `agent_group`, `domain` |
| Priority range | 1–10 (10 = highest; resolves law conflicts) |
| Quality gates | 9 HARD + 10 SOFT |
## Patterns
| Pattern | Correct Form |
|---------|-------------|
| Imperative statement | "Systems MUST validate output before committing" — one sentence, one modal verb |
| Enforcement naming | Name exact mechanism: "pre-commit hook", "CI gate", "runtime validator H05" |
| Exception list | Concrete conditions OR `[]` — never omit the field |
| Rationale vs statement | Rationale answers WHY; never restate the statement |
| Number as PK | `number` is the unique key across all laws; never reuse a retired number |
| Priority 10 | Reserved for laws that win all conflicts unconditionally |
| Scope narrowing | `domain` scope: law applies only within named domain, not system-wide |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `kind: rule` or `kind: mandate` | H04 hard gate — exact literal "invariant" required |
| Statement without MUST/SHALL/NEVER/ALWAYS | Not imperative; enforcement is ambiguous |
| `quality: 7.5` (any number) | H05 hard gate — must be `null`; self-scoring prohibited |
| Omitting `exceptions` field | Gate failure — absence means no exceptions considered |
| Rationale restates statement | Zero information gain; density check fails |
| `id: p08_law_01` (leading zero) | Fails regex `^p08_law_[0-9]+$` |
| Body > 3072 bytes | Exceeds max_bytes hard constraint |
| Enforcement = "enforced automatically" | Must name the specific tool, hook, or gate |
| `number` collision with existing law | Uniqueness gate — verify against all P08 laws first |
## Application
1. Find next sequential `number` — verify no collision with existing P08 laws
2. Set `id: p08_law_{number}` and filename `p08_law_{number}.md` — must match exactly
3. Write `statement`: one imperative sentence using MUST / SHALL / NEVER / ALWAYS
4. Write `rationale`: WHY this law exists — must not restate the statement
5. Name the exact `enforcement` mechanism (hook name, gate ID, validator, CI step)
6. Set `exceptions`: explicit list of conditions, or `[]` if none apply
7. Set `scope` (system / agent_group / domain) and `priority` (1–10)
8. Write all 8 body sections: Statement, Rationale, Enforcement, Exceptions, Examples, Violations, History, References
9. Validate: H02 id pattern, H04 kind literal, H05 null quality, H08 unique number, H09 imperative mood — plus 10 SOFT gates
## References
- invariant-builder SCHEMA.md v1.0.0
- invariant-builder QUALITY_GATES.md (9 HARD + 10 SOFT)
- RFC 2119 — requirement levels MUST/SHALL/SHOULD
