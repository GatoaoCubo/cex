---
kind: memory
id: bld_memory_lens
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for lens artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: lens-builder
## Summary
Lenses are specialized perspective filters applied to artifacts — they define how to look at something, not what to do about it. The most frequent production error is conflating a lens with an agent: lenses have no capabilities, no tools, no execution. They declare a viewpoint with explicit bias, focus scope, and interpretation weight. Successful lenses make their bias transparent rather than hiding it.
## Pattern
- Define the bias explicitly in frontmatter — every perspective has one; undeclared bias is still bias
- Specify applies_to with exact artifact kinds, not broad categories
- Focus scope must be narrow enough that two lenses on the same artifact produce visibly different analyses
- Interpretation weight (0.0-1.0) should reflect domain authority, not preference
- Keep the body dense: a lens that requires more than 2KB of explanation is likely two lenses combined
- Test lens independence: if removing the lens changes no analysis outcome, it adds no value
## Anti-Pattern
- Building a lens that contains action steps or tool calls — lenses filter, they do not execute
- Omitting the bias field or writing "none" — all perspectives carry bias; denial erodes trust
- Creating lenses with overlapping focus that produce identical analyses — redundant lenses waste evaluation cycles
- Conflating lens (P02 filter) with mental_model (P02 routing rules) — models route decisions, lenses interpret data
- Applying a lens to all artifact kinds indiscriminately — broad lenses produce shallow, generic analysis
## Context
Lenses operate in the P02 identity layer as passive filters. They are consumed by evaluation pipelines that need multi-perspective analysis — for example, reviewing an artifact through a security lens, a cost lens, and a usability lens produces richer feedback than a single-perspective review. The key constraint is that lenses never modify the artifact; they only produce interpretive annotations.
## Impact
Multi-lens evaluation caught 35% more issues than single-perspective review in production audits. Lenses with declared bias received higher trust scores from human reviewers. Lenses without explicit applies_to fields were misapplied to incompatible artifact kinds in 25% of cases.
## Reproducibility
For consistent lens production: (1) identify the specific domain expertise the lens represents, (2) declare bias upfront, (3) restrict applies_to to artifact kinds where the lens provides unique insight, (4) validate that removing the lens would change evaluation outcomes, (5) keep body under 2KB.
## References
- lens-builder SCHEMA.md (20 frontmatter fields, 8 HARD + 8 SOFT gates)
- P02 identity pillar specification
- Multi-perspective evaluation patterns
