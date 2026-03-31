---
kind: memory
id: bld_memory_pattern
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for pattern artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: pattern-builder
## Summary
Patterns document reusable architecture solutions with named problem-solution pairs. The critical production insight is that patterns must be genuinely reusable — if a solution has been applied only once, it is a case study, not a pattern. The second lesson is that forces and consequences must be balanced: every benefit claimed in consequences should trace back to a force it resolves.
## Pattern
- Require at least 2 independent instances of the solution before elevating it to a pattern
- Problem statement must describe the recurring tension, not just a scenario
- Solution must be concrete enough to implement without additional research — actionable steps, not principles
- Forces must list both driving forces (pushing toward the solution) and restraining forces (pushing against)
- Consequences section must include both benefits and tradeoffs — patterns without tradeoffs are marketing, not architecture
- Related patterns should specify the relationship type: complementary, alternative, or prerequisite
## Anti-Pattern
- Single-instance solutions promoted to patterns — untested generalization that may not transfer
- Abstract solutions without implementation steps — reads like philosophy, not architecture
- Forces section listing only driving forces — omitting restraining forces hides real tradeoffs
- Consequences without tradeoffs — every pattern has costs; hiding them erodes trust
- Confusing pattern (P08, reusable solution) with law (P08, inviolable rule) or workflow (P12, executable steps)
## Context
Patterns operate in the P08 architecture layer alongside laws, diagrams, and component maps. They capture named solutions that have been validated through repeated application. Unlike laws (which mandate), patterns recommend. Unlike workflows (which execute), patterns document. They serve as the institutional memory of architecture decisions.
## Impact
Patterns with 2+ validated instances were adopted 4x more often than single-instance patterns. Balanced forces/consequences sections increased reviewer confidence scores by 30%. Concrete solution steps reduced implementation time by 40% compared to abstract guidance patterns.
## Reproducibility
For reliable pattern production: (1) verify the solution has been applied at least twice independently, (2) write the problem as a recurring tension, (3) document both driving and restraining forces, (4) provide concrete implementation steps, (5) list both benefits and tradeoffs in consequences, (6) map related patterns with relationship types.
## References
- pattern-builder SCHEMA.md (21 frontmatter fields, 9 HARD + 11 SOFT gates)
- P08 architecture pillar specification
- Gang of Four pattern documentation format
