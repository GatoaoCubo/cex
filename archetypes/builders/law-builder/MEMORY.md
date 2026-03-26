---
id: law-builder-memory
kind: memory
pillar: P08
parent: law-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [memory, law-builder, mistakes, patterns, P08]
---

# law-builder — MEMORY

## Common Mistakes

1. **Setting quality to a number** — `quality: 8.5` triggers H05 rejection. Always `quality: null`.
2. **Advisory language in statement** — "should", "try to", "consider" make laws unenforceable. Use MUST/SHALL/NEVER/ALWAYS.
3. **Missing enforcement mechanism** — stating "law must be followed" without specifying HOW violation is detected. Unenforced laws are wishes.
4. **Omitting exceptions without explicit "None"** — leaving exceptions field absent creates ambiguity. Either list conditions or write `exceptions: []`.
5. **Confusing law with guardrail** — ask: "is this about safety (guardrail) or operational consistency (law)?" Safety = P11. Operations = P08.
6. **Confusing law with instruction** — ask: "is this mandatory with consequences (law) or flexible with guidance (instruction)?" Flexible = P03.
7. **Multi-sentence statement** — laws MUST have exactly one imperative sentence. Split compound rules into separate laws.
8. **Number collision** — always check LAWS_v3_PRACTICAL.md for existing numbers. Laws 1-11 are taken; new laws start at 12.
9. **Wrong id prefix** — `law_5` and `p08_rule_5` both fail H02. Only `p08_law_5` is valid.
10. **Rationale restates statement** — "this law exists because artifacts should not have quality scores" is restatement. Explain the WHY: bias, metric corruption, calibration failure.

## Law Governance Catalog

| Domain | Common laws | Boundary watch |
|--------|------------|----------------|
| Quality | No self-scoring, minimum density threshold | vs quality_gate (P11) — gates enforce, laws define |
| Operations | Commit before pause, signal completion | vs instruction (P03) — instructions guide, laws mandate |
| Security | No hardcoded secrets, scope fence | vs guardrail (P11) — guardrails restrict safety, laws govern ops |
| Architecture | Max terminals, naming conventions | vs pattern (P08) — patterns recommend, laws mandate |
| Satellites | STELLA never executes, routing mandates | vs satellite_spec (P08) — specs define capability, laws constrain behavior |

## Enforcement Patterns (Proven)

| Pattern | Example | Reuse |
|---------|---------|-------|
| HARD gate in builder | H05 checks `quality == null` | Most reliable; use when builder controls output |
| CI/CD pre-commit hook | Rejects files without required fields | File-level; use for filesystem compliance |
| Runtime guard in satellite | Satellite refuses to proceed without signal | Behavioral; use for process compliance |
| Review gate | Human rejects artifact missing enforcement | Fallback when automation not feasible |

## Statement Formulation Guide

| Mood | Example | Valid? |
|------|---------|--------|
| MUST (obligation) | "Every artifact MUST have quality: null" | YES |
| SHALL (formal obligation) | "No producer SHALL self-assign a score" | YES |
| NEVER (prohibition) | "Satellites NEVER execute tasks directly" | YES |
| ALWAYS (invariant) | "Authors ALWAYS set quality: null" | YES |
| should (recommendation) | "Artifacts should have quality: null" | NO — instruction, not law |
| consider (advisory) | "Consider setting quality: null" | NO — not a law |
| try to (soft) | "Try to avoid self-scoring" | NO — not a law |

## Production Counter

| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just initialized) |
| Average quality score | — |
| Most common friction point | enforcement specificity + exception handling |
| Last updated | 2026-03-26 |

## Evolution Notes

- Laws 1-11 exist in LAWS_v3_PRACTICAL.md — do NOT reuse those numbers
- Law numbers are permanent; even deprecated laws retain their number
- When revising a law: increment version, update `updated` field, add entry to History section
- When deprecating a law: add `deprecated: true` field, document reason in History
