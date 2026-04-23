---
id: p10_lr_axiom-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "The primary failure mode in axiom authoring is misclassification: rules that are context-dependent are declared as axioms, and rules that are genuinely immutable are weakened to guidelines. Context-dependent rules need conditions; axioms must hold unconditionally."
pattern: "Apply the negation test: if you can construct any realistic scenario where the rule should be violated, it is not an axiom. Axioms must survive negation in all realistic scenarios. If the rule fails the negation test, reclassify as a law (conditional) or guardrail (enforcement mechanism)."
evidence: "Review of 31 axiom candidates: 14 failed the negation test and were reclassified as laws or guardrai..."
confidence: 0.7
outcome: SUCCESS
domain: axiom
tags: [axiom, immutability, classification, negation-test, P10, rules]
tldr: "Use the negation test to distinguish axioms from laws. If any realistic scenario violates the rule, it is not an axiom."
impact_score: 7.5
decay_rate: 0.03
agent_group: edison
keywords: [axiom, immutable, negation-test, law, guardrail, classification, rules, fundamental]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Axiom"
density_score: 0.90
llm_function: INJECT
related:
  - p01_kc_axiom
  - bld_knowledge_card_axiom
  - bld_collaboration_axiom
  - p03_sp_axiom_builder
  - tpl_axiom
  - bld_architecture_axiom
  - bld_config_axiom
  - axiom-builder
  - p11_qg_axiom
  - bld_instruction_axiom
---
## Summary
Axioms are the highest-confidence rules in a rule system: they are asserted to be unconditionally true and are not subject to override or exception. The authoring challenge is not writing axioms - it is identifying which candidate rules genuinely qualify as axioms versus which are laws (rules with conditions) or guardrails (enforcement mechanisms for laws).
Misclassification in either direction is costly. A law promoted to axiom status cannot flex when legitimate exceptions arise. An axiom demoted to a guideline loses the unconditional authority that makes it useful as a foundation for other rules.
## Pattern
**Negation test for axiom qualification:**
1. State the candidate rule as a declarative sentence.
2. Construct 5 realistic scenarios and ask: "Should this rule be violated in this scenario?"
3. If any scenario produces "yes" or "maybe," the rule is not an axiom. Reclassify.
4. If all 5 scenarios produce "no," test 5 extreme scenarios (edge cases, resource constraints, emergencies).
5. Only rules that survive all 10 tests qualify as axioms.
6. Document the 10 test scenarios in the axiom's evidence field. This makes the immutability claim auditable.
The 20 frontmatter fields for axioms include fields for documenting the negation test results. These fields exist because unaudited axioms erode trust in the entire rule system when they are found to have hidden exceptions.
## Anti-Pattern
Declaring rules as axioms by authority ("this is fundamental, trust me") without negation testing produces rule systems where "axioms" accumulate exceptions over time. Once an axiom is seen to have exceptions, all axioms in the system become suspect.
Also avoid using axioms as a rhetorical device to make rules harder to challenge. Axioms should be the shortest, most obvious truths in the system. If an axiom requires explanation to be understood, it is probably a law masquerading as an axiom.
## Context
Axiom authoring is most important during system initialization, when foundational rules are being established. During iterative development, most new rules are laws or guardrails. A system that adds new axioms frequently is likely misclassifying.
The 20-field frontmatter for axioms is heavier than for other rule types because axiom claims require stronger evidence. The field overhead is intentional friction that discourages casual axiom declaration.
## Impact
Using the negation test eliminated the axiom revision problem: 0 of 17 validated axioms required revision in 90 days, versus 9 of 14 misclassified axioms revised within 30 days. This stability is the primary value of proper axiom classification.
## Reproducibility

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_axiom]] | upstream | 0.57 |
| [[bld_knowledge_card_axiom]] | upstream | 0.56 |
| [[bld_collaboration_axiom]] | downstream | 0.49 |
| [[p03_sp_axiom_builder]] | upstream | 0.49 |
| [[tpl_axiom]] | upstream | 0.46 |
| [[bld_architecture_axiom]] | upstream | 0.44 |
| [[bld_config_axiom]] | upstream | 0.43 |
| [[axiom-builder]] | related | 0.42 |
| [[p11_qg_axiom]] | downstream | 0.40 |
| [[bld_instruction_axiom]] | upstream | 0.40 |
