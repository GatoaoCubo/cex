---
kind: memory
id: bld_memory_law
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for law artifact generation
---

# Memory: law-builder

## Summary

Building law artifacts requires extreme precision in distinguishing inviolable operational mandates from flexible guidelines. The most common failure mode is producing rules that read like suggestions rather than enforceable mandates. Successful law artifacts always include a concrete enforcement mechanism and explicit exception protocol — without these, the artifact degrades into an instruction.

## Pattern

- Always define the enforcement mechanism before writing the statement — if you cannot enforce it, it is not a law
- Write the violation section first; it clarifies the boundary between compliance and breach
- Use imperative mood for the statement field: "All X MUST Y" not "X should Y"
- Include at least one concrete historical trigger (incident, failure, or mandate source) in the rationale
- Scope boundaries must be explicit: name which domains, agents, or artifact kinds are covered
- Exception protocol requires both the condition and the authority that grants the exception

## Anti-Pattern

- Writing laws that overlap with existing guardrails (P11) — guardrails restrict for safety, laws mandate for operations
- Using vague enforcement like "review periodically" — enforcement must be machine-checkable or have a named human gate
- Omitting the conflict resolution priority — when two laws contradict, the system needs a tiebreaker
- Creating laws from single incidents without pattern validation — one failure is not enough to justify a permanent mandate
- Frontmatter missing severity or scope fields leading to ambiguous application

## Context

Laws operate in the P08 governance layer alongside patterns, diagrams, and component maps. The key distinction is that laws are non-negotiable — patterns recommend, laws require. Production environments demand laws when repeated failures show that optional guidance is insufficient. Typical triggers: post-incident reviews, compliance requirements, or architectural invariants that must never be violated.

## Impact

Well-formed laws prevent entire categories of recurring failures. A single law with clear enforcement eliminated repeated configuration drift issues across multiple production runs. Poorly formed laws (missing enforcement) were ignored in 60%+ of cases, providing no value while consuming review bandwidth.

## Reproducibility

To reliably produce high-quality law artifacts: (1) confirm the rule is truly inviolable, not just preferred, (2) draft enforcement mechanism first, (3) write violation examples from real incidents, (4) validate scope covers all affected domains without over-reach, (5) run through all 9 HARD gates before delivery.

## References

- law-builder SCHEMA.md (19+ frontmatter fields, 8 body sections)
- P08 governance pillar documentation
- Operational governance design patterns
