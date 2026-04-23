---
kind: architecture
id: bld_architecture_pattern
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of pattern — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - pattern-builder
  - bld_collaboration_pattern
  - p03_sp_pattern_builder
  - p11_qg_pattern
  - p01_kc_pattern
  - bld_memory_pattern
  - bld_architecture_invariant
  - p03_ins_pattern
  - bld_knowledge_card_pattern
  - component-map-builder
---

# Architecture: pattern in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 21-field metadata header (id, kind, pillar, domain, category, etc.) | pattern-builder | active |
| problem_statement | The recurring problem this pattern solves, expressed concretely | author | active |
| solution | The named, reusable solution with structural description | author | active |
| forces | Competing concerns and tensions that the pattern balances | author | active |
| consequences | Positive and negative outcomes of applying this pattern | author | active |
| applicability | Conditions under which this pattern should and should not be used | author | active |
| related_patterns | Cross-references to complementary and conflicting patterns | author | active |
## Dependency Graph
```
knowledge_card  --produces-->  pattern  --consumed_by-->  agent
learning_record --produces-->  pattern  --referenced_by-> law
pattern         --signals-->   pattern_application
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | pattern | data_flow | domain facts supporting problem identification |
| learning_record (P10) | pattern | data_flow | observed successes formalized as reusable solutions |
| pattern | agent (P02) | consumes | agent applies pattern to solve recurring problems |
| pattern | law (P08) | data_flow | pattern may be elevated to inviolable mandate |
| pattern | diagram (P08) | data_flow | pattern structure visualized in architecture diagrams |
| pattern | related_patterns | dependency | patterns reference each other for composition |
| pattern | pattern_application | signals | recorded when pattern is successfully applied |
## Boundary Table
| pattern IS | pattern IS NOT |
|------------|---------------|
| A named, reusable solution for a recurring architecture problem | An inviolable operational mandate (law P08) |
| Documents forces, consequences, and applicability | A visual representation of structure (diagram P08) |
| Recommends — does not mandate — adoption | An inventory of system parts (component_map P08) |
| Derived from observed successes and documented failures | A specification of a agent_group component (agent_card P08) |
| Cross-references related and anti-patterns | A multi-step execution sequence (workflow P12) |
| Dense (>=0.80 density), max 4KB | A verbose tutorial or guide |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Evidence | knowledge_card, learning_record | Supply domain facts and observed successes |
| Problem | frontmatter, problem_statement, forces | Define the problem and competing tensions |
| Solution | solution, consequences, applicability | Describe the reusable solution and when to apply it |
| Relationships | related_patterns | Map connections to complementary and conflicting patterns |
| Downstream | agent, law, diagram | Consumers that apply, mandate, or visualize the pattern |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[pattern-builder]] | related | 0.54 |
| [[bld_collaboration_pattern]] | related | 0.39 |
| [[p03_sp_pattern_builder]] | upstream | 0.37 |
| [[p11_qg_pattern]] | downstream | 0.37 |
| [[p01_kc_pattern]] | related | 0.35 |
| [[bld_memory_pattern]] | downstream | 0.35 |
| [[bld_architecture_invariant]] | sibling | 0.32 |
| [[p03_ins_pattern]] | upstream | 0.31 |
| [[bld_knowledge_card_pattern]] | upstream | 0.31 |
| [[component-map-builder]] | related | 0.27 |
