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
related:
  - bld_architecture_axiom
  - p11_qg_axiom
  - bld_config_axiom
  - bld_instruction_axiom
  - p01_kc_axiom
  - p03_sp_axiom_builder
  - bld_output_template_axiom
  - bld_collaboration_axiom
  - p10_lr_axiom-builder
  - bld_knowledge_card_axiom
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_axiom]] | downstream | 0.43 |
| [[p11_qg_axiom]] | downstream | 0.41 |
| [[bld_config_axiom]] | downstream | 0.39 |
| [[bld_instruction_axiom]] | downstream | 0.37 |
| [[p01_kc_axiom]] | related | 0.37 |
| [[p03_sp_axiom_builder]] | downstream | 0.36 |
| [[bld_output_template_axiom]] | downstream | 0.36 |
| [[bld_collaboration_axiom]] | downstream | 0.36 |
| [[p10_lr_axiom-builder]] | downstream | 0.35 |
| [[bld_knowledge_card_axiom]] | upstream | 0.34 |
