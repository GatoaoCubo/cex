---
id: tpl_axiom
kind: axiom
pillar: P02
version: 1.0.0
title: "Template — Axiom"
tags: [template, axiom, rule, invariant, constraint]
tldr: "An axiom is an immutable system rule that all agents and artifacts must obey. Axioms define hard boundaries — violations trigger immediate rejection."
quality: 9.0
updated: "2026-04-07"
domain: "model configuration"
author: n03_builder
created: "2026-04-07"
density_score: 0.93
---

# Axiom: [AXIOM_TITLE]

## Statement
[AXIOM_STATEMENT — one sentence, imperative mood, unambiguous]

Example: "Every artifact must have valid YAML frontmatter with id, kind, and pillar fields."

## Rationale
[WHY this axiom exists — what breaks if violated, what it protects]

## Scope

| Dimension | Value |
|-----------|-------|
| Applies to | [artifacts \| agents \| workflows \| all] |
| Pillars | [P01-P12 \| specific pillar] |
| Enforcement | [compile-time \| runtime \| review] |
| Exceptions | [none \| list specific exceptions] |

## Implications
- [IMPLICATION_1 — what this axiom forces in practice]
- [IMPLICATION_2 — downstream effect on other axioms]
- [IMPLICATION_3 — tooling requirements]

## Violation Examples

| Violation | Why It Breaks | Detection |
|-----------|--------------|-----------|
| [VIOLATION_1] | [CONSEQUENCE] | [HOW_DETECTED] |
| [VIOLATION_2] | [CONSEQUENCE] | [HOW_DETECTED] |

## Relationship to Other Axioms
- **Depends on**: [AXIOM_ID] — this axiom assumes [X] is already enforced
- **Conflicts with**: [none \| AXIOM_ID] — resolution: [PRIORITY_RULE]
- **Strengthens**: [AXIOM_ID] — together they enforce [PROPERTY]

## Quality Gate
- [ ] Statement is ≤ 1 sentence
- [ ] Rationale explains "what breaks" (not just "it's best practice")
- [ ] At least 1 violation example with detection method
- [ ] Scope explicitly defined

## Cross-References

- **Pillar**: P02 (Model)
- **Kind**: `axiom`
- **Artifact ID**: `tpl_axiom`
- **Tags**: [template, axiom, rule, invariant, constraint]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P02 | Model domain |
| Kind `axiom` | Artifact type |
| Pipeline | 8F (F1→F8) |
