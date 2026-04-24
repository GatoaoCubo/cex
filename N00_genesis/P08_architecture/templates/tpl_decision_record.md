---
id: p08_decision_record
kind: decision_record
8f: F4_reason
pillar: P08
version: 1.0.0
title: "Template — Architecture Decision Record"
tags: [template, adr, decision, architecture, rationale]
tldr: "Records an architectural decision with context, options considered, decision made, and consequences. Prevents revisiting decided questions and documents trade-offs."
quality: 9.0
updated: "2026-04-07"
domain: "system architecture"
author: n03_builder
created: "2026-04-07"
density_score: 0.93
related:
  - decision-record-builder
  - bld_knowledge_card_decision_record
  - bld_output_template_decision_record
  - p03_sp_decision_record_builder
  - p10_lr_decision_record_builder
  - bld_instruction_decision_record
  - p01_kc_decision_record
  - bld_schema_decision_record
  - bld_architecture_decision_record
  - bld_collaboration_decision_record
---

# ADR-[NNN]: [DECISION_TITLE]

## Status
[proposed | accepted | deprecated | superseded by ADR-NNN]

## Context
[WHAT problem or question prompted this decision. Include technical constraints, business requirements, and relevant prior decisions.]

## Options Considered

| Option | Pros | Cons |
|--------|------|------|
| [OPTION_A] | [PRO_1, PRO_2] | [CON_1, CON_2] |
| [OPTION_B] | [PRO_1, PRO_2] | [CON_1, CON_2] |
| [OPTION_C] | [PRO_1, PRO_2] | [CON_1, CON_2] |

## Decision
We chose **[OPTION_X]** because [PRIMARY_REASON].

## Consequences
- **Positive**: [WHAT_IMPROVES]
- **Negative**: [WHAT_GETS_HARDER]
- **Neutral**: [WHAT_STAYS_THE_SAME]

## Compliance
- **Enforced by**: [tool, review process, or convention]
- **Verified by**: [test, doctor check, or CI gate]
- **Exceptions**: [none | list specific exceptions with rationale]

## References
- Related ADRs: [ADR-NNN]
- External: [URL to documentation, RFC, or discussion]
- Date decided: [YYYY-MM-DD]
- Participants: [WHO was involved in the decision]

## Quality Gate
- [ ] Context explains WHY (not just WHAT)
- [ ] ≥ 2 options considered (no rubber-stamping)
- [ ] Consequences include positives AND negatives
- [ ] Status is explicit

## Cross-References

- **Pillar**: P08 (Architecture)
- **Kind**: `decision record`
- **Artifact ID**: `p08_decision_record`
- **Tags**: [template, adr, decision, architecture, rationale]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P08 | Architecture domain |
| Kind `decision record` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[decision-record-builder]] | related | 0.49 |
| [[bld_knowledge_card_decision_record]] | upstream | 0.44 |
| [[bld_output_template_decision_record]] | upstream | 0.44 |
| [[p03_sp_decision_record_builder]] | related | 0.43 |
| [[p10_lr_decision_record_builder]] | downstream | 0.42 |
| [[bld_instruction_decision_record]] | upstream | 0.41 |
| [[p01_kc_decision_record]] | related | 0.40 |
| [[bld_schema_decision_record]] | upstream | 0.38 |
| [[bld_architecture_decision_record]] | related | 0.37 |
| [[bld_collaboration_decision_record]] | downstream | 0.37 |
