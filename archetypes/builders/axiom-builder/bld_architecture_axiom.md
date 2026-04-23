---
kind: architecture
id: bld_architecture_axiom
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of axiom — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - axiom-builder
  - p03_sp_axiom_builder
  - bld_collaboration_axiom
  - bld_config_axiom
  - bld_instruction_axiom
  - tpl_axiom
  - p01_kc_axiom
  - p11_qg_axiom
  - bld_output_template_axiom
  - bld_knowledge_card_axiom
---

# Architecture: axiom in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 20-field metadata header (id, kind, pillar, domain, immutable: true, etc.) | axiom-builder | required |
| axiom_statement | Single declarative sentence expressing the fundamental truth | author | required |
| rationale | Explanation of why this truth is permanent and foundational | author | required |
| scope | Domain or system boundary within which the axiom holds | author | required |
| implications | Downstream consequences — which laws, guardrails, or behaviors this axiom anchors | author | required |
| anti_examples | Statements that look like axioms but are not (operational rules, changeable policies) | author | required |
| version_lock | Explicit immutability declaration — version never increments past 1.0.0 | axiom-builder | required |
## Dependency Graph
```
domain_knowledge  --produces-->  axiom  --produces_for-->  law
axiom             --produces_for-->  guardrail
axiom             --produces_for-->  learning_record (validates against axiom over time)
axiom             --produces-->  system_prompt (via IHP injection)
brain_query       --queried_by-->  axiom
axiom             --signals-->   system identity (anchors agent worldview)
```
| From | To | Type | Data |
|------|----|------|------|
| domain_knowledge | axiom | data_flow | raw fundamental truths requiring formalization |
| axiom | law (P08) | produces | operational rules derived from the permanent truth |
| axiom | guardrail (P11) | produces | safety boundaries enforced from axiom principles |
| axiom | learning_record (P10) | produces | baseline against which learning is validated |
| axiom | system_prompt (P03) | data_flow | injected as foundational context via IHP |
| brain_query | axiom | data_flow | retrieved during agent context assembly |
| axiom | agent behavior | signals | constrains what the agent will and will not do |
## Boundary Table
| axiom IS | axiom IS NOT |
|----------|--------------|
| A permanent, immutable truth about a domain | An operational rule that can evolve (law) |
| A declarative statement, not a command | A behavioral restriction enforced at runtime (guardrail) |
| The foundational layer that other rules are derived from | A lifecycle management rule (lifecycle_rule) |
| Version-locked at 1.0.0 — never updated | A learning artifact that improves with experience (learning_record) |
| Injected into prompts as non-negotiable context | An executable instruction with steps (instruction) |
| Domain-scoped and universally applicable within that scope | A task-specific or session-specific artifact |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Formalization | frontmatter, axiom_statement, rationale, scope | Capture and declare the permanent truth with full context |
| Boundary | anti_examples, version_lock, implications | Define what the axiom covers, what it excludes, and what it anchors |
| Injection | brain_query retrieval, IHP, system_prompt | Make the axiom available to agents as foundational context |
| Derivation | law, guardrail, learning_record | Downstream artifacts that operationalize the axiom's truth |
| Validation | learning_record cross-reference | Confirm over time that the axiom remains true and universally applicable |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[axiom-builder]] | downstream | 0.65 |
| [[p03_sp_axiom_builder]] | upstream | 0.61 |
| [[bld_collaboration_axiom]] | downstream | 0.59 |
| [[bld_config_axiom]] | downstream | 0.57 |
| [[bld_instruction_axiom]] | upstream | 0.55 |
| [[tpl_axiom]] | upstream | 0.54 |
| [[p01_kc_axiom]] | upstream | 0.54 |
| [[p11_qg_axiom]] | downstream | 0.53 |
| [[bld_output_template_axiom]] | upstream | 0.47 |
| [[bld_knowledge_card_axiom]] | upstream | 0.46 |
